from biolomirri.tests.utils import create_full_data_strain
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
    raise ImportError(
        'You need a secrets.py in the project dir. with CLIENT_ID, SECRET_ID, USERNAME, PASSWORD')


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

    def xtest_create_strain(self):
        client = BiolomicsMirriClient(SERVER_URL, CLIENT_ID, SECRET_ID,
                                      USERNAME, PASSWORD)
        strain = create_full_data_strain()
        response = client.create_strain(strain)
        print(response)


if __name__ == "__main__":
    # import sys;sys.argv = ['',
    #                        'BiolomicsWriter.test_mirri_excel_parser_invalid']
    unittest.main()
