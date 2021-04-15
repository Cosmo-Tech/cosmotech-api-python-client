# cosmotech_api.SimulationApi

All URIs are relative to *https://api.azure.cosmo-platform.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_simulation**](SimulationApi.md#delete_simulation) | **DELETE** /organizations/{organization_id}/simulations/{simulation_id} | Delete a simulation
[**find_simulation_by_id**](SimulationApi.md#find_simulation_by_id) | **GET** /organizations/{organization_id}/simulations/{simulation_id} | Get the details of a simulation
[**get_scenario_simulation**](SimulationApi.md#get_scenario_simulation) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/simulations/{simulation_id} | get the Simulation for the Scenario
[**get_scenario_simulation_logs**](SimulationApi.md#get_scenario_simulation_logs) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/simulations/{simulation_id}/logs | get the logs for the Simulation
[**get_scenario_simulations**](SimulationApi.md#get_scenario_simulations) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/simulations | get the list of Simulations for the Scenario
[**get_workspace_simulations**](SimulationApi.md#get_workspace_simulations) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/simulations | get the list of Simulations for the Workspace
[**run_scenario**](SimulationApi.md#run_scenario) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/run | run a Simulation for the Scenario
[**search_simulation_logs**](SimulationApi.md#search_simulation_logs) | **POST** /organizations/{organization_id}/simulations/{simulation_id}/logs/search | Search the logs of a simulation
[**search_simulations**](SimulationApi.md#search_simulations) | **POST** /organizations/{organization_id}/simulations/search | Search Simulations
[**start_simulation_containers**](SimulationApi.md#start_simulation_containers) | **POST** /organizations/{organization_id}/simulations/startcontainers | Start a new simulation with raw containers definition
[**start_simulation_scenario**](SimulationApi.md#start_simulation_scenario) | **POST** /organizations/{organization_id}/simulations/start | Start a new simulation for a Scenario
[**start_simulation_simulator**](SimulationApi.md#start_simulation_simulator) | **POST** /organizations/{organization_id}/simulations/startsimulator | Start a new simulation for a Simulator Analysis


# **delete_simulation**
> Simulation delete_simulation(organization_id, simulation_id)

Delete a simulation

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulation_api
from cosmotech_api.model.simulation import Simulation
from pprint import pprint
# Defining the host is optional and defaults to https://api.azure.cosmo-platform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simulation_api.SimulationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    simulation_id = "simulation_id_example" # str | the Simulation identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete a simulation
        api_response = api_instance.delete_simulation(organization_id, simulation_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulationApi->delete_simulation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **simulation_id** | **str**| the Simulation identifier |

### Return type

[**Simulation**](Simulation.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the simulation details |  -  |
**400** | Bad request |  -  |
**404** | the Simulation specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_simulation_by_id**
> Simulation find_simulation_by_id(organization_id, simulation_id)

Get the details of a simulation

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulation_api
from cosmotech_api.model.simulation import Simulation
from pprint import pprint
# Defining the host is optional and defaults to https://api.azure.cosmo-platform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simulation_api.SimulationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    simulation_id = "simulation_id_example" # str | the Simulation identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a simulation
        api_response = api_instance.find_simulation_by_id(organization_id, simulation_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulationApi->find_simulation_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **simulation_id** | **str**| the Simulation identifier |

### Return type

[**Simulation**](Simulation.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Simulation details |  -  |
**404** | the Simulation specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_simulation**
> Simulation get_scenario_simulation(organization_id, workspace_id, scenario_id, simulation_id)

get the Simulation for the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulation_api
from cosmotech_api.model.simulation import Simulation
from pprint import pprint
# Defining the host is optional and defaults to https://api.azure.cosmo-platform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simulation_api.SimulationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier
    simulation_id = "simulation_id_example" # str | the Simulation identifier

    # example passing only required values which don't have defaults set
    try:
        # get the Simulation for the Scenario
        api_response = api_instance.get_scenario_simulation(organization_id, workspace_id, scenario_id, simulation_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulationApi->get_scenario_simulation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |
 **simulation_id** | **str**| the Simulation identifier |

### Return type

[**Simulation**](Simulation.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the simulation details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_simulation_logs**
> SimulationLogs get_scenario_simulation_logs(organization_id, workspace_id, scenario_id, simulation_id)

get the logs for the Simulation

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulation_api
from cosmotech_api.model.simulation_logs import SimulationLogs
from pprint import pprint
# Defining the host is optional and defaults to https://api.azure.cosmo-platform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simulation_api.SimulationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier
    simulation_id = "simulation_id_example" # str | the Simulation identifier

    # example passing only required values which don't have defaults set
    try:
        # get the logs for the Simulation
        api_response = api_instance.get_scenario_simulation_logs(organization_id, workspace_id, scenario_id, simulation_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulationApi->get_scenario_simulation_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |
 **simulation_id** | **str**| the Simulation identifier |

### Return type

[**SimulationLogs**](SimulationLogs.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the simulation logs details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_simulations**
> [SimulationBase] get_scenario_simulations(organization_id, workspace_id, scenario_id)

get the list of Simulations for the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulation_api
from cosmotech_api.model.simulation_base import SimulationBase
from pprint import pprint
# Defining the host is optional and defaults to https://api.azure.cosmo-platform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simulation_api.SimulationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier

    # example passing only required values which don't have defaults set
    try:
        # get the list of Simulations for the Scenario
        api_response = api_instance.get_scenario_simulations(organization_id, workspace_id, scenario_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulationApi->get_scenario_simulations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |

### Return type

[**[SimulationBase]**](SimulationBase.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the simulation details list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_simulations**
> [SimulationBase] get_workspace_simulations(organization_id, workspace_id)

get the list of Simulations for the Workspace

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulation_api
from cosmotech_api.model.simulation_base import SimulationBase
from pprint import pprint
# Defining the host is optional and defaults to https://api.azure.cosmo-platform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simulation_api.SimulationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier

    # example passing only required values which don't have defaults set
    try:
        # get the list of Simulations for the Workspace
        api_response = api_instance.get_workspace_simulations(organization_id, workspace_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulationApi->get_workspace_simulations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |

### Return type

[**[SimulationBase]**](SimulationBase.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the simulation details list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_scenario**
> SimulationBase run_scenario(organization_id, workspace_id, scenario_id)

run a Simulation for the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulation_api
from cosmotech_api.model.simulation_base import SimulationBase
from pprint import pprint
# Defining the host is optional and defaults to https://api.azure.cosmo-platform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simulation_api.SimulationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier

    # example passing only required values which don't have defaults set
    try:
        # run a Simulation for the Scenario
        api_response = api_instance.run_scenario(organization_id, workspace_id, scenario_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulationApi->run_scenario: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |

### Return type

[**SimulationBase**](SimulationBase.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the simulation details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_simulation_logs**
> SimulationLogs search_simulation_logs(organization_id, simulation_id, simulation_logs_options)

Search the logs of a simulation

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulation_api
from cosmotech_api.model.simulation_logs import SimulationLogs
from cosmotech_api.model.simulation_logs_options import SimulationLogsOptions
from pprint import pprint
# Defining the host is optional and defaults to https://api.azure.cosmo-platform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simulation_api.SimulationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    simulation_id = "simulation_id_example" # str | the Simulation identifier
    simulation_logs_options = SimulationLogsOptions(
        container_ids=[
            "container_ids_example",
        ],
        plain_text=True,
    ) # SimulationLogsOptions | the options to search logs

    # example passing only required values which don't have defaults set
    try:
        # Search the logs of a simulation
        api_response = api_instance.search_simulation_logs(organization_id, simulation_id, simulation_logs_options)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulationApi->search_simulation_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **simulation_id** | **str**| the Simulation identifier |
 **simulation_logs_options** | [**SimulationLogsOptions**](SimulationLogsOptions.md)| the options to search logs |

### Return type

[**SimulationLogs**](SimulationLogs.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Simulation logs |  -  |
**400** | Bad request |  -  |
**404** | the Simulation specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_simulations**
> [SimulationBase] search_simulations(organization_id, simulation_search)

Search Simulations

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulation_api
from cosmotech_api.model.simulation_search import SimulationSearch
from cosmotech_api.model.simulation_base import SimulationBase
from pprint import pprint
# Defining the host is optional and defaults to https://api.azure.cosmo-platform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simulation_api.SimulationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    simulation_search = SimulationSearch(
        simulator_id="simulator_id_example",
        simulator_analysis_id="simulator_analysis_id_example",
        workspace_id="workspace_id_example",
        scenario_id="scenario_id_example",
        state="state_example",
        job_id="job_id_example",
        owner_id="owner_id_example",
    ) # SimulationSearch | the Simulation search parameters

    # example passing only required values which don't have defaults set
    try:
        # Search Simulations
        api_response = api_instance.search_simulations(organization_id, simulation_search)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulationApi->search_simulations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **simulation_search** | [**SimulationSearch**](SimulationSearch.md)| the Simulation search parameters |

### Return type

[**[SimulationBase]**](SimulationBase.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the simulation details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_simulation_containers**
> Simulation start_simulation_containers(organization_id, simulation_start_containers)

Start a new simulation with raw containers definition

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulation_api
from cosmotech_api.model.simulation import Simulation
from cosmotech_api.model.simulation_start_containers import SimulationStartContainers
from pprint import pprint
# Defining the host is optional and defaults to https://api.azure.cosmo-platform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simulation_api.SimulationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    simulation_start_containers = SimulationStartContainers(
        node_label="node_label_example",
        init_containers=[
            SimulationContainers(
                id="id_example",
                env_vars={},
                image="image_example",
                run_args=[
                    "run_args_example",
                ],
            ),
        ],
        main_container=SimulationContainers(
            id="id_example",
            env_vars={},
            image="image_example",
            run_args=[],
        ),
    ) # SimulationStartContainers | the raw containers definition

    # example passing only required values which don't have defaults set
    try:
        # Start a new simulation with raw containers definition
        api_response = api_instance.start_simulation_containers(organization_id, simulation_start_containers)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulationApi->start_simulation_containers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **simulation_start_containers** | [**SimulationStartContainers**](SimulationStartContainers.md)| the raw containers definition |

### Return type

[**Simulation**](Simulation.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | the simulation details |  -  |
**400** | Bad request |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_simulation_scenario**
> Simulation start_simulation_scenario(organization_id, simulation_start_scenario)

Start a new simulation for a Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulation_api
from cosmotech_api.model.simulation import Simulation
from cosmotech_api.model.simulation_start_scenario import SimulationStartScenario
from pprint import pprint
# Defining the host is optional and defaults to https://api.azure.cosmo-platform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simulation_api.SimulationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    simulation_start_scenario = SimulationStartScenario(
        workspace_id="workspace_id_example",
        scenario_id="scenario_id_example",
    ) # SimulationStartScenario | the Scenario information to start

    # example passing only required values which don't have defaults set
    try:
        # Start a new simulation for a Scenario
        api_response = api_instance.start_simulation_scenario(organization_id, simulation_start_scenario)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulationApi->start_simulation_scenario: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **simulation_start_scenario** | [**SimulationStartScenario**](SimulationStartScenario.md)| the Scenario information to start |

### Return type

[**Simulation**](Simulation.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | the simulation details |  -  |
**400** | Bad request |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_simulation_simulator**
> Simulation start_simulation_simulator(organization_id, simulation_start_simulator)

Start a new simulation for a Simulator Analysis

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulation_api
from cosmotech_api.model.simulation import Simulation
from cosmotech_api.model.simulation_start_simulator import SimulationStartSimulator
from pprint import pprint
# Defining the host is optional and defaults to https://api.azure.cosmo-platform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simulation_api.SimulationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    simulation_start_simulator = SimulationStartSimulator(
        simulator_id="simulator_id_example",
        simulator_analysis_id="simulator_analysis_id_example",
        dataset_list=[
            "dataset_list_example",
        ],
        parameters_values=[
            SimulationAnalysisParameterValue(
                parameter_id="parameter_id_example",
                var_type="var_type_example",
                value="value_example",
            ),
        ],
        send_input_to_data_warehouse=True,
        data_warehouse_db="data_warehouse_db_example",
        results_event_bus_resource_uri="results_event_bus_resource_uri_example",
        simulation_event_bus_resource_uri="simulation_event_bus_resource_uri_example",
    ) # SimulationStartSimulator | the Simulator Analysis information to start

    # example passing only required values which don't have defaults set
    try:
        # Start a new simulation for a Simulator Analysis
        api_response = api_instance.start_simulation_simulator(organization_id, simulation_start_simulator)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulationApi->start_simulation_simulator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **simulation_start_simulator** | [**SimulationStartSimulator**](SimulationStartSimulator.md)| the Simulator Analysis information to start |

### Return type

[**Simulation**](Simulation.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | the simulation details |  -  |
**400** | Bad request |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

