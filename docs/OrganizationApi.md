# cosmotech_api.OrganizationApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_organization_access_control**](OrganizationApi.md#add_organization_access_control) | **POST** /organizations/{organization_id}/security/access | Add a control access to the Organization
[**find_all_organizations**](OrganizationApi.md#find_all_organizations) | **GET** /organizations | List all Organizations
[**find_organization_by_id**](OrganizationApi.md#find_organization_by_id) | **GET** /organizations/{organization_id} | Get the details of an Organization
[**get_all_permissions**](OrganizationApi.md#get_all_permissions) | **GET** /organizations/permissions | Get all permissions per components
[**get_organization_access_control**](OrganizationApi.md#get_organization_access_control) | **GET** /organizations/{organization_id}/security/access/{identity_id} | Get a control access for the Organization
[**get_organization_permissions**](OrganizationApi.md#get_organization_permissions) | **GET** /organizations/{organization_id}/permissions/{role} | Get the Organization permissions by given role
[**get_organization_security**](OrganizationApi.md#get_organization_security) | **GET** /organizations/{organization_id}/security | Get the Organization security information
[**get_organization_security_users**](OrganizationApi.md#get_organization_security_users) | **GET** /organizations/{organization_id}/security/users | Get the Organization security users list
[**register_organization**](OrganizationApi.md#register_organization) | **POST** /organizations | Register a new organization
[**remove_organization_access_control**](OrganizationApi.md#remove_organization_access_control) | **DELETE** /organizations/{organization_id}/security/access/{identity_id} | Remove the specified access from the given Organization
[**set_organization_default_security**](OrganizationApi.md#set_organization_default_security) | **POST** /organizations/{organization_id}/security/default | Set the Organization default security
[**unregister_organization**](OrganizationApi.md#unregister_organization) | **DELETE** /organizations/{organization_id} | Unregister an organization
[**update_organization**](OrganizationApi.md#update_organization) | **PATCH** /organizations/{organization_id} | Update an Organization
[**update_organization_access_control**](OrganizationApi.md#update_organization_access_control) | **PATCH** /organizations/{organization_id}/security/access/{identity_id} | Update the specified access to User for an Organization
[**update_solutions_container_registry_by_organization_id**](OrganizationApi.md#update_solutions_container_registry_by_organization_id) | **PATCH** /organizations/{organization_id}/services/solutionsContainerRegistry | Update the solutions container registry configuration for the Organization specified
[**update_storage_by_organization_id**](OrganizationApi.md#update_storage_by_organization_id) | **PATCH** /organizations/{organization_id}/services/storage | Update storage configuration for the Organization specified
[**update_tenant_credentials_by_organization_id**](OrganizationApi.md#update_tenant_credentials_by_organization_id) | **PATCH** /organizations/{organization_id}/services/tenantCredentials | Update tenant credentials for the Organization specified


# **add_organization_access_control**
> OrganizationAccessControl add_organization_access_control(organization_id, organization_access_control)

Add a control access to the Organization

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
from cosmotech_api.model.organization_access_control import OrganizationAccessControl
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    organization_access_control = OrganizationAccessControl(
        id="id_example",
        role="role_example",
    ) # OrganizationAccessControl | the new Organization security access to add.

    # example passing only required values which don't have defaults set
    try:
        # Add a control access to the Organization
        api_response = api_instance.add_organization_access_control(organization_id, organization_access_control)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->add_organization_access_control: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **organization_access_control** | [**OrganizationAccessControl**](OrganizationAccessControl.md)| the new Organization security access to add. |

### Return type

[**OrganizationAccessControl**](OrganizationAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Organization access |  -  |
**404** | the Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_organizations**
> [Organization] find_all_organizations()

List all Organizations

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
from cosmotech_api.model.organization import Organization
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
    api_instance = organization_api.OrganizationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all Organizations
        api_response = api_instance.find_all_organizations()
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->find_all_organizations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Organization]**](Organization.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the list of Organizations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_organization_by_id**
> Organization find_organization_by_id(organization_id)

Get the details of an Organization

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
from cosmotech_api.model.organization import Organization
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of an Organization
        api_response = api_instance.find_organization_by_id(organization_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->find_organization_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |

### Return type

[**Organization**](Organization.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Organization details |  -  |
**404** | the Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_permissions**
> [ComponentRolePermissions] get_all_permissions()

Get all permissions per components

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
from cosmotech_api.model.component_role_permissions import ComponentRolePermissions
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
    api_instance = organization_api.OrganizationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all permissions per components
        api_response = api_instance.get_all_permissions()
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->get_all_permissions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ComponentRolePermissions]**](ComponentRolePermissions.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Scenarios security permission list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_access_control**
> OrganizationAccessControl get_organization_access_control(organization_id, identity_id)

Get a control access for the Organization

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
from cosmotech_api.model.organization_access_control import OrganizationAccessControl
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    identity_id = "identity_id_example" # str | the User identifier

    # example passing only required values which don't have defaults set
    try:
        # Get a control access for the Organization
        api_response = api_instance.get_organization_access_control(organization_id, identity_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->get_organization_access_control: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **identity_id** | **str**| the User identifier |

### Return type

[**OrganizationAccessControl**](OrganizationAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Organization access |  -  |
**404** | The Organization or user specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_permissions**
> [str] get_organization_permissions(organization_id, role)

Get the Organization permissions by given role

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    role = "role_example" # str | the Role

    # example passing only required values which don't have defaults set
    try:
        # Get the Organization permissions by given role
        api_response = api_instance.get_organization_permissions(organization_id, role)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->get_organization_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
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
**200** | The Organization security permission list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_security**
> OrganizationSecurity get_organization_security(organization_id)

Get the Organization security information

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
from cosmotech_api.model.organization_security import OrganizationSecurity
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the Organization security information
        api_response = api_instance.get_organization_security(organization_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->get_organization_security: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |

### Return type

[**OrganizationSecurity**](OrganizationSecurity.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Organization security |  -  |
**404** | the Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_security_users**
> [str] get_organization_security_users(organization_id)

Get the Organization security users list

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | The Organization identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the Organization security users list
        api_response = api_instance.get_organization_security_users(organization_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->get_organization_security_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The Organization identifier |

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
**200** | The Organization security users list |  -  |
**404** | the Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_organization**
> Organization register_organization(organization)

Register a new organization

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
from cosmotech_api.model.organization import Organization
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization = Organization(
        name="name_example",
        services=OrganizationServices(
            tenant_credentials={},
            storage=OrganizationService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
            solutions_container_registry=OrganizationService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
        ),
        security=None,
    ) # Organization | the Organization to register

    # example passing only required values which don't have defaults set
    try:
        # Register a new organization
        api_response = api_instance.register_organization(organization)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->register_organization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | [**Organization**](Organization.md)| the Organization to register |

### Return type

[**Organization**](Organization.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the Organization details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_organization_access_control**
> remove_organization_access_control(organization_id, identity_id)

Remove the specified access from the given Organization

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    identity_id = "identity_id_example" # str | the User identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove the specified access from the given Organization
        api_instance.remove_organization_access_control(organization_id, identity_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->remove_organization_access_control: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
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
**404** | the Organization or the user specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_organization_default_security**
> OrganizationSecurity set_organization_default_security(organization_id, organization_role)

Set the Organization default security

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
from cosmotech_api.model.organization_role import OrganizationRole
from cosmotech_api.model.organization_security import OrganizationSecurity
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    organization_role = OrganizationRole(
        role="role_example",
    ) # OrganizationRole | the new Organization default security.

    # example passing only required values which don't have defaults set
    try:
        # Set the Organization default security
        api_response = api_instance.set_organization_default_security(organization_id, organization_role)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->set_organization_default_security: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **organization_role** | [**OrganizationRole**](OrganizationRole.md)| the new Organization default security. |

### Return type

[**OrganizationSecurity**](OrganizationSecurity.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Organization default visibility |  -  |
**404** | the Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_organization**
> unregister_organization(organization_id)

Unregister an organization

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier

    # example passing only required values which don't have defaults set
    try:
        # Unregister an organization
        api_instance.unregister_organization(organization_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->unregister_organization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |

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
**404** | the Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization**
> Organization update_organization(organization_id, organization)

Update an Organization

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
from cosmotech_api.model.organization import Organization
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    organization = Organization(
        name="name_example",
        services=OrganizationServices(
            tenant_credentials={},
            storage=OrganizationService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
            solutions_container_registry=OrganizationService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
        ),
        security=None,
    ) # Organization | the new Organization details

    # example passing only required values which don't have defaults set
    try:
        # Update an Organization
        api_response = api_instance.update_organization(organization_id, organization)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->update_organization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **organization** | [**Organization**](Organization.md)| the new Organization details |

### Return type

[**Organization**](Organization.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the organization details |  -  |
**400** | Bad request |  -  |
**404** | the Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_access_control**
> OrganizationAccessControl update_organization_access_control(organization_id, identity_id, organization_role)

Update the specified access to User for an Organization

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
from cosmotech_api.model.organization_access_control import OrganizationAccessControl
from cosmotech_api.model.organization_role import OrganizationRole
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    identity_id = "identity_id_example" # str | the User identifier
    organization_role = OrganizationRole(
        role="role_example",
    ) # OrganizationRole | The new Organization Access Control

    # example passing only required values which don't have defaults set
    try:
        # Update the specified access to User for an Organization
        api_response = api_instance.update_organization_access_control(organization_id, identity_id, organization_role)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->update_organization_access_control: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **identity_id** | **str**| the User identifier |
 **organization_role** | [**OrganizationRole**](OrganizationRole.md)| The new Organization Access Control |

### Return type

[**OrganizationAccessControl**](OrganizationAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Organization access |  -  |
**404** | The Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_solutions_container_registry_by_organization_id**
> OrganizationService update_solutions_container_registry_by_organization_id(organization_id, organization_service)

Update the solutions container registry configuration for the Organization specified

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
from cosmotech_api.model.organization_service import OrganizationService
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    organization_service = OrganizationService(
        cloud_service="cloud_service_example",
        base_uri="base_uri_example",
        platform_service="platform_service_example",
        resource_uri="resource_uri_example",
        credentials={},
    ) # OrganizationService | the new solutions container registry configuration to use

    # example passing only required values which don't have defaults set
    try:
        # Update the solutions container registry configuration for the Organization specified
        api_response = api_instance.update_solutions_container_registry_by_organization_id(organization_id, organization_service)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->update_solutions_container_registry_by_organization_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **organization_service** | [**OrganizationService**](OrganizationService.md)| the new solutions container registry configuration to use |

### Return type

[**OrganizationService**](OrganizationService.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Organization solutions container registry configuration |  -  |
**404** | the Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storage_by_organization_id**
> OrganizationService update_storage_by_organization_id(organization_id, organization_service)

Update storage configuration for the Organization specified

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
from cosmotech_api.model.organization_service import OrganizationService
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    organization_service = OrganizationService(
        cloud_service="cloud_service_example",
        base_uri="base_uri_example",
        platform_service="platform_service_example",
        resource_uri="resource_uri_example",
        credentials={},
    ) # OrganizationService | the new Storage configuration to use

    # example passing only required values which don't have defaults set
    try:
        # Update storage configuration for the Organization specified
        api_response = api_instance.update_storage_by_organization_id(organization_id, organization_service)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->update_storage_by_organization_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **organization_service** | [**OrganizationService**](OrganizationService.md)| the new Storage configuration to use |

### Return type

[**OrganizationService**](OrganizationService.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Organization Storage configuration |  -  |
**404** | the Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant_credentials_by_organization_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_tenant_credentials_by_organization_id(organization_id, request_body)

Update tenant credentials for the Organization specified

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | the new Tenant Credentials to use

    # example passing only required values which don't have defaults set
    try:
        # Update tenant credentials for the Organization specified
        api_response = api_instance.update_tenant_credentials_by_organization_id(organization_id, request_body)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->update_tenant_credentials_by_organization_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| the new Tenant Credentials to use |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Organization Tenant Credentials |  -  |
**404** | the Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

