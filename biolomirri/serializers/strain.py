import re

import pycountry

from mirri import rgetattr, rsetattr
from mirri.entities.date_range import DateRange
from mirri.entities.strain import ORG_TYPES, OrganismType, Strain, StrainId
from mirri.io.parsers.mirri_excel import add_taxon_to_strain

from mirri.settings import (
    ALLOWED_FORMS_OF_SUPPLY,
    NAGOYA_PROBABLY_SCOPE,
    NAGOYA_NO_RESTRICTIONS,
    NAGOYA_DOCS_AVAILABLE,
    NO_RESTRICTION,
    ONLY_RESEARCH,
    COMMERCIAL_USE_WITH_AGREEMENT,
)
from biolomirri.settings import MIRRI_FIELDS

NAGOYA_TRANSLATOR = {
    NAGOYA_NO_RESTRICTIONS: "no known restrictions under the Nagoya protocol",
    NAGOYA_DOCS_AVAILABLE: "documents providing proof of legal access and terms of use available at the collection",
    NAGOYA_PROBABLY_SCOPE: "strain probably in scope, please contact the culture collection",
}
REV_NAGOYA_TRANSLATOR = {v: k for k, v in NAGOYA_TRANSLATOR.items()}

RESTRICTION_USE_TRANSLATOR = {
    NO_RESTRICTION: "no restriction apply",
    ONLY_RESEARCH: "for research use only",
    COMMERCIAL_USE_WITH_AGREEMENT: "for commercial development a special agreement is requested",
}

REV_RESTRICTION_USE_TRANSLATOR = {v: k for k,
                                  v in RESTRICTION_USE_TRANSLATOR.items()}

DATE_TYPE_FIELDS = ("Date of collection", "Date of isolation",
                    "Date of deposit", "Date of inclusion in the catalogue")
BOOLEAN_TYPE_FIELDS = ("Strain from a registered collection", "Dual use",
                       "Quarantine in Europe", "Interspecific hybrid")  # , 'GMO')
FILE_TYPE_FIELDS = ("MTA file", "ABS related files")
MAX_MIN_TYPE_FIELDS = ("Tested temperature growth range",
                       "Recommended growth temperature")
LIST_TYPES_TO_JOIN = ('Other denomination', 'Plasmids',
                      'Plasmids collections fields')


class StrainMirri(Strain):

    @property
    def record_id(self):
        return self._data.get('record_id', None)

    @record_id.setter
    def record_id(self, value: int):
        self._data['record_id'] = value

    @property
    def record_name(self):
        return self._data.get('record_name', None)

    @record_name.setter
    def record_name(self, value: int):
        self._data['record_name'] = value


