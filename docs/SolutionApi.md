# cosmotech_api.SolutionApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_solution**](SolutionApi.md#create_solution) | **POST** /organizations/{organization_id}/solutions | Create a new solution
[**create_solution_access_control**](SolutionApi.md#create_solution_access_control) | **POST** /organizations/{organization_id}/solutions/{solution_id}/security/access | Create solution access control
[**create_solution_parameter**](SolutionApi.md#create_solution_parameter) | **POST** /organizations/{organization_id}/solutions/{solution_id}/parameters | Create solution parameter for a solution
[**create_solution_parameter_group**](SolutionApi.md#create_solution_parameter_group) | **POST** /organizations/{organization_id}/solutions/{solution_id}/parameterGroups | Create a solution parameter group
[**create_solution_run_template**](SolutionApi.md#create_solution_run_template) | **POST** /organizations/{organization_id}/solutions/{solution_id}/runTemplates | Create a solution run template
[**delete_solution**](SolutionApi.md#delete_solution) | **DELETE** /organizations/{organization_id}/solutions/{solution_id} | Delete a solution
[**delete_solution_access_control**](SolutionApi.md#delete_solution_access_control) | **DELETE** /organizations/{organization_id}/solutions/{solution_id}/security/access/{identity_id} | Delete solution access control
[**delete_solution_parameter**](SolutionApi.md#delete_solution_parameter) | **DELETE** /organizations/{organization_id}/solutions/{solution_id}/parameters/{parameter_id} | Delete specific parameter from the solution
[**delete_solution_parameter_group**](SolutionApi.md#delete_solution_parameter_group) | **DELETE** /organizations/{organization_id}/solutions/{solution_id}/parameterGroups/{parameter_group_id} | Delete a parameter group from the solution
[**delete_solution_run_template**](SolutionApi.md#delete_solution_run_template) | **DELETE** /organizations/{organization_id}/solutions/{solution_id}/runTemplates/{run_template_id} | Delete a specific run template
[**get_run_template**](SolutionApi.md#get_run_template) | **GET** /organizations/{organization_id}/solutions/{solution_id}/runTemplates/{run_template_id} | Retrieve a solution run templates
[**get_solution**](SolutionApi.md#get_solution) | **GET** /organizations/{organization_id}/solutions/{solution_id} | Get the details of a solution
[**get_solution_access_control**](SolutionApi.md#get_solution_access_control) | **GET** /organizations/{organization_id}/solutions/{solution_id}/security/access/{identity_id} | Get solution access control
[**get_solution_parameter**](SolutionApi.md#get_solution_parameter) | **GET** /organizations/{organization_id}/solutions/{solution_id}/parameters/{parameter_id} | Get the details of a solution parameter
[**get_solution_parameter_group**](SolutionApi.md#get_solution_parameter_group) | **GET** /organizations/{organization_id}/solutions/{solution_id}/parameterGroups/{parameter_group_id} | Get details of a solution parameter group
[**get_solution_security**](SolutionApi.md#get_solution_security) | **GET** /organizations/{organization_id}/solutions/{solution_id}/security | Get solution security information
[**list_run_templates**](SolutionApi.md#list_run_templates) | **GET** /organizations/{organization_id}/solutions/{solution_id}/runTemplates | List all solution run templates
[**list_solution_parameter_groups**](SolutionApi.md#list_solution_parameter_groups) | **GET** /organizations/{organization_id}/solutions/{solution_id}/parameterGroups | List all solution parameter groups
[**list_solution_parameters**](SolutionApi.md#list_solution_parameters) | **GET** /organizations/{organization_id}/solutions/{solution_id}/parameters | List all solution parameters
[**list_solution_security_users**](SolutionApi.md#list_solution_security_users) | **GET** /organizations/{organization_id}/solutions/{solution_id}/security/users | List solution security users
[**list_solutions**](SolutionApi.md#list_solutions) | **GET** /organizations/{organization_id}/solutions | List all Solutions
[**update_solution**](SolutionApi.md#update_solution) | **PATCH** /organizations/{organization_id}/solutions/{solution_id} | Update a solution
[**update_solution_access_control**](SolutionApi.md#update_solution_access_control) | **PATCH** /organizations/{organization_id}/solutions/{solution_id}/security/access/{identity_id} | Update solution access control
[**update_solution_default_security**](SolutionApi.md#update_solution_default_security) | **PATCH** /organizations/{organization_id}/solutions/{solution_id}/security/default | Update solution default security
[**update_solution_parameter**](SolutionApi.md#update_solution_parameter) | **PATCH** /organizations/{organization_id}/solutions/{solution_id}/parameters/{parameter_id} | Update solution parameter
[**update_solution_parameter_group**](SolutionApi.md#update_solution_parameter_group) | **PATCH** /organizations/{organization_id}/solutions/{solution_id}/parameterGroups/{parameter_group_id} | Update a solution parameter group
[**update_solution_run_template**](SolutionApi.md#update_solution_run_template) | **PATCH** /organizations/{organization_id}/solutions/{solution_id}/runTemplates/{run_template_id} | Update a specific run template


# **create_solution**
> Solution create_solution(organization_id, solution_create_request)

Create a new solution

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.solution import Solution
from cosmotech_api.models.solution_create_request import SolutionCreateRequest
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_create_request = cosmotech_api.SolutionCreateRequest() # SolutionCreateRequest | The Solution to create

    try:
        # Create a new solution
        api_response = api_instance.create_solution(organization_id, solution_create_request)
        print("The response of SolutionApi->create_solution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->create_solution: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_create_request** | [**SolutionCreateRequest**](SolutionCreateRequest.md)| The Solution to create | 

### Return type

[**Solution**](Solution.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Solution successfully created |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_solution_access_control**
> SolutionAccessControl create_solution_access_control(organization_id, solution_id, solution_access_control)

Create solution access control

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.solution_access_control import SolutionAccessControl
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    solution_access_control = cosmotech_api.SolutionAccessControl() # SolutionAccessControl | Access control to create

    try:
        # Create solution access control
        api_response = api_instance.create_solution_access_control(organization_id, solution_id, solution_access_control)
        print("The response of SolutionApi->create_solution_access_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->create_solution_access_control: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **solution_access_control** | [**SolutionAccessControl**](SolutionAccessControl.md)| Access control to create | 

### Return type

[**SolutionAccessControl**](SolutionAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Solution access control successfully created |  -  |
**404** | Solution not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_solution_parameter**
> RunTemplateParameter create_solution_parameter(organization_id, solution_id, run_template_parameter_create_request)

Create solution parameter for a solution

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run_template_parameter import RunTemplateParameter
from cosmotech_api.models.run_template_parameter_create_request import RunTemplateParameterCreateRequest
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    run_template_parameter_create_request = cosmotech_api.RunTemplateParameterCreateRequest() # RunTemplateParameterCreateRequest | Parameter to create

    try:
        # Create solution parameter for a solution
        api_response = api_instance.create_solution_parameter(organization_id, solution_id, run_template_parameter_create_request)
        print("The response of SolutionApi->create_solution_parameter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->create_solution_parameter: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **run_template_parameter_create_request** | [**RunTemplateParameterCreateRequest**](RunTemplateParameterCreateRequest.md)| Parameter to create | 

### Return type

[**RunTemplateParameter**](RunTemplateParameter.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Parameters successfully created |  -  |
**400** | Bad request |  -  |
**404** | Solution not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_solution_parameter_group**
> RunTemplateParameterGroup create_solution_parameter_group(organization_id, solution_id, run_template_parameter_group_create_request)

Create a solution parameter group

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run_template_parameter_group import RunTemplateParameterGroup
from cosmotech_api.models.run_template_parameter_group_create_request import RunTemplateParameterGroupCreateRequest
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    run_template_parameter_group_create_request = cosmotech_api.RunTemplateParameterGroupCreateRequest() # RunTemplateParameterGroupCreateRequest | Parameter group to create

    try:
        # Create a solution parameter group
        api_response = api_instance.create_solution_parameter_group(organization_id, solution_id, run_template_parameter_group_create_request)
        print("The response of SolutionApi->create_solution_parameter_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->create_solution_parameter_group: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **run_template_parameter_group_create_request** | [**RunTemplateParameterGroupCreateRequest**](RunTemplateParameterGroupCreateRequest.md)| Parameter group to create | 

### Return type

[**RunTemplateParameterGroup**](RunTemplateParameterGroup.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Parameter group successfully created |  -  |
**400** | Bad request - Invalid parameter group |  -  |
**404** | Solution not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_solution_run_template**
> RunTemplate create_solution_run_template(organization_id, solution_id, run_template_create_request)

Create a solution run template

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run_template import RunTemplate
from cosmotech_api.models.run_template_create_request import RunTemplateCreateRequest
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    run_template_create_request = cosmotech_api.RunTemplateCreateRequest() # RunTemplateCreateRequest | Run template to create

    try:
        # Create a solution run template
        api_response = api_instance.create_solution_run_template(organization_id, solution_id, run_template_create_request)
        print("The response of SolutionApi->create_solution_run_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->create_solution_run_template: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **run_template_create_request** | [**RunTemplateCreateRequest**](RunTemplateCreateRequest.md)| Run template to create | 

### Return type

[**RunTemplate**](RunTemplate.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Run template successfully created |  -  |
**400** | Bad request - Invalid run template |  -  |
**404** | Solution not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_solution**
> delete_solution(organization_id, solution_id)

Delete a solution

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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier

    try:
        # Delete a solution
        api_instance.delete_solution(organization_id, solution_id)
    except Exception as e:
        print("Exception when calling SolutionApi->delete_solution: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 

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
**204** | Solution successfully deleted |  -  |
**404** | Solution not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_solution_access_control**
> delete_solution_access_control(organization_id, solution_id, identity_id)

Delete solution access control

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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    identity_id = 'identity_id_example' # str | The User identifier

    try:
        # Delete solution access control
        api_instance.delete_solution_access_control(organization_id, solution_id, identity_id)
    except Exception as e:
        print("Exception when calling SolutionApi->delete_solution_access_control: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **identity_id** | **str**| The User identifier | 

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
**204** | Solution access control successfully deleted |  -  |
**404** | Solution or user not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_solution_parameter**
> delete_solution_parameter(organization_id, solution_id, parameter_id)

Delete specific parameter from the solution

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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    parameter_id = 'parameter_id_example' # str | The solution parameter identifier

    try:
        # Delete specific parameter from the solution
        api_instance.delete_solution_parameter(organization_id, solution_id, parameter_id)
    except Exception as e:
        print("Exception when calling SolutionApi->delete_solution_parameter: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **parameter_id** | **str**| The solution parameter identifier | 

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
**204** | Parameter successfully deleted |  -  |
**404** | Solution or parameter not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_solution_parameter_group**
> delete_solution_parameter_group(organization_id, solution_id, parameter_group_id)

Delete a parameter group from the solution

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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    parameter_group_id = 'parameter_group_id_example' # str | The parameter group identifier

    try:
        # Delete a parameter group from the solution
        api_instance.delete_solution_parameter_group(organization_id, solution_id, parameter_group_id)
    except Exception as e:
        print("Exception when calling SolutionApi->delete_solution_parameter_group: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **parameter_group_id** | **str**| The parameter group identifier | 

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
**204** | Parameter group successfully deleted |  -  |
**404** | Solution or parameter group not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_solution_run_template**
> delete_solution_run_template(organization_id, solution_id, run_template_id)

Delete a specific run template

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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    run_template_id = 'run_template_id_example' # str | The Run Template identifier

    try:
        # Delete a specific run template
        api_instance.delete_solution_run_template(organization_id, solution_id, run_template_id)
    except Exception as e:
        print("Exception when calling SolutionApi->delete_solution_run_template: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **run_template_id** | **str**| The Run Template identifier | 

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
**204** | Run template successfully deleted |  -  |
**404** | Solution or run template not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_template**
> RunTemplate get_run_template(organization_id, solution_id, run_template_id)

Retrieve a solution run templates

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run_template import RunTemplate
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    run_template_id = 'run_template_id_example' # str | The Run Template identifier

    try:
        # Retrieve a solution run templates
        api_response = api_instance.get_run_template(organization_id, solution_id, run_template_id)
        print("The response of SolutionApi->get_run_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->get_run_template: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **run_template_id** | **str**| The Run Template identifier | 

### Return type

[**RunTemplate**](RunTemplate.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run template successfully retrieved |  -  |
**404** | Solution not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solution**
> Solution get_solution(organization_id, solution_id)

Get the details of a solution

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.solution import Solution
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier

    try:
        # Get the details of a solution
        api_response = api_instance.get_solution(organization_id, solution_id)
        print("The response of SolutionApi->get_solution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->get_solution: %s\n" % e)
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
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Solution details successfully retrieved |  -  |
**404** | Solution not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solution_access_control**
> SolutionAccessControl get_solution_access_control(organization_id, solution_id, identity_id)

Get solution access control

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.solution_access_control import SolutionAccessControl
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    identity_id = 'identity_id_example' # str | The User identifier

    try:
        # Get solution access control
        api_response = api_instance.get_solution_access_control(organization_id, solution_id, identity_id)
        print("The response of SolutionApi->get_solution_access_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->get_solution_access_control: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **identity_id** | **str**| The User identifier | 

### Return type

[**SolutionAccessControl**](SolutionAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Solution access control successfully retrieved |  -  |
**404** | Solution or user not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solution_parameter**
> RunTemplateParameter get_solution_parameter(organization_id, solution_id, parameter_id)

Get the details of a solution parameter

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run_template_parameter import RunTemplateParameter
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    parameter_id = 'parameter_id_example' # str | The solution parameter identifier

    try:
        # Get the details of a solution parameter
        api_response = api_instance.get_solution_parameter(organization_id, solution_id, parameter_id)
        print("The response of SolutionApi->get_solution_parameter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->get_solution_parameter: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **parameter_id** | **str**| The solution parameter identifier | 

### Return type

[**RunTemplateParameter**](RunTemplateParameter.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Parameters successfully retrieved |  -  |
**400** | Bad Request |  -  |
**404** | Solution or parameter not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solution_parameter_group**
> RunTemplateParameterGroup get_solution_parameter_group(organization_id, solution_id, parameter_group_id)

Get details of a solution parameter group

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run_template_parameter_group import RunTemplateParameterGroup
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    parameter_group_id = 'parameter_group_id_example' # str | The parameter group identifier

    try:
        # Get details of a solution parameter group
        api_response = api_instance.get_solution_parameter_group(organization_id, solution_id, parameter_group_id)
        print("The response of SolutionApi->get_solution_parameter_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->get_solution_parameter_group: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **parameter_group_id** | **str**| The parameter group identifier | 

### Return type

[**RunTemplateParameterGroup**](RunTemplateParameterGroup.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Parameter groups successfully retrieved |  -  |
**404** | Solution or parameter group not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solution_security**
> SolutionSecurity get_solution_security(organization_id, solution_id)

Get solution security information

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.solution_security import SolutionSecurity
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier

    try:
        # Get solution security information
        api_response = api_instance.get_solution_security(organization_id, solution_id)
        print("The response of SolutionApi->get_solution_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->get_solution_security: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 

### Return type

[**SolutionSecurity**](SolutionSecurity.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Solution security information successfully retrieved |  -  |
**404** | Solution not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_run_templates**
> List[RunTemplate] list_run_templates(organization_id, solution_id)

List all solution run templates

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run_template import RunTemplate
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier

    try:
        # List all solution run templates
        api_response = api_instance.list_run_templates(organization_id, solution_id)
        print("The response of SolutionApi->list_run_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->list_run_templates: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 

### Return type

[**List[RunTemplate]**](RunTemplate.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run templates successfully listed |  -  |
**404** | Solution not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_solution_parameter_groups**
> List[RunTemplateParameterGroup] list_solution_parameter_groups(organization_id, solution_id)

List all solution parameter groups

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run_template_parameter_group import RunTemplateParameterGroup
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier

    try:
        # List all solution parameter groups
        api_response = api_instance.list_solution_parameter_groups(organization_id, solution_id)
        print("The response of SolutionApi->list_solution_parameter_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->list_solution_parameter_groups: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 

### Return type

[**List[RunTemplateParameterGroup]**](RunTemplateParameterGroup.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Parameter groups successfully listed |  -  |
**404** | Solution not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_solution_parameters**
> List[RunTemplateParameter] list_solution_parameters(organization_id, solution_id)

List all solution parameters

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run_template_parameter import RunTemplateParameter
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier

    try:
        # List all solution parameters
        api_response = api_instance.list_solution_parameters(organization_id, solution_id)
        print("The response of SolutionApi->list_solution_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->list_solution_parameters: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 

### Return type

[**List[RunTemplateParameter]**](RunTemplateParameter.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Parameters successfully retrieved |  -  |
**400** | Bad Request |  -  |
**404** | Solution not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_solution_security_users**
> List[str] list_solution_security_users(organization_id, solution_id)

List solution security users

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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier

    try:
        # List solution security users
        api_response = api_instance.list_solution_security_users(organization_id, solution_id)
        print("The response of SolutionApi->list_solution_security_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->list_solution_security_users: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 

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
**200** | Solution security users list successfully retrieved |  -  |
**404** | Solution not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_solutions**
> List[Solution] list_solutions(organization_id, page=page, size=size)

List all Solutions

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.solution import Solution
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    page = 56 # int | Page number to query (first page is at index 0) (optional)
    size = 56 # int | Amount of result by page (optional)

    try:
        # List all Solutions
        api_response = api_instance.list_solutions(organization_id, page=page, size=size)
        print("The response of SolutionApi->list_solutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->list_solutions: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **page** | **int**| Page number to query (first page is at index 0) | [optional] 
 **size** | **int**| Amount of result by page | [optional] 

### Return type

[**List[Solution]**](Solution.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of solutions successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_solution**
> Solution update_solution(organization_id, solution_id, solution_update_request)

Update a solution

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.solution import Solution
from cosmotech_api.models.solution_update_request import SolutionUpdateRequest
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    solution_update_request = cosmotech_api.SolutionUpdateRequest() # SolutionUpdateRequest | The new Solution details. This endpoint can't be used to update security

    try:
        # Update a solution
        api_response = api_instance.update_solution(organization_id, solution_id, solution_update_request)
        print("The response of SolutionApi->update_solution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->update_solution: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **solution_update_request** | [**SolutionUpdateRequest**](SolutionUpdateRequest.md)| The new Solution details. This endpoint can&#39;t be used to update security | 

### Return type

[**Solution**](Solution.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Solution successfully updated |  -  |
**400** | Bad request - Invalid update parameters |  -  |
**404** | Solution not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_solution_access_control**
> SolutionAccessControl update_solution_access_control(organization_id, solution_id, identity_id, solution_role)

Update solution access control

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.solution_access_control import SolutionAccessControl
from cosmotech_api.models.solution_role import SolutionRole
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    identity_id = 'identity_id_example' # str | The User identifier
    solution_role = cosmotech_api.SolutionRole() # SolutionRole | Access control updates

    try:
        # Update solution access control
        api_response = api_instance.update_solution_access_control(organization_id, solution_id, identity_id, solution_role)
        print("The response of SolutionApi->update_solution_access_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->update_solution_access_control: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **identity_id** | **str**| The User identifier | 
 **solution_role** | [**SolutionRole**](SolutionRole.md)| Access control updates | 

### Return type

[**SolutionAccessControl**](SolutionAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Solution access control successfully updated |  -  |
**404** | Solution not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_solution_default_security**
> SolutionSecurity update_solution_default_security(organization_id, solution_id, solution_role)

Update solution default security

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.solution_role import SolutionRole
from cosmotech_api.models.solution_security import SolutionSecurity
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    solution_role = cosmotech_api.SolutionRole() # SolutionRole | This changes the solution default security. The default security is the role assigned to any person not on the Access Control List. If the default security is None, then nobody outside of the ACL can access the solution.

    try:
        # Update solution default security
        api_response = api_instance.update_solution_default_security(organization_id, solution_id, solution_role)
        print("The response of SolutionApi->update_solution_default_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->update_solution_default_security: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **solution_role** | [**SolutionRole**](SolutionRole.md)| This changes the solution default security. The default security is the role assigned to any person not on the Access Control List. If the default security is None, then nobody outside of the ACL can access the solution. | 

### Return type

[**SolutionSecurity**](SolutionSecurity.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Solution default security successfully updated |  -  |
**404** | Solution not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_solution_parameter**
> RunTemplateParameter update_solution_parameter(organization_id, solution_id, parameter_id, run_template_parameter_update_request)

Update solution parameter

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run_template_parameter import RunTemplateParameter
from cosmotech_api.models.run_template_parameter_update_request import RunTemplateParameterUpdateRequest
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    parameter_id = 'parameter_id_example' # str | The solution parameter identifier
    run_template_parameter_update_request = cosmotech_api.RunTemplateParameterUpdateRequest() # RunTemplateParameterUpdateRequest | Parameter to update

    try:
        # Update solution parameter
        api_response = api_instance.update_solution_parameter(organization_id, solution_id, parameter_id, run_template_parameter_update_request)
        print("The response of SolutionApi->update_solution_parameter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->update_solution_parameter: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **parameter_id** | **str**| The solution parameter identifier | 
 **run_template_parameter_update_request** | [**RunTemplateParameterUpdateRequest**](RunTemplateParameterUpdateRequest.md)| Parameter to update | 

### Return type

[**RunTemplateParameter**](RunTemplateParameter.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Parameters successfully updated |  -  |
**400** | Bad request |  -  |
**404** | Solution or parameter not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_solution_parameter_group**
> RunTemplateParameterGroup update_solution_parameter_group(organization_id, solution_id, parameter_group_id, run_template_parameter_group_update_request)

Update a solution parameter group

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run_template_parameter_group import RunTemplateParameterGroup
from cosmotech_api.models.run_template_parameter_group_update_request import RunTemplateParameterGroupUpdateRequest
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    parameter_group_id = 'parameter_group_id_example' # str | The parameter group identifier
    run_template_parameter_group_update_request = cosmotech_api.RunTemplateParameterGroupUpdateRequest() # RunTemplateParameterGroupUpdateRequest | Parameter groups to update

    try:
        # Update a solution parameter group
        api_response = api_instance.update_solution_parameter_group(organization_id, solution_id, parameter_group_id, run_template_parameter_group_update_request)
        print("The response of SolutionApi->update_solution_parameter_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->update_solution_parameter_group: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **parameter_group_id** | **str**| The parameter group identifier | 
 **run_template_parameter_group_update_request** | [**RunTemplateParameterGroupUpdateRequest**](RunTemplateParameterGroupUpdateRequest.md)| Parameter groups to update | 

### Return type

[**RunTemplateParameterGroup**](RunTemplateParameterGroup.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Parameter groups successfully updated |  -  |
**400** | Bad request - Invalid parameter group |  -  |
**404** | Solution or parameter group not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_solution_run_template**
> RunTemplate update_solution_run_template(organization_id, solution_id, run_template_id, run_template_update_request)

Update a specific run template

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.run_template import RunTemplate
from cosmotech_api.models.run_template_update_request import RunTemplateUpdateRequest
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
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    run_template_id = 'run_template_id_example' # str | The Run Template identifier
    run_template_update_request = cosmotech_api.RunTemplateUpdateRequest() # RunTemplateUpdateRequest | Run template updates

    try:
        # Update a specific run template
        api_response = api_instance.update_solution_run_template(organization_id, solution_id, run_template_id, run_template_update_request)
        print("The response of SolutionApi->update_solution_run_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->update_solution_run_template: %s\n" % e)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **run_template_id** | **str**| The Run Template identifier | 
 **run_template_update_request** | [**RunTemplateUpdateRequest**](RunTemplateUpdateRequest.md)| Run template updates | 

### Return type

[**RunTemplate**](RunTemplate.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run template successfully updated |  -  |
**400** | Bad request - Invalid run template updates |  -  |
**404** | Solution or run template not found or insufficient access rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

