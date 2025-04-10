# coding: utf-8

"""
    Cosmo Tech Platform API

    Cosmo Tech Platform API

    The version of the OpenAPI document: 5.0.1-SNAPSHOT
    Contact: platform@cosmotech.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cosmotech_api.models.dataset_connector import DatasetConnector

class TestDatasetConnector(unittest.TestCase):
    """DatasetConnector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasetConnector:
        """Test DatasetConnector
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatasetConnector`
        """
        model = DatasetConnector()
        if include_optional:
            return DatasetConnector(
                id = '',
                name = '',
                version = '',
                parameters_values = {
                    'key' : ''
                    }
            )
        else:
            return DatasetConnector(
        )
        """

    def testDatasetConnector(self):
        """Test DatasetConnector"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
