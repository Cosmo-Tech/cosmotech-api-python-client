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

from cosmotech_api.models.connector import Connector

class TestConnector(unittest.TestCase):
    """Connector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Connector:
        """Test Connector
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Connector`
        """
        model = Connector()
        if include_optional:
            return Connector(
                id = '',
                key = '',
                name = '',
                description = '',
                repository = '',
                version = '',
                tags = [
                    ''
                    ],
                owner_id = '',
                url = '',
                io_types = [
                    'read'
                    ],
                parameter_groups = [
                    cosmotech_api.models.connector_parameter_group.ConnectorParameterGroup(
                        id = '', 
                        label = '', 
                        parameters = [
                            cosmotech_api.models.connector_parameter.ConnectorParameter(
                                id = '', 
                                label = '', 
                                value_type = '', 
                                options = [
                                    ''
                                    ], 
                                default = '', 
                                env_var = '', )
                            ], )
                    ]
            )
        else:
            return Connector(
        )
        """

    def testConnector(self):
        """Test Connector"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
