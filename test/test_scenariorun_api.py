"""
    Cosmo Tech Platform API

    Cosmo Tech Platform API  # noqa: E501

    The version of the OpenAPI document: 3.1.10
    Contact: platform@cosmotech.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import cosmotech_api
from cosmotech_api.api.scenariorun_api import ScenariorunApi  # noqa: E501


class TestScenariorunApi(unittest.TestCase):
    """ScenariorunApi unit test stubs"""

    def setUp(self):
        self.api = ScenariorunApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_historical_data_organization(self):
        """Test case for delete_historical_data_organization

        Delete all historical ScenarioRuns in the Organization  # noqa: E501
        """
        pass

    def test_delete_historical_data_scenario(self):
        """Test case for delete_historical_data_scenario

        Delete all historical ScenarioRuns in the Scenario  # noqa: E501
        """
        pass

    def test_delete_historical_data_workspace(self):
        """Test case for delete_historical_data_workspace

        Delete all historical ScenarioRuns in the Workspace  # noqa: E501
        """
        pass

    def test_delete_scenario_run(self):
        """Test case for delete_scenario_run

        Delete a scenariorun  # noqa: E501
        """
        pass

    def test_find_scenario_run_by_id(self):
        """Test case for find_scenario_run_by_id

        Get the details of a scenariorun  # noqa: E501
        """
        pass

    def test_get_scenario_run_cumulated_logs(self):
        """Test case for get_scenario_run_cumulated_logs

        Get the cumulated logs of a scenariorun  # noqa: E501
        """
        pass

    def test_get_scenario_run_logs(self):
        """Test case for get_scenario_run_logs

        get the logs for the ScenarioRun  # noqa: E501
        """
        pass

    def test_get_scenario_run_status(self):
        """Test case for get_scenario_run_status

        get the status for the ScenarioRun  # noqa: E501
        """
        pass

    def test_get_scenario_runs(self):
        """Test case for get_scenario_runs

        get the list of ScenarioRuns for the Scenario  # noqa: E501
        """
        pass

    def test_get_workspace_scenario_runs(self):
        """Test case for get_workspace_scenario_runs

        get the list of ScenarioRuns for the Workspace  # noqa: E501
        """
        pass

    def test_run_scenario(self):
        """Test case for run_scenario

        run a ScenarioRun for the Scenario  # noqa: E501
        """
        pass

    def test_search_scenario_runs(self):
        """Test case for search_scenario_runs

        Search ScenarioRuns  # noqa: E501
        """
        pass

    def test_start_scenario_run_containers(self):
        """Test case for start_scenario_run_containers

        Start a new scenariorun with raw containers definition  # noqa: E501
        """
        pass

    def test_stop_scenario_run(self):
        """Test case for stop_scenario_run

        stop a ScenarioRun for the Scenario  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
