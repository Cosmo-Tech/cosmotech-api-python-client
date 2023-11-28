# cosmotech_api.WorkspaceApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_workspace_access_control**](WorkspaceApi.md#add_workspace_access_control) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/security/access | Add a control access to the Workspace
[**create_secret**](WorkspaceApi.md#create_secret) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/secret | Create a secret for the Workspace
[**create_workspace**](WorkspaceApi.md#create_workspace) | **POST** /organizations/{organization_id}/workspaces | Create a new workspace
[**delete_all_workspace_files**](WorkspaceApi.md#delete_all_workspace_files) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/files | Delete all Workspace files
[**delete_workspace**](WorkspaceApi.md#delete_workspace) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id} | Delete a workspace
[**delete_workspace_file**](WorkspaceApi.md#delete_workspace_file) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/files/delete | Delete a workspace file
[**download_workspace_file**](WorkspaceApi.md#download_workspace_file) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/files/download | Download the Workspace File specified
[**find_all_workspace_files**](WorkspaceApi.md#find_all_workspace_files) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/files | List all Workspace files
[**find_all_workspaces**](WorkspaceApi.md#find_all_workspaces) | **GET** /organizations/{organization_id}/workspaces | List all Workspaces
[**find_workspace_by_id**](WorkspaceApi.md#find_workspace_by_id) | **GET** /organizations/{organization_id}/workspaces/{workspace_id} | Get the details of an workspace
[**get_workspace_access_control**](WorkspaceApi.md#get_workspace_access_control) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/security/access/{identity_id} | Get a control access for the Workspace
[**get_workspace_permissions**](WorkspaceApi.md#get_workspace_permissions) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/permissions/{role} | Get the Workspace permission by given role
[**get_workspace_security**](WorkspaceApi.md#get_workspace_security) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/security | Get the Workspace security information
[**get_workspace_security_users**](WorkspaceApi.md#get_workspace_security_users) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/security/users | Get the Workspace security users list
[**import_workspace**](WorkspaceApi.md#import_workspace) | **POST** /organizations/{organization_id}/workspaces/import | Import a workspace
[**remove_workspace_access_control**](WorkspaceApi.md#remove_workspace_access_control) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/security/access/{identity_id} | Remove the specified access from the given Organization Workspace
[**set_workspace_default_security**](WorkspaceApi.md#set_workspace_default_security) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/security/default | Set the Workspace default security
[**update_workspace**](WorkspaceApi.md#update_workspace) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id} | Update a workspace
[**update_workspace_access_control**](WorkspaceApi.md#update_workspace_access_control) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id}/security/access/{identity_id} | Update the specified access to User for a Workspace
[**upload_workspace_file**](WorkspaceApi.md#upload_workspace_file) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/files | Upload a file for the Workspace


# **add_workspace_access_control**
> WorkspaceAccessControl add_workspace_access_control(organization_id, workspace_id, workspace_access_control)

Add a control access to the Workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace_access_control import WorkspaceAccessControl
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    workspace_access_control = WorkspaceAccessControl(
        id="id_example",
        role="role_example",
    ) # WorkspaceAccessControl | the new Workspace security access to add.

    # example passing only required values which don't have defaults set
    try:
        # Add a control access to the Workspace
        api_response = api_instance.add_workspace_access_control(organization_id, workspace_id, workspace_access_control)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->add_workspace_access_control: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **workspace_access_control** | [**WorkspaceAccessControl**](WorkspaceAccessControl.md)| the new Workspace security access to add. |

### Return type

[**WorkspaceAccessControl**](WorkspaceAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Workspace access |  -  |
**404** | the Workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_secret**
> create_secret(organization_id, workspace_id, workspace_secret)

Create a secret for the Workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace_secret import WorkspaceSecret
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    workspace_secret = WorkspaceSecret(
        dedicated_event_hub_key="dedicated_event_hub_key_example",
    ) # WorkspaceSecret | the definition of the secret

    # example passing only required values which don't have defaults set
    try:
        # Create a secret for the Workspace
        api_instance.create_secret(organization_id, workspace_id, workspace_secret)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->create_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **workspace_secret** | [**WorkspaceSecret**](WorkspaceSecret.md)| the definition of the secret |

### Return type

void (empty response body)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Request succeeded |  -  |
**404** | the Workspace or the User specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace**
> Workspace create_workspace(organization_id, workspace)

Create a new workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace import Workspace
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace = Workspace(
        key="key_example",
        name="name_example",
        description="description_example",
        version="version_example",
        tags=[
            "tags_example",
        ],
        solution=WorkspaceSolution(
            solution_id="solution_id_example",
            run_template_filter=[
                "run_template_filter_example",
            ],
            default_run_template_dataset={},
        ),
        web_app=WorkspaceWebApp(
            url="url_example",
            iframes={},
            options={},
        ),
        send_input_to_data_warehouse=True,
        use_dedicated_event_hub_namespace=False,
        dedicated_event_hub_sas_key_name="dedicated_event_hub_sas_key_name_example",
        dedicated_event_hub_authentication_strategy="dedicated_event_hub_authentication_strategy_example",
        send_scenario_run_to_event_hub=True,
        send_scenario_metadata_to_event_hub=False,
        security=None,
    ) # Workspace | the Workspace to create

    # example passing only required values which don't have defaults set
    try:
        # Create a new workspace
        api_response = api_instance.create_workspace(organization_id, workspace)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->create_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace** | [**Workspace**](Workspace.md)| the Workspace to create |

### Return type

[**Workspace**](Workspace.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the workspace details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_workspace_files**
> delete_all_workspace_files(organization_id, workspace_id)

Delete all Workspace files

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete all Workspace files
        api_instance.delete_all_workspace_files(organization_id, workspace_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->delete_all_workspace_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |

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
**404** | the Workspace specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**
> Workspace delete_workspace(organization_id, workspace_id)

Delete a workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace import Workspace
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete a workspace
        api_response = api_instance.delete_workspace(organization_id, workspace_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->delete_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |

### Return type

[**Workspace**](Workspace.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the workspace details |  -  |
**400** | Bad request |  -  |
**404** | the Workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_file**
> delete_workspace_file(organization_id, workspace_id, file_name)

Delete a workspace file

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    file_name = "file_name_example" # str | the file name

    # example passing only required values which don't have defaults set
    try:
        # Delete a workspace file
        api_instance.delete_workspace_file(organization_id, workspace_id, file_name)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->delete_workspace_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **file_name** | **str**| the file name |

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
**404** | the Workspace or the file specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_workspace_file**
> file_type download_workspace_file(organization_id, workspace_id, file_name)

Download the Workspace File specified

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    file_name = "file_name_example" # str | the file name

    # example passing only required values which don't have defaults set
    try:
        # Download the Workspace File specified
        api_response = api_instance.download_workspace_file(organization_id, workspace_id, file_name)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->download_workspace_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **file_name** | **str**| the file name |

### Return type

**file_type**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the workspace file as a resource |  -  |
**404** | the Workspace file specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_workspace_files**
> [WorkspaceFile] find_all_workspace_files(organization_id, workspace_id)

List all Workspace files

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace_file import WorkspaceFile
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier

    # example passing only required values which don't have defaults set
    try:
        # List all Workspace files
        api_response = api_instance.find_all_workspace_files(organization_id, workspace_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->find_all_workspace_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |

### Return type

[**[WorkspaceFile]**](WorkspaceFile.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the workspace files |  -  |
**404** | the Workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_workspaces**
> [Workspace] find_all_workspaces(organization_id)

List all Workspaces

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace import Workspace
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    page = 1 # int | page number to query (optional)
    size = 1 # int | amount of result by page (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all Workspaces
        api_response = api_instance.find_all_workspaces(organization_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->find_all_workspaces: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all Workspaces
        api_response = api_instance.find_all_workspaces(organization_id, page=page, size=size)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->find_all_workspaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **page** | **int**| page number to query | [optional]
 **size** | **int**| amount of result by page | [optional]

### Return type

[**[Workspace]**](Workspace.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the workspace details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_workspace_by_id**
> Workspace find_workspace_by_id(organization_id, workspace_id)

Get the details of an workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace import Workspace
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of an workspace
        api_response = api_instance.find_workspace_by_id(organization_id, workspace_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->find_workspace_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |

### Return type

[**Workspace**](Workspace.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Workspace details |  -  |
**404** | The Workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_access_control**
> WorkspaceAccessControl get_workspace_access_control(organization_id, workspace_id, identity_id)

Get a control access for the Workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace_access_control import WorkspaceAccessControl
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    identity_id = "identity_id_example" # str | the User identifier

    # example passing only required values which don't have defaults set
    try:
        # Get a control access for the Workspace
        api_response = api_instance.get_workspace_access_control(organization_id, workspace_id, identity_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->get_workspace_access_control: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **identity_id** | **str**| the User identifier |

### Return type

[**WorkspaceAccessControl**](WorkspaceAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Workspace access |  -  |
**404** | The Workspace or user specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_permissions**
> [str] get_workspace_permissions(organization_id, workspace_id, role)

Get the Workspace permission by given role

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    role = "role_example" # str | the Role

    # example passing only required values which don't have defaults set
    try:
        # Get the Workspace permission by given role
        api_response = api_instance.get_workspace_permissions(organization_id, workspace_id, role)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->get_workspace_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **role** | **str**| the Role |

### Return type

**[str]**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Workspace security permission list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_security**
> WorkspaceSecurity get_workspace_security(organization_id, workspace_id)

Get the Workspace security information

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace_security import WorkspaceSecurity
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the Workspace security information
        api_response = api_instance.get_workspace_security(organization_id, workspace_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->get_workspace_security: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |

### Return type

[**WorkspaceSecurity**](WorkspaceSecurity.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Workspace security |  -  |
**404** | the Workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_security_users**
> [str] get_workspace_security_users(organization_id, workspace_id)

Get the Workspace security users list

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the Workspace security users list
        api_response = api_instance.get_workspace_security_users(organization_id, workspace_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->get_workspace_security_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |

### Return type

**[str]**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Workspace security users list |  -  |
**404** | the Workspace or the User specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_workspace**
> Workspace import_workspace(organization_id, workspace)

Import a workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace import Workspace
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace = Workspace(
        key="key_example",
        name="name_example",
        description="description_example",
        version="version_example",
        tags=[
            "tags_example",
        ],
        solution=WorkspaceSolution(
            solution_id="solution_id_example",
            run_template_filter=[
                "run_template_filter_example",
            ],
            default_run_template_dataset={},
        ),
        web_app=WorkspaceWebApp(
            url="url_example",
            iframes={},
            options={},
        ),
        send_input_to_data_warehouse=True,
        use_dedicated_event_hub_namespace=False,
        dedicated_event_hub_sas_key_name="dedicated_event_hub_sas_key_name_example",
        dedicated_event_hub_authentication_strategy="dedicated_event_hub_authentication_strategy_example",
        send_scenario_run_to_event_hub=True,
        send_scenario_metadata_to_event_hub=False,
        security=None,
    ) # Workspace | the Workspace to import

    # example passing only required values which don't have defaults set
    try:
        # Import a workspace
        api_response = api_instance.import_workspace(organization_id, workspace)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->import_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace** | [**Workspace**](Workspace.md)| the Workspace to import |

### Return type

[**Workspace**](Workspace.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the workspace details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_workspace_access_control**
> remove_workspace_access_control(organization_id, workspace_id, identity_id)

Remove the specified access from the given Organization Workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    identity_id = "identity_id_example" # str | the User identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove the specified access from the given Organization Workspace
        api_instance.remove_workspace_access_control(organization_id, workspace_id, identity_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->remove_workspace_access_control: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
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
**404** | The Workspace or the user specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_workspace_default_security**
> WorkspaceSecurity set_workspace_default_security(organization_id, workspace_id, workspace_role)

Set the Workspace default security

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace_role import WorkspaceRole
from cosmotech_api.model.workspace_security import WorkspaceSecurity
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    workspace_role = WorkspaceRole(
        role="role_example",
    ) # WorkspaceRole | the new Workspace default security.

    # example passing only required values which don't have defaults set
    try:
        # Set the Workspace default security
        api_response = api_instance.set_workspace_default_security(organization_id, workspace_id, workspace_role)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->set_workspace_default_security: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **workspace_role** | [**WorkspaceRole**](WorkspaceRole.md)| the new Workspace default security. |

### Return type

[**WorkspaceSecurity**](WorkspaceSecurity.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Workspace default visibility |  -  |
**404** | the Workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace**
> Workspace update_workspace(organization_id, workspace_id, workspace)

Update a workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace import Workspace
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    workspace = Workspace(
        key="key_example",
        name="name_example",
        description="description_example",
        version="version_example",
        tags=[
            "tags_example",
        ],
        solution=WorkspaceSolution(
            solution_id="solution_id_example",
            run_template_filter=[
                "run_template_filter_example",
            ],
            default_run_template_dataset={},
        ),
        web_app=WorkspaceWebApp(
            url="url_example",
            iframes={},
            options={},
        ),
        send_input_to_data_warehouse=True,
        use_dedicated_event_hub_namespace=False,
        dedicated_event_hub_sas_key_name="dedicated_event_hub_sas_key_name_example",
        dedicated_event_hub_authentication_strategy="dedicated_event_hub_authentication_strategy_example",
        send_scenario_run_to_event_hub=True,
        send_scenario_metadata_to_event_hub=False,
        security=None,
    ) # Workspace | The new Workspace details.

    # example passing only required values which don't have defaults set
    try:
        # Update a workspace
        api_response = api_instance.update_workspace(organization_id, workspace_id, workspace)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->update_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **workspace** | [**Workspace**](Workspace.md)| The new Workspace details. |

### Return type

[**Workspace**](Workspace.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the workspace details |  -  |
**400** | Bad request |  -  |
**404** | the Workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace_access_control**
> WorkspaceAccessControl update_workspace_access_control(organization_id, workspace_id, identity_id, workspace_role)

Update the specified access to User for a Workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace_role import WorkspaceRole
from cosmotech_api.model.workspace_access_control import WorkspaceAccessControl
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    identity_id = "identity_id_example" # str | the User identifier
    workspace_role = WorkspaceRole(
        role="role_example",
    ) # WorkspaceRole | The new Workspace Access Control

    # example passing only required values which don't have defaults set
    try:
        # Update the specified access to User for a Workspace
        api_response = api_instance.update_workspace_access_control(organization_id, workspace_id, identity_id, workspace_role)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->update_workspace_access_control: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **identity_id** | **str**| the User identifier |
 **workspace_role** | [**WorkspaceRole**](WorkspaceRole.md)| The new Workspace Access Control |

### Return type

[**WorkspaceAccessControl**](WorkspaceAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Workspace access |  -  |
**404** | The Workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_workspace_file**
> WorkspaceFile upload_workspace_file(organization_id, workspace_id, file)

Upload a file for the Workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace_file import WorkspaceFile
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    file = open('/path/to/file', 'rb') # file_type | 
    overwrite = False # bool |  (optional) if omitted the server will use the default value of False
    destination = "path/to/a/directory/" # str | Destination path. Must end with a '/' if specifying a folder. Note that paths may or may not start with a '/', but they are always treated as relative to the Workspace root location.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload a file for the Workspace
        api_response = api_instance.upload_workspace_file(organization_id, workspace_id, file)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->upload_workspace_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload a file for the Workspace
        api_response = api_instance.upload_workspace_file(organization_id, workspace_id, file, overwrite=overwrite, destination=destination)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->upload_workspace_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **file** | **file_type**|  |
 **overwrite** | **bool**|  | [optional] if omitted the server will use the default value of False
 **destination** | **str**| Destination path. Must end with a &#39;/&#39; if specifying a folder. Note that paths may or may not start with a &#39;/&#39;, but they are always treated as relative to the Workspace root location.  | [optional]

### Return type

[**WorkspaceFile**](WorkspaceFile.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the file resource details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

