
from biolomirri.remote.biolomics_client import BiolomicsMirriClient, SERVER_URL
import unittest
from pprint import pprint
from biolomirri.serializers import serialize_to_biolomics
from biolomirri.tests.utils import create_full_data_strain
try:
    from biolomirri.secrets import CLIENT_ID, SECRET_ID, USERNAME, PASSWORD
except ImportError:
    raise ImportError(
        'You need a secrets.py in the project dir. with CLIENT_ID, SECRET_ID, USERNAME, PASSWORD')


class BiolomicsWriter(unittest.TestCase):
    def test_serialize_basic(self):
        strain = create_full_data_strain()
        strain = serialize_to_biolomics(strain, client=None)
        # pprint(strain)

    def test_serialize_basic_remote(self):
        client = BiolomicsMirriClient(SERVER_URL, CLIENT_ID, SECRET_ID,
                                      USERNAME, PASSWORD)
        strain = create_full_data_strain()
        strain.growth.recommended_media = ['AAA']
        strain = serialize_to_biolomics(strain, client=client)
        # pprint(strain)


if __name__ == "__main__":
    # import sys;sys.argv = ['',
    #                        'BiolomicsWriter.test_mirri_excel_parser_invalid']
    unittest.main()
