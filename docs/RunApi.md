# cosmotech_api.RunApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_run**](RunApi.md#delete_run) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/runs/{run_id} | Delete a run
[**get_run**](RunApi.md#get_run) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/runs/{run_id} | Get the details of a run
[**get_run_logs**](RunApi.md#get_run_logs) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/runs/{run_id}/logs | get the logs for the Run
[**get_run_status**](RunApi.md#get_run_status) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/runs/{run_id}/status | get the status for the Run
[**list_runs**](RunApi.md#list_runs) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/runs | get the list of Runs for the Runner


# **delete_run**
> delete_run(organization_id, workspace_id, runner_id, run_id)

Delete a run

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import run_api
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
    api_instance = run_api.RunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    runner_id = "runner_id_example" # str | the Runner identifier
    run_id = "run_id_example" # str | the Run identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete a run
        api_instance.delete_run(organization_id, workspace_id, runner_id, run_id)
    except cosmotech_api.ApiException as e:
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
import time
import cosmotech_api
from cosmotech_api.api import run_api
from cosmotech_api.model.run import Run
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
    api_instance = run_api.RunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    runner_id = "runner_id_example" # str | the Runner identifier
    run_id = "run_id_example" # str | the Run identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a run
        api_response = api_instance.get_run(organization_id, workspace_id, runner_id, run_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
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
 - **Accept**: application/json


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
import time
import cosmotech_api
from cosmotech_api.api import run_api
from cosmotech_api.model.run_logs import RunLogs
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
    api_instance = run_api.RunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    runner_id = "runner_id_example" # str | the Runner identifier
    run_id = "run_id_example" # str | the Run identifier

    # example passing only required values which don't have defaults set
    try:
        # get the logs for the Run
        api_response = api_instance.get_run_logs(organization_id, workspace_id, runner_id, run_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
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
 - **Accept**: application/json


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
import time
import cosmotech_api
from cosmotech_api.api import run_api
from cosmotech_api.model.run_status import RunStatus
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
    api_instance = run_api.RunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    runner_id = "runner_id_example" # str | the Runner identifier
    run_id = "run_id_example" # str | the Run identifier

    # example passing only required values which don't have defaults set
    try:
        # get the status for the Run
        api_response = api_instance.get_run_status(organization_id, workspace_id, runner_id, run_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the run status details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_runs**
> [Run] list_runs(organization_id, workspace_id, runner_id)

get the list of Runs for the Runner

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import run_api
from cosmotech_api.model.run import Run
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
    api_instance = run_api.RunApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    runner_id = "runner_id_example" # str | the Runner identifier
    page = 1 # int | page number to query (optional)
    size = 1 # int | amount of result by page (optional)

    # example passing only required values which don't have defaults set
    try:
        # get the list of Runs for the Runner
        api_response = api_instance.list_runs(organization_id, workspace_id, runner_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling RunApi->list_runs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # get the list of Runs for the Runner
        api_response = api_instance.list_runs(organization_id, workspace_id, runner_id, page=page, size=size)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling RunApi->list_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **runner_id** | **str**| the Runner identifier |
 **page** | **int**| page number to query | [optional]
 **size** | **int**| amount of result by page | [optional]

### Return type

[**[Run]**](Run.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the run details list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

