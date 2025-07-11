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

from cosmotech_api.models.dataset_part_update_request import DatasetPartUpdateRequest

class TestDatasetPartUpdateRequest(unittest.TestCase):
    """DatasetPartUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasetPartUpdateRequest:
        """Test DatasetPartUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatasetPartUpdateRequest`
        """
        model = DatasetPartUpdateRequest()
        if include_optional:
            return DatasetPartUpdateRequest(
                description = '',
                tags = [
                    ''
                    ]
            )
        else:
            return DatasetPartUpdateRequest(
        )
        """

    def testDatasetPartUpdateRequest(self):
        """Test DatasetPartUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
