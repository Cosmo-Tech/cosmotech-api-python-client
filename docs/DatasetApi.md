# cosmotech_api.DatasetApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset**](DatasetApi.md#create_dataset) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/datasets | Create a Dataset
[**create_dataset_access_control**](DatasetApi.md#create_dataset_access_control) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id}/security/access | Add a control access to the Dataset
[**create_dataset_part**](DatasetApi.md#create_dataset_part) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id}/parts | Create a data part of a Dataset
[**delete_dataset**](DatasetApi.md#delete_dataset) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id} | Delete a Dataset
[**delete_dataset_access_control**](DatasetApi.md#delete_dataset_access_control) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id}/security/access/{identity_id} | Remove the specified access from the given Dataset
[**delete_dataset_part**](DatasetApi.md#delete_dataset_part) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id}/parts/{dataset_part_id} | Delete a Dataset part
[**download_dataset_part**](DatasetApi.md#download_dataset_part) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id}/parts/{dataset_part_id}/download | Download data from a dataset part
[**get_dataset**](DatasetApi.md#get_dataset) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id} | Retrieve a Dataset
[**get_dataset_access_control**](DatasetApi.md#get_dataset_access_control) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id}/security/access/{identity_id} | Get a control access for the Dataset
[**get_dataset_part**](DatasetApi.md#get_dataset_part) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id}/parts/{dataset_part_id} | Retrieve a data part of a Dataset
[**list_dataset_parts**](DatasetApi.md#list_dataset_parts) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id}/parts | Retrieve all dataset parts of a Dataset
[**list_dataset_security_users**](DatasetApi.md#list_dataset_security_users) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id}/security/users | Get the Dataset security users list
[**list_datasets**](DatasetApi.md#list_datasets) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/datasets | Retrieve a list of defined Dataset
[**query_data**](DatasetApi.md#query_data) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id}/parts/{dataset_part_id}/query | Query data of a Dataset part. This endpoint is only available for dataset parts that support queries (type &#x3D;&#x3D; DB). 
[**replace_dataset_part**](DatasetApi.md#replace_dataset_part) | **PUT** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id}/parts/{dataset_part_id} | Replace existing dataset parts of a Dataset
[**search_dataset_parts**](DatasetApi.md#search_dataset_parts) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id}/parts/search | Search Dataset parts by tags
[**search_datasets**](DatasetApi.md#search_datasets) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/search | Search Datasets by tags
[**update_dataset**](DatasetApi.md#update_dataset) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id} | Update a Dataset
[**update_dataset_access_control**](DatasetApi.md#update_dataset_access_control) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id}/security/access/{identity_id} | Update the specified access to User for a Dataset
[**update_dataset_default_security**](DatasetApi.md#update_dataset_default_security) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id}/security/default | Set the Dataset default security
[**update_dataset_part**](DatasetApi.md#update_dataset_part) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id}/datasets/{dataset_id}/parts/{dataset_part_id} | Update existing dataset parts information of a Dataset


# **create_dataset**
> Dataset create_dataset(organization_id, workspace_id, dataset_create_request, files=files)

Create a Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.dataset import Dataset
from cosmotech_api.models.dataset_create_request import DatasetCreateRequest
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_create_request = cosmotech_api.DatasetCreateRequest() # DatasetCreateRequest | 
    files = None # List[bytearray] | Notes:   - Each parts defined in dataset should have a file defined in this list   - Please ensure that upload files order match with data parts list defined     - First file uploaded will match with first dataset parts and so on  (optional)

    try:
        # Create a Dataset
        api_response = api_instance.create_dataset(organization_id, workspace_id, dataset_create_request, files=files)
        print("The response of DatasetApi->create_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->create_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_create_request** | [**DatasetCreateRequest**](DatasetCreateRequest.md)|  | 
 **files** | **List[bytearray]**| Notes:   - Each parts defined in dataset should have a file defined in this list   - Please ensure that upload files order match with data parts list defined     - First file uploaded will match with first dataset parts and so on  | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Dataset successfully created |  -  |
**400** | Bad request |  -  |
**403** | Insufficient permissions on organization, workspace or dataset |  -  |
**404** | Organization, workspace specified is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dataset_access_control**
> DatasetAccessControl create_dataset_access_control(organization_id, workspace_id, dataset_id, dataset_access_control)

Add a control access to the Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.dataset_access_control import DatasetAccessControl
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier
    dataset_access_control = cosmotech_api.DatasetAccessControl() # DatasetAccessControl | the new Dataset security access to add.

    try:
        # Add a control access to the Dataset
        api_response = api_instance.create_dataset_access_control(organization_id, workspace_id, dataset_id, dataset_access_control)
        print("The response of DatasetApi->create_dataset_access_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->create_dataset_access_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 
 **dataset_access_control** | [**DatasetAccessControl**](DatasetAccessControl.md)| the new Dataset security access to add. | 

### Return type

[**DatasetAccessControl**](DatasetAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Dataset access |  -  |
**404** | the Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dataset_part**
> DatasetPart create_dataset_part(organization_id, workspace_id, dataset_id, file, dataset_part_create_request)

Create a data part of a Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.dataset_part import DatasetPart
from cosmotech_api.models.dataset_part_create_request import DatasetPartCreateRequest
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier
    file = None # bytearray | Data file to upload
    dataset_part_create_request = cosmotech_api.DatasetPartCreateRequest() # DatasetPartCreateRequest | 

    try:
        # Create a data part of a Dataset
        api_response = api_instance.create_dataset_part(organization_id, workspace_id, dataset_id, file, dataset_part_create_request)
        print("The response of DatasetApi->create_dataset_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->create_dataset_part: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 
 **file** | **bytearray**| Data file to upload | 
 **dataset_part_create_request** | [**DatasetPartCreateRequest**](DatasetPartCreateRequest.md)|  | 

### Return type

[**DatasetPart**](DatasetPart.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Dataset part successfully created |  -  |
**400** | Bad request - Dataset part cannot be created |  -  |
**403** | Insufficient permissions on organization, workspace or dataset |  -  |
**404** | Dataset specified is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset**
> delete_dataset(organization_id, workspace_id, dataset_id)

Delete a Dataset

Delete a dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier

    try:
        # Delete a Dataset
        api_instance.delete_dataset(organization_id, workspace_id, dataset_id)
    except Exception as e:
        print("Exception when calling DatasetApi->delete_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
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
**204** | Dataset successfully deleted |  -  |
**403** | Insufficient permissions on organization, workspace or dataset |  -  |
**404** | Organization or workspace or dataset specified is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset_access_control**
> delete_dataset_access_control(organization_id, workspace_id, dataset_id, identity_id)

Remove the specified access from the given Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier
    identity_id = 'identity_id_example' # str | the User identifier

    try:
        # Remove the specified access from the given Dataset
        api_instance.delete_dataset_access_control(organization_id, workspace_id, dataset_id, identity_id)
    except Exception as e:
        print("Exception when calling DatasetApi->delete_dataset_access_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
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

# **delete_dataset_part**
> delete_dataset_part(organization_id, workspace_id, dataset_id, dataset_part_id)

Delete a Dataset part

Delete a dataset part

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier
    dataset_part_id = 'dataset_part_id_example' # str | the Dataset part identifier

    try:
        # Delete a Dataset part
        api_instance.delete_dataset_part(organization_id, workspace_id, dataset_id, dataset_part_id)
    except Exception as e:
        print("Exception when calling DatasetApi->delete_dataset_part: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 
 **dataset_part_id** | **str**| the Dataset part identifier | 

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
**204** | Dataset part successfully deleted |  -  |
**403** | Insufficient permissions on organization, workspace or dataset |  -  |
**404** | Dataset part specified is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_dataset_part**
> bytearray download_dataset_part(organization_id, workspace_id, dataset_id, dataset_part_id)

Download data from a dataset part

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier
    dataset_part_id = 'dataset_part_id_example' # str | the Dataset part identifier

    try:
        # Download data from a dataset part
        api_response = api_instance.download_dataset_part(organization_id, workspace_id, dataset_id, dataset_part_id)
        print("The response of DatasetApi->download_dataset_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->download_dataset_part: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 
 **dataset_part_id** | **str**| the Dataset part identifier | 

### Return type

**bytearray**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset part successfully downloaded |  -  |
**403** | Insufficient permissions on organization, workspace or dataset |  -  |
**404** | Dataset part specified is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset**
> Dataset get_dataset(organization_id, workspace_id, dataset_id)

Retrieve a Dataset

Retrieve a dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.dataset import Dataset
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier

    try:
        # Retrieve a Dataset
        api_response = api_instance.get_dataset(organization_id, workspace_id, dataset_id)
        print("The response of DatasetApi->get_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->get_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset successfully retrieved |  -  |
**403** | Insufficient permissions on organization, workspace or dataset |  -  |
**404** | Organization, workspace or dataset specified is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_access_control**
> DatasetAccessControl get_dataset_access_control(organization_id, workspace_id, dataset_id, identity_id)

Get a control access for the Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.dataset_access_control import DatasetAccessControl
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier
    identity_id = 'identity_id_example' # str | the User identifier

    try:
        # Get a control access for the Dataset
        api_response = api_instance.get_dataset_access_control(organization_id, workspace_id, dataset_id, identity_id)
        print("The response of DatasetApi->get_dataset_access_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->get_dataset_access_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 
 **identity_id** | **str**| the User identifier | 

### Return type

[**DatasetAccessControl**](DatasetAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Dataset access |  -  |
**404** | The Dataset or user specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_part**
> DatasetPart get_dataset_part(organization_id, workspace_id, dataset_id, dataset_part_id)

Retrieve a data part of a Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.dataset_part import DatasetPart
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier
    dataset_part_id = 'dataset_part_id_example' # str | the Dataset part identifier

    try:
        # Retrieve a data part of a Dataset
        api_response = api_instance.get_dataset_part(organization_id, workspace_id, dataset_id, dataset_part_id)
        print("The response of DatasetApi->get_dataset_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->get_dataset_part: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 
 **dataset_part_id** | **str**| the Dataset part identifier | 

### Return type

[**DatasetPart**](DatasetPart.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset part successfully retrieved |  -  |
**403** | Insufficient permissions on organization, workspace or dataset |  -  |
**404** | Dataset part specified is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dataset_parts**
> List[DatasetPart] list_dataset_parts(organization_id, workspace_id, dataset_id, page=page, size=size)

Retrieve all dataset parts of a Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.dataset_part import DatasetPart
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier
    page = 56 # int | Page number to query (first page is at index 0) (optional)
    size = 56 # int | Amount of result by page (optional)

    try:
        # Retrieve all dataset parts of a Dataset
        api_response = api_instance.list_dataset_parts(organization_id, workspace_id, dataset_id, page=page, size=size)
        print("The response of DatasetApi->list_dataset_parts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->list_dataset_parts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 
 **page** | **int**| Page number to query (first page is at index 0) | [optional] 
 **size** | **int**| Amount of result by page | [optional] 

### Return type

[**List[DatasetPart]**](DatasetPart.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of dataset parts |  -  |
**403** | Insufficient permissions on organization, workspace or dataset |  -  |
**404** | Dataset specified is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dataset_security_users**
> List[str] list_dataset_security_users(organization_id, workspace_id, dataset_id)

Get the Dataset security users list

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier

    try:
        # Get the Dataset security users list
        api_response = api_instance.list_dataset_security_users(organization_id, workspace_id, dataset_id)
        print("The response of DatasetApi->list_dataset_security_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->list_dataset_security_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 

### Return type

**List[str]**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Dataset security users list |  -  |
**404** | the Dataset or the User specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_datasets**
> List[Dataset] list_datasets(organization_id, workspace_id, page=page, size=size)

Retrieve a list of defined Dataset

List all datasets

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.dataset import Dataset
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    page = 56 # int | Page number to query (first page is at index 0) (optional)
    size = 56 # int | Amount of result by page (optional)

    try:
        # Retrieve a list of defined Dataset
        api_response = api_instance.list_datasets(organization_id, workspace_id, page=page, size=size)
        print("The response of DatasetApi->list_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->list_datasets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **page** | **int**| Page number to query (first page is at index 0) | [optional] 
 **size** | **int**| Amount of result by page | [optional] 

### Return type

[**List[Dataset]**](Dataset.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Datasets successfully retrieved |  -  |
**403** | Insufficient permissions on organization, workspace or dataset |  -  |
**404** | Organization, workspace or dataset specified is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_data**
> bytearray query_data(organization_id, workspace_id, dataset_id, dataset_part_id, selects=selects, sums=sums, avgs=avgs, counts=counts, mins=mins, maxs=maxs, offset=offset, limit=limit, group_bys=group_bys, order_bys=order_bys)

Query data of a Dataset part. This endpoint is only available for dataset parts that support queries (type == DB). 

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier
    dataset_part_id = 'dataset_part_id_example' # str | the Dataset part identifier
    selects = ['selects_example'] # List[str] | Column names that should be part of the response data. You can specify a column name like:  - id  - stock  - quantity  - ... If you want to select only distinct columns, add a * at the end of the column name (e.g. stock*).  (optional)
    sums = ['sums_example'] # List[str] | Column names to sum by. If you want to sum only distinct columns, add a * at the end of the column name (e.g. stock*).  (optional)
    avgs = ['avgs_example'] # List[str] | Column names to average by. If you want to apply 'average' only on distinct columns, add a * at the end of the column name (e.g. stock*).  (optional)
    counts = ['counts_example'] # List[str] | Column names to count by. If you want to count only distinct columns, add a * at the end of the column name (e.g. stock*).  (optional)
    mins = ['mins_example'] # List[str] | Column names to min by. If you want to apply 'min' only on distinct columns, add a * at the end of the column name (e.g. stock*).  (optional)
    maxs = ['maxs_example'] # List[str] | Column names to max by. If you want to apply 'max' only on distinct columns, add a * at the end of the column name (e.g. stock*).  (optional)
    offset = 56 # int | The query offset (optional)
    limit = 56 # int | The query limit (optional)
    group_bys = ['group_bys_example'] # List[str] | Column names to group by (optional)
    order_bys = ['order_bys_example'] # List[str] | Column names to order by. Default order is ascending. If you want to specify 'descending' order, add a '!' at the beginning of the column name (e.g. !stock).  (optional)

    try:
        # Query data of a Dataset part. This endpoint is only available for dataset parts that support queries (type == DB). 
        api_response = api_instance.query_data(organization_id, workspace_id, dataset_id, dataset_part_id, selects=selects, sums=sums, avgs=avgs, counts=counts, mins=mins, maxs=maxs, offset=offset, limit=limit, group_bys=group_bys, order_bys=order_bys)
        print("The response of DatasetApi->query_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->query_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 
 **dataset_part_id** | **str**| the Dataset part identifier | 
 **selects** | [**List[str]**](str.md)| Column names that should be part of the response data. You can specify a column name like:  - id  - stock  - quantity  - ... If you want to select only distinct columns, add a * at the end of the column name (e.g. stock*).  | [optional] 
 **sums** | [**List[str]**](str.md)| Column names to sum by. If you want to sum only distinct columns, add a * at the end of the column name (e.g. stock*).  | [optional] 
 **avgs** | [**List[str]**](str.md)| Column names to average by. If you want to apply &#39;average&#39; only on distinct columns, add a * at the end of the column name (e.g. stock*).  | [optional] 
 **counts** | [**List[str]**](str.md)| Column names to count by. If you want to count only distinct columns, add a * at the end of the column name (e.g. stock*).  | [optional] 
 **mins** | [**List[str]**](str.md)| Column names to min by. If you want to apply &#39;min&#39; only on distinct columns, add a * at the end of the column name (e.g. stock*).  | [optional] 
 **maxs** | [**List[str]**](str.md)| Column names to max by. If you want to apply &#39;max&#39; only on distinct columns, add a * at the end of the column name (e.g. stock*).  | [optional] 
 **offset** | **int**| The query offset | [optional] 
 **limit** | **int**| The query limit | [optional] 
 **group_bys** | [**List[str]**](str.md)| Column names to group by | [optional] 
 **order_bys** | [**List[str]**](str.md)| Column names to order by. Default order is ascending. If you want to specify &#39;descending&#39; order, add a &#39;!&#39; at the beginning of the column name (e.g. !stock).  | [optional] 

### Return type

**bytearray**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data related to provided information |  -  |
**400** | Bad request - Data cannot be retrieved from provided information |  -  |
**403** | Insufficient permissions on organization, workspace or dataset |  -  |
**404** | Dataset specified is not found or you don&#39;t have access to it |  -  |
**422** | Targeted dataset do not support requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_dataset_part**
> DatasetPart replace_dataset_part(organization_id, workspace_id, dataset_id, dataset_part_id, file, dataset_part_update_request=dataset_part_update_request)

Replace existing dataset parts of a Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.dataset_part import DatasetPart
from cosmotech_api.models.dataset_part_update_request import DatasetPartUpdateRequest
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier
    dataset_part_id = 'dataset_part_id_example' # str | the Dataset part identifier
    file = None # bytearray | Data file to upload
    dataset_part_update_request = cosmotech_api.DatasetPartUpdateRequest() # DatasetPartUpdateRequest |  (optional)

    try:
        # Replace existing dataset parts of a Dataset
        api_response = api_instance.replace_dataset_part(organization_id, workspace_id, dataset_id, dataset_part_id, file, dataset_part_update_request=dataset_part_update_request)
        print("The response of DatasetApi->replace_dataset_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->replace_dataset_part: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 
 **dataset_part_id** | **str**| the Dataset part identifier | 
 **file** | **bytearray**| Data file to upload | 
 **dataset_part_update_request** | [**DatasetPartUpdateRequest**](DatasetPartUpdateRequest.md)|  | [optional] 

### Return type

[**DatasetPart**](DatasetPart.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset part successfully replaced |  -  |
**400** | Bad request |  -  |
**403** | Insufficient permissions on organization, workspace or dataset |  -  |
**404** | Dataset part specified is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_dataset_parts**
> List[DatasetPart] search_dataset_parts(organization_id, workspace_id, dataset_id, request_body, page=page, size=size)

Search Dataset parts by tags

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.dataset_part import DatasetPart
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier
    request_body = ['request_body_example'] # List[str] | the Dataset parts search parameters
    page = 56 # int | Page number to query (first page is at index 0) (optional)
    size = 56 # int | Amount of result by page (optional)

    try:
        # Search Dataset parts by tags
        api_response = api_instance.search_dataset_parts(organization_id, workspace_id, dataset_id, request_body, page=page, size=size)
        print("The response of DatasetApi->search_dataset_parts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->search_dataset_parts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 
 **request_body** | [**List[str]**](str.md)| the Dataset parts search parameters | 
 **page** | **int**| Page number to query (first page is at index 0) | [optional] 
 **size** | **int**| Amount of result by page | [optional] 

### Return type

[**List[DatasetPart]**](DatasetPart.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset part list containing tags |  -  |
**400** | Bad request |  -  |
**403** | Insufficient permissions on organization, workspace or dataset |  -  |
**404** | Dataset specified is not found or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_datasets**
> List[Dataset] search_datasets(organization_id, workspace_id, request_body, page=page, size=size)

Search Datasets by tags

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.dataset import Dataset
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    request_body = ['request_body_example'] # List[str] | the Dataset search parameters
    page = 56 # int | Page number to query (first page is at index 0) (optional)
    size = 56 # int | Amount of result by page (optional)

    try:
        # Search Datasets by tags
        api_response = api_instance.search_datasets(organization_id, workspace_id, request_body, page=page, size=size)
        print("The response of DatasetApi->search_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->search_datasets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **request_body** | [**List[str]**](str.md)| the Dataset search parameters | 
 **page** | **int**| Page number to query (first page is at index 0) | [optional] 
 **size** | **int**| Amount of result by page | [optional] 

### Return type

[**List[Dataset]**](Dataset.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset list containing tags |  -  |
**403** | Insufficient permissions on organization, workspace or dataset |  -  |
**404** | Organization, workspace or dataset specified is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset**
> Dataset update_dataset(organization_id, workspace_id, dataset_id, dataset_update_request, files=files)

Update a Dataset

Update a dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.dataset import Dataset
from cosmotech_api.models.dataset_update_request import DatasetUpdateRequest
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier
    dataset_update_request = cosmotech_api.DatasetUpdateRequest() # DatasetUpdateRequest | 
    files = None # List[bytearray] | Notes:   - Each parts defined in dataset should have a file defined in this list   - Please ensure that upload files order match with data parts list defined     - First file uploaded will match with first dataset parts and so on  (optional)

    try:
        # Update a Dataset
        api_response = api_instance.update_dataset(organization_id, workspace_id, dataset_id, dataset_update_request, files=files)
        print("The response of DatasetApi->update_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->update_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 
 **dataset_update_request** | [**DatasetUpdateRequest**](DatasetUpdateRequest.md)|  | 
 **files** | **List[bytearray]**| Notes:   - Each parts defined in dataset should have a file defined in this list   - Please ensure that upload files order match with data parts list defined     - First file uploaded will match with first dataset parts and so on  | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset successfully updated |  -  |
**400** | Bad request |  -  |
**403** | Insufficient permissions on organization, workspace or dataset |  -  |
**404** | Organization, workspace or dataset specified is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset_access_control**
> DatasetAccessControl update_dataset_access_control(organization_id, workspace_id, dataset_id, identity_id, dataset_role)

Update the specified access to User for a Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.dataset_access_control import DatasetAccessControl
from cosmotech_api.models.dataset_role import DatasetRole
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier
    identity_id = 'identity_id_example' # str | the User identifier
    dataset_role = cosmotech_api.DatasetRole() # DatasetRole | The new Dataset Access Control

    try:
        # Update the specified access to User for a Dataset
        api_response = api_instance.update_dataset_access_control(organization_id, workspace_id, dataset_id, identity_id, dataset_role)
        print("The response of DatasetApi->update_dataset_access_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->update_dataset_access_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 
 **identity_id** | **str**| the User identifier | 
 **dataset_role** | [**DatasetRole**](DatasetRole.md)| The new Dataset Access Control | 

### Return type

[**DatasetAccessControl**](DatasetAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Dataset access |  -  |
**404** | The Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset_default_security**
> DatasetSecurity update_dataset_default_security(organization_id, workspace_id, dataset_id, dataset_role)

Set the Dataset default security

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.dataset_role import DatasetRole
from cosmotech_api.models.dataset_security import DatasetSecurity
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier
    dataset_role = cosmotech_api.DatasetRole() # DatasetRole | This change the dataset default security. The default security is the role assigned to any person not on the Access Control List. If the default security is None, then nobody outside of the ACL can access the dataset.

    try:
        # Set the Dataset default security
        api_response = api_instance.update_dataset_default_security(organization_id, workspace_id, dataset_id, dataset_role)
        print("The response of DatasetApi->update_dataset_default_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->update_dataset_default_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 
 **dataset_role** | [**DatasetRole**](DatasetRole.md)| This change the dataset default security. The default security is the role assigned to any person not on the Access Control List. If the default security is None, then nobody outside of the ACL can access the dataset. | 

### Return type

[**DatasetSecurity**](DatasetSecurity.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Dataset default visibility |  -  |
**404** | the Dataset specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset_part**
> DatasetPart update_dataset_part(organization_id, workspace_id, dataset_id, dataset_part_id, dataset_part_update_request)

Update existing dataset parts information of a Dataset

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.dataset_part import DatasetPart
from cosmotech_api.models.dataset_part_update_request import DatasetPartUpdateRequest
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.DatasetApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    dataset_id = 'dataset_id_example' # str | the Dataset identifier
    dataset_part_id = 'dataset_part_id_example' # str | the Dataset part identifier
    dataset_part_update_request = cosmotech_api.DatasetPartUpdateRequest() # DatasetPartUpdateRequest | Dataset part information to update

    try:
        # Update existing dataset parts information of a Dataset
        api_response = api_instance.update_dataset_part(organization_id, workspace_id, dataset_id, dataset_part_id, dataset_part_update_request)
        print("The response of DatasetApi->update_dataset_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->update_dataset_part: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **dataset_id** | **str**| the Dataset identifier | 
 **dataset_part_id** | **str**| the Dataset part identifier | 
 **dataset_part_update_request** | [**DatasetPartUpdateRequest**](DatasetPartUpdateRequest.md)| Dataset part information to update | 

### Return type

[**DatasetPart**](DatasetPart.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset part information successfully updated |  -  |
**400** | Bad request |  -  |
**403** | Insufficient permissions on organization, workspace or dataset |  -  |
**404** | Dataset part specified is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

