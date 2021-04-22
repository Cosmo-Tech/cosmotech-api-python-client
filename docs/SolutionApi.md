# cosmotech_api.SolutionApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_solution**](SolutionApi.md#create_solution) | **POST** /organizations/{organization_id}/solutions | Register a new solution
[**delete_solution**](SolutionApi.md#delete_solution) | **DELETE** /organizations/{organization_id}/solutions/{solution_id} | Delete a solution
[**find_all_solutions**](SolutionApi.md#find_all_solutions) | **GET** /organizations/{organization_id}/solutions | List all Solutions
[**find_solution_by_id**](SolutionApi.md#find_solution_by_id) | **GET** /organizations/{organization_id}/solutions/{solution_id} | Get the details of a solution
[**update_solution**](SolutionApi.md#update_solution) | **PATCH** /organizations/{organization_id}/solutions/{solution_id} | Update a solution
[**upload**](SolutionApi.md#upload) | **POST** /organizations/{organization_id}/solutions/upload | Upload and register a new solution


# **create_solution**
> Solution create_solution(organization_id, solution)

Register a new solution

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.solution import Solution
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution = Solution(
        id="id_example",
        key="key_example",
        name="name_example",
        description="description_example",
        repository="repository_example",
        csm_simulator="csm_simulator_example",
        version="version_example",
        owner_id="owner_id_example",
        url="url_example",
        tags=[
            "tags_example",
        ],
        parameters=[
            RunTemplateParameter(
                id="id_example",
                labels=TranslatedLabels(),
                var_type="var_type_example",
                options={},
            ),
        ],
        parameter_groups=[
            RunTemplateParameterGroup(
                id="id_example",
                labels=TranslatedLabels(),
                is_table=True,
                options={},
                parent_id="parent_id_example",
                parameters=[
                    "parameters_example",
                ],
            ),
        ],
        run_templates=[
            RunTemplate(
                id="id_example",
                name="name_example",
                description="description_example",
                csm_simulation="csm_simulation_example",
                tags=[
                    "tags_example",
                ],
                compute_size="compute_size_example",
                parameters_handler_resource=RunTemplateResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                dataset_validator_resource=RunTemplateResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                pre_run_resource=RunTemplateResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                engine_resource=RunTemplateResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                post_run_resource=RunTemplateResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                send_datasets_to_data_warehouse=True,
                send_input_parameters_to_data_warehouse=True,
                parameter_groups=[
                    "parameter_groups_example",
                ],
            ),
        ],
    ) # Solution | the Solution to create

    # example passing only required values which don't have defaults set
    try:
        # Register a new solution
        api_response = api_instance.create_solution(organization_id, solution)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SolutionApi->create_solution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **solution** | [**Solution**](Solution.md)| the Solution to create |

### Return type

[**Solution**](Solution.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the solution details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_solution**
> Solution delete_solution(organization_id, solution_id)

Delete a solution

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.solution import Solution
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete a solution
        api_response = api_instance.delete_solution(organization_id, solution_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SolutionApi->delete_solution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **solution_id** | **str**| the Solution identifier |

### Return type

[**Solution**](Solution.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the solution details |  -  |
**400** | Bad request |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_solutions**
> [Solution] find_all_solutions(organization_id)

List all Solutions

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.solution import Solution
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier

    # example passing only required values which don't have defaults set
    try:
        # List all Solutions
        api_response = api_instance.find_all_solutions(organization_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SolutionApi->find_all_solutions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |

### Return type

[**[Solution]**](Solution.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the solution details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_solution_by_id**
> Solution find_solution_by_id(organization_id, solution_id)

Get the details of a solution

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.solution import Solution
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a solution
        api_response = api_instance.find_solution_by_id(organization_id, solution_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SolutionApi->find_solution_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **solution_id** | **str**| the Solution identifier |

### Return type

[**Solution**](Solution.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Solution details |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_solution**
> Solution update_solution(organization_id, solution_id, solution)

Update a solution

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.solution import Solution
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier
    solution = Solution(
        id="id_example",
        key="key_example",
        name="name_example",
        description="description_example",
        repository="repository_example",
        csm_simulator="csm_simulator_example",
        version="version_example",
        owner_id="owner_id_example",
        url="url_example",
        tags=[
            "tags_example",
        ],
        parameters=[
            RunTemplateParameter(
                id="id_example",
                labels=TranslatedLabels(),
                var_type="var_type_example",
                options={},
            ),
        ],
        parameter_groups=[
            RunTemplateParameterGroup(
                id="id_example",
                labels=TranslatedLabels(),
                is_table=True,
                options={},
                parent_id="parent_id_example",
                parameters=[
                    "parameters_example",
                ],
            ),
        ],
        run_templates=[
            RunTemplate(
                id="id_example",
                name="name_example",
                description="description_example",
                csm_simulation="csm_simulation_example",
                tags=[
                    "tags_example",
                ],
                compute_size="compute_size_example",
                parameters_handler_resource=RunTemplateResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                dataset_validator_resource=RunTemplateResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                pre_run_resource=RunTemplateResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                engine_resource=RunTemplateResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                post_run_resource=RunTemplateResourceStorage(
                    storage_type="local",
                    _resource_path="_resource_path_example",
                    custom_uri="custom_uri_example",
                ),
                send_datasets_to_data_warehouse=True,
                send_input_parameters_to_data_warehouse=True,
                parameter_groups=[
                    "parameter_groups_example",
                ],
            ),
        ],
    ) # Solution | the new Solution details.

    # example passing only required values which don't have defaults set
    try:
        # Update a solution
        api_response = api_instance.update_solution(organization_id, solution_id, solution)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SolutionApi->update_solution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **solution_id** | **str**| the Solution identifier |
 **solution** | [**Solution**](Solution.md)| the new Solution details. |

### Return type

[**Solution**](Solution.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the solution details |  -  |
**400** | Bad request |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> Solution upload(organization_id, body)

Upload and register a new solution

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.solution import Solution
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    body = open('/path/to/file', 'rb') # file_type | the Solution to upload and register

    # example passing only required values which don't have defaults set
    try:
        # Upload and register a new solution
        api_response = api_instance.upload(organization_id, body)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SolutionApi->upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **body** | **file_type**| the Solution to upload and register |

### Return type

[**Solution**](Solution.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/yaml
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the solution details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

