# cosmotech_api.DatasetApi

All URIs are relative to *https://api.azure.cosmo-platform.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset**](DatasetApi.md#create_dataset) | **POST** /organizations/{organization_id}/datasets | Register a new dataset
[**delete_dataset**](DatasetApi.md#delete_dataset) | **DELETE** /organizations/{organization_id}/datasets/{dataset_id} | Delete a dataset
[**find_all_datasets**](DatasetApi.md#find_all_datasets) | **GET** /organizations/{organization_id}/datasets | List all Datasets
[**find_dataset_by_id**](DatasetApi.md#find_dataset_by_id) | **GET** /organizations/{organization_id}/datasets/{dataset_id} | Get the details of a dataset
[**update_dataset**](DatasetApi.md#update_dataset) | **PATCH** /organizations/{organization_id}/datasets/{dataset_id} | Update a dataset


# **create_dataset**
> Dataset create_dataset(organization_id, dataset)

Register a new dataset

### Example

* OAuth Authentication (AADOAuth2AuthCode):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset import Dataset
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
    api_instance = dataset_api.DatasetApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    dataset = Dataset(
        id="id_example",
        name="name_example",
        description="description_example",
        owner_id="owner_id_example",
        tags=[
            "tags_example",
        ],
        connector=DatasetConnector(
            id="id_example",
            parameters_values={},
        ),
        fragments_ids=[
            "fragments_ids_example",
        ],
        validator_id="validator_id_example",
        compatibility=[
            DatasetCompatibility(
                simulator_key="simulator_key_example",
                minimum_version="minimum_version_example",
                maximum_version="maximum_version_example",
            ),
        ],
    ) # Dataset | the Dataset to create

    # example passing only required values which don't have defaults set
    try:
        # Register a new dataset
        api_response = api_instance.create_dataset(organization_id, dataset)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->create_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset** | [**Dataset**](Dataset.md)| the Dataset to create |

### Return type

[**Dataset**](Dataset.md)

### Authorization

[AADOAuth2AuthCode](../README.md#AADOAuth2AuthCode), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the dataset details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset**
> Dataset delete_dataset(organization_id, dataset_id)

Delete a dataset

### Example

* OAuth Authentication (AADOAuth2AuthCode):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset import Dataset
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
    api_instance = dataset_api.DatasetApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    dataset_id = "dataset_id_example" # str | the Dataset identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete a dataset
        api_response = api_instance.delete_dataset(organization_id, dataset_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->delete_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |

### Return type

[**Dataset**](Dataset.md)

### Authorization

[AADOAuth2AuthCode](../README.md#AADOAuth2AuthCode), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the dataset details |  -  |
**400** | Bad request |  -  |
**404** | the Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_datasets**
> [Dataset] find_all_datasets(organization_id)

List all Datasets

### Example

* OAuth Authentication (AADOAuth2AuthCode):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset import Dataset
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
    api_instance = dataset_api.DatasetApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier

    # example passing only required values which don't have defaults set
    try:
        # List all Datasets
        api_response = api_instance.find_all_datasets(organization_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->find_all_datasets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |

### Return type

[**[Dataset]**](Dataset.md)

### Authorization

[AADOAuth2AuthCode](../README.md#AADOAuth2AuthCode), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the dataset details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_dataset_by_id**
> Dataset find_dataset_by_id(organization_id, dataset_id)

Get the details of a dataset

### Example

* OAuth Authentication (AADOAuth2AuthCode):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset import Dataset
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
    api_instance = dataset_api.DatasetApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    dataset_id = "dataset_id_example" # str | the Dataset identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a dataset
        api_response = api_instance.find_dataset_by_id(organization_id, dataset_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->find_dataset_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |

### Return type

[**Dataset**](Dataset.md)

### Authorization

[AADOAuth2AuthCode](../README.md#AADOAuth2AuthCode), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Dataset details |  -  |
**404** | the Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset**
> Dataset update_dataset(organization_id, dataset_id, dataset)

Update a dataset

### Example

* OAuth Authentication (AADOAuth2AuthCode):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset import Dataset
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
    api_instance = dataset_api.DatasetApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    dataset_id = "dataset_id_example" # str | the Dataset identifier
    dataset = Dataset(
        id="id_example",
        name="name_example",
        description="description_example",
        owner_id="owner_id_example",
        tags=[
            "tags_example",
        ],
        connector=DatasetConnector(
            id="id_example",
            parameters_values={},
        ),
        fragments_ids=[
            "fragments_ids_example",
        ],
        validator_id="validator_id_example",
        compatibility=[
            DatasetCompatibility(
                simulator_key="simulator_key_example",
                minimum_version="minimum_version_example",
                maximum_version="maximum_version_example",
            ),
        ],
    ) # Dataset | the new Dataset details.

    # example passing only required values which don't have defaults set
    try:
        # Update a dataset
        api_response = api_instance.update_dataset(organization_id, dataset_id, dataset)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->update_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |
 **dataset** | [**Dataset**](Dataset.md)| the new Dataset details. |

### Return type

[**Dataset**](Dataset.md)

### Authorization

[AADOAuth2AuthCode](../README.md#AADOAuth2AuthCode), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the dataset details |  -  |
**400** | Bad request |  -  |
**404** | the Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
