
import unittest
from pathlib import Path
from pprint import pprint
from biolomirri.serializers import serialize_to_biolomics
from mirri.entities.strain import Strain, StrainId, OrganismType, GenomicSequence
from mirri.entities.date_range import DateRange
from mirri.entities.publication import Publication
from mirri.settings import NAGOYA_APPLIES

TEST_DATA_DIR = Path(__file__).parent / "data"


class BiolomicsWriter(unittest.TestCase):
    def test_serialize_basic(self):
        strain = create_full_data_strain()
        strain = serialize_to_biolomics(strain, client=None)
        pprint(strain)


def create_full_data_strain():
    strain = Strain()

    strain.id.number = "5433"
    strain.id.collection = "CECT"
    strain.id.url = "https://cect/2342"

    strain.nagoya_protocol = NAGOYA_APPLIES
    strain.collect.location.country = "spain"
    strain.genetics.ploidy = 9

    strain.growth.recommended_media = ["asd"]
    strain.isolation.date = DateRange(year=1900)

    strain.deposit.who = "pepe"

    strain.growth.recommended_media = ["11"]

    strain.taxonomy.organism_type = [OrganismType(2)]

    strain.other_numbers.append(StrainId(collection="aaa", number="a"))
    strain.other_numbers.append(StrainId(collection="aaa3", number="a3"))
    strain.form_of_supply = ["Agar", "Lyo"]
    gen_seq = GenomicSequence()
    gen_seq.marker_id = "pepe"
    gen_seq.marker_type = "16S rRNA"
    strain.genetics.markers.append(gen_seq)

    strain.collect.habitat_ontobiotope = "OBT:111111"
    strain.catalog_inclusion_date = DateRange(year=1999, month=1)
    pub = Publication()
    pub.id = "1"
    strain.publications = [pub]
    return strain


if __name__ == "__main__":
    # import sys;sys.argv = ['',
    #                        'BiolomicsWriter.test_mirri_excel_parser_invalid']
    unittest.main()
