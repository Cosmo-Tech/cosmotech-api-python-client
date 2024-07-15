# cosmotech_api.RunnerApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_runner_access_control**](RunnerApi.md#add_runner_access_control) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/security/access | Add a control access to the Runner
[**create_runner**](RunnerApi.md#create_runner) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/runners | Create a new Runner
[**delete_runner**](RunnerApi.md#delete_runner) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id} | Delete a runner
[**get_runner**](RunnerApi.md#get_runner) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id} | Get the details of an runner
[**get_runner_access_control**](RunnerApi.md#get_runner_access_control) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/security/access/{identity_id} | Get a control access for the Runner
[**get_runner_permissions**](RunnerApi.md#get_runner_permissions) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/permissions/{role} | Get the Runner permission by given role
[**get_runner_security**](RunnerApi.md#get_runner_security) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/security | Get the Runner security information
[**get_runner_security_users**](RunnerApi.md#get_runner_security_users) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/security/users | Get the Runner security users list
[**list_runners**](RunnerApi.md#list_runners) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/runners | List all Runners
[**remove_runner_access_control**](RunnerApi.md#remove_runner_access_control) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/security/access/{identity_id} | Remove the specified access from the given Organization Runner
[**set_runner_default_security**](RunnerApi.md#set_runner_default_security) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/security/default | Set the Runner default security
[**start_run**](RunnerApi.md#start_run) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/start | Start a run with runner parameters
[**stop_run**](RunnerApi.md#stop_run) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/stop | Stop the last run
[**update_runner**](RunnerApi.md#update_runner) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id} | Update a runner
[**update_runner_access_control**](RunnerApi.md#update_runner_access_control) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id}/runners/{runner_id}/security/access/{identity_id} | Update the specified access to User for a Runner


# **add_runner_access_control**
> RunnerAccessControl add_runner_access_control(organization_id, workspace_id, runner_id, runner_access_control)

Add a control access to the Runner

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.runner_access_control import RunnerAccessControl
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
    api_instance = cosmotech_api.RunnerApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier
    runner_access_control = cosmotech_api.RunnerAccessControl() # RunnerAccessControl | the new Runner security access to add.

    try:
        # Add a control access to the Runner
        api_response = api_instance.add_runner_access_control(organization_id, workspace_id, runner_id, runner_access_control)
        print("The response of RunnerApi->add_runner_access_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerApi->add_runner_access_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 
 **runner_access_control** | [**RunnerAccessControl**](RunnerAccessControl.md)| the new Runner security access to add. | 

### Return type

[**RunnerAccessControl**](RunnerAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Runner access |  -  |
**404** | the Runner specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_runner**
> Runner create_runner(organization_id, workspace_id, runner)

Create a new Runner

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.runner import Runner
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
    api_instance = cosmotech_api.RunnerApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner = cosmotech_api.Runner() # Runner | the Runner to create

    try:
        # Create a new Runner
        api_response = api_instance.create_runner(organization_id, workspace_id, runner)
        print("The response of RunnerApi->create_runner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerApi->create_runner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner** | [**Runner**](Runner.md)| the Runner to create | 

### Return type

[**Runner**](Runner.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the runner details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_runner**
> delete_runner(organization_id, workspace_id, runner_id)

Delete a runner

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
    api_instance = cosmotech_api.RunnerApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier

    try:
        # Delete a runner
        api_instance.delete_runner(organization_id, workspace_id, runner_id)
    except Exception as e:
        print("Exception when calling RunnerApi->delete_runner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 

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
**404** | the Runner specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runner**
> Runner get_runner(organization_id, workspace_id, runner_id)

Get the details of an runner

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.runner import Runner
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
    api_instance = cosmotech_api.RunnerApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier

    try:
        # Get the details of an runner
        api_response = api_instance.get_runner(organization_id, workspace_id, runner_id)
        print("The response of RunnerApi->get_runner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerApi->get_runner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 

### Return type

[**Runner**](Runner.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Runner details |  -  |
**404** | the Runner specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runner_access_control**
> RunnerAccessControl get_runner_access_control(organization_id, workspace_id, runner_id, identity_id)

Get a control access for the Runner

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.runner_access_control import RunnerAccessControl
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
    api_instance = cosmotech_api.RunnerApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier
    identity_id = 'identity_id_example' # str | the User identifier

    try:
        # Get a control access for the Runner
        api_response = api_instance.get_runner_access_control(organization_id, workspace_id, runner_id, identity_id)
        print("The response of RunnerApi->get_runner_access_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerApi->get_runner_access_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 
 **identity_id** | **str**| the User identifier | 

### Return type

[**RunnerAccessControl**](RunnerAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Runner access |  -  |
**404** | the Runner or user specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runner_permissions**
> List[str] get_runner_permissions(organization_id, workspace_id, runner_id, role)

Get the Runner permission by given role

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
    api_instance = cosmotech_api.RunnerApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier
    role = 'role_example' # str | the Role

    try:
        # Get the Runner permission by given role
        api_response = api_instance.get_runner_permissions(organization_id, workspace_id, runner_id, role)
        print("The response of RunnerApi->get_runner_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerApi->get_runner_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 
 **role** | **str**| the Role | 

### Return type

**List[str]**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Runners security permission list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runner_security**
> RunnerSecurity get_runner_security(organization_id, workspace_id, runner_id)

Get the Runner security information

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.runner_security import RunnerSecurity
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
    api_instance = cosmotech_api.RunnerApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier

    try:
        # Get the Runner security information
        api_response = api_instance.get_runner_security(organization_id, workspace_id, runner_id)
        print("The response of RunnerApi->get_runner_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerApi->get_runner_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 

### Return type

[**RunnerSecurity**](RunnerSecurity.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Runner security |  -  |
**404** | the Runner specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runner_security_users**
> List[str] get_runner_security_users(organization_id, workspace_id, runner_id)

Get the Runner security users list

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
    api_instance = cosmotech_api.RunnerApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier

    try:
        # Get the Runner security users list
        api_response = api_instance.get_runner_security_users(organization_id, workspace_id, runner_id)
        print("The response of RunnerApi->get_runner_security_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerApi->get_runner_security_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 

### Return type

**List[str]**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Runner security users list |  -  |
**404** | the Runner specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_runners**
> List[Runner] list_runners(organization_id, workspace_id, page=page, size=size)

List all Runners

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.runner import Runner
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
    api_instance = cosmotech_api.RunnerApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    page = 56 # int | page number to query (optional)
    size = 56 # int | amount of result by page (optional)

    try:
        # List all Runners
        api_response = api_instance.list_runners(organization_id, workspace_id, page=page, size=size)
        print("The response of RunnerApi->list_runners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerApi->list_runners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **page** | **int**| page number to query | [optional] 
 **size** | **int**| amount of result by page | [optional] 

### Return type

[**List[Runner]**](Runner.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the list of Runners |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_runner_access_control**
> remove_runner_access_control(organization_id, workspace_id, runner_id, identity_id)

Remove the specified access from the given Organization Runner

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
    api_instance = cosmotech_api.RunnerApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier
    identity_id = 'identity_id_example' # str | the User identifier

    try:
        # Remove the specified access from the given Organization Runner
        api_instance.remove_runner_access_control(organization_id, workspace_id, runner_id, identity_id)
    except Exception as e:
        print("Exception when calling RunnerApi->remove_runner_access_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 
 **identity_id** | **str**| the User identifier | 

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
**404** | the Runner or the user specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_runner_default_security**
> RunnerSecurity set_runner_default_security(organization_id, workspace_id, runner_id, runner_role)

Set the Runner default security

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.runner_role import RunnerRole
from cosmotech_api.models.runner_security import RunnerSecurity
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
    api_instance = cosmotech_api.RunnerApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier
    runner_role = cosmotech_api.RunnerRole() # RunnerRole | This change the runner default security. The default security is the role assigned to any person not on the Access Control List. If the default security is None, then nobody outside of the ACL can access the runner.

    try:
        # Set the Runner default security
        api_response = api_instance.set_runner_default_security(organization_id, workspace_id, runner_id, runner_role)
        print("The response of RunnerApi->set_runner_default_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerApi->set_runner_default_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 
 **runner_role** | [**RunnerRole**](RunnerRole.md)| This change the runner default security. The default security is the role assigned to any person not on the Access Control List. If the default security is None, then nobody outside of the ACL can access the runner. | 

### Return type

[**RunnerSecurity**](RunnerSecurity.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Runner default visibility |  -  |
**404** | the Runner specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_run**
> str start_run(organization_id, workspace_id, runner_id)

Start a run with runner parameters

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
    api_instance = cosmotech_api.RunnerApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier

    try:
        # Start a run with runner parameters
        api_response = api_instance.start_run(organization_id, workspace_id, runner_id)
        print("The response of RunnerApi->start_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerApi->start_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 

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
**202** | the Run id started |  -  |
**404** | the Runner specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_run**
> stop_run(organization_id, workspace_id, runner_id)

Stop the last run

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
    api_instance = cosmotech_api.RunnerApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier

    try:
        # Stop the last run
        api_instance.stop_run(organization_id, workspace_id, runner_id)
    except Exception as e:
        print("Exception when calling RunnerApi->stop_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 

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
**202** | the last Run has been stopped |  -  |
**404** | the Runner specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_runner**
> Runner update_runner(organization_id, workspace_id, runner_id, runner)

Update a runner

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.runner import Runner
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
    api_instance = cosmotech_api.RunnerApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier
    runner = cosmotech_api.Runner() # Runner | the new Runner details. This endpoint can't be used to update security

    try:
        # Update a runner
        api_response = api_instance.update_runner(organization_id, workspace_id, runner_id, runner)
        print("The response of RunnerApi->update_runner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerApi->update_runner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 
 **runner** | [**Runner**](Runner.md)| the new Runner details. This endpoint can&#39;t be used to update security | 

### Return type

[**Runner**](Runner.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the runner details |  -  |
**400** | Bad request |  -  |
**404** | the Runner specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_runner_access_control**
> RunnerAccessControl update_runner_access_control(organization_id, workspace_id, runner_id, identity_id, runner_role)

Update the specified access to User for a Runner

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.runner_access_control import RunnerAccessControl
from cosmotech_api.models.runner_role import RunnerRole
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
    api_instance = cosmotech_api.RunnerApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    runner_id = 'runner_id_example' # str | the Runner identifier
    identity_id = 'identity_id_example' # str | the User identifier
    runner_role = cosmotech_api.RunnerRole() # RunnerRole | The new Runner Access Control

    try:
        # Update the specified access to User for a Runner
        api_response = api_instance.update_runner_access_control(organization_id, workspace_id, runner_id, identity_id, runner_role)
        print("The response of RunnerApi->update_runner_access_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerApi->update_runner_access_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **runner_id** | **str**| the Runner identifier | 
 **identity_id** | **str**| the User identifier | 
 **runner_role** | [**RunnerRole**](RunnerRole.md)| The new Runner Access Control | 

### Return type

[**RunnerAccessControl**](RunnerAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Runner access |  -  |
**404** | The Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

