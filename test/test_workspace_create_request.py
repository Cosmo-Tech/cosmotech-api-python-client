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

from cosmotech_api.models.workspace_create_request import WorkspaceCreateRequest

class TestWorkspaceCreateRequest(unittest.TestCase):
    """WorkspaceCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkspaceCreateRequest:
        """Test WorkspaceCreateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkspaceCreateRequest`
        """
        model = WorkspaceCreateRequest()
        if include_optional:
            return WorkspaceCreateRequest(
                key = '0',
                name = 'FranceOffice',
                description = '',
                version = '1.0.0',
                tags = [
                    ''
                    ],
                solution = cosmotech_api.models.workspace_solution.WorkspaceSolution(
                    solution_id = 'sol-HqXzyCBw3_uufVPI', 
                    run_template_filter = [
                        ''
                        ], 
                    default_run_template_dataset = { }, ),
                web_app = cosmotech_api.models.workspace_web_app.WorkspaceWebApp(
                    url = '', 
                    iframes = { }, 
                    options = { }, ),
                dataset_copy = True,
                security = cosmotech_api.models.workspace_security.WorkspaceSecurity(
                    default = '', 
                    access_control_list = [
                        cosmotech_api.models.workspace_access_control.WorkspaceAccessControl(
                            id = '', 
                            role = '', )
                        ], )
            )
        else:
            return WorkspaceCreateRequest(
                key = '0',
                name = 'FranceOffice',
                solution = cosmotech_api.models.workspace_solution.WorkspaceSolution(
                    solution_id = 'sol-HqXzyCBw3_uufVPI', 
                    run_template_filter = [
                        ''
                        ], 
                    default_run_template_dataset = { }, ),
        )
        """

    def testWorkspaceCreateRequest(self):
        """Test WorkspaceCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
