# cosmotech_api.WorkspaceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_workspace_access_control**](WorkspaceApi.md#add_workspace_access_control) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/security/access | Add a control access to the Workspace
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
[**link_dataset**](WorkspaceApi.md#link_dataset) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/link | 
[**remove_workspace_access_control**](WorkspaceApi.md#remove_workspace_access_control) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/security/access/{identity_id} | Remove the specified access from the given Organization Workspace
[**set_workspace_default_security**](WorkspaceApi.md#set_workspace_default_security) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/security/default | Set the Workspace default security
[**unlink_dataset**](WorkspaceApi.md#unlink_dataset) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/unlink | 
[**update_workspace**](WorkspaceApi.md#update_workspace) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id} | Update a workspace
[**update_workspace_access_control**](WorkspaceApi.md#update_workspace_access_control) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id}/security/access/{identity_id} | Update the specified access to User for a Workspace
[**upload_workspace_file**](WorkspaceApi.md#upload_workspace_file) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/files | Upload a file for the Workspace


# **add_workspace_access_control**
> WorkspaceAccessControl add_workspace_access_control(organization_id, workspace_id, workspace_access_control)

Add a control access to the Workspace

### Example


```python
import cosmotech_api
from cosmotech_api.models.workspace_access_control import WorkspaceAccessControl
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    workspace_access_control = cosmotech_api.WorkspaceAccessControl() # WorkspaceAccessControl | the new Workspace security access to add.

    try:
        # Add a control access to the Workspace
        api_response = api_instance.add_workspace_access_control(organization_id, workspace_id, workspace_access_control)
        print("The response of WorkspaceApi->add_workspace_access_control:\n")
        pprint(api_response)
    except Exception as e:
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Workspace access |  -  |
**404** | the Workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace**
> Workspace create_workspace(organization_id, workspace)

Create a new workspace

### Example


```python
import cosmotech_api
from cosmotech_api.models.workspace import Workspace
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace = cosmotech_api.Workspace() # Workspace | the Workspace to create

    try:
        # Create a new workspace
        api_response = api_instance.create_workspace(organization_id, workspace)
        print("The response of WorkspaceApi->create_workspace:\n")
        pprint(api_response)
    except Exception as e:
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

No authorization required

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


```python
import cosmotech_api
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier

    try:
        # Delete all Workspace files
        api_instance.delete_all_workspace_files(organization_id, workspace_id)
    except Exception as e:
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

No authorization required

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
> delete_workspace(organization_id, workspace_id)

Delete a workspace

### Example


```python
import cosmotech_api
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier

    try:
        # Delete a workspace
        api_instance.delete_workspace(organization_id, workspace_id)
    except Exception as e:
        print("Exception when calling WorkspaceApi->delete_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | the workspace details |  -  |
**400** | Bad request |  -  |
**404** | the Workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_file**
> delete_workspace_file(organization_id, workspace_id, file_name)

Delete a workspace file

### Example


```python
import cosmotech_api
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    file_name = 'file_name_example' # str | the file name

    try:
        # Delete a workspace file
        api_instance.delete_workspace_file(organization_id, workspace_id, file_name)
    except Exception as e:
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

No authorization required

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
> bytearray download_workspace_file(organization_id, workspace_id, file_name)

Download the Workspace File specified

### Example


```python
import cosmotech_api
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    file_name = 'file_name_example' # str | the file name

    try:
        # Download the Workspace File specified
        api_response = api_instance.download_workspace_file(organization_id, workspace_id, file_name)
        print("The response of WorkspaceApi->download_workspace_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->download_workspace_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **file_name** | **str**| the file name | 

### Return type

**bytearray**

### Authorization

No authorization required

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
> List[WorkspaceFile] find_all_workspace_files(organization_id, workspace_id)

List all Workspace files

### Example


```python
import cosmotech_api
from cosmotech_api.models.workspace_file import WorkspaceFile
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier

    try:
        # List all Workspace files
        api_response = api_instance.find_all_workspace_files(organization_id, workspace_id)
        print("The response of WorkspaceApi->find_all_workspace_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->find_all_workspace_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 

### Return type

[**List[WorkspaceFile]**](WorkspaceFile.md)

### Authorization

No authorization required

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
> List[Workspace] find_all_workspaces(organization_id, page=page, size=size)

List all Workspaces

### Example


```python
import cosmotech_api
from cosmotech_api.models.workspace import Workspace
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    page = 56 # int | page number to query (optional)
    size = 56 # int | amount of result by page (optional)

    try:
        # List all Workspaces
        api_response = api_instance.find_all_workspaces(organization_id, page=page, size=size)
        print("The response of WorkspaceApi->find_all_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->find_all_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **page** | **int**| page number to query | [optional] 
 **size** | **int**| amount of result by page | [optional] 

### Return type

[**List[Workspace]**](Workspace.md)

### Authorization

No authorization required

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


```python
import cosmotech_api
from cosmotech_api.models.workspace import Workspace
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier

    try:
        # Get the details of an workspace
        api_response = api_instance.find_workspace_by_id(organization_id, workspace_id)
        print("The response of WorkspaceApi->find_workspace_by_id:\n")
        pprint(api_response)
    except Exception as e:
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

No authorization required

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


```python
import cosmotech_api
from cosmotech_api.models.workspace_access_control import WorkspaceAccessControl
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    identity_id = 'identity_id_example' # str | the User identifier

    try:
        # Get a control access for the Workspace
        api_response = api_instance.get_workspace_access_control(organization_id, workspace_id, identity_id)
        print("The response of WorkspaceApi->get_workspace_access_control:\n")
        pprint(api_response)
    except Exception as e:
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

No authorization required

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
> List[str] get_workspace_permissions(organization_id, workspace_id, role)

Get the Workspace permission by given role

### Example


```python
import cosmotech_api
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    role = 'role_example' # str | the Role

    try:
        # Get the Workspace permission by given role
        api_response = api_instance.get_workspace_permissions(organization_id, workspace_id, role)
        print("The response of WorkspaceApi->get_workspace_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->get_workspace_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **role** | **str**| the Role | 

### Return type

**List[str]**

### Authorization

No authorization required

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


```python
import cosmotech_api
from cosmotech_api.models.workspace_security import WorkspaceSecurity
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier

    try:
        # Get the Workspace security information
        api_response = api_instance.get_workspace_security(organization_id, workspace_id)
        print("The response of WorkspaceApi->get_workspace_security:\n")
        pprint(api_response)
    except Exception as e:
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

No authorization required

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
> List[str] get_workspace_security_users(organization_id, workspace_id)

Get the Workspace security users list

### Example


```python
import cosmotech_api
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier

    try:
        # Get the Workspace security users list
        api_response = api_instance.get_workspace_security_users(organization_id, workspace_id)
        print("The response of WorkspaceApi->get_workspace_security_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->get_workspace_security_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Workspace security users list |  -  |
**404** | the Workspace or the User specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_dataset**
> Workspace link_dataset(organization_id, workspace_id, dataset_id)



### Example


```python
import cosmotech_api
from cosmotech_api.models.workspace import Workspace
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | dataset id to be linked to

    try:
        api_response = api_instance.link_dataset(organization_id, workspace_id, dataset_id)
        print("The response of WorkspaceApi->link_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->link_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| dataset id to be linked to | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the workspace details |  -  |
**400** | Bad request |  -  |
**404** | the workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_workspace_access_control**
> remove_workspace_access_control(organization_id, workspace_id, identity_id)

Remove the specified access from the given Organization Workspace

### Example


```python
import cosmotech_api
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    identity_id = 'identity_id_example' # str | the User identifier

    try:
        # Remove the specified access from the given Organization Workspace
        api_instance.remove_workspace_access_control(organization_id, workspace_id, identity_id)
    except Exception as e:
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

No authorization required

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


```python
import cosmotech_api
from cosmotech_api.models.workspace_role import WorkspaceRole
from cosmotech_api.models.workspace_security import WorkspaceSecurity
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    workspace_role = cosmotech_api.WorkspaceRole() # WorkspaceRole | This change the workspace default security. The default security is the role assigned to any person not on the Access Control List. If the default security is None, then nobody outside of the ACL can access the workspace.

    try:
        # Set the Workspace default security
        api_response = api_instance.set_workspace_default_security(organization_id, workspace_id, workspace_role)
        print("The response of WorkspaceApi->set_workspace_default_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->set_workspace_default_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **workspace_role** | [**WorkspaceRole**](WorkspaceRole.md)| This change the workspace default security. The default security is the role assigned to any person not on the Access Control List. If the default security is None, then nobody outside of the ACL can access the workspace. | 

### Return type

[**WorkspaceSecurity**](WorkspaceSecurity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Workspace default visibility |  -  |
**404** | the Workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_dataset**
> Workspace unlink_dataset(organization_id, workspace_id, dataset_id)



### Example


```python
import cosmotech_api
from cosmotech_api.models.workspace import Workspace
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | dataset id to be linked to

    try:
        api_response = api_instance.unlink_dataset(organization_id, workspace_id, dataset_id)
        print("The response of WorkspaceApi->unlink_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->unlink_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| dataset id to be linked to | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the workspace details |  -  |
**400** | Bad request |  -  |
**404** | the Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace**
> Workspace update_workspace(organization_id, workspace_id, workspace)

Update a workspace

### Example


```python
import cosmotech_api
from cosmotech_api.models.workspace import Workspace
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    workspace = cosmotech_api.Workspace() # Workspace | The new Workspace details. This endpoint can't be used to update security

    try:
        # Update a workspace
        api_response = api_instance.update_workspace(organization_id, workspace_id, workspace)
        print("The response of WorkspaceApi->update_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->update_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **workspace** | [**Workspace**](Workspace.md)| The new Workspace details. This endpoint can&#39;t be used to update security | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

No authorization required

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


```python
import cosmotech_api
from cosmotech_api.models.workspace_access_control import WorkspaceAccessControl
from cosmotech_api.models.workspace_role import WorkspaceRole
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    identity_id = 'identity_id_example' # str | the User identifier
    workspace_role = cosmotech_api.WorkspaceRole() # WorkspaceRole | The new Workspace Access Control

    try:
        # Update the specified access to User for a Workspace
        api_response = api_instance.update_workspace_access_control(organization_id, workspace_id, identity_id, workspace_role)
        print("The response of WorkspaceApi->update_workspace_access_control:\n")
        pprint(api_response)
    except Exception as e:
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

No authorization required

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
> WorkspaceFile upload_workspace_file(organization_id, workspace_id, file, overwrite=overwrite, destination=destination)

Upload a file for the Workspace

### Example


```python
import cosmotech_api
from cosmotech_api.models.workspace_file import WorkspaceFile
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    file = None # bytearray | 
    overwrite = False # bool |  (optional) (default to False)
    destination = 'destination_example' # str | Destination path. Must end with a '/' if specifying a folder. Note that paths may or may not start with a '/', but they are always treated as relative to the Workspace root location.  (optional)

    try:
        # Upload a file for the Workspace
        api_response = api_instance.upload_workspace_file(organization_id, workspace_id, file, overwrite=overwrite, destination=destination)
        print("The response of WorkspaceApi->upload_workspace_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->upload_workspace_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **file** | **bytearray**|  | 
 **overwrite** | **bool**|  | [optional] [default to False]
 **destination** | **str**| Destination path. Must end with a &#39;/&#39; if specifying a folder. Note that paths may or may not start with a &#39;/&#39;, but they are always treated as relative to the Workspace root location.  | [optional] 

### Return type

[**WorkspaceFile**](WorkspaceFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the file resource details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

