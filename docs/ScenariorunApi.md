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
[**run_scenario**](ScenariorunApi.md#run_scenario) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/run | run a ScenarioRun for the Scenario
[**search_scenario_runs**](ScenariorunApi.md#search_scenario_runs) | **POST** /organizations/{organization_id}/scenarioruns/search | Search ScenarioRuns
[**start_scenario_run_containers**](ScenariorunApi.md#start_scenario_run_containers) | **POST** /organizations/{organization_id}/scenarioruns/startcontainers | Start a new scenariorun with raw containers definition
[**stop_scenario_run**](ScenariorunApi.md#stop_scenario_run) | **POST** /organizations/{organization_id}/scenarioruns/{scenariorun_id}/stop | stop a ScenarioRun for the Scenario


# **delete_historical_data_organization**
> delete_historical_data_organization(organization_id, delete_unknown=delete_unknown)

Delete all historical ScenarioRuns in the Organization

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenariorunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    delete_unknown = False # bool | condition to delete runs with an Unknown status (optional) (default to False)

    try:
        # Delete all historical ScenarioRuns in the Organization
        api_instance.delete_historical_data_organization(organization_id, delete_unknown=delete_unknown)
    except Exception as e:
        print("Exception when calling ScenariorunApi->delete_historical_data_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **delete_unknown** | **bool**| condition to delete runs with an Unknown status | [optional] [default to False]

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
> delete_historical_data_scenario(organization_id, workspace_id, scenario_id, delete_unknown=delete_unknown)

Delete all historical ScenarioRuns in the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenariorunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier
    delete_unknown = False # bool | condition to delete runs with an Unknown status (optional) (default to False)

    try:
        # Delete all historical ScenarioRuns in the Scenario
        api_instance.delete_historical_data_scenario(organization_id, workspace_id, scenario_id, delete_unknown=delete_unknown)
    except Exception as e:
        print("Exception when calling ScenariorunApi->delete_historical_data_scenario: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 
 **delete_unknown** | **bool**| condition to delete runs with an Unknown status | [optional] [default to False]

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
> delete_historical_data_workspace(organization_id, workspace_id, delete_unknown=delete_unknown)

Delete all historical ScenarioRuns in the Workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenariorunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    delete_unknown = False # bool | condition to delete runs with an Unknown status (optional) (default to False)

    try:
        # Delete all historical ScenarioRuns in the Workspace
        api_instance.delete_historical_data_workspace(organization_id, workspace_id, delete_unknown=delete_unknown)
    except Exception as e:
        print("Exception when calling ScenariorunApi->delete_historical_data_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **delete_unknown** | **bool**| condition to delete runs with an Unknown status | [optional] [default to False]

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
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenariorunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    scenariorun_id = 'scenariorun_id_example' # str | the ScenarioRun identifier

    try:
        # Delete a scenariorun
        api_instance.delete_scenario_run(organization_id, scenariorun_id)
    except Exception as e:
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
import cosmotech_api
from cosmotech_api.models.scenario_run import ScenarioRun
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenariorunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    scenariorun_id = 'scenariorun_id_example' # str | the ScenarioRun identifier

    try:
        # Get the details of a scenariorun
        api_response = api_instance.find_scenario_run_by_id(organization_id, scenariorun_id)
        print("The response of ScenariorunApi->find_scenario_run_by_id:\n")
        pprint(api_response)
    except Exception as e:
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
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenariorunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    scenariorun_id = 'scenariorun_id_example' # str | the ScenarioRun identifier

    try:
        # Get the cumulated logs of a scenariorun
        api_response = api_instance.get_scenario_run_cumulated_logs(organization_id, scenariorun_id)
        print("The response of ScenariorunApi->get_scenario_run_cumulated_logs:\n")
        pprint(api_response)
    except Exception as e:
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
import cosmotech_api
from cosmotech_api.models.scenario_run_logs import ScenarioRunLogs
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenariorunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    scenariorun_id = 'scenariorun_id_example' # str | the ScenarioRun identifier

    try:
        # get the logs for the ScenarioRun
        api_response = api_instance.get_scenario_run_logs(organization_id, scenariorun_id)
        print("The response of ScenariorunApi->get_scenario_run_logs:\n")
        pprint(api_response)
    except Exception as e:
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
import cosmotech_api
from cosmotech_api.models.scenario_run_status import ScenarioRunStatus
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenariorunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    scenariorun_id = 'scenariorun_id_example' # str | the ScenarioRun identifier

    try:
        # get the status for the ScenarioRun
        api_response = api_instance.get_scenario_run_status(organization_id, scenariorun_id)
        print("The response of ScenariorunApi->get_scenario_run_status:\n")
        pprint(api_response)
    except Exception as e:
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
> List[ScenarioRun] get_scenario_runs(organization_id, workspace_id, scenario_id, page=page, size=size)

get the list of ScenarioRuns for the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario_run import ScenarioRun
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenariorunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier
    page = 56 # int | page number to query (optional)
    size = 56 # int | amount of result by page (optional)

    try:
        # get the list of ScenarioRuns for the Scenario
        api_response = api_instance.get_scenario_runs(organization_id, workspace_id, scenario_id, page=page, size=size)
        print("The response of ScenariorunApi->get_scenario_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenariorunApi->get_scenario_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 
 **page** | **int**| page number to query | [optional] 
 **size** | **int**| amount of result by page | [optional] 

### Return type

[**List[ScenarioRun]**](ScenarioRun.md)

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
> List[ScenarioRun] get_workspace_scenario_runs(organization_id, workspace_id, page=page, size=size)

get the list of ScenarioRuns for the Workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario_run import ScenarioRun
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenariorunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    page = 56 # int | page number to query (optional)
    size = 56 # int | amount of result by page (optional)

    try:
        # get the list of ScenarioRuns for the Workspace
        api_response = api_instance.get_workspace_scenario_runs(organization_id, workspace_id, page=page, size=size)
        print("The response of ScenariorunApi->get_workspace_scenario_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenariorunApi->get_workspace_scenario_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **page** | **int**| page number to query | [optional] 
 **size** | **int**| amount of result by page | [optional] 

### Return type

[**List[ScenarioRun]**](ScenarioRun.md)

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
> ScenarioRun run_scenario(organization_id, workspace_id, scenario_id)

run a ScenarioRun for the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario_run import ScenarioRun
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenariorunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier

    try:
        # run a ScenarioRun for the Scenario
        api_response = api_instance.run_scenario(organization_id, workspace_id, scenario_id)
        print("The response of ScenariorunApi->run_scenario:\n")
        pprint(api_response)
    except Exception as e:
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
> List[ScenarioRun] search_scenario_runs(organization_id, scenario_run_search, page=page, size=size)

Search ScenarioRuns

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario_run import ScenarioRun
from cosmotech_api.models.scenario_run_search import ScenarioRunSearch
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenariorunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    scenario_run_search = cosmotech_api.ScenarioRunSearch() # ScenarioRunSearch | the ScenarioRun search parameters
    page = 56 # int | page number to query (optional)
    size = 56 # int | amount of result by page (optional)

    try:
        # Search ScenarioRuns
        api_response = api_instance.search_scenario_runs(organization_id, scenario_run_search, page=page, size=size)
        print("The response of ScenariorunApi->search_scenario_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenariorunApi->search_scenario_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **scenario_run_search** | [**ScenarioRunSearch**](ScenarioRunSearch.md)| the ScenarioRun search parameters | 
 **page** | **int**| page number to query | [optional] 
 **size** | **int**| amount of result by page | [optional] 

### Return type

[**List[ScenarioRun]**](ScenarioRun.md)

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
import cosmotech_api
from cosmotech_api.models.scenario_run import ScenarioRun
from cosmotech_api.models.scenario_run_start_containers import ScenarioRunStartContainers
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenariorunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    scenario_run_start_containers = cosmotech_api.ScenarioRunStartContainers() # ScenarioRunStartContainers | the raw containers definition

    try:
        # Start a new scenariorun with raw containers definition
        api_response = api_instance.start_scenario_run_containers(organization_id, scenario_run_start_containers)
        print("The response of ScenariorunApi->start_scenario_run_containers:\n")
        pprint(api_response)
    except Exception as e:
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
import cosmotech_api
from cosmotech_api.models.scenario_run_status import ScenarioRunStatus
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenariorunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    scenariorun_id = 'scenariorun_id_example' # str | the scenariorun identifier

    try:
        # stop a ScenarioRun for the Scenario
        api_response = api_instance.stop_scenario_run(organization_id, scenariorun_id)
        print("The response of ScenariorunApi->stop_scenario_run:\n")
        pprint(api_response)
    except Exception as e:
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

