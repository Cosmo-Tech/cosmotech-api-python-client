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

from cosmotech_api.api.workspace_api import WorkspaceApi


class TestWorkspaceApi(unittest.TestCase):
    """WorkspaceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WorkspaceApi()

    def tearDown(self) -> None:
        pass

    def test_create_workspace(self) -> None:
        """Test case for create_workspace

        Create a new workspace
        """
        pass

    def test_create_workspace_access_control(self) -> None:
        """Test case for create_workspace_access_control

        Add a control access to the Workspace
        """
        pass

    def test_create_workspace_file(self) -> None:
        """Test case for create_workspace_file

        Upload a file for the Workspace
        """
        pass

    def test_delete_workspace(self) -> None:
        """Test case for delete_workspace

        Delete a workspace
        """
        pass

    def test_delete_workspace_access_control(self) -> None:
        """Test case for delete_workspace_access_control

        Remove the specified access from the given Workspace
        """
        pass

    def test_delete_workspace_file(self) -> None:
        """Test case for delete_workspace_file

        Delete a workspace file
        """
        pass

    def test_delete_workspace_files(self) -> None:
        """Test case for delete_workspace_files

        Delete all Workspace files
        """
        pass

    def test_get_workspace(self) -> None:
        """Test case for get_workspace

        Get the details of a workspace
        """
        pass

    def test_get_workspace_access_control(self) -> None:
        """Test case for get_workspace_access_control

        Get a control access for the Workspace
        """
        pass

    def test_get_workspace_file(self) -> None:
        """Test case for get_workspace_file

        Download the Workspace File specified
        """
        pass

    def test_get_workspace_security(self) -> None:
        """Test case for get_workspace_security

        Get the Workspace security information
        """
        pass

    def test_list_workspace_files(self) -> None:
        """Test case for list_workspace_files

        List all Workspace files
        """
        pass

    def test_list_workspace_role_permissions(self) -> None:
        """Test case for list_workspace_role_permissions

        Get the Workspace permission by given role
        """
        pass

    def test_list_workspace_security_users(self) -> None:
        """Test case for list_workspace_security_users

        Get the Workspace security users list
        """
        pass

    def test_list_workspaces(self) -> None:
        """Test case for list_workspaces

        List all Workspaces
        """
        pass

    def test_update_workspace(self) -> None:
        """Test case for update_workspace

        Update a workspace
        """
        pass

    def test_update_workspace_access_control(self) -> None:
        """Test case for update_workspace_access_control

        Update the specified access to User for a Workspace
        """
        pass

    def test_update_workspace_default_security(self) -> None:
        """Test case for update_workspace_default_security

        Update the Workspace default security
        """
        pass


if __name__ == '__main__':
    unittest.main()
