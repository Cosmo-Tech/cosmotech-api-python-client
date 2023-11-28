# cosmotech_api.DatasetApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_or_replace_dataset_compatibility_elements**](DatasetApi.md#add_or_replace_dataset_compatibility_elements) | **POST** /organizations/{organization_id}/datasets/{dataset_id}/compatibility | Add Dataset Compatibility elements.
[**copy_dataset**](DatasetApi.md#copy_dataset) | **POST** /organizations/{organization_id}/datasets/copy | Copy a Dataset to another Dataset. Source must have a read capable connector and Target a write capable connector.
[**create_dataset**](DatasetApi.md#create_dataset) | **POST** /organizations/{organization_id}/datasets | Create a new Dataset
[**delete_dataset**](DatasetApi.md#delete_dataset) | **DELETE** /organizations/{organization_id}/datasets/{dataset_id} | Delete a dataset
[**find_all_datasets**](DatasetApi.md#find_all_datasets) | **GET** /organizations/{organization_id}/datasets | List all Datasets
[**find_dataset_by_id**](DatasetApi.md#find_dataset_by_id) | **GET** /organizations/{organization_id}/datasets/{dataset_id} | Get the details of a Dataset
[**import_dataset**](DatasetApi.md#import_dataset) | **POST** /organizations/{organization_id}/datasets/import | Import a new Dataset
[**remove_all_dataset_compatibility_elements**](DatasetApi.md#remove_all_dataset_compatibility_elements) | **DELETE** /organizations/{organization_id}/datasets/{dataset_id}/compatibility | Remove all Dataset Compatibility elements from the Dataset specified
[**search_datasets**](DatasetApi.md#search_datasets) | **POST** /organizations/{organization_id}/datasets/search | Search Datasets
[**update_dataset**](DatasetApi.md#update_dataset) | **PATCH** /organizations/{organization_id}/datasets/{dataset_id} | Update a dataset


# **add_or_replace_dataset_compatibility_elements**
> [DatasetCompatibility] add_or_replace_dataset_compatibility_elements(organization_id, dataset_id, dataset_compatibility)

Add Dataset Compatibility elements.

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset_compatibility import DatasetCompatibility
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
    api_instance = dataset_api.DatasetApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    dataset_id = "dataset_id_example" # str | the Dataset identifier
    dataset_compatibility = [
        DatasetCompatibility(
            solution_key="solution_key_example",
            minimum_version="minimum_version_example",
            maximum_version="maximum_version_example",
        ),
    ] # [DatasetCompatibility] | the Dataset Compatibility elements

    # example passing only required values which don't have defaults set
    try:
        # Add Dataset Compatibility elements.
        api_response = api_instance.add_or_replace_dataset_compatibility_elements(organization_id, dataset_id, dataset_compatibility)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->add_or_replace_dataset_compatibility_elements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |
 **dataset_compatibility** | [**[DatasetCompatibility]**](DatasetCompatibility.md)| the Dataset Compatibility elements |

### Return type

[**[DatasetCompatibility]**](DatasetCompatibility.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the Dataset Compatibility elements |  -  |
**400** | Bad request |  -  |
**404** | the Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_dataset**
> DatasetCopyParameters copy_dataset(organization_id, dataset_copy_parameters)

Copy a Dataset to another Dataset. Source must have a read capable connector and Target a write capable connector.

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset_copy_parameters import DatasetCopyParameters
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
    api_instance = dataset_api.DatasetApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    dataset_copy_parameters = DatasetCopyParameters(
        source_id="source_id_example",
        target_id="target_id_example",
        options={},
    ) # DatasetCopyParameters | the Dataset copy parameters

    # example passing only required values which don't have defaults set
    try:
        # Copy a Dataset to another Dataset. Source must have a read capable connector and Target a write capable connector.
        api_response = api_instance.copy_dataset(organization_id, dataset_copy_parameters)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->copy_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_copy_parameters** | [**DatasetCopyParameters**](DatasetCopyParameters.md)| the Dataset copy parameters |

### Return type

[**DatasetCopyParameters**](DatasetCopyParameters.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the Dataset copy operation parameters |  -  |
**400** | Bad request |  -  |
**404** | the Dataset specified as Source or Target is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dataset**
> Dataset create_dataset(organization_id, dataset)

Create a new Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset import Dataset
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
    api_instance = dataset_api.DatasetApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    dataset = Dataset(
        name="name_example",
        description="description_example",
        tags=[
            "tags_example",
        ],
        connector=DatasetConnector(
            id="id_example",
            name="name_example",
            version="version_example",
            parameters_values={
                "key": "key_example",
            },
        ),
        fragments_ids=[
            "fragments_ids_example",
        ],
        validator_id="validator_id_example",
        compatibility=[
            DatasetCompatibility(
                solution_key="solution_key_example",
                minimum_version="minimum_version_example",
                maximum_version="maximum_version_example",
            ),
        ],
    ) # Dataset | the Dataset to create

    # example passing only required values which don't have defaults set
    try:
        # Create a new Dataset
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

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the dataset details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset**
> delete_dataset(organization_id, dataset_id)

Delete a dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
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
    api_instance = dataset_api.DatasetApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    dataset_id = "dataset_id_example" # str | the Dataset identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete a dataset
        api_instance.delete_dataset(organization_id, dataset_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->delete_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |

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
**404** | the Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_datasets**
> [Dataset] find_all_datasets(organization_id)

List all Datasets

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset import Dataset
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
    api_instance = dataset_api.DatasetApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    page = 1 # int | page number to query (optional)
    size = 1 # int | amount of result by page (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all Datasets
        api_response = api_instance.find_all_datasets(organization_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->find_all_datasets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all Datasets
        api_response = api_instance.find_all_datasets(organization_id, page=page, size=size)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->find_all_datasets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **page** | **int**| page number to query | [optional]
 **size** | **int**| amount of result by page | [optional]

### Return type

[**[Dataset]**](Dataset.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the list of Datasets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_dataset_by_id**
> Dataset find_dataset_by_id(organization_id, dataset_id)

Get the details of a Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset import Dataset
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
    api_instance = dataset_api.DatasetApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    dataset_id = "dataset_id_example" # str | the Dataset identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a Dataset
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

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Dataset details |  -  |
**404** | the Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_dataset**
> Dataset import_dataset(organization_id, dataset)

Import a new Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset import Dataset
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
    api_instance = dataset_api.DatasetApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    dataset = Dataset(
        name="name_example",
        description="description_example",
        tags=[
            "tags_example",
        ],
        connector=DatasetConnector(
            id="id_example",
            name="name_example",
            version="version_example",
            parameters_values={
                "key": "key_example",
            },
        ),
        fragments_ids=[
            "fragments_ids_example",
        ],
        validator_id="validator_id_example",
        compatibility=[
            DatasetCompatibility(
                solution_key="solution_key_example",
                minimum_version="minimum_version_example",
                maximum_version="maximum_version_example",
            ),
        ],
    ) # Dataset | the Dataset to import

    # example passing only required values which don't have defaults set
    try:
        # Import a new Dataset
        api_response = api_instance.import_dataset(organization_id, dataset)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->import_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset** | [**Dataset**](Dataset.md)| the Dataset to import |

### Return type

[**Dataset**](Dataset.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the dataset details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_dataset_compatibility_elements**
> remove_all_dataset_compatibility_elements(organization_id, dataset_id)

Remove all Dataset Compatibility elements from the Dataset specified

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
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
    api_instance = dataset_api.DatasetApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    dataset_id = "dataset_id_example" # str | the Dataset identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove all Dataset Compatibility elements from the Dataset specified
        api_instance.remove_all_dataset_compatibility_elements(organization_id, dataset_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->remove_all_dataset_compatibility_elements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |

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
**404** | the Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_datasets**
> [Dataset] search_datasets(organization_id, dataset_search)

Search Datasets

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset import Dataset
from cosmotech_api.model.dataset_search import DatasetSearch
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
    api_instance = dataset_api.DatasetApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    dataset_search = DatasetSearch(
        dataset_tags=[
            "dataset_tags_example",
        ],
    ) # DatasetSearch | the Dataset search parameters
    page = 1 # int | page number to query (optional)
    size = 1 # int | amount of result by page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Datasets
        api_response = api_instance.search_datasets(organization_id, dataset_search)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->search_datasets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Datasets
        api_response = api_instance.search_datasets(organization_id, dataset_search, page=page, size=size)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->search_datasets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_search** | [**DatasetSearch**](DatasetSearch.md)| the Dataset search parameters |
 **page** | **int**| page number to query | [optional]
 **size** | **int**| amount of result by page | [optional]

### Return type

[**[Dataset]**](Dataset.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the list of Datasets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset**
> Dataset update_dataset(organization_id, dataset_id, dataset)

Update a dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset import Dataset
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
    api_instance = dataset_api.DatasetApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    dataset_id = "dataset_id_example" # str | the Dataset identifier
    dataset = Dataset(
        name="name_example",
        description="description_example",
        tags=[
            "tags_example",
        ],
        connector=DatasetConnector(
            id="id_example",
            name="name_example",
            version="version_example",
            parameters_values={
                "key": "key_example",
            },
        ),
        fragments_ids=[
            "fragments_ids_example",
        ],
        validator_id="validator_id_example",
        compatibility=[
            DatasetCompatibility(
                solution_key="solution_key_example",
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

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the dataset details |  -  |
**400** | Bad request |  -  |
**404** | the Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

