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

from cosmotech_api.models.run_template_parameter_group_create_request import RunTemplateParameterGroupCreateRequest

class TestRunTemplateParameterGroupCreateRequest(unittest.TestCase):
    """RunTemplateParameterGroupCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RunTemplateParameterGroupCreateRequest:
        """Test RunTemplateParameterGroupCreateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RunTemplateParameterGroupCreateRequest`
        """
        model = RunTemplateParameterGroupCreateRequest()
        if include_optional:
            return RunTemplateParameterGroupCreateRequest(
                id = '0',
                description = '',
                labels = {
                    'key' : ''
                    },
                is_table = True,
                options = { },
                parent_id = '',
                parameters = [
                    ''
                    ]
            )
        else:
            return RunTemplateParameterGroupCreateRequest(
                id = '0',
        )
        """

    def testRunTemplateParameterGroupCreateRequest(self):
        """Test RunTemplateParameterGroupCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