def serialize_to_biolomics(strain: Strain, client=None, update=False):  # sourcery no-metrics
    strain_record_details = {}

    for field in MIRRI_FIELDS:
        try:
            biolomics_field = field["biolomics"]["field"]
            biolomics_type = field["biolomics"]["type"]
        except KeyError:
            print(f'biolomics not configured: {field["label"]}')
            continue

        label = field["label"]
        attribute = field["attribute"]
        value = rgetattr(strain, attribute, None)
        if value is None:
            continue

        if label == "Accession number":
            value = f"{strain.id.collection} {strain.id.number}"
        if label == "Restrictions on use":
            value = RESTRICTION_USE_TRANSLATOR[value]
        elif label == "Nagoya protocol restrictions and compliance conditions":
            value = NAGOYA_TRANSLATOR[value]
        elif label in FILE_TYPE_FIELDS:
            value = [{"Name": "link", "Value": fname} for fname in value]
        elif label == "Other culture collection numbers":
            value = "; ".join(on.strain_id for on in value)
        elif label in BOOLEAN_TYPE_FIELDS:
            value = 'yes' if value else 'no'
        elif label in 'GMO':
            value = 'Yes' if value else 'No'
        elif label == "Organism type":
            org_types = [ot.name for ot in value]

            value = []
            for ot in ORG_TYPES.keys():
                is_organism = "yes" if ot in org_types else "no"
                value.append({"Name": ot, "Value": is_organism})
        elif label == 'Taxon name':
            if client:
                value = get_remote_rlink(client, 'taxonomy', strain.taxonomy.long_name)

        elif label in DATE_TYPE_FIELDS:
            year = value._year
            month = value._month or 1
            day = value._day or 1
            if year is None:
                continue
            value = f"{year}-{month:02}-{day:02}"
        elif label == 'History of deposit':
            value = " > ".join(value)
        elif label in MAX_MIN_TYPE_FIELDS:
            if isinstance(value, (int, float)):
                _max, _min = value, value
            else:
                _max, _min = value['max'], value['min']

            content = {"MaxValue": _max, "MinValue": _min,
                       "FieldType": biolomics_type}
            strain_record_details[biolomics_field] = content
            continue
        elif label in LIST_TYPES_TO_JOIN:
            value = '; '.join(value)
        # TODO: Check how to deal with crossrefs
        elif label == "Recommended medium for growth":
            if client is not None:
                ref_value = []
                for medium in value:
                    ws_gm = client.retrieve_by_name('growth_medium', medium)
                    if ws_gm is None:
                        raise ValueError(
                            f'Can not find the growth medium: {medium}')
                    gm = {"Name": {"Value": medium, "FieldType": "E"},
                          "RecordId": ws_gm.record_id}
                    ref_value.append(gm)
                value = ref_value
            else:
                value = None

        elif label == "Form of supply":
            _value = []
            for form in ALLOWED_FORMS_OF_SUPPLY:
                is_form = "yes" if form in value else "no"
                _value.append({"Name": form, "Value": is_form})
            value = _value
        # print(label, value), biolomics_field
        elif label == "Coordinates of geographic origin":
            value = {'Latitude': strain.collect.location.latitude,
                     'Longitude': strain.collect.location.longitude}
            precision = strain.collect.location.coord_uncertainty
            if precision is not None:
                value['Precision'] = precision
        elif label == "Geographic origin":
            if client is not None and value.country is not None:
                _country = pycountry.countries.get(alpha_3=value.country)
                _value = get_remote_rlink(client, 'country', _country.name)
                content = {"Value": _value, "FieldType": "RLink"}
                strain_record_details['Country'] = content
            _value = []
            for sector in ('state', 'municipality', 'site'):
                sector_val = getattr(value, sector, None)
                if sector_val:
                    _value.append(sector_val)
            value = "; ".join(_value) if _value else None

        elif label == "Literature":
            continue

        elif label == "Ontobiotope":
            if client and value:
                value = get_remote_rlink(client, 'ontobiotope', value)

        elif label == 'Ploidy':
            value = _translate_polidy(value)

        content = {"Value": value, "FieldType": biolomics_type}
        strain_record_details[biolomics_field] = content

    # if False:
    #     record_details["Data provided by"] = {
    #         "Value": strain.id.collection, "FieldType": "V"}
    strain_structure = {"RecordDetails": strain_record_details}
    if update:
        strain_structure['RecordId'] = strain.record_id
        strain_structure['RecordName'] = strain.record_name
    else:
        strain_structure["Acronym"] =  "MIRRI "

    return strain_structure


def get_remote_rlink(client, endpoint, record_name):
    entity = client.retrieve_by_name(endpoint, record_name)
    if entity:
        return [{
            "Name": {
                "Value": entity["RecordName"],
                "FieldType": "E"
            },
            "RecordId": entity["RecordId"]
        }]


def add_strain_rlink_to_entity(record, strain_id, strain_name):
    field_strain = {
        "FieldType": "RLink",
        'Value': [{
            'Name': {'Value': strain_name, 'FieldType': "E"},
            'RecordId': strain_id
        }]
    }
    record['RecordDetails']['Strains'] = field_strain
    return record


PLOIDY_TRANSLATOR = {
    1: 'Haploid',
    2: 'Diploid',
    3: 'Triploid',
    4: 'Tetraploid',
    9: 'Polyploid'
}

REV_PLOIDY_TRANSLATOR = {v: k for k, v in PLOIDY_TRANSLATOR.items()}


def _translate_polidy(ploidy):
    try:
        ploidy = int(ploidy)
    except TypeError:
        return '?'
    try:
        ploidy = PLOIDY_TRANSLATOR[ploidy]
    except KeyError:
        ploidy = 'Polyploid'
    return ploidy


