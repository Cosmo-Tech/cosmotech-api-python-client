# cosmotech_api.WorkspaceApi

All URIs are relative to *https://api.azure.cosmo-platform.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace**](WorkspaceApi.md#create_workspace) | **POST** /organizations/{organization_id}/workspaces | Create a new workspace
[**delete_workspace**](WorkspaceApi.md#delete_workspace) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id} | Delete a workspace
[**find_all_workspaces**](WorkspaceApi.md#find_all_workspaces) | **GET** /organizations/{organization_id}/workspaces | List all Workspaces
[**find_workspace_by_id**](WorkspaceApi.md#find_workspace_by_id) | **GET** /organizations/{organization_id}/workspaces/{workspace_id} | Get the details of an workspace
[**update_workspace**](WorkspaceApi.md#update_workspace) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id} | Update a workspace


# **create_workspace**
> Workspace create_workspace(organization_id, workspace)

Create a new workspace

### Example

* OAuth Authentication (AADOAuth2AuthCode):
* Api Key Authentication (ApiKeyAuth):
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

# Configure OAuth2 access token for authorization: AADOAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

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
        simulator=WorkspaceSimulator(
            simulator_id="simulator_id_example",
            simulator_analysis_filter=[
                "simulator_analysis_filter_example",
            ],
            default_analysis_dataset={},
        ),
        user_list=[
            WorkspaceUser(
                id="id_example",
                name="name_example",
                roles="Viewer",
            ),
        ],
        web_app=WorkspaceWebApp(
            url="url_example",
            iframes={},
            options={},
        ),
        resources={},
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

[AADOAuth2AuthCode](../README.md#AADOAuth2AuthCode), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

* OAuth Authentication (AADOAuth2AuthCode):
* Api Key Authentication (ApiKeyAuth):
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

# Configure OAuth2 access token for authorization: AADOAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

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

[AADOAuth2AuthCode](../README.md#AADOAuth2AuthCode), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

# **find_all_workspaces**
> [Workspace] find_all_workspaces(organization_id)

List all Workspaces

### Example

* OAuth Authentication (AADOAuth2AuthCode):
* Api Key Authentication (ApiKeyAuth):
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

# Configure OAuth2 access token for authorization: AADOAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

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

[AADOAuth2AuthCode](../README.md#AADOAuth2AuthCode), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

* OAuth Authentication (AADOAuth2AuthCode):
* Api Key Authentication (ApiKeyAuth):
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

# Configure OAuth2 access token for authorization: AADOAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

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

[AADOAuth2AuthCode](../README.md#AADOAuth2AuthCode), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Workspace details |  -  |
**404** | the Workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace**
> Workspace update_workspace(organization_id, workspace_id, workspace)

Update a workspace

### Example

* OAuth Authentication (AADOAuth2AuthCode):
* Api Key Authentication (ApiKeyAuth):
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

# Configure OAuth2 access token for authorization: AADOAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "https://api.azure.cosmo-platform.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

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
        simulator=WorkspaceSimulator(
            simulator_id="simulator_id_example",
            simulator_analysis_filter=[
                "simulator_analysis_filter_example",
            ],
            default_analysis_dataset={},
        ),
        user_list=[
            WorkspaceUser(
                id="id_example",
                name="name_example",
                roles="Viewer",
            ),
        ],
        web_app=WorkspaceWebApp(
            url="url_example",
            iframes={},
            options={},
        ),
        resources={},
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

[AADOAuth2AuthCode](../README.md#AADOAuth2AuthCode), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the workspace details |  -  |
**400** | Bad request |  -  |
**404** | the Workspace specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
