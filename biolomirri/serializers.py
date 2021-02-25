from copy import deepcopy
from mirri.entities.strain import ORG_TYPES
from mirri import rgetattr

from mirri.settings import (
    ALLOWED_FORMS_OF_SUPPLY,
    NAGOYA_APPLIES,
    NAGOYA_NO_APPLIES,
    NAGOYA_NO_CLEAR_APPLIES,
    NO_RESTRICTION,
    ONLY_RESEARCH,
    COMMERCIAL_USE_WITH_AGREEMENT,
)
from biolomirri.settings import MIRRI_FIELDS

NAGOYA_TRANSLATOR = {
    NAGOYA_NO_APPLIES: "no known restrictions under the nagoya protocol",
    NAGOYA_APPLIES: "documents providing proof of legal access and terms of use available at the collection",
    NAGOYA_NO_CLEAR_APPLIES: "strain probably in scope, please contact the culture collection",
}
RESTRICTION_USE_TRANSLATOR = {
    NO_RESTRICTION: "no restrictions apply",
    ONLY_RESEARCH: "for research use only",
    COMMERCIAL_USE_WITH_AGREEMENT: "for commercial development a special agreement is requested",
}


def serialize_to_biolomics(strain, client=None):
    record_details = {}

    for field in MIRRI_FIELDS:
        label = field["label"]
        attribute = field["attribute"]
        try:
            biolomics_field = field["biolomics"]["field"]
            biolomics_type = field["biolomics"]["type"]
        except KeyError:
            # print(f"biolomics not configured: {label}")
            continue
        if label == "Accession number":
            value = f"{strain.id.collection} {strain.id.number}"

        elif label == "Nagoya protocol restrictions and compliance conditions":
            value = value = rgetattr(strain, attribute, None)
            if value is not None:
                value = NAGOYA_TRANSLATOR[value]
        elif label == "Restrictions on use":
            value = rgetattr(strain, attribute, None)
            if value is not None:
                value = RESTRICTION_USE_TRANSLATOR[value]
        elif label in ("MTA file", "ABS related files"):
            value = rgetattr(strain, attribute, None)
            if value is not None:
                value = [{"Name": "link", "Value": fname} for fname in value]
        elif label == "Organism type":
            value = rgetattr(strain, attribute, None)
            if value is not None:
                org_types = [ot.name for ot in value]
                value = []
                for ot in ORG_TYPES.keys():
                    is_organism = "Yes" if ot in org_types else "No"
                    value.append({"Name": ot, "Value": is_organism})
        elif attribute in ("deposit.date", "collect.date", "isolation.date",
                           "catalog_inclusion_date"):
            date_range = rgetattr(strain, attribute, None)
            if date_range:
                year = date_range._year
                month = date_range._month if date_range._month else 1
                day = date_range._day if date_range._day else 1
                value = f"{year}-{month:02}-{day:02}"
            else:
                value = None
        elif label == "Recommended growth temperature":
            value = rgetattr(strain, attribute, None)
            if value:
                content = {
                    "MaxValue": value,
                    "MinValue": value,
                    "FieldType": "S",
                }
                record_details[biolomics_field] = content
            continue
        elif label == "Form of supply":
            form_of_supplies = rgetattr(strain, attribute, None)
            if form_of_supplies is not None:
                value = []
                for form in ALLOWED_FORMS_OF_SUPPLY:
                    is_form = "yes" if form in form_of_supplies else "No"
                    value.append({"Name": form, "Value": is_form})
            else:
                value = None
        elif attribute == "growth.recommended_media":
            growth_media = rgetattr(strain, attribute, None)
            if growth_media is not None and client is not None:
                value = []
                print('a')
                for medium in growth_media:
                    ws_gm = client.retrieve_growth_medium_by_name(medium)
                    if ws_gm is None:
                        raise ValueError(
                            'Can not find the growth medium: {medium}')
                    gm = {"Name": {"Value": "medium", "FieldType": "E", },
                          "RecordId": ws_gm['Record Id']}
                    value.append(gm)
            else:
                value = None
        else:
            value = rgetattr(strain, attribute, None)
        #print(label, value), biolomics_field
        if value is not None:
            content = {"Value": value, "FieldType": biolomics_type}
            record_details[biolomics_field] = content

    record_details["Data provided by"] = {
        "Value": strain.id.collection, "FieldType": "V"}
    return {"RecordDetails": record_details, "RecordName": "Strains record"}
