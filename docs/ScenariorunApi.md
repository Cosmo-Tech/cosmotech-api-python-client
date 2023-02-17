# cosmotech_api.ScenariorunApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_historical_data_organization**](ScenariorunApi.md#delete_historical_data_organization) | **DELETE** /organizations/{organization_id}/scenarioruns/historicaldata | Delete all historical ScenarioRuns in the Organization
[**delete_historical_data_scenario**](ScenariorunApi.md#delete_historical_data_scenario) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/scenarioruns/historicaldata | Delete all historical ScenarioRuns in the Scenario
[**delete_historical_data_workspace**](ScenariorunApi.md#delete_historical_data_workspace) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/scenarioruns/historicaldata | Delete all historical ScenarioRuns in the Workspace
[**delete_scenario_run**](ScenariorunApi.md#delete_scenario_run) | **DELETE** /organizations/{organization_id}/scenarioruns/{scenariorun_id} | Delete a scenariorun
[**find_scenario_run_by_id**](ScenariorunApi.md#find_scenario_run_by_id) | **GET** /organizations/{organization_id}/scenarioruns/{scenariorun_id} | Get the details of a scenariorun
[**get_scenario_run_cumulated_logs**](ScenariorunApi.md#get_scenario_run_cumulated_logs) | **GET** /organizations/{organization_id}/scenarioruns/{scenariorun_id}/cumulatedlogs | Get the cumulated logs of a scenariorun
[**get_scenario_run_logs**](ScenariorunApi.md#get_scenario_run_logs) | **GET** /organizations/{organization_id}/scenarioruns/{scenariorun_id}/logs | get the logs for the ScenarioRun
[**get_scenario_run_status**](ScenariorunApi.md#get_scenario_run_status) | **GET** /organizations/{organization_id}/scenarioruns/{scenariorun_id}/status | get the status for the ScenarioRun
[**get_scenario_runs**](ScenariorunApi.md#get_scenario_runs) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/scenarioruns | get the list of ScenarioRuns for the Scenario
[**get_workspace_scenario_runs**](ScenariorunApi.md#get_workspace_scenario_runs) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarioruns | get the list of ScenarioRuns for the Workspace
[**import_scenario_run**](ScenariorunApi.md#import_scenario_run) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/run/import | import a ScenarioRun for the Scenario
[**run_scenario**](ScenariorunApi.md#run_scenario) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/run | run a ScenarioRun for the Scenario
[**search_scenario_runs**](ScenariorunApi.md#search_scenario_runs) | **POST** /organizations/{organization_id}/scenarioruns/search | Search ScenarioRuns
[**start_scenario_run_containers**](ScenariorunApi.md#start_scenario_run_containers) | **POST** /organizations/{organization_id}/scenarioruns/startcontainers | Start a new scenariorun with raw containers definition
[**stop_scenario_run**](ScenariorunApi.md#stop_scenario_run) | **POST** /organizations/{organization_id}/scenarioruns/{scenariorun_id}/stop | stop a ScenarioRun for the Scenario


# **delete_historical_data_organization**
> delete_historical_data_organization(organization_id)

Delete all historical ScenarioRuns in the Organization

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev.api.cosmotech.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    delete_unknown = False # bool | condition to delete runs with an Unknown status (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete all historical ScenarioRuns in the Organization
        api_instance.delete_historical_data_organization(organization_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->delete_historical_data_organization: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete all historical ScenarioRuns in the Organization
        api_instance.delete_historical_data_organization(organization_id, delete_unknown=delete_unknown)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->delete_historical_data_organization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **delete_unknown** | **bool**| condition to delete runs with an Unknown status | [optional] if omitted the server will use the default value of False

### Return type

void (empty response body)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request succeeded |  -  |
**400** | Bad request |  -  |
**404** | the Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_historical_data_scenario**
> delete_historical_data_scenario(organization_id, workspace_id, scenario_id)

Delete all historical ScenarioRuns in the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev.api.cosmotech.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier
    delete_unknown = False # bool | condition to delete runs with an Unknown status (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete all historical ScenarioRuns in the Scenario
        api_instance.delete_historical_data_scenario(organization_id, workspace_id, scenario_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->delete_historical_data_scenario: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete all historical ScenarioRuns in the Scenario
        api_instance.delete_historical_data_scenario(organization_id, workspace_id, scenario_id, delete_unknown=delete_unknown)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->delete_historical_data_scenario: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |
 **delete_unknown** | **bool**| condition to delete runs with an Unknown status | [optional] if omitted the server will use the default value of False

### Return type

void (empty response body)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request succeeded |  -  |
**400** | Bad request |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_historical_data_workspace**
> delete_historical_data_workspace(organization_id, workspace_id)

Delete all historical ScenarioRuns in the Workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev.api.cosmotech.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    delete_unknown = False # bool | condition to delete runs with an Unknown status (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete all historical ScenarioRuns in the Workspace
        api_instance.delete_historical_data_workspace(organization_id, workspace_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->delete_historical_data_workspace: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete all historical ScenarioRuns in the Workspace
        api_instance.delete_historical_data_workspace(organization_id, workspace_id, delete_unknown=delete_unknown)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->delete_historical_data_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **delete_unknown** | **bool**| condition to delete runs with an Unknown status | [optional] if omitted the server will use the default value of False

### Return type

void (empty response body)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request succeeded |  -  |
**400** | Bad request |  -  |
**404** | the Organization or Workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scenario_run**
> delete_scenario_run(organization_id, scenariorun_id)

Delete a scenariorun

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev.api.cosmotech.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
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
        api_instance.delete_scenario_run(organization_id, scenariorun_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->delete_scenario_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **scenariorun_id** | **str**| the ScenarioRun identifier |

### Return type

void (empty response body)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request succeeded |  -  |
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
# Defining the host is optional and defaults to https://dev.api.cosmotech.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
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

# **get_scenario_run_cumulated_logs**
> str get_scenario_run_cumulated_logs(organization_id, scenariorun_id)

Get the cumulated logs of a scenariorun

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev.api.cosmotech.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
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
        # Get the cumulated logs of a scenariorun
        api_response = api_instance.get_scenario_run_cumulated_logs(organization_id, scenariorun_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->get_scenario_run_cumulated_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **scenariorun_id** | **str**| the ScenarioRun identifier |

### Return type

**str**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the ScenarioRun cumulated logs |  -  |
**400** | Bad request |  -  |
**404** | the ScenarioRun specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_run_logs**
> ScenarioRunLogs get_scenario_run_logs(organization_id, scenariorun_id)

get the logs for the ScenarioRun

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run_logs import ScenarioRunLogs
from pprint import pprint
# Defining the host is optional and defaults to https://dev.api.cosmotech.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
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
        # get the logs for the ScenarioRun
        api_response = api_instance.get_scenario_run_logs(organization_id, scenariorun_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->get_scenario_run_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
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

# **get_scenario_run_status**
> ScenarioRunStatus get_scenario_run_status(organization_id, scenariorun_id)

get the status for the ScenarioRun

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run_status import ScenarioRunStatus
from pprint import pprint
# Defining the host is optional and defaults to https://dev.api.cosmotech.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
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
        # get the status for the ScenarioRun
        api_response = api_instance.get_scenario_run_status(organization_id, scenariorun_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->get_scenario_run_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **scenariorun_id** | **str**| the ScenarioRun identifier |

### Return type

[**ScenarioRunStatus**](ScenarioRunStatus.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the scenariorun status details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_runs**
> [ScenarioRun] get_scenario_runs(organization_id, workspace_id, scenario_id)

get the list of ScenarioRuns for the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run import ScenarioRun
from pprint import pprint
# Defining the host is optional and defaults to https://dev.api.cosmotech.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
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
        api_response = api_instance.get_scenario_runs(organization_id, workspace_id, scenario_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->get_scenario_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |

### Return type

[**[ScenarioRun]**](ScenarioRun.md)

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
> [ScenarioRun] get_workspace_scenario_runs(organization_id, workspace_id)

get the list of ScenarioRuns for the Workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run import ScenarioRun
from pprint import pprint
# Defining the host is optional and defaults to https://dev.api.cosmotech.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
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

[**[ScenarioRun]**](ScenarioRun.md)

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

# **import_scenario_run**
> ScenarioRun import_scenario_run(organization_id, workspace_id, scenario_id, scenario_run)

import a ScenarioRun for the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run import ScenarioRun
from pprint import pprint
# Defining the host is optional and defaults to https://dev.api.cosmotech.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier
    scenario_run = ScenarioRun(
        state=None,
        organization_id="organization_id_example",
        workflow_id="workflow_id_example",
        generate_name="generate_name_example",
        workflow_name="workflow_name_example",
        sdk_version="sdk_version_example",
        no_data_ingestion_state=True,
        containers=[
            ScenarioRunContainer(
                name="name_example",
                labels={
                    "key": "key_example",
                },
                env_vars={
                    "key": "key_example",
                },
                image="image_example",
                entrypoint="entrypoint_example",
                run_args=[
                    "run_args_example",
                ],
                dependencies=[
                    "dependencies_example",
                ],
                node_label="node_label_example",
                run_sizing=ContainerResourceSizing(
                    requests=ContainerResourceSizeInfo(
                        cpu="cpu_example",
                        memory="memory_example",
                    ),
                    limits=ContainerResourceSizeInfo(
                        cpu="cpu_example",
                        memory="memory_example",
                    ),
                ),
                artifacts=[
                    ScenarioRunContainerArtifact(
                        name="name_example",
                        path="path_example",
                    ),
                ],
            ),
        ],
    ) # ScenarioRun | the ScenarioRun to import

    # example passing only required values which don't have defaults set
    try:
        # import a ScenarioRun for the Scenario
        api_response = api_instance.import_scenario_run(organization_id, workspace_id, scenario_id, scenario_run)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->import_scenario_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |
 **scenario_run** | [**ScenarioRun**](ScenarioRun.md)| the ScenarioRun to import |

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
**200** | the scenariorun details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_scenario**
> ScenarioRun run_scenario(organization_id, workspace_id, scenario_id)

run a ScenarioRun for the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run import ScenarioRun
from pprint import pprint
# Defining the host is optional and defaults to https://dev.api.cosmotech.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
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

# **search_scenario_runs**
> [ScenarioRun] search_scenario_runs(organization_id, scenario_run_search)

Search ScenarioRuns

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run_search import ScenarioRunSearch
from cosmotech_api.model.scenario_run import ScenarioRun
from pprint import pprint
# Defining the host is optional and defaults to https://dev.api.cosmotech.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
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
        state="FetchingDatasets",
        workflow_id="workflow_id_example",
        workflow_name="workflow_name_example",
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

[**[ScenarioRun]**](ScenarioRun.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
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
# Defining the host is optional and defaults to https://dev.api.cosmotech.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    scenario_run_start_containers = ScenarioRunStartContainers(
        generate_name="generate_name_example",
        csm_simulation_id="csm_simulation_id_example",
        node_label="node_label_example",
        labels={
            "key": "key_example",
        },
        containers=[
            ScenarioRunContainer(
                name="name_example",
                labels={
                    "key": "key_example",
                },
                env_vars={
                    "key": "key_example",
                },
                image="image_example",
                entrypoint="entrypoint_example",
                run_args=[
                    "run_args_example",
                ],
                dependencies=[
                    "dependencies_example",
                ],
                node_label="node_label_example",
                run_sizing=ContainerResourceSizing(
                    requests=ContainerResourceSizeInfo(
                        cpu="cpu_example",
                        memory="memory_example",
                    ),
                    limits=ContainerResourceSizeInfo(
                        cpu="cpu_example",
                        memory="memory_example",
                    ),
                ),
                artifacts=[
                    ScenarioRunContainerArtifact(
                        name="name_example",
                        path="path_example",
                    ),
                ],
            ),
        ],
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

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | the scenariorun details |  -  |
**400** | Bad request |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_scenario_run**
> ScenarioRunStatus stop_scenario_run(organization_id, scenariorun_id)

stop a ScenarioRun for the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorun_api
from cosmotech_api.model.scenario_run_status import ScenarioRunStatus
from pprint import pprint
# Defining the host is optional and defaults to https://dev.api.cosmotech.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://dev.api.cosmotech.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scenariorun_api.ScenariorunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    scenariorun_id = "scenariorun_id_example" # str | the scenariorun identifier

    # example passing only required values which don't have defaults set
    try:
        # stop a ScenarioRun for the Scenario
        api_response = api_instance.stop_scenario_run(organization_id, scenariorun_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunApi->stop_scenario_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **scenariorun_id** | **str**| the scenariorun identifier |

### Return type

[**ScenarioRunStatus**](ScenarioRunStatus.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the scenariorun status details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

