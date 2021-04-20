# cosmotech_api.ScenariorunApi

All URIs are relative to *https://api.azure.cosmo-platform.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_scenario_run**](ScenariorunApi.md#delete_scenario_run) | **DELETE** /organizations/{organization_id}/scenarioruns/{scenariorun_id} | Delete a scenariorun
[**find_scenario_run_by_id**](ScenariorunApi.md#find_scenario_run_by_id) | **GET** /organizations/{organization_id}/scenarioruns/{scenariorun_id} | Get the details of a scenariorun
[**get_scenario_scenario_run**](ScenariorunApi.md#get_scenario_scenario_run) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/scenarioruns/{scenariorun_id} | get the ScenarioRun for the Scenario
[**get_scenario_scenario_run_logs**](ScenariorunApi.md#get_scenario_scenario_run_logs) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/scenarioruns/{scenariorun_id}/logs | get the logs for the ScenarioRun
[**get_scenario_scenario_runs**](ScenariorunApi.md#get_scenario_scenario_runs) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/scenarioruns | get the list of ScenarioRuns for the Scenario
[**get_workspace_scenario_runs**](ScenariorunApi.md#get_workspace_scenario_runs) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarioruns | get the list of ScenarioRuns for the Workspace
[**run_scenario**](ScenariorunApi.md#run_scenario) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/run | run a ScenarioRun for the Scenario
[**search_scenario_run_logs**](ScenariorunApi.md#search_scenario_run_logs) | **POST** /organizations/{organization_id}/scenarioruns/{scenariorun_id}/logs/search | Search the logs of a scenariorun
[**search_scenario_runs**](ScenariorunApi.md#search_scenario_runs) | **POST** /organizations/{organization_id}/scenarioruns/search | Search ScenarioRuns
[**start_scenario_run_containers**](ScenariorunApi.md#start_scenario_run_containers) | **POST** /organizations/{organization_id}/scenarioruns/startcontainers | Start a new scenariorun with raw containers definition
[**start_scenario_run_scenario**](ScenariorunApi.md#start_scenario_run_scenario) | **POST** /organizations/{organization_id}/scenarioruns/start | Start a new scenariorun for a Scenario
[**start_scenario_run_solution**](ScenariorunApi.md#start_scenario_run_solution) | **POST** /organizations/{organization_id}/scenarioruns/startsolution | Start a new scenariorun for a Solution Run Template


# **delete_scenario_run**
> ScenarioRun delete_scenario_run(organization_id, scenariorun_id)

Delete a scenariorun

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run import ScenarioRun
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
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    scenariorun_id = "scenariorun_id_example" # str | the ScenarioRun identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete a scenariorun
        api_response = api_instance.delete_scenario_run(organization_id, scenariorun_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->delete_scenario_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **scenariorun_id** | **str**| the ScenarioRun identifier |

### Return type

[**ScenarioRun**](ScenarioRun.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the scenariorun details |  -  |
**400** | Bad request |  -  |
**404** | the ScenarioRun specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_scenario_run_by_id**
> ScenarioRun find_scenario_run_by_id(organization_id, scenariorun_id)

Get the details of a scenariorun

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run import ScenarioRun
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
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    scenariorun_id = "scenariorun_id_example" # str | the ScenarioRun identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a scenariorun
        api_response = api_instance.find_scenario_run_by_id(organization_id, scenariorun_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->find_scenario_run_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **scenariorun_id** | **str**| the ScenarioRun identifier |

### Return type

[**ScenarioRun**](ScenarioRun.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the ScenarioRun details |  -  |
**404** | the ScenarioRun specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_scenario_run**
> ScenarioRun get_scenario_scenario_run(organization_id, workspace_id, scenario_id, scenariorun_id)

get the ScenarioRun for the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run import ScenarioRun
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
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier
    scenariorun_id = "scenariorun_id_example" # str | the ScenarioRun identifier

    # example passing only required values which don't have defaults set
    try:
        # get the ScenarioRun for the Scenario
        api_response = api_instance.get_scenario_scenario_run(organization_id, workspace_id, scenario_id, scenariorun_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->get_scenario_scenario_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |
 **scenariorun_id** | **str**| the ScenarioRun identifier |

### Return type

[**ScenarioRun**](ScenarioRun.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the scenariorun details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_scenario_run_logs**
> ScenarioRunLogs get_scenario_scenario_run_logs(organization_id, workspace_id, scenario_id, scenariorun_id)

get the logs for the ScenarioRun

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run_logs import ScenarioRunLogs
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
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier
    scenariorun_id = "scenariorun_id_example" # str | the ScenarioRun identifier

    # example passing only required values which don't have defaults set
    try:
        # get the logs for the ScenarioRun
        api_response = api_instance.get_scenario_scenario_run_logs(organization_id, workspace_id, scenario_id, scenariorun_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->get_scenario_scenario_run_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |
 **scenariorun_id** | **str**| the ScenarioRun identifier |

### Return type

[**ScenarioRunLogs**](ScenarioRunLogs.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the scenariorun logs details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_scenario_runs**
> [ScenarioRunBase] get_scenario_scenario_runs(organization_id, workspace_id, scenario_id)

get the list of ScenarioRuns for the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run_base import ScenarioRunBase
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
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier

    # example passing only required values which don't have defaults set
    try:
        # get the list of ScenarioRuns for the Scenario
        api_response = api_instance.get_scenario_scenario_runs(organization_id, workspace_id, scenario_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->get_scenario_scenario_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |

### Return type

[**[ScenarioRunBase]**](ScenarioRunBase.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the scenariorun details list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_scenario_runs**
> [ScenarioRunBase] get_workspace_scenario_runs(organization_id, workspace_id)

get the list of ScenarioRuns for the Workspace

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run_base import ScenarioRunBase
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
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier

    # example passing only required values which don't have defaults set
    try:
        # get the list of ScenarioRuns for the Workspace
        api_response = api_instance.get_workspace_scenario_runs(organization_id, workspace_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->get_workspace_scenario_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |

### Return type

[**[ScenarioRunBase]**](ScenarioRunBase.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the scenariorun details list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_scenario**
> ScenarioRunBase run_scenario(organization_id, workspace_id, scenario_id)

run a ScenarioRun for the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run_base import ScenarioRunBase
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
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier

    # example passing only required values which don't have defaults set
    try:
        # run a ScenarioRun for the Scenario
        api_response = api_instance.run_scenario(organization_id, workspace_id, scenario_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->run_scenario: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |

### Return type

[**ScenarioRunBase**](ScenarioRunBase.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the scenariorun details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_scenario_run_logs**
> ScenarioRunLogs search_scenario_run_logs(organization_id, scenariorun_id, scenario_run_logs_options)

Search the logs of a scenariorun

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run_logs_options import ScenarioRunLogsOptions
from cosmotech_api.model.scenario_run_logs import ScenarioRunLogs
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
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    scenariorun_id = "scenariorun_id_example" # str | the ScenarioRun identifier
    scenario_run_logs_options = ScenarioRunLogsOptions(
        container_ids=[
            "container_ids_example",
        ],
        plain_text=True,
    ) # ScenarioRunLogsOptions | the options to search logs

    # example passing only required values which don't have defaults set
    try:
        # Search the logs of a scenariorun
        api_response = api_instance.search_scenario_run_logs(organization_id, scenariorun_id, scenario_run_logs_options)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->search_scenario_run_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **scenariorun_id** | **str**| the ScenarioRun identifier |
 **scenario_run_logs_options** | [**ScenarioRunLogsOptions**](ScenarioRunLogsOptions.md)| the options to search logs |

### Return type

[**ScenarioRunLogs**](ScenarioRunLogs.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the ScenarioRun logs |  -  |
**400** | Bad request |  -  |
**404** | the ScenarioRun specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_scenario_runs**
> [ScenarioRunBase] search_scenario_runs(organization_id, scenario_run_search)

Search ScenarioRuns

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run_base import ScenarioRunBase
from cosmotech_api.model.scenario_run_search import ScenarioRunSearch
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
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    scenario_run_search = ScenarioRunSearch(
        solution_id="solution_id_example",
        run_template_id="run_template_id_example",
        workspace_id="workspace_id_example",
        scenario_id="scenario_id_example",
        state="state_example",
        job_id="job_id_example",
        owner_id="owner_id_example",
    ) # ScenarioRunSearch | the ScenarioRun search parameters

    # example passing only required values which don't have defaults set
    try:
        # Search ScenarioRuns
        api_response = api_instance.search_scenario_runs(organization_id, scenario_run_search)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->search_scenario_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **scenario_run_search** | [**ScenarioRunSearch**](ScenarioRunSearch.md)| the ScenarioRun search parameters |

### Return type

[**[ScenarioRunBase]**](ScenarioRunBase.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the scenariorun details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_scenario_run_containers**
> ScenarioRun start_scenario_run_containers(organization_id, scenario_run_start_containers)

Start a new scenariorun with raw containers definition

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run_start_containers import ScenarioRunStartContainers
from cosmotech_api.model.scenario_run import ScenarioRun
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
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    scenario_run_start_containers = ScenarioRunStartContainers(
        node_label="node_label_example",
        init_containers=[
            ScenarioRunContainers(
                id="id_example",
                env_vars={},
                image="image_example",
                run_args=[
                    "run_args_example",
                ],
            ),
        ],
        main_container=ScenarioRunContainers(
            id="id_example",
            env_vars={},
            image="image_example",
            run_args=[],
        ),
    ) # ScenarioRunStartContainers | the raw containers definition

    # example passing only required values which don't have defaults set
    try:
        # Start a new scenariorun with raw containers definition
        api_response = api_instance.start_scenario_run_containers(organization_id, scenario_run_start_containers)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->start_scenario_run_containers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **scenario_run_start_containers** | [**ScenarioRunStartContainers**](ScenarioRunStartContainers.md)| the raw containers definition |

### Return type

[**ScenarioRun**](ScenarioRun.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | the scenariorun details |  -  |
**400** | Bad request |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_scenario_run_scenario**
> ScenarioRun start_scenario_run_scenario(organization_id, scenario_run_start)

Start a new scenariorun for a Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run_start import ScenarioRunStart
from cosmotech_api.model.scenario_run import ScenarioRun
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
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    scenario_run_start = ScenarioRunStart(
        workspace_id="workspace_id_example",
        scenario_id="scenario_id_example",
    ) # ScenarioRunStart | the Scenario information to start

    # example passing only required values which don't have defaults set
    try:
        # Start a new scenariorun for a Scenario
        api_response = api_instance.start_scenario_run_scenario(organization_id, scenario_run_start)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->start_scenario_run_scenario: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **scenario_run_start** | [**ScenarioRunStart**](ScenarioRunStart.md)| the Scenario information to start |

### Return type

[**ScenarioRun**](ScenarioRun.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | the scenariorun details |  -  |
**400** | Bad request |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_scenario_run_solution**
> ScenarioRun start_scenario_run_solution(organization_id, scenario_run_start_solution)

Start a new scenariorun for a Solution Run Template

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run_start_solution import ScenarioRunStartSolution
from cosmotech_api.model.scenario_run import ScenarioRun
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
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    scenario_run_start_solution = ScenarioRunStartSolution(
        solution_id="solution_id_example",
        run_template_id="run_template_id_example",
        dataset_list=[
            "dataset_list_example",
        ],
        parameters_values=[
            RunTemplateParameterValue(
                parameter_id="parameter_id_example",
                var_type="var_type_example",
                value="value_example",
            ),
        ],
        send_input_to_data_warehouse=True,
        data_warehouse_db="data_warehouse_db_example",
        results_event_bus_resource_uri="results_event_bus_resource_uri_example",
        scenariorun_event_bus_resource_uri="scenariorun_event_bus_resource_uri_example",
    ) # ScenarioRunStartSolution | the Solution Run Template information to start

    # example passing only required values which don't have defaults set
    try:
        # Start a new scenariorun for a Solution Run Template
        api_response = api_instance.start_scenario_run_solution(organization_id, scenario_run_start_solution)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->start_scenario_run_solution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **scenario_run_start_solution** | [**ScenarioRunStartSolution**](ScenarioRunStartSolution.md)| the Solution Run Template information to start |

### Return type

[**ScenarioRun**](ScenarioRun.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | the scenariorun details |  -  |
**400** | Bad request |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

