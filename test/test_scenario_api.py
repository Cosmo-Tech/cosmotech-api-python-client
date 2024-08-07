"""
    Cosmo Tech Platform API

    Cosmo Tech Platform API  # noqa: E501

    The version of the OpenAPI document: 3.1.10
    Contact: platform@cosmotech.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import cosmotech_api
from cosmotech_api.api.scenario_api import ScenarioApi  # noqa: E501


class TestScenarioApi(unittest.TestCase):
    """ScenarioApi unit test stubs"""

    def setUp(self):
        self.api = ScenarioApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_or_replace_scenario_parameter_values(self):
        """Test case for add_or_replace_scenario_parameter_values

        Add (or replace) Parameter Values for the Scenario specified  # noqa: E501
        """
        pass

    def test_add_scenario_access_control(self):
        """Test case for add_scenario_access_control

        Add a control access to the Scenario  # noqa: E501
        """
        pass

    def test_compare_scenarios(self):
        """Test case for compare_scenarios

        Compare the Scenario with another one and returns the difference for parameters values  # noqa: E501
        """
        pass

    def test_create_scenario(self):
        """Test case for create_scenario

        Create a new Scenario  # noqa: E501
        """
        pass

    def test_delete_all_scenarios(self):
        """Test case for delete_all_scenarios

        Delete all Scenarios of the Workspace  # noqa: E501
        """
        pass

    def test_delete_scenario(self):
        """Test case for delete_scenario

        Delete a scenario  # noqa: E501
        """
        pass

    def test_download_scenario_data(self):
        """Test case for download_scenario_data

        Download Scenario data  # noqa: E501
        """
        pass

    def test_find_all_scenarios(self):
        """Test case for find_all_scenarios

        List all Scenarios  # noqa: E501
        """
        pass

    def test_find_all_scenarios_by_validation_status(self):
        """Test case for find_all_scenarios_by_validation_status

        List all Scenarios by validation status  # noqa: E501
        """
        pass

    def test_find_scenario_by_id(self):
        """Test case for find_scenario_by_id

        Get the details of an scenario  # noqa: E501
        """
        pass

    def test_get_scenario_access_control(self):
        """Test case for get_scenario_access_control

        Get a control access for the Scenario  # noqa: E501
        """
        pass

    def test_get_scenario_data_download_job_info(self):
        """Test case for get_scenario_data_download_job_info

        Get Scenario data download URL  # noqa: E501
        """
        pass

    def test_get_scenario_permissions(self):
        """Test case for get_scenario_permissions

        Get the Scenario permission by given role  # noqa: E501
        """
        pass

    def test_get_scenario_security(self):
        """Test case for get_scenario_security

        Get the Scenario security information  # noqa: E501
        """
        pass

    def test_get_scenario_security_users(self):
        """Test case for get_scenario_security_users

        Get the Scenario security users list  # noqa: E501
        """
        pass

    def test_get_scenario_validation_status_by_id(self):
        """Test case for get_scenario_validation_status_by_id

        Get the validation status of an scenario  # noqa: E501
        """
        pass

    def test_get_scenarios_tree(self):
        """Test case for get_scenarios_tree

        Get the Scenarios Tree  # noqa: E501
        """
        pass

    def test_remove_all_scenario_parameter_values(self):
        """Test case for remove_all_scenario_parameter_values

        Remove all Parameter Values from the Scenario specified  # noqa: E501
        """
        pass

    def test_remove_scenario_access_control(self):
        """Test case for remove_scenario_access_control

        Remove the specified access from the given Organization Scenario  # noqa: E501
        """
        pass

    def test_set_scenario_default_security(self):
        """Test case for set_scenario_default_security

        Set the Scenario default security  # noqa: E501
        """
        pass

    def test_update_scenario(self):
        """Test case for update_scenario

        Update a scenario  # noqa: E501
        """
        pass

    def test_update_scenario_access_control(self):
        """Test case for update_scenario_access_control

        Update the specified access to User for a Scenario  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
