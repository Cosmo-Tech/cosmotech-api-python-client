# cosmotech_api.PlatformApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_platform**](PlatformApi.md#create_platform) | **POST** /platform | Create a new platform
[**get_platform**](PlatformApi.md#get_platform) | **GET** /platform | Get the details of the platform
[**update_platform**](PlatformApi.md#update_platform) | **PATCH** /platform | Update a platform


# **create_platform**
> Platform create_platform(platform)

Create a new platform

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import platform_api
from cosmotech_api.model.platform import Platform
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "http://localhost:8080"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api.PlatformApi(api_client)
    platform = Platform(
        name="name_example",
        description="description_example",
        version="version_example",
        owner_id="owner_id_example",
        api_host="api_host_example",
        web_app_url="web_app_url_example",
        services=PlatformServices(
            provider="Azure",
            credentials={},
            storage=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            core_container_registry=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            solutions_container_registry=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            event_bus_cluster=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            data_warehouse_cluster=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            database_cluster=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            key_vault=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            kubernetes_cluster=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            directory=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            monitoring=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            analytic=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
        ),
    ) # Platform | the Platform to create

    # example passing only required values which don't have defaults set
    try:
        # Create a new platform
        api_response = api_instance.create_platform(platform)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling PlatformApi->create_platform: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | [**Platform**](Platform.md)| the Platform to create |

### Return type

[**Platform**](Platform.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the platform details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_platform**
> Platform get_platform()

Get the details of the platform

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import platform_api
from cosmotech_api.model.platform import Platform
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "http://localhost:8080"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api.PlatformApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the details of the platform
        api_response = api_instance.get_platform()
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling PlatformApi->get_platform: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Platform**](Platform.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Platform details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_platform**
> Platform update_platform(platform)

Update a platform

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import platform_api
from cosmotech_api.model.platform import Platform
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2AuthCode
configuration = cosmotech_api.Configuration(
    host = "http://localhost:8080"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api.PlatformApi(api_client)
    platform = Platform(
        name="name_example",
        description="description_example",
        version="version_example",
        owner_id="owner_id_example",
        api_host="api_host_example",
        web_app_url="web_app_url_example",
        services=PlatformServices(
            provider="Azure",
            credentials={},
            storage=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            core_container_registry=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            solutions_container_registry=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            event_bus_cluster=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            data_warehouse_cluster=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            database_cluster=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            key_vault=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            kubernetes_cluster=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            directory=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            monitoring=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
            analytic=PlatformService(
                cloud_service="cloud_service_example",
                base_uri="base_uri_example",
                resource_uri="resource_uri_example",
                credentials={},
                options={},
            ),
        ),
    ) # Platform | the new Platform details.

    # example passing only required values which don't have defaults set
    try:
        # Update a platform
        api_response = api_instance.update_platform(platform)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling PlatformApi->update_platform: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | [**Platform**](Platform.md)| the new Platform details. |

### Return type

[**Platform**](Platform.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the platform details |  -  |
**400** | Bad request |  -  |
**404** | the Platform specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

