# cosmotech_api.WorkspaceApi

All URIs are relative to *https://api.azure.cosmo-platform.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_users_to_organization_workspace**](WorkspaceApi.md#add_users_to_organization_workspace) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/users | Add (or replace) users to the Workspace specified
[**create_workspace**](WorkspaceApi.md#create_workspace) | **POST** /organizations/{organization_id}/workspaces | Create a new workspace
[**delete_workspace**](WorkspaceApi.md#delete_workspace) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id} | Delete a workspace
[**delete_workspace_file**](WorkspaceApi.md#delete_workspace_file) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/files | Delete a workspace file
[**find_all_workspace_files**](WorkspaceApi.md#find_all_workspace_files) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/files | List all Workspace files
[**find_all_workspaces**](WorkspaceApi.md#find_all_workspaces) | **GET** /organizations/{organization_id}/workspaces | List all Workspaces
[**find_workspace_by_id**](WorkspaceApi.md#find_workspace_by_id) | **GET** /organizations/{organization_id}/workspaces/{workspace_id} | Get the details of an workspace
[**remove_all_users_of_workspace**](WorkspaceApi.md#remove_all_users_of_workspace) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/users | Remove all users from the Workspace specified
[**update_workspace**](WorkspaceApi.md#update_workspace) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id} | Update a workspace
[**upload_workspace_file**](WorkspaceApi.md#upload_workspace_file) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/files | Upload a file for the Workspace


# **add_users_to_organization_workspace**
> [WorkspaceUser] add_users_to_organization_workspace(organization_id, workspace_id, workspace_user)

Add (or replace) users to the Workspace specified

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace_user import WorkspaceUser
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    workspace_user = [
        WorkspaceUser(
            id="id_example",
            name="name_example",
            roles=[
                "Admin",
            ],
        ),
    ] # [WorkspaceUser] | the Users to add. Any User with the same ID is overwritten

    # example passing only required values which don't have defaults set
    try:
        # Add (or replace) users to the Workspace specified
        api_response = api_instance.add_users_to_organization_workspace(organization_id, workspace_id, workspace_user)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->add_users_to_organization_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **workspace_user** | [**[WorkspaceUser]**](WorkspaceUser.md)| the Users to add. Any User with the same ID is overwritten |

### Return type

[**[WorkspaceUser]**](WorkspaceUser.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Workspace Users |  -  |
**404** | the Workspace specified is unknown or you don&#39;t have access to it |  -  |

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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace = Workspace(
        id="id_example",
        name="name_example",
        description="description_example",
        version="version_example",
        tags=[
            "tags_example",
        ],
        owner_id="owner_id_example",
        solution=WorkspaceSolution(
            solution_id="solution_id_example",
            run_template_filter=[
                "run_template_filter_example",
            ],
            default_run_template_dataset={},
        ),
        users=[
            WorkspaceUser(
                id="id_example",
                name="name_example",
                roles=[
                    "Admin",
                ],
            ),
        ],
        web_app=WorkspaceWebApp(
            url="url_example",
            iframes={},
            options={},
        ),
        services=WorkspaceServices(
            tenant_credentials={},
            results_event_bus=WorkspaceService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
            scenariorun_event_bus=WorkspaceService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
            data_warehouse=WorkspaceService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
            storage=WorkspaceService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
        ),
        send_input_to_data_warehouse=True,
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
> WorkspaceFile delete_workspace_file(organization_id, workspace_id, workspace_file)

Delete a workspace file

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace_file import WorkspaceFile
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    workspace_file = WorkspaceFile(
        file_name="file_name_example",
    ) # WorkspaceFile | the file to upload

    # example passing only required values which don't have defaults set
    try:
        # Delete a workspace file
        api_response = api_instance.delete_workspace_file(organization_id, workspace_id, workspace_file)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->delete_workspace_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **workspace_file** | [**WorkspaceFile**](WorkspaceFile.md)| the file to upload |

### Return type

[**WorkspaceFile**](WorkspaceFile.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the file resource details |  -  |
**400** | Bad request |  -  |
**404** | the Workspace specified is unknown or you don&#39;t have access to it |  -  |

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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier

    # example passing only required values which don't have defaults set
    try:
        # List all Workspaces
        api_response = api_instance.find_all_workspaces(organization_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->find_all_workspaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |

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
**404** | the Workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_users_of_workspace**
> remove_all_users_of_workspace(organization_id, workspace_id)

Remove all users from the Workspace specified

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove all users from the Workspace specified
        api_instance.remove_all_users_of_workspace(organization_id, workspace_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->remove_all_users_of_workspace: %s\n" % e)
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
**204** | the operation succeeded |  -  |
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    workspace = Workspace(
        id="id_example",
        name="name_example",
        description="description_example",
        version="version_example",
        tags=[
            "tags_example",
        ],
        owner_id="owner_id_example",
        solution=WorkspaceSolution(
            solution_id="solution_id_example",
            run_template_filter=[
                "run_template_filter_example",
            ],
            default_run_template_dataset={},
        ),
        users=[
            WorkspaceUser(
                id="id_example",
                name="name_example",
                roles=[
                    "Admin",
                ],
            ),
        ],
        web_app=WorkspaceWebApp(
            url="url_example",
            iframes={},
            options={},
        ),
        services=WorkspaceServices(
            tenant_credentials={},
            results_event_bus=WorkspaceService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
            scenariorun_event_bus=WorkspaceService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
            data_warehouse=WorkspaceService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
            storage=WorkspaceService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
        ),
        send_input_to_data_warehouse=True,
    ) # Workspace | the new Workspace details.

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
 **workspace** | [**Workspace**](Workspace.md)| the new Workspace details. |

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

# **upload_workspace_file**
> WorkspaceFile upload_workspace_file(organization_id, workspace_id)

Upload a file for the Workspace

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import workspace_api
from cosmotech_api.model.workspace_file import WorkspaceFile
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
    api_instance = workspace_api.WorkspaceApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    file_name = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload a file for the Workspace
        api_response = api_instance.upload_workspace_file(organization_id, workspace_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->upload_workspace_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload a file for the Workspace
        api_response = api_instance.upload_workspace_file(organization_id, workspace_id, file_name=file_name)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling WorkspaceApi->upload_workspace_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **file_name** | **file_type**|  | [optional]

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

