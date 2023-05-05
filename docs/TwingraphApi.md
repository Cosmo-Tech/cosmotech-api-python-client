# cosmotech_api.TwingraphApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](TwingraphApi.md#delete) | **DELETE** /organizations/{organization_id}/twingraph/{graph_id} | 
[**find_all_twingraphs**](TwingraphApi.md#find_all_twingraphs) | **GET** /organizations/{organization_id}/twingraphs | 
[**get_graph_meta_data**](TwingraphApi.md#get_graph_meta_data) | **GET** /organizations/{organization_id}/twingraph/{graph_id}/metadata | 
[**import_graph**](TwingraphApi.md#import_graph) | **POST** /organizations/{organization_id}/twingraph/import | 
[**job_status**](TwingraphApi.md#job_status) | **GET** /organizations/{organization_id}/job/{job_id}/status | 
[**query**](TwingraphApi.md#query) | **POST** /organizations/{organization_id}/twingraph/{graph_id}/query | 


# **delete**
> delete(organization_id, graph_id)



Launch a mass delete job

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

# **find_all_twingraphs**
> [str] find_all_twingraphs(organization_id)



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

# **get_graph_meta_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_graph_meta_data(organization_id, graph_id)



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

