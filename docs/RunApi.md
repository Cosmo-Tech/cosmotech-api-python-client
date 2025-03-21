# cosmotech_api.RunApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_run**](RunApi.md#delete_run) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/runs/{run_id} | Delete a run
[**get_run**](RunApi.md#get_run) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/runs/{run_id} | Get the details of a run
[**get_run_logs**](RunApi.md#get_run_logs) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/runs/{run_id}/logs | get the logs for the Run
[**get_run_status**](RunApi.md#get_run_status) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/runs/{run_id}/status | get the status for the Run
[**list_runs**](RunApi.md#list_runs) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/runs | get the list of Runs for the Runner
[**query_run_data**](RunApi.md#query_run_data) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/runs/{run_id}/data/query | query the run data
[**send_run_data**](RunApi.md#send_run_data) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/runs/{run_id}/data/send | Send data associated to a run


# **delete_run**
> delete_run(organization_id, workspace_id, runner_id, run_id)

Delete a run

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.RunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier
    run_id = 'run_id_example' # str | the Run identifier

    try:
        # Delete a run
        api_instance.delete_run(organization_id, workspace_id, runner_id, run_id)
    except Exception as e:
        print("Exception when calling RunApi->delete_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 
 **run_id** | **str**| the Run identifier | 

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
**404** | the Run specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run**
> Run get_run(organization_id, workspace_id, runner_id, run_id)

Get the details of a run

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run import Run
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.RunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier
    run_id = 'run_id_example' # str | the Run identifier

    try:
        # Get the details of a run
        api_response = api_instance.get_run(organization_id, workspace_id, runner_id, run_id)
        print("The response of RunApi->get_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->get_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 
 **run_id** | **str**| the Run identifier | 

### Return type

[**Run**](Run.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Run details |  -  |
**404** | the Run specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_logs**
> RunLogs get_run_logs(organization_id, workspace_id, runner_id, run_id)

get the logs for the Run

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run_logs import RunLogs
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.RunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier
    run_id = 'run_id_example' # str | the Run identifier

    try:
        # get the logs for the Run
        api_response = api_instance.get_run_logs(organization_id, workspace_id, runner_id, run_id)
        print("The response of RunApi->get_run_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->get_run_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 
 **run_id** | **str**| the Run identifier | 

### Return type

[**RunLogs**](RunLogs.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the run logs details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_status**
> RunStatus get_run_status(organization_id, workspace_id, runner_id, run_id)

get the status for the Run

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run_status import RunStatus
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.RunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier
    run_id = 'run_id_example' # str | the Run identifier

    try:
        # get the status for the Run
        api_response = api_instance.get_run_status(organization_id, workspace_id, runner_id, run_id)
        print("The response of RunApi->get_run_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->get_run_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 
 **run_id** | **str**| the Run identifier | 

### Return type

[**RunStatus**](RunStatus.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the run status details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_runs**
> List[Run] list_runs(organization_id, workspace_id, runner_id, page=page, size=size)

get the list of Runs for the Runner

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run import Run
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.RunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier
    page = 56 # int | page number to query (first page is at index 0) (optional)
    size = 56 # int | amount of result by page (optional)

    try:
        # get the list of Runs for the Runner
        api_response = api_instance.list_runs(organization_id, workspace_id, runner_id, page=page, size=size)
        print("The response of RunApi->list_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->list_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 
 **page** | **int**| page number to query (first page is at index 0) | [optional] 
 **size** | **int**| amount of result by page | [optional] 

### Return type

[**List[Run]**](Run.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the run details list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_run_data**
> QueryResult query_run_data(organization_id, workspace_id, runner_id, run_id, run_data_query)

query the run data

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.query_result import QueryResult
from cosmotech_api.models.run_data_query import RunDataQuery
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.RunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier
    run_id = 'run_id_example' # str | the Run identifier
    run_data_query = cosmotech_api.RunDataQuery() # RunDataQuery | the query to run

    try:
        # query the run data
        api_response = api_instance.query_run_data(organization_id, workspace_id, runner_id, run_id, run_data_query)
        print("The response of RunApi->query_run_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->query_run_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 
 **run_id** | **str**| the Run identifier | 
 **run_data_query** | [**RunDataQuery**](RunDataQuery.md)| the query to run | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the query response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_run_data**
> RunData send_run_data(organization_id, workspace_id, runner_id, run_id, send_run_data_request)

Send data associated to a run

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run_data import RunData
from cosmotech_api.models.send_run_data_request import SendRunDataRequest
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.RunApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier
    run_id = 'run_id_example' # str | the Run identifier
    send_run_data_request = cosmotech_api.SendRunDataRequest() # SendRunDataRequest | Custom data to register

    try:
        # Send data associated to a run
        api_response = api_instance.send_run_data(organization_id, workspace_id, runner_id, run_id, send_run_data_request)
        print("The response of RunApi->send_run_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->send_run_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 
 **run_id** | **str**| the Run identifier | 
 **send_run_data_request** | [**SendRunDataRequest**](SendRunDataRequest.md)| Custom data to register | 

### Return type

[**RunData**](RunData.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Data stored |  -  |
**400** | Data sent format is malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

