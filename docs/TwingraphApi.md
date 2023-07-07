# cosmotech_api.TwingraphApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_query**](TwingraphApi.md#batch_query) | **POST** /organizations/{organization_id}/twingraph/{graph_id}/batch-query | Run a query on a graph instance and return the result as a zip file in async mode
[**batch_upload_update**](TwingraphApi.md#batch_upload_update) | **POST** /organizations/{organization_id}/twingraph/{graph_id}/batch | Async batch update by loading a CSV file on a graph instance 
[**create_entities**](TwingraphApi.md#create_entities) | **POST** /organizations/{organization_id}/twingraph/{graph_id}/entity/{type} | Create new entities in a graph instance
[**create_graph**](TwingraphApi.md#create_graph) | **POST** /organizations/{organization_id}/twingraph/{graph_id} | Create a new graph
[**delete**](TwingraphApi.md#delete) | **DELETE** /organizations/{organization_id}/twingraph/{graph_id} | Delete all versions of a graph and his metadatas
[**delete_entities**](TwingraphApi.md#delete_entities) | **DELETE** /organizations/{organization_id}/twingraph/{graph_id}/entity/{type} | Delete entities in a graph instance
[**download_graph**](TwingraphApi.md#download_graph) | **GET** /organizations/{organization_id}/twingraph/download/{hash} | Download a graph compressed in a zip file
[**find_all_twingraphs**](TwingraphApi.md#find_all_twingraphs) | **GET** /organizations/{organization_id}/twingraphs | Return the list of all graphs stored in the organization
[**get_entities**](TwingraphApi.md#get_entities) | **GET** /organizations/{organization_id}/twingraph/{graph_id}/entity/{type} | Get entities in a graph instance
[**get_graph_meta_data**](TwingraphApi.md#get_graph_meta_data) | **GET** /organizations/{organization_id}/twingraph/{graph_id}/metadata | Return the metaData of the specified graph
[**import_graph**](TwingraphApi.md#import_graph) | **POST** /organizations/{organization_id}/twingraph/import | Import a new version of a twin graph
[**job_status**](TwingraphApi.md#job_status) | **GET** /organizations/{organization_id}/job/{job_id}/status | Get the status of a job
[**query**](TwingraphApi.md#query) | **POST** /organizations/{organization_id}/twingraph/{graph_id}/query | Run a query on a graph instance
[**update_entities**](TwingraphApi.md#update_entities) | **PATCH** /organizations/{organization_id}/twingraph/{graph_id}/entity/{type} | Update entities in a graph instance
[**update_graph_meta_data**](TwingraphApi.md#update_graph_meta_data) | **PATCH** /organizations/{organization_id}/twingraph/{graph_id}/metadata | Update the metaData of the specified graph


# **batch_query**
> TwinGraphHash batch_query(organization_id, graph_id, twin_graph_query)

Run a query on a graph instance and return the result as a zip file in async mode

Run a query on a graph instance and return the result as a zip file in async mode

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import twingraph_api
from cosmotech_api.model.twin_graph_hash import TwinGraphHash
from cosmotech_api.model.twin_graph_query import TwinGraphQuery
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
    api_instance = twingraph_api.TwingraphApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    graph_id = "graph_id_example" # str | the Graph Identifier
    twin_graph_query = TwinGraphQuery(
        version="version_example",
        query="query_example",
    ) # TwinGraphQuery | the query to run

    # example passing only required values which don't have defaults set
    try:
        # Run a query on a graph instance and return the result as a zip file in async mode
        api_response = api_instance.batch_query(organization_id, graph_id, twin_graph_query)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->batch_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **graph_id** | **str**| the Graph Identifier |
 **twin_graph_query** | [**TwinGraphQuery**](TwinGraphQuery.md)| the query to run |

### Return type

[**TwinGraphHash**](TwinGraphHash.md)

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

# **batch_upload_update**
> TwinGraphBatchResult batch_upload_update(organization_id, graph_id, twin_graph_query, body)

Async batch update by loading a CSV file on a graph instance 

Async batch update by loading a CSV file on a graph instance 

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import twingraph_api
from cosmotech_api.model.twin_graph_query import TwinGraphQuery
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
    api_instance = twingraph_api.TwingraphApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    graph_id = "graph_id_example" # str | the Graph Identifier
    twin_graph_query = TwinGraphQuery(
        version="version_example",
        query="query_example",
    ) # TwinGraphQuery | 
    body = open('id,name,rank
1,"John Doe",37
2,"Joe Bloggs",14
', 'rb') # file_type | 

    # example passing only required values which don't have defaults set
    try:
        # Async batch update by loading a CSV file on a graph instance 
        api_response = api_instance.batch_upload_update(organization_id, graph_id, twin_graph_query, body)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->batch_upload_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **graph_id** | **str**| the Graph Identifier |
 **twin_graph_query** | **TwinGraphQuery**|  |
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

# **create_entities**
> str create_entities(organization_id, graph_id, type, graph_properties)

Create new entities in a graph instance

create new entities in a graph instance

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import twingraph_api
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
    api_instance = twingraph_api.TwingraphApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    graph_id = "graph_id_example" # str | the Graph Identifier
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
        api_response = api_instance.create_entities(organization_id, graph_id, type, graph_properties)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->create_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **graph_id** | **str**| the Graph Identifier |
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

# **create_graph**
> create_graph(organization_id, graph_id)

Create a new graph

To create a new graph from flat files,  you need to create a Zip file. This Zip file must countain two folders named Edges and Nodes.  .zip hierarchy: *main_folder/Nodes *main_folder/Edges  In each folder you can place one or multiple csv files containing your Nodes or Edges data.  Your csv files must follow the following header (column name) requirements:  The Nodes CSVs requires at least one column (the 1st).Column name = 'Id'. It will represent the nodes ID Ids must be populated with string  The Edges CSVs require three columns named, in order, * source * target * Id  those colomns represent * The source of the edge * The target of the edge * The Id of the edge  All following columns content are up to you. 

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import twingraph_api
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
    api_instance = twingraph_api.TwingraphApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    graph_id = "graph_id_example" # str | the Graph Identifier
    body = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new graph
        api_instance.create_graph(organization_id, graph_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->create_graph: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new graph
        api_instance.create_graph(organization_id, graph_id, body=body)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->create_graph: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **graph_id** | **str**| the Graph Identifier |
 **body** | **file_type**|  | [optional]

### Return type

void (empty response body)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(organization_id, graph_id)

Delete all versions of a graph and his metadatas

Delete all versions of a graph and his metadatas

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import twingraph_api
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
    api_instance = twingraph_api.TwingraphApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    graph_id = "graph_id_example" # str | the Graph Identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete all versions of a graph and his metadatas
        api_instance.delete(organization_id, graph_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **graph_id** | **str**| the Graph Identifier |

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
**204** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entities**
> delete_entities(organization_id, graph_id, type, ids)

Delete entities in a graph instance

delete entities in a graph instance

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import twingraph_api
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
    api_instance = twingraph_api.TwingraphApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    graph_id = "graph_id_example" # str | the Graph Identifier
    type = "node" # str | the entity model type
    ids = [
        "ids_example",
    ] # [str] | the entities to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete entities in a graph instance
        api_instance.delete_entities(organization_id, graph_id, type, ids)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->delete_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **graph_id** | **str**| the Graph Identifier |
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

# **download_graph**
> file_type download_graph(organization_id, hash)

Download a graph compressed in a zip file

Download a graph compressed in a zip file

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import twingraph_api
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
    api_instance = twingraph_api.TwingraphApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    hash = "hash_example" # str | the Graph download identifier

    # example passing only required values which don't have defaults set
    try:
        # Download a graph compressed in a zip file
        api_response = api_instance.download_graph(organization_id, hash)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->download_graph: %s\n" % e)
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

# **find_all_twingraphs**
> [str] find_all_twingraphs(organization_id)

Return the list of all graphs stored in the organization

Return the list of all graphs stored in the organization

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import twingraph_api
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
    api_instance = twingraph_api.TwingraphApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier

    # example passing only required values which don't have defaults set
    try:
        # Return the list of all graphs stored in the organization
        api_response = api_instance.find_all_twingraphs(organization_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->find_all_twingraphs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entities**
> str get_entities(organization_id, graph_id, type, ids)

Get entities in a graph instance

get entities in a graph instance

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import twingraph_api
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
    api_instance = twingraph_api.TwingraphApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    graph_id = "graph_id_example" # str | the Graph Identifier
    type = "node" # str | the entity model type
    ids = [
        "ids_example",
    ] # [str] | the entities to get

    # example passing only required values which don't have defaults set
    try:
        # Get entities in a graph instance
        api_response = api_instance.get_entities(organization_id, graph_id, type, ids)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->get_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **graph_id** | **str**| the Graph Identifier |
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

# **get_graph_meta_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_graph_meta_data(organization_id, graph_id)

Return the metaData of the specified graph

Return the metaData of the specified graph

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import twingraph_api
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
    api_instance = twingraph_api.TwingraphApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    graph_id = "graph_id_example" # str | the Graph Identifier

    # example passing only required values which don't have defaults set
    try:
        # Return the metaData of the specified graph
        api_response = api_instance.get_graph_meta_data(organization_id, graph_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->get_graph_meta_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **graph_id** | **str**| the Graph Identifier |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **import_graph**
> TwinGraphImportInfo import_graph(organization_id, twin_graph_import)

Import a new version of a twin graph

Import a new version of a twin graph

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import twingraph_api
from cosmotech_api.model.twin_graph_import import TwinGraphImport
from cosmotech_api.model.twin_graph_import_info import TwinGraphImportInfo
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
    api_instance = twingraph_api.TwingraphApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    twin_graph_import = TwinGraphImport(
        source=SourceInfo(
            name="name_example",
            location="location_example",
            path="path_example",
            type="ADT",
        ),
        graph_id="graph_id_example",
        version="version_example",
    ) # TwinGraphImport | the graph to import

    # example passing only required values which don't have defaults set
    try:
        # Import a new version of a twin graph
        api_response = api_instance.import_graph(organization_id, twin_graph_import)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->import_graph: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **twin_graph_import** | [**TwinGraphImport**](TwinGraphImport.md)| the graph to import |

### Return type

[**TwinGraphImportInfo**](TwinGraphImportInfo.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_status**
> str job_status(organization_id, job_id)

Get the status of a job

Get the status of a job

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import twingraph_api
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
    api_instance = twingraph_api.TwingraphApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    job_id = "job_id_example" # str | the job identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the status of a job
        api_response = api_instance.job_status(organization_id, job_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->job_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **job_id** | **str**| the job identifier |

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

# **query**
> str query(organization_id, graph_id, twin_graph_query)

Run a query on a graph instance

Run a query on a graph instance

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import twingraph_api
from cosmotech_api.model.twin_graph_query import TwinGraphQuery
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
    api_instance = twingraph_api.TwingraphApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    graph_id = "graph_id_example" # str | the Graph Identifier
    twin_graph_query = TwinGraphQuery(
        version="version_example",
        query="query_example",
    ) # TwinGraphQuery | the query to run

    # example passing only required values which don't have defaults set
    try:
        # Run a query on a graph instance
        api_response = api_instance.query(organization_id, graph_id, twin_graph_query)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **graph_id** | **str**| the Graph Identifier |
 **twin_graph_query** | [**TwinGraphQuery**](TwinGraphQuery.md)| the query to run |

### Return type

**str**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entities**
> str update_entities(organization_id, graph_id, type, graph_properties)

Update entities in a graph instance

update entities in a graph instance

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import twingraph_api
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
    api_instance = twingraph_api.TwingraphApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    graph_id = "graph_id_example" # str | the Graph Identifier
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
        api_response = api_instance.update_entities(organization_id, graph_id, type, graph_properties)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->update_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **graph_id** | **str**| the Graph Identifier |
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

# **update_graph_meta_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_graph_meta_data(organization_id, graph_id, request_body)

Update the metaData of the specified graph

Update the metaData of the specified graph

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import twingraph_api
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
    api_instance = twingraph_api.TwingraphApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    graph_id = "graph_id_example" # str | the Graph Identifier
    request_body = {
        "key": "key_example",
    } # {str: (str,)} | the metaData to update

    # example passing only required values which don't have defaults set
    try:
        # Update the metaData of the specified graph
        api_response = api_instance.update_graph_meta_data(organization_id, graph_id, request_body)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling TwingraphApi->update_graph_meta_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **graph_id** | **str**| the Graph Identifier |
 **request_body** | **{str: (str,)}**| the metaData to update |

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

