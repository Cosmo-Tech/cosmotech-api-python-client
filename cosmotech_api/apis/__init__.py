
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.connector_api import ConnectorApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from cosmotech_api.api.connector_api import ConnectorApi
from cosmotech_api.api.dataset_api import DatasetApi
from cosmotech_api.api.organization_api import OrganizationApi
from cosmotech_api.api.scenario_api import ScenarioApi
from cosmotech_api.api.scenariorun_api import ScenariorunApi
from cosmotech_api.api.solution_api import SolutionApi
from cosmotech_api.api.user_api import UserApi
from cosmotech_api.api.validator_api import ValidatorApi
from cosmotech_api.api.workspace_api import WorkspaceApi
