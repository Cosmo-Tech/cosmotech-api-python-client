"""
    Cosmo Tech Platform API

    Cosmo Tech Platform API  # noqa: E501

    The version of the OpenAPI document: 3.1.10
    Contact: platform@cosmotech.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import cosmotech_api
from cosmotech_api.model.scenario_job_state import ScenarioJobState
from cosmotech_api.model.scenario_last_run import ScenarioLastRun
from cosmotech_api.model.scenario_resource_sizing import ScenarioResourceSizing
from cosmotech_api.model.scenario_run_template_parameter_value import ScenarioRunTemplateParameterValue
from cosmotech_api.model.scenario_security import ScenarioSecurity
from cosmotech_api.model.scenario_validation_status import ScenarioValidationStatus
globals()['ScenarioJobState'] = ScenarioJobState
globals()['ScenarioLastRun'] = ScenarioLastRun
globals()['ScenarioResourceSizing'] = ScenarioResourceSizing
globals()['ScenarioRunTemplateParameterValue'] = ScenarioRunTemplateParameterValue
globals()['ScenarioSecurity'] = ScenarioSecurity
globals()['ScenarioValidationStatus'] = ScenarioValidationStatus
from cosmotech_api.model.scenario import Scenario


class TestScenario(unittest.TestCase):
    """Scenario unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScenario(self):
        """Test Scenario"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Scenario()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
