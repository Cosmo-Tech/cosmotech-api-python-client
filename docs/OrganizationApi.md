# cosmotech_api.OrganizationApi

All URIs are relative to *https://api.azure.cosmo-platform.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all_organizations**](OrganizationApi.md#find_all_organizations) | **GET** /organizations | List all Organizations
[**find_organization_by_id**](OrganizationApi.md#find_organization_by_id) | **GET** /organizations/{organization_id} | Get the details of an organization
[**register_organization**](OrganizationApi.md#register_organization) | **POST** /organizations | Register a new organization
[**unregister_organization**](OrganizationApi.md#unregister_organization) | **DELETE** /organizations/{organization_id} | Unregister an organization
[**update_organization**](OrganizationApi.md#update_organization) | **PATCH** /organizations/{organization_id} | Update an organization


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
**200** | the organization details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_organization_by_id**
> Organization find_organization_by_id(organization_id)

Get the details of an organization

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
from cosmotech_api.model.organization import Organization
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of an organization
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization = Organization(
        id="id_example",
        name="name_example",
        owner_id="owner_id_example",
        users=[
            OrganizationUser(
                id="id_example",
                name="name_example",
                organization_id="organization_id_example",
                roles=[
                    "Admin",
                ],
            ),
        ],
        services=OrganizationServices(
            tenant_credentials={},
            storage=OrganizationService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
            simulators_container_registry=OrganizationService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
        ),
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

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the organization details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_organization**
> Organization unregister_organization(organization_id)

Unregister an organization

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
from cosmotech_api.model.organization import Organization
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier

    # example passing only required values which don't have defaults set
    try:
        # Unregister an organization
        api_response = api_instance.unregister_organization(organization_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling OrganizationApi->unregister_organization: %s\n" % e)
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
**200** | the organization details |  -  |
**400** | Bad request |  -  |
**404** | the Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization**
> Organization update_organization(organization_id, organization)

Update an organization

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import organization_api
from cosmotech_api.model.organization import Organization
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
    api_instance = organization_api.OrganizationApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    organization = Organization(
        id="id_example",
        name="name_example",
        owner_id="owner_id_example",
        users=[
            OrganizationUser(
                id="id_example",
                name="name_example",
                organization_id="organization_id_example",
                roles=[
                    "Admin",
                ],
            ),
        ],
        services=OrganizationServices(
            tenant_credentials={},
            storage=OrganizationService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
            simulators_container_registry=OrganizationService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                platform_service="platform_service_example",
                resource_uri="resource_uri_example",
                credentials={},
            ),
        ),
    ) # Organization | the new Organization details

    # example passing only required values which don't have defaults set
    try:
        # Update an organization
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

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the organization details |  -  |
**400** | Bad request |  -  |
**404** | the Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

