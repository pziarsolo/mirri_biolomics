import unittest
from pprint import pprint
from mirri.entities.strain import Strain
from biolomirri.serializers import serialize_to_biolomics
from biolomirri.remote.biolomics_client import (
    BiolomicsMirriClient, SERVER_URL, BiolomicsClientBackend,
    BiolomicsClientPassword)

try:
    from biolomirri.secrets import CLIENT_ID, SECRET_ID, USERNAME, PASSWORD
except ImportError:
    CLIENT_ID = None
    SECRET_ID = None
    USERNAME = None
    PASSWORD = None


class BiolomicsClientTest(unittest.TestCase):

    def test_authenticationbackend(self):
        client = BiolomicsClientBackend(SERVER_URL, CLIENT_ID, SECRET_ID)
        access1 = client.get_access_token()
        access2 = client.get_access_token()
        self.assertEqual(access1, access2)

    def test_authentication(self):
        client = BiolomicsClientPassword(
            SERVER_URL, CLIENT_ID, SECRET_ID, USERNAME, PASSWORD)
        access1 = client.get_access_token()
        access2 = client.get_access_token()
        assert access1 is not None
        self.assertEqual(access1, access2)

    def test_get_strain(self):
        client = BiolomicsMirriClient(SERVER_URL, CLIENT_ID, SECRET_ID,
                                      USERNAME, PASSWORD)

        accession_number = "BEA 0014B"
        strain = client.retrieve_strain_by_accession_number(accession_number)

        self.assertEqual(accession_number,
                         strain["Collection accession number"])

        accession_number = "BEA 0014B__"
        strain = client.retrieve_strain_by_accession_number(accession_number)
        self.assertIsNone(strain)

    def test_growth_media_by_name(self):
        client = BiolomicsMirriClient(SERVER_URL, CLIENT_ID, SECRET_ID,
                                      USERNAME, PASSWORD)
        gm = client.retrieve_growth_medium_by_name('AAA')
        self.assertEqual(gm['Record Id'], 1)

    def _build_strain(self):
        strain_data = {
            "status": "type of Bacillus alcalophilus",
            "quarantine": False,
            "id": {"collection_code": "TESTCC", "accession_number": "1"},
            "taxonomy": {
                "organism_type": [3],
                "genus": {"name": "Bacillus"},
                "species": {"name": "alcalophilus"},
            },
            "deposit": {
                "depositor": "NCTC, National Collection of Type Cultures - NCTC, London, United Kingdom of Great Britain and Northern Ireland.",
                "date_of_inclusion_on_catalog": "19850502",
            },
            "collect": {
                "location": {
                    "countryOfOriginCode": "Unknown",
                    "state": "Unknown",
                    "municipality": "Unknown",
                    "site": "Unknown",
                }
            },
            "growth": {
                "recommended_medium_for_growth": ["1", "2"],
                "recommended_growth_temperature": "30",
            },
            "genetics": {
                "Markers": [{"marker_type": "16S rRNA", "INSDC": "X76436"}],
                "gmo": False,
                "ploidy": 1,
            },
            "other_culture_collection_numbers": [
                {"collection_code": "ATCC", "accession_number": "27647"},
                {"collection_code": "DSM", "accession_number": "485"},
                {"collection_code": "NCIB", "accession_number": "10436"},
                {"collection_code": "NCIB", "accession_number": "8772"},
                {"collection_code": "NCTC", "accession_number": "4553"},
                {"collection_code": "Vedder", "accession_number": "1"},
            ],
            "restriction_on_use": "commercial_use_with_agreement",
            "nagoya_protocol": "nagoya_does_not_apply",
            "strain_from_a_registered_collection": False,
            "risk_group": "1",
            "history_of_deposit": ["NCTC", "A. Vedder"],
            "form_of_supply": ["Lyo"],
        }
        strain = Strain(strain_data)
        return strain

    def xtest_create_strain_strain_from_biolomics(self):
        client = BiolomicsClient(
            server_url=SERVER_URL,
            client_id=CLIENT_ID,
            client_secret=SECRET_ID,
            username=USERNAME,
            password=PASSWORD,
        )
        strain = self._build_strain()
        biolomics_strain = serialize_to_biolomics(strain)
        returned_strain = create_strain(biolomics_strain, client)
        id = returned_strain["RecordId"]
        remove_strain(id, client)

        strain.id.number = "test_peio"

        returned_strain = create_strain(biolomics_strain, client)
        id = returned_strain["RecordId"]
        remove_strain(id, client)

        try:
            remove_strain(id, client)
            self.fail()
        except RuntimeError:
            pass


if __name__ == "__main__":
    # import sys;sys.argv = ['',
    #                        'BiolomicsWriter.test_mirri_excel_parser_invalid']
    unittest.main()
