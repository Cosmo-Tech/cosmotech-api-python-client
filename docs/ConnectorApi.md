# cosmotech_api.ConnectorApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all_connectors**](ConnectorApi.md#find_all_connectors) | **GET** /connectors | List all Connectors
[**find_connector_by_id**](ConnectorApi.md#find_connector_by_id) | **GET** /connectors/{connector_id} | Get the details of a connector
[**register_connector**](ConnectorApi.md#register_connector) | **POST** /connectors | Register a new connector
[**unregister_connector**](ConnectorApi.md#unregister_connector) | **DELETE** /connectors/{connector_id} | Unregister a connector


# **find_all_connectors**
> [Connector] find_all_connectors()

List all Connectors

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import connector_api
from cosmotech_api.model.connector import Connector
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
    api_instance = connector_api.ConnectorApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all Connectors
        api_response = api_instance.find_all_connectors()
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ConnectorApi->find_all_connectors: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Connector]**](Connector.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the list of Connectors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_connector_by_id**
> Connector find_connector_by_id(connector_id)

Get the details of a connector

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import connector_api
from cosmotech_api.model.connector import Connector
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connector_id_example" # str | the Connector identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a connector
        api_response = api_instance.find_connector_by_id(connector_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ConnectorApi->find_connector_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| the Connector identifier |

### Return type

[**Connector**](Connector.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Connector details |  -  |
**404** | the Connector specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_connector**
> Connector register_connector(connector)

Register a new connector

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import connector_api
from cosmotech_api.model.connector import Connector
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector = Connector(
        key="key_example",
        name="name_example",
        description="description_example",
        repository="repository_example",
        version="version_example",
        tags=[
            "tags_example",
        ],
        url="url_example",
        azure_managed_identity=True,
        azure_authentication_with_customer_app_registration=True,
        io_types=[
            "read",
        ],
        parameter_groups=[
            ConnectorParameterGroup(
                id="id_example",
                label="label_example",
                parameters=[
                    ConnectorParameter(
                        id="id_example",
                        label="label_example",
                        value_type="value_type_example",
                        options=[
                            "options_example",
                        ],
                        default="default_example",
                        env_var="env_var_example",
                    ),
                ],
            ),
        ],
    ) # Connector | the Connector to register

    # example passing only required values which don't have defaults set
    try:
        # Register a new connector
        api_response = api_instance.register_connector(connector)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ConnectorApi->register_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector** | [**Connector**](Connector.md)| the Connector to register |

### Return type

[**Connector**](Connector.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the connector details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_connector**
> unregister_connector(connector_id)

Unregister a connector

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import connector_api
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connector_id_example" # str | the Connector identifier

    # example passing only required values which don't have defaults set
    try:
        # Unregister a connector
        api_instance.unregister_connector(connector_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ConnectorApi->unregister_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| the Connector identifier |

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
**204** | Request successful |  -  |
**404** | the Connector specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

