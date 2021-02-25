from mirri.entities.strain import Strain, StrainId, OrganismType, GenomicSequence
from mirri.entities.date_range import DateRange
from mirri.entities.publication import Publication
from mirri.settings import NAGOYA_APPLIES


def create_full_data_strain():
    strain = Strain()

    strain.id.number = "1"
    strain.id.collection = "TESTCC"
    strain.id.url = "https://cect/2342"

    strain.nagoya_protocol = NAGOYA_APPLIES
    # strain.
    strain.risk_group = '1'

    strain.status = "type of Bacillus alcalophilus"
    strain.is_subject_to_quarantine = False

    strain.isolation.date = DateRange(year=1900)

    # already existing media in test_mirri

    strain.taxonomy.organism_type = [OrganismType(2)]
    strain.taxonomy.genus = 'Bacillus'
    strain.taxonomy.species = 'alcalophilus'

    strain.deposit.who = "NCTC, National Collection of Type Cultures - NCTC, London, United Kingdom of Great Britain and Northern Ireland."
    strain.deposit.date = DateRange(year=1985, month=5, day=2)
    strain.catalog_inclusion_date = DateRange(year=1985, month=5, day=2)

    strain.collect.location.country = "ESP"
    strain.collect.location.state = "Unknown"
    strain.collect.location.municipality = "Unknown"
    strain.collect.location.site = "Unknown"
    strain.collect.habitat_ontobiotope = "OBT:111111"

    strain.growth.recommended_temp = 30
    strain.growth.recommended_media = ["AAA"]

    strain.other_numbers.append(StrainId(collection="aaa", number="a"))
    strain.other_numbers.append(StrainId(collection="aaa3", number="a3"))
    strain.form_of_supply = ["Agar", "Lyo"]
    gen_seq = GenomicSequence()
    gen_seq.marker_id = "pepe"
    gen_seq.marker_type = "16S rRNA"
    strain.genetics.markers.append(gen_seq)
    strain.genetics.ploidy = 9

    strain.catalog_inclusion_date = DateRange(year=1999, month=1)
    pub = Publication()
    pub.id = "1"
    strain.publications = [pub]
    return strain


if __name__ == '__main__':
    create_full_data_strain()
