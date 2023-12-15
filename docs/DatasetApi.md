# cosmotech_api.DatasetApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dataset_access_control**](DatasetApi.md#add_dataset_access_control) | **POST** /organizations/{organization_id}/datasets/{dataset_id}/security/access | Add a control access to the Dataset
[**add_or_replace_dataset_compatibility_elements**](DatasetApi.md#add_or_replace_dataset_compatibility_elements) | **POST** /organizations/{organization_id}/datasets/{dataset_id}/compatibility | Add Dataset Compatibility elements.
[**copy_dataset**](DatasetApi.md#copy_dataset) | **POST** /organizations/{organization_id}/datasets/copy | Copy a Dataset to another Dataset.
[**create_dataset**](DatasetApi.md#create_dataset) | **POST** /organizations/{organization_id}/datasets | Create a new Dataset
[**create_sub_dataset**](DatasetApi.md#create_sub_dataset) | **POST** /organizations/{organization_id}/datasets/{dataset_id}/subdataset | Create a sub-dataset from the dataset in parameter
[**create_twingraph_entities**](DatasetApi.md#create_twingraph_entities) | **POST** /organizations/{organization_id}/datasets/{dataset_id}/twingraph/{type} | Create new entities in a graph instance
[**delete_dataset**](DatasetApi.md#delete_dataset) | **DELETE** /organizations/{organization_id}/datasets/{dataset_id} | Delete a dataset
[**delete_twingraph_entities**](DatasetApi.md#delete_twingraph_entities) | **DELETE** /organizations/{organization_id}/datasets/{dataset_id}/twingraph/{type} | Delete entities in a graph instance
[**download_twingraph**](DatasetApi.md#download_twingraph) | **GET** /organizations/{organization_id}/datasets/twingraph/download/{hash} | Download a graph as a zip file
[**find_all_datasets**](DatasetApi.md#find_all_datasets) | **GET** /organizations/{organization_id}/datasets | List all Datasets
[**find_dataset_by_id**](DatasetApi.md#find_dataset_by_id) | **GET** /organizations/{organization_id}/datasets/{dataset_id} | Get the details of a Dataset
[**get_dataset_access_control**](DatasetApi.md#get_dataset_access_control) | **GET** /organizations/{organization_id}/datasets/{dataset_id}/security/access/{identity_id} | Get a control access for the Dataset
[**get_dataset_security**](DatasetApi.md#get_dataset_security) | **GET** /organizations/{organization_id}/datasets/{dataset_id}/security | Get the Dataset security information
[**get_dataset_security_users**](DatasetApi.md#get_dataset_security_users) | **GET** /organizations/{organization_id}/datasets/{dataset_id}/security/users | Get the Dataset security users list
[**get_dataset_twingraph_status**](DatasetApi.md#get_dataset_twingraph_status) | **GET** /organizations/{organization_id}/datasets/{dataset_id}/status | Get the dataset&#39;s refresh job status
[**get_twingraph_entities**](DatasetApi.md#get_twingraph_entities) | **GET** /organizations/{organization_id}/datasets/{dataset_id}/twingraph/{type} | Get entities in a graph instance
[**refresh_dataset**](DatasetApi.md#refresh_dataset) | **POST** /organizations/{organization_id}/datasets/{dataset_id}/refresh | Refresh data on dataset from dataset&#39;s source
[**remove_all_dataset_compatibility_elements**](DatasetApi.md#remove_all_dataset_compatibility_elements) | **DELETE** /organizations/{organization_id}/datasets/{dataset_id}/compatibility | Remove all Dataset Compatibility elements from the Dataset specified
[**remove_dataset_access_control**](DatasetApi.md#remove_dataset_access_control) | **DELETE** /organizations/{organization_id}/datasets/{dataset_id}/security/access/{identity_id} | Remove the specified access from the given Dataset
[**rollback_refresh**](DatasetApi.md#rollback_refresh) | **POST** /organizations/{organization_id}/datasets/{dataset_id}/refresh/rollback | Rollback the dataset after a failed refresh
[**search_datasets**](DatasetApi.md#search_datasets) | **POST** /organizations/{organization_id}/datasets/search | Search Datasets by tags
[**set_dataset_default_security**](DatasetApi.md#set_dataset_default_security) | **POST** /organizations/{organization_id}/datasets/{dataset_id}/security/default | Set the Dataset default security
[**twingraph_batch_query**](DatasetApi.md#twingraph_batch_query) | **POST** /organizations/{organization_id}/datasets/{dataset_id}/batch-query | Run a query on a graph instance and return the result as a zip file in async mode
[**twingraph_batch_update**](DatasetApi.md#twingraph_batch_update) | **POST** /organizations/{organization_id}/datasets/{dataset_id}/batch | Async batch update by loading a CSV file on a graph instance 
[**twingraph_query**](DatasetApi.md#twingraph_query) | **POST** /organizations/{organization_id}/datasets/{dataset_id}/twingraph | Return the result of a query made on the graph instance as a json
[**update_dataset**](DatasetApi.md#update_dataset) | **PATCH** /organizations/{organization_id}/datasets/{dataset_id} | Update a dataset
[**update_dataset_access_control**](DatasetApi.md#update_dataset_access_control) | **PATCH** /organizations/{organization_id}/datasets/{dataset_id}/security/access/{identity_id} | Update the specified access to User for a Dataset
[**update_twingraph_entities**](DatasetApi.md#update_twingraph_entities) | **PATCH** /organizations/{organization_id}/datasets/{dataset_id}/twingraph/{type} | Update entities in a graph instance
[**upload_twingraph**](DatasetApi.md#upload_twingraph) | **POST** /organizations/{organization_id}/datasets/{dataset_id} | Upload data from zip file to dataset&#39;s twingraph


# **add_dataset_access_control**
> DatasetAccessControl add_dataset_access_control(organization_id, dataset_id, dataset_access_control)

Add a control access to the Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset_access_control import DatasetAccessControl
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
    dataset_access_control = DatasetAccessControl(
        id="id_example",
        role="role_example",
    ) # DatasetAccessControl | the new Dataset security access to add.

    # example passing only required values which don't have defaults set
    try:
        # Add a control access to the Dataset
        api_response = api_instance.add_dataset_access_control(organization_id, dataset_id, dataset_access_control)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->add_dataset_access_control: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |
 **dataset_access_control** | [**DatasetAccessControl**](DatasetAccessControl.md)| the new Dataset security access to add. |

### Return type

[**DatasetAccessControl**](DatasetAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Dataset access |  -  |
**404** | the Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

Copy a Dataset to another Dataset.

Not implemented!

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
        # Copy a Dataset to another Dataset.
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
        parent_id="parent_id_example",
        twingraph_id="twingraph_id_example",
        main=True,
        source_type=DatasetSourceType("ADT"),
        source=SourceInfo(
            name="name_example",
            location="location_example",
            path="path_example",
            job_id="job_id_example",
        ),
        ingestion_status="NONE",
        twincache_status="EMPTY",
        queries=[
            "queries_example",
        ],
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
        security=None,
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

# **create_sub_dataset**
> Dataset create_sub_dataset(organization_id, dataset_id, sub_dataset_graph_query)

Create a sub-dataset from the dataset in parameter

Create a copy of the dataset using the results of the list of queries given in parameter.

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.sub_dataset_graph_query import SubDatasetGraphQuery
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
    sub_dataset_graph_query = SubDatasetGraphQuery(
        name="name_example",
        description="description_example",
        queries=[
            "queries_example",
        ],
        main=True,
    ) # SubDatasetGraphQuery | the Cypher query to filter

    # example passing only required values which don't have defaults set
    try:
        # Create a sub-dataset from the dataset in parameter
        api_response = api_instance.create_sub_dataset(organization_id, dataset_id, sub_dataset_graph_query)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->create_sub_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |
 **sub_dataset_graph_query** | [**SubDatasetGraphQuery**](SubDatasetGraphQuery.md)| the Cypher query to filter |

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_twingraph_entities**
> str create_twingraph_entities(organization_id, dataset_id, type, graph_properties)

Create new entities in a graph instance

create new entities in a graph instance

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.graph_properties import GraphProperties
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
    dataset_id = "dataset_id_example" # str | the Dataset Identifier
    type = "node" # str | the entity model type
    graph_properties = [
        GraphProperties(
            type="type_example",
            source="source_example",
            target="target_example",
            name="name_example",
            params="params_example",
        ),
    ] # [GraphProperties] | the entities to create

    # example passing only required values which don't have defaults set
    try:
        # Create new entities in a graph instance
        api_response = api_instance.create_twingraph_entities(organization_id, dataset_id, type, graph_properties)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->create_twingraph_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset Identifier |
 **type** | **str**| the entity model type |
 **graph_properties** | [**[GraphProperties]**](GraphProperties.md)| the entities to create |

### Return type

**str**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

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

# **delete_twingraph_entities**
> delete_twingraph_entities(organization_id, dataset_id, type, ids)

Delete entities in a graph instance

delete entities in a graph instance

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
    dataset_id = "dataset_id_example" # str | the Dataset Identifier
    type = "node" # str | the entity model type
    ids = [
        "ids_example",
    ] # [str] | the entities to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete entities in a graph instance
        api_instance.delete_twingraph_entities(organization_id, dataset_id, type, ids)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->delete_twingraph_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset Identifier |
 **type** | **str**| the entity model type |
 **ids** | **[str]**| the entities to delete |

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_twingraph**
> file_type download_twingraph(organization_id, hash)

Download a graph as a zip file

Download the compressed graph reference by the hash in a zip file

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
    hash = "hash_example" # str | the Graph download identifier

    # example passing only required values which don't have defaults set
    try:
        # Download a graph as a zip file
        api_response = api_instance.download_twingraph(organization_id, hash)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->download_twingraph: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **hash** | **str**| the Graph download identifier |

### Return type

**file_type**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

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

# **get_dataset_access_control**
> DatasetAccessControl get_dataset_access_control(organization_id, dataset_id, identity_id)

Get a control access for the Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset_access_control import DatasetAccessControl
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
    identity_id = "identity_id_example" # str | the User identifier

    # example passing only required values which don't have defaults set
    try:
        # Get a control access for the Dataset
        api_response = api_instance.get_dataset_access_control(organization_id, dataset_id, identity_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->get_dataset_access_control: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |
 **identity_id** | **str**| the User identifier |

### Return type

[**DatasetAccessControl**](DatasetAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Dataset access |  -  |
**404** | The Dataset or user specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_security**
> DatasetSecurity get_dataset_security(organization_id, dataset_id)

Get the Dataset security information

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset_security import DatasetSecurity
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
        # Get the Dataset security information
        api_response = api_instance.get_dataset_security(organization_id, dataset_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->get_dataset_security: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |

### Return type

[**DatasetSecurity**](DatasetSecurity.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Dataset security |  -  |
**404** | the Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_security_users**
> [str] get_dataset_security_users(organization_id, dataset_id)

Get the Dataset security users list

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
        # Get the Dataset security users list
        api_response = api_instance.get_dataset_security_users(organization_id, dataset_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->get_dataset_security_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |

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
**200** | The Dataset security users list |  -  |
**404** | the Dataset or the User specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_twingraph_status**
> str get_dataset_twingraph_status(organization_id, dataset_id)

Get the dataset's refresh job status

Get the status of the import workflow lauch on the dataset's refresh. This endpoint needs to be called to update a dataset IngestionStatus or TwincacheStatus

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
    dataset_id = "dataset_id_example" # str | the dataset identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the dataset's refresh job status
        api_response = api_instance.get_dataset_twingraph_status(organization_id, dataset_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->get_dataset_twingraph_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the dataset identifier |

### Return type

**str**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yaml, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_twingraph_entities**
> str get_twingraph_entities(organization_id, dataset_id, type, ids)

Get entities in a graph instance

get entities in a graph instance

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
    dataset_id = "dataset_id_example" # str | the Dataset Identifier
    type = "node" # str | the entity model type
    ids = [
        "ids_example",
    ] # [str] | the entities to get

    # example passing only required values which don't have defaults set
    try:
        # Get entities in a graph instance
        api_response = api_instance.get_twingraph_entities(organization_id, dataset_id, type, ids)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->get_twingraph_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset Identifier |
 **type** | **str**| the entity model type |
 **ids** | **[str]**| the entities to get |

### Return type

**str**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_dataset**
> DatasetTwinGraphInfo refresh_dataset(organization_id, dataset_id)

Refresh data on dataset from dataset's source

Refresh dataset from parent source. At date, sources can be:      dataset (refresh from another dataset)      Azure Digital twin       Azure storage      Local File (import a new file)  During refresh, datas are overwritten 

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset_twin_graph_info import DatasetTwinGraphInfo
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
        # Refresh data on dataset from dataset's source
        api_response = api_instance.refresh_dataset(organization_id, dataset_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->refresh_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |

### Return type

[**DatasetTwinGraphInfo**](DatasetTwinGraphInfo.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

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

# **remove_dataset_access_control**
> remove_dataset_access_control(organization_id, dataset_id, identity_id)

Remove the specified access from the given Dataset

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
    identity_id = "identity_id_example" # str | the User identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove the specified access from the given Dataset
        api_instance.remove_dataset_access_control(organization_id, dataset_id, identity_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->remove_dataset_access_control: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |
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
**404** | The Dataset or the user specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_refresh**
> str rollback_refresh(organization_id, dataset_id)

Rollback the dataset after a failed refresh

Rollback the twingraph on a dataset after a failed refresh

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
        # Rollback the dataset after a failed refresh
        api_response = api_instance.rollback_refresh(organization_id, dataset_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->rollback_refresh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |

### Return type

**str**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_datasets**
> [Dataset] search_datasets(organization_id, dataset_search)

Search Datasets by tags

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
        # Search Datasets by tags
        api_response = api_instance.search_datasets(organization_id, dataset_search)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->search_datasets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Datasets by tags
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

# **set_dataset_default_security**
> DatasetSecurity set_dataset_default_security(organization_id, dataset_id, dataset_role)

Set the Dataset default security

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset_role import DatasetRole
from cosmotech_api.model.dataset_security import DatasetSecurity
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
    dataset_role = DatasetRole(
        role="role_example",
    ) # DatasetRole | This change the dataset default security. The default security is the role assigned to any person not on the Access Control List. If the default security is None, then nobody outside of the ACL can access the dataset.

    # example passing only required values which don't have defaults set
    try:
        # Set the Dataset default security
        api_response = api_instance.set_dataset_default_security(organization_id, dataset_id, dataset_role)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->set_dataset_default_security: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |
 **dataset_role** | [**DatasetRole**](DatasetRole.md)| This change the dataset default security. The default security is the role assigned to any person not on the Access Control List. If the default security is None, then nobody outside of the ACL can access the dataset. |

### Return type

[**DatasetSecurity**](DatasetSecurity.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Dataset default visibility |  -  |
**404** | the Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **twingraph_batch_query**
> DatasetTwinGraphHash twingraph_batch_query(organization_id, dataset_id, dataset_twin_graph_query)

Run a query on a graph instance and return the result as a zip file in async mode

Run a query on a graph instance and return the result as a zip file in async mode

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset_twin_graph_hash import DatasetTwinGraphHash
from cosmotech_api.model.dataset_twin_graph_query import DatasetTwinGraphQuery
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
    dataset_id = "dataset_id_example" # str | the Graph Identifier
    dataset_twin_graph_query = DatasetTwinGraphQuery(
        query="query_example",
    ) # DatasetTwinGraphQuery | the query to run

    # example passing only required values which don't have defaults set
    try:
        # Run a query on a graph instance and return the result as a zip file in async mode
        api_response = api_instance.twingraph_batch_query(organization_id, dataset_id, dataset_twin_graph_query)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->twingraph_batch_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Graph Identifier |
 **dataset_twin_graph_query** | [**DatasetTwinGraphQuery**](DatasetTwinGraphQuery.md)| the query to run |

### Return type

[**DatasetTwinGraphHash**](DatasetTwinGraphHash.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **twingraph_batch_update**
> TwinGraphBatchResult twingraph_batch_update(organization_id, dataset_id, twin_graph_query, body)

Async batch update by loading a CSV file on a graph instance 

Async batch update by loading a CSV file on a graph instance 

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset_twin_graph_query import DatasetTwinGraphQuery
from cosmotech_api.model.twin_graph_batch_result import TwinGraphBatchResult
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
    dataset_id = "dataset_id_example" # str | the Dataset Identifier
    twin_graph_query = DatasetTwinGraphQuery(
        query="query_example",
    ) # DatasetTwinGraphQuery | 
    body = open('id,name,rank
1,"John Doe",37
2,"Joe Bloggs",14
', 'rb') # file_type | 

    # example passing only required values which don't have defaults set
    try:
        # Async batch update by loading a CSV file on a graph instance 
        api_response = api_instance.twingraph_batch_update(organization_id, dataset_id, twin_graph_query, body)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->twingraph_batch_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset Identifier |
 **twin_graph_query** | **DatasetTwinGraphQuery**|  |
 **body** | **file_type**|  |

### Return type

[**TwinGraphBatchResult**](TwinGraphBatchResult.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: text/csv, application/octet-stream
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | csv file processed |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **twingraph_query**
> str twingraph_query(organization_id, dataset_id, dataset_twin_graph_query)

Return the result of a query made on the graph instance as a json

Run a query on a graph instance and return the result as a json

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset_twin_graph_query import DatasetTwinGraphQuery
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
    dataset_twin_graph_query = DatasetTwinGraphQuery(
        query="query_example",
    ) # DatasetTwinGraphQuery | the query to run

    # example passing only required values which don't have defaults set
    try:
        # Return the result of a query made on the graph instance as a json
        api_response = api_instance.twingraph_query(organization_id, dataset_id, dataset_twin_graph_query)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->twingraph_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |
 **dataset_twin_graph_query** | [**DatasetTwinGraphQuery**](DatasetTwinGraphQuery.md)| the query to run |

### Return type

**str**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

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
        parent_id="parent_id_example",
        twingraph_id="twingraph_id_example",
        main=True,
        source_type=DatasetSourceType("ADT"),
        source=SourceInfo(
            name="name_example",
            location="location_example",
            path="path_example",
            job_id="job_id_example",
        ),
        ingestion_status="NONE",
        twincache_status="EMPTY",
        queries=[
            "queries_example",
        ],
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
        security=None,
    ) # Dataset | the new Dataset details. This endpoint can't be used to update security

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
 **dataset** | [**Dataset**](Dataset.md)| the new Dataset details. This endpoint can&#39;t be used to update security |

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

# **update_dataset_access_control**
> DatasetAccessControl update_dataset_access_control(organization_id, dataset_id, identity_id, dataset_role)

Update the specified access to User for a Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.dataset_role import DatasetRole
from cosmotech_api.model.dataset_access_control import DatasetAccessControl
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
    identity_id = "identity_id_example" # str | the User identifier
    dataset_role = DatasetRole(
        role="role_example",
    ) # DatasetRole | The new Dataset Access Control

    # example passing only required values which don't have defaults set
    try:
        # Update the specified access to User for a Dataset
        api_response = api_instance.update_dataset_access_control(organization_id, dataset_id, identity_id, dataset_role)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->update_dataset_access_control: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |
 **identity_id** | **str**| the User identifier |
 **dataset_role** | [**DatasetRole**](DatasetRole.md)| The new Dataset Access Control |

### Return type

[**DatasetAccessControl**](DatasetAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Dataset access |  -  |
**404** | The Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_twingraph_entities**
> str update_twingraph_entities(organization_id, dataset_id, type, graph_properties)

Update entities in a graph instance

update entities in a graph instance

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.graph_properties import GraphProperties
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
    dataset_id = "dataset_id_example" # str | the Dataset Identifier
    type = "node" # str | the entity model type
    graph_properties = [
        GraphProperties(
            type="type_example",
            source="source_example",
            target="target_example",
            name="name_example",
            params="params_example",
        ),
    ] # [GraphProperties] | the entities to update

    # example passing only required values which don't have defaults set
    try:
        # Update entities in a graph instance
        api_response = api_instance.update_twingraph_entities(organization_id, dataset_id, type, graph_properties)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->update_twingraph_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset Identifier |
 **type** | **str**| the entity model type |
 **graph_properties** | [**[GraphProperties]**](GraphProperties.md)| the entities to update |

### Return type

**str**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_twingraph**
> FileUploadValidation upload_twingraph(organization_id, dataset_id, body)

Upload data from zip file to dataset's twingraph

To create a new graph from flat files,  you need to create a Zip file. This Zip file must countain two folders named Edges and Nodes.  .zip hierarchy: *main_folder/Nodes *main_folder/Edges  In each folder you can place one or multiple csv files containing your Nodes or Edges data.  Your csv files must follow the following header (column name) requirements:  The Nodes CSVs requires at least one column (the 1st).Column name = 'id'. It will represent the nodes ID Ids must be populated with string  The Edges CSVs require three columns named, in order, * source * target * id  those colomns represent * The source of the edge * The target of the edge * The id of the edge  All following columns content are up to you. 

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import dataset_api
from cosmotech_api.model.file_upload_validation import FileUploadValidation
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
    body = open('/path/to/file', 'rb') # file_type | 

    # example passing only required values which don't have defaults set
    try:
        # Upload data from zip file to dataset's twingraph
        api_response = api_instance.upload_twingraph(organization_id, dataset_id, body)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling DatasetApi->upload_twingraph: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **dataset_id** | **str**| the Dataset identifier |
 **body** | **file_type**|  |

### Return type

[**FileUploadValidation**](FileUploadValidation.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | File uploaded successfully. Processing... |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

