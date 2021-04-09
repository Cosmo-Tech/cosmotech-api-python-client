# cosmotech_api.SimulatorApi

All URIs are relative to *https://api.azure.cosmo-platform.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_simulator**](SimulatorApi.md#create_simulator) | **POST** /organizations/{organization_id}/simulators | Register a new simulator
[**delete_simulator**](SimulatorApi.md#delete_simulator) | **DELETE** /organizations/{organization_id}/simulators/{simulator_id} | Delete a simulator
[**find_all_simulators**](SimulatorApi.md#find_all_simulators) | **GET** /organizations/{organization_id}/simulators | List all Simulators
[**find_simulator_by_id**](SimulatorApi.md#find_simulator_by_id) | **GET** /organizations/{organization_id}/simulators/{simulator_id} | Get the details of a simulator
[**update_simulator**](SimulatorApi.md#update_simulator) | **PATCH** /organizations/{organization_id}/simulators/{simulator_id} | Update a simulator


# **create_simulator**
> Simulator create_simulator(organization_id, simulator)

Register a new simulator

### Example

* OAuth Authentication (AADOAuth2AuthCode):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulator_api
from cosmotech_api.model.simulator import Simulator
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
    api_instance = simulator_api.SimulatorApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    simulator = Simulator(
        id="id_example",
        simulator_key="simulator_key_example",
        name="name_example",
        description="description_example",
        repository="repository_example",
        version="version_example",
        owner_id="owner_id_example",
        url="url_example",
        tags=[
            "tags_example",
        ],
        analysis=[
            SimulatorAnalysis(
                id="id_example",
                name="name_example",
                description="description_example",
                simulation="simulation_example",
                tags=[
                    "tags_example",
                ],
                compute_size="compute_size_example",
                parameters_handler_resource=AnalysisResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                dataset_validator_resource=AnalysisResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                custom_driver_resource=AnalysisResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                parameter_groups=[
                    AnalysisParameterGroup(
                        id="id_example",
                        labels=TranslatedLabels([
                            TranslatedLabel(),
                        ]),
                        order=1,
                        is_table=True,
                        options={},
                        parent_id="parent_id_example",
                        parameters=[
                            AnalysisParameter(
                                id="id_example",
                                labels=TranslatedLabels(TranslatedLabels),
                                var_type="var_type_example",
                                order=1,
                                options={},
                            ),
                        ],
                    ),
                ],
            ),
        ],
    ) # Simulator | the Simulator to create

    # example passing only required values which don't have defaults set
    try:
        # Register a new simulator
        api_response = api_instance.create_simulator(organization_id, simulator)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulatorApi->create_simulator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **simulator** | [**Simulator**](Simulator.md)| the Simulator to create |

### Return type

[**Simulator**](Simulator.md)

### Authorization

[AADOAuth2AuthCode](../README.md#AADOAuth2AuthCode), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the simulator details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_simulator**
> Simulator delete_simulator(organization_id, simulator_id)

Delete a simulator

### Example

* OAuth Authentication (AADOAuth2AuthCode):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulator_api
from cosmotech_api.model.simulator import Simulator
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
    api_instance = simulator_api.SimulatorApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    simulator_id = "simulator_id_example" # str | the Simulator identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete a simulator
        api_response = api_instance.delete_simulator(organization_id, simulator_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulatorApi->delete_simulator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **simulator_id** | **str**| the Simulator identifier |

### Return type

[**Simulator**](Simulator.md)

### Authorization

[AADOAuth2AuthCode](../README.md#AADOAuth2AuthCode), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the simulator details |  -  |
**400** | Bad request |  -  |
**404** | the Simulator specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_simulators**
> [Simulator] find_all_simulators(organization_id)

List all Simulators

### Example

* OAuth Authentication (AADOAuth2AuthCode):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulator_api
from cosmotech_api.model.simulator import Simulator
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
    api_instance = simulator_api.SimulatorApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier

    # example passing only required values which don't have defaults set
    try:
        # List all Simulators
        api_response = api_instance.find_all_simulators(organization_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulatorApi->find_all_simulators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |

### Return type

[**[Simulator]**](Simulator.md)

### Authorization

[AADOAuth2AuthCode](../README.md#AADOAuth2AuthCode), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the simulator details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_simulator_by_id**
> Simulator find_simulator_by_id(organization_id, simulator_id)

Get the details of a simulator

### Example

* OAuth Authentication (AADOAuth2AuthCode):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulator_api
from cosmotech_api.model.simulator import Simulator
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
    api_instance = simulator_api.SimulatorApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    simulator_id = "simulator_id_example" # str | the Simulator identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a simulator
        api_response = api_instance.find_simulator_by_id(organization_id, simulator_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulatorApi->find_simulator_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **simulator_id** | **str**| the Simulator identifier |

### Return type

[**Simulator**](Simulator.md)

### Authorization

[AADOAuth2AuthCode](../README.md#AADOAuth2AuthCode), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Simulator details |  -  |
**404** | the Simulator specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_simulator**
> Simulator update_simulator(organization_id, simulator_id, simulator)

Update a simulator

### Example

* OAuth Authentication (AADOAuth2AuthCode):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import cosmotech_api
from cosmotech_api.api import simulator_api
from cosmotech_api.model.simulator import Simulator
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
    api_instance = simulator_api.SimulatorApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    simulator_id = "simulator_id_example" # str | the Simulator identifier
    simulator = Simulator(
        id="id_example",
        simulator_key="simulator_key_example",
        name="name_example",
        description="description_example",
        repository="repository_example",
        version="version_example",
        owner_id="owner_id_example",
        url="url_example",
        tags=[
            "tags_example",
        ],
        analysis=[
            SimulatorAnalysis(
                id="id_example",
                name="name_example",
                description="description_example",
                simulation="simulation_example",
                tags=[
                    "tags_example",
                ],
                compute_size="compute_size_example",
                parameters_handler_resource=AnalysisResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                dataset_validator_resource=AnalysisResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                custom_driver_resource=AnalysisResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                parameter_groups=[
                    AnalysisParameterGroup(
                        id="id_example",
                        labels=TranslatedLabels([
                            TranslatedLabel(),
                        ]),
                        order=1,
                        is_table=True,
                        options={},
                        parent_id="parent_id_example",
                        parameters=[
                            AnalysisParameter(
                                id="id_example",
                                labels=TranslatedLabels(TranslatedLabels),
                                var_type="var_type_example",
                                order=1,
                                options={},
                            ),
                        ],
                    ),
                ],
            ),
        ],
    ) # Simulator | the new Simulator details.

    # example passing only required values which don't have defaults set
    try:
        # Update a simulator
        api_response = api_instance.update_simulator(organization_id, simulator_id, simulator)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SimulatorApi->update_simulator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **simulator_id** | **str**| the Simulator identifier |
 **simulator** | [**Simulator**](Simulator.md)| the new Simulator details. |

### Return type

[**Simulator**](Simulator.md)

### Authorization

[AADOAuth2AuthCode](../README.md#AADOAuth2AuthCode), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the simulator details |  -  |
**400** | Bad request |  -  |
**404** | the Simulator specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

