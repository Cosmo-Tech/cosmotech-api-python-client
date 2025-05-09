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

from cosmotech_api.models.workspace_edit_info import WorkspaceEditInfo

class TestWorkspaceEditInfo(unittest.TestCase):
    """WorkspaceEditInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkspaceEditInfo:
        """Test WorkspaceEditInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkspaceEditInfo`
        """
        model = WorkspaceEditInfo()
        if include_optional:
            return WorkspaceEditInfo(
                timestamp = 56,
                user_id = ''
            )
        else:
            return WorkspaceEditInfo(
                timestamp = 56,
                user_id = '',
        )
        """

    def testWorkspaceEditInfo(self):
        """Test WorkspaceEditInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