def serialize_from_biolomics(biolomics_strain):  # sourcery no-metrics
    strain = StrainMirri()
    strain.record_id = biolomics_strain.get('RecordId', None)
    strain.record_name = biolomics_strain.get('RecordName', None)
    for field in MIRRI_FIELDS:
        try:
            biolomics_field = field["biolomics"]["field"]
        except KeyError:
            print(f'biolomics not configured: {field["label"]}')
            continue

        label = field["label"]
        attribute = field["attribute"]
        field_data = biolomics_strain['RecordDetails'].get(biolomics_field, None)
        if field_data is None:
            continue

        if biolomics_field in ('Tested temperature growth range', 'Recommended growth temperature'):
            value = {'max': field_data.get('MaxValue', None),
                     'min': field_data.get('MinValue', None)}
        else:
            value = field_data['Value']
        if value in (None, '', [], {}, '?', 'Unknown'):
            continue

        # print(label, attribute, biolomics_field, value)

        if label == 'Accession number':
            collection, number = strain.record_name.split(' ', 1)
            mirri_id = StrainId(collection=collection, number=number)
            strain.synonyms = [mirri_id]
            coll, num = value.split(' ', 1)
            accession_number_id = StrainId(collection=coll, number=num)
            strain.id = accession_number_id
            continue
        elif label == "Restrictions on use":
            value = REV_RESTRICTION_USE_TRANSLATOR[value]
        elif label == 'Nagoya protocol restrictions and compliance conditions':
            value = REV_NAGOYA_TRANSLATOR[value]
        elif label in FILE_TYPE_FIELDS:
            value = [f['Value'] for f in value]
        elif label == "Other culture collection numbers":
            other_numbers = []
            for on in value.split(";"):
                on = on.strip()
                try:
                    collection, number = on.split(" ", 1)
                except ValueError:
                    collection = None
                    number = on
                _id = StrainId(collection=collection, number=number)
                other_numbers.append(_id)
            value = other_numbers
        elif label in BOOLEAN_TYPE_FIELDS:
            value = value
            value = value == 'yes'
        elif label == 'GMO':
            value = value == 'Yes'
        elif label == "Organism type":
            organism_types = [OrganismType(item['Name']) for item in value if item['Value'] == 'yes']
            if organism_types:
                value = organism_types
        elif label in 'Taxon name':
            value = value[0]['Name']['Value']
            add_taxon_to_strain(strain, value)
            continue

        elif label in DATE_TYPE_FIELDS:
            #date_range = DateRange()
            value = DateRange().strpdate(value)

        elif label == "Recommended growth temperature":
            value = float((value['max'] + value['min']) / 2)
        elif label == "Recommended medium for growth":
            value = [v['Name']['Value'] for v in value]
        elif label == "Form of supply":
            value = [item['Name'] for item in value if item['Value'] == 'yes']
        elif label in LIST_TYPES_TO_JOIN:
            value = [v.strip() for v in value.split(";")]
        elif label == "Coordinates of geographic origin":
            if ('Longitude' in value and 'latitude' in value and
                    isinstance(value['Longitude'], float) and
                    isinstance(value['Latitude'], float)):
                strain.collect.location.longitude = value['Longitude']
                strain.collect.location.latitude = value['Latitude']
                strain.collect.location.coord_uncertainty = value['Precision']
            continue
        elif label == "Altitude of geographic origin":
            value = float(value)
        elif label == "Geographic origin":
            strain.collect.location.site = value
            continue
        elif label == 'Ontobiotope':
            try:
                value = re.search("(OBT:[0-9]{5,7})", value[0]['Name']['Value']).group()
            except (KeyError, IndexError, AttributeError):
                continue

        elif label == 'Ploidy':
            value = REV_PLOIDY_TRANSLATOR[value]
        rsetattr(strain, attribute, value)
    # fields that are not in MIRRI FIELD list
    # country
    if 'Country' in biolomics_strain and biolomics_strain['Country']:
        country_name = biolomics_strain['Country'][0]['Name']
        strain.collect.location.country = pycountry.countries.get(
            name=country_name).alpha_3
    return strain

