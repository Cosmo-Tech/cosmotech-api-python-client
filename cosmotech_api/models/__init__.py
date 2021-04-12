# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from cosmotech_api.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from cosmotech_api.model.analysis_parameter import AnalysisParameter
from cosmotech_api.model.analysis_parameter_group import AnalysisParameterGroup
from cosmotech_api.model.analysis_resource_storage import AnalysisResourceStorage
from cosmotech_api.model.connector import Connector
from cosmotech_api.model.connector_parameter import ConnectorParameter
from cosmotech_api.model.connector_parameter_group import ConnectorParameterGroup
from cosmotech_api.model.dataset import Dataset
from cosmotech_api.model.dataset_compatibility import DatasetCompatibility
from cosmotech_api.model.dataset_connector import DatasetConnector
from cosmotech_api.model.dataset_copy_parameters import DatasetCopyParameters
from cosmotech_api.model.organization import Organization
from cosmotech_api.model.organization_user import OrganizationUser
from cosmotech_api.model.scenario import Scenario
from cosmotech_api.model.scenario_all_of import ScenarioAllOf
from cosmotech_api.model.scenario_analysis import ScenarioAnalysis
from cosmotech_api.model.scenario_analysis_parameter_value import ScenarioAnalysisParameterValue
from cosmotech_api.model.scenario_base import ScenarioBase
from cosmotech_api.model.scenario_changed_parameter_value import ScenarioChangedParameterValue
from cosmotech_api.model.scenario_comparison_result import ScenarioComparisonResult
from cosmotech_api.model.scenario_data_warehouse_query import ScenarioDataWarehouseQuery
from cosmotech_api.model.scenario_data_warehouse_query_result import ScenarioDataWarehouseQueryResult
from cosmotech_api.model.scenario_failed_analysis import ScenarioFailedAnalysis
from cosmotech_api.model.scenario_failed_analysis_all_of import ScenarioFailedAnalysisAllOf
from cosmotech_api.model.scenario_running_analysis import ScenarioRunningAnalysis
from cosmotech_api.model.scenario_running_analysis_all_of import ScenarioRunningAnalysisAllOf
from cosmotech_api.model.scenario_successful_analysis import ScenarioSuccessfulAnalysis
from cosmotech_api.model.scenario_successful_analysis_all_of import ScenarioSuccessfulAnalysisAllOf
from cosmotech_api.model.scenario_user import ScenarioUser
from cosmotech_api.model.simulator import Simulator
from cosmotech_api.model.simulator_analysis import SimulatorAnalysis
from cosmotech_api.model.translated_labels import TranslatedLabels
from cosmotech_api.model.user import User
from cosmotech_api.model.user_details import UserDetails
from cosmotech_api.model.user_details_all_of import UserDetailsAllOf
from cosmotech_api.model.user_organization import UserOrganization
from cosmotech_api.model.validator import Validator
from cosmotech_api.model.validator_run import ValidatorRun
from cosmotech_api.model.workspace import Workspace
from cosmotech_api.model.workspace_services import WorkspaceServices
from cosmotech_api.model.workspace_simulator import WorkspaceSimulator
from cosmotech_api.model.workspace_user import WorkspaceUser
from cosmotech_api.model.workspace_web_app import WorkspaceWebApp
