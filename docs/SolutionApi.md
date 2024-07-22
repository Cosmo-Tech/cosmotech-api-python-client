# cosmotech_api.SolutionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_or_replace_parameter_groups**](SolutionApi.md#add_or_replace_parameter_groups) | **POST** /organizations/{organization_id}/solutions/{solution_id}/parameterGroups | Add Parameter Groups. Any item with the same ID will be overwritten
[**add_or_replace_parameters**](SolutionApi.md#add_or_replace_parameters) | **POST** /organizations/{organization_id}/solutions/{solution_id}/parameters | Add Parameters. Any item with the same ID will be overwritten
[**add_or_replace_run_templates**](SolutionApi.md#add_or_replace_run_templates) | **POST** /organizations/{organization_id}/solutions/{solution_id}/runTemplates | Add Run Templates. Any item with the same ID will be overwritten
[**add_solution_access_control**](SolutionApi.md#add_solution_access_control) | **POST** /organizations/{organization_id}/solutions/{solution_id}/security/access | Add a control access to the Solution
[**create_solution**](SolutionApi.md#create_solution) | **POST** /organizations/{organization_id}/solutions | Register a new solution
[**delete_solution**](SolutionApi.md#delete_solution) | **DELETE** /organizations/{organization_id}/solutions/{solution_id} | Delete a solution
[**delete_solution_run_template**](SolutionApi.md#delete_solution_run_template) | **DELETE** /organizations/{organization_id}/solutions/{solution_id}/runTemplates/{run_template_id} | Remove the specified Solution Run Template
[**find_all_solutions**](SolutionApi.md#find_all_solutions) | **GET** /organizations/{organization_id}/solutions | List all Solutions
[**find_solution_by_id**](SolutionApi.md#find_solution_by_id) | **GET** /organizations/{organization_id}/solutions/{solution_id} | Get the details of a solution
[**get_solution_access_control**](SolutionApi.md#get_solution_access_control) | **GET** /organizations/{organization_id}/solutions/{solution_id}/security/access/{identity_id} | Get a control access for the Solution
[**get_solution_security**](SolutionApi.md#get_solution_security) | **GET** /organizations/{organization_id}/solutions/{solution_id}/security | Get the Solution security information
[**get_solution_security_users**](SolutionApi.md#get_solution_security_users) | **GET** /organizations/{organization_id}/solutions/{solution_id}/security/users | Get the Solution security users list
[**remove_all_run_templates**](SolutionApi.md#remove_all_run_templates) | **DELETE** /organizations/{organization_id}/solutions/{solution_id}/runTemplates | Remove all Run Templates from the Solution specified
[**remove_all_solution_parameter_groups**](SolutionApi.md#remove_all_solution_parameter_groups) | **DELETE** /organizations/{organization_id}/solutions/{solution_id}/parameterGroups | Remove all Parameter Groups from the Solution specified
[**remove_all_solution_parameters**](SolutionApi.md#remove_all_solution_parameters) | **DELETE** /organizations/{organization_id}/solutions/{solution_id}/parameters | Remove all Parameters from the Solution specified
[**remove_solution_access_control**](SolutionApi.md#remove_solution_access_control) | **DELETE** /organizations/{organization_id}/solutions/{solution_id}/security/access/{identity_id} | Remove the specified access from the given Organization Solution
[**set_solution_default_security**](SolutionApi.md#set_solution_default_security) | **POST** /organizations/{organization_id}/solutions/{solution_id}/security/default | Set the Solution default security
[**update_solution**](SolutionApi.md#update_solution) | **PATCH** /organizations/{organization_id}/solutions/{solution_id} | Update a solution
[**update_solution_access_control**](SolutionApi.md#update_solution_access_control) | **PATCH** /organizations/{organization_id}/solutions/{solution_id}/security/access/{identity_id} | Update the specified access to User for a Solution
[**update_solution_run_template**](SolutionApi.md#update_solution_run_template) | **PATCH** /organizations/{organization_id}/solutions/{solution_id}/runTemplates/{run_template_id} | Update the specified Solution Run Template


# **add_or_replace_parameter_groups**
> List[RunTemplateParameterGroup] add_or_replace_parameter_groups(organization_id, solution_id, run_template_parameter_group)

Add Parameter Groups. Any item with the same ID will be overwritten

### Example


```python
import cosmotech_api
from cosmotech_api.models.run_template_parameter_group import RunTemplateParameterGroup
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    run_template_parameter_group = [cosmotech_api.RunTemplateParameterGroup()] # List[RunTemplateParameterGroup] | the Parameter Groups

    try:
        # Add Parameter Groups. Any item with the same ID will be overwritten
        api_response = api_instance.add_or_replace_parameter_groups(organization_id, solution_id, run_template_parameter_group)
        print("The response of SolutionApi->add_or_replace_parameter_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->add_or_replace_parameter_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **run_template_parameter_group** | [**List[RunTemplateParameterGroup]**](RunTemplateParameterGroup.md)| the Parameter Groups | 

### Return type

[**List[RunTemplateParameterGroup]**](RunTemplateParameterGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the Parameter Groups |  -  |
**400** | Bad request |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_or_replace_parameters**
> List[RunTemplateParameter] add_or_replace_parameters(organization_id, solution_id, run_template_parameter)

Add Parameters. Any item with the same ID will be overwritten

### Example


```python
import cosmotech_api
from cosmotech_api.models.run_template_parameter import RunTemplateParameter
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    run_template_parameter = [cosmotech_api.RunTemplateParameter()] # List[RunTemplateParameter] | the Parameters

    try:
        # Add Parameters. Any item with the same ID will be overwritten
        api_response = api_instance.add_or_replace_parameters(organization_id, solution_id, run_template_parameter)
        print("The response of SolutionApi->add_or_replace_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->add_or_replace_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **run_template_parameter** | [**List[RunTemplateParameter]**](RunTemplateParameter.md)| the Parameters | 

### Return type

[**List[RunTemplateParameter]**](RunTemplateParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the Parameters |  -  |
**400** | Bad request |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_or_replace_run_templates**
> List[RunTemplate] add_or_replace_run_templates(organization_id, solution_id, run_template)

Add Run Templates. Any item with the same ID will be overwritten

### Example


```python
import cosmotech_api
from cosmotech_api.models.run_template import RunTemplate
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    run_template = [cosmotech_api.RunTemplate()] # List[RunTemplate] | the Run Templates

    try:
        # Add Run Templates. Any item with the same ID will be overwritten
        api_response = api_instance.add_or_replace_run_templates(organization_id, solution_id, run_template)
        print("The response of SolutionApi->add_or_replace_run_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->add_or_replace_run_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **run_template** | [**List[RunTemplate]**](RunTemplate.md)| the Run Templates | 

### Return type

[**List[RunTemplate]**](RunTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the Parameters |  -  |
**400** | Bad request |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_solution_access_control**
> SolutionAccessControl add_solution_access_control(organization_id, solution_id, solution_access_control)

Add a control access to the Solution

### Example


```python
import cosmotech_api
from cosmotech_api.models.solution_access_control import SolutionAccessControl
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    solution_access_control = cosmotech_api.SolutionAccessControl() # SolutionAccessControl | the new Solution security access to add.

    try:
        # Add a control access to the Solution
        api_response = api_instance.add_solution_access_control(organization_id, solution_id, solution_access_control)
        print("The response of SolutionApi->add_solution_access_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->add_solution_access_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **solution_access_control** | [**SolutionAccessControl**](SolutionAccessControl.md)| the new Solution security access to add. | 

### Return type

[**SolutionAccessControl**](SolutionAccessControl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Solution access |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_solution**
> Solution create_solution(organization_id, solution)

Register a new solution

### Example


```python
import cosmotech_api
from cosmotech_api.models.solution import Solution
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution = cosmotech_api.Solution() # Solution | the Solution to create

    try:
        # Register a new solution
        api_response = api_instance.create_solution(organization_id, solution)
        print("The response of SolutionApi->create_solution:\n")
        pprint(api_response)
    except Exception as e:
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the solution details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_solution**
> delete_solution(organization_id, solution_id)

Delete a solution

### Example


```python
import cosmotech_api
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request succeeded |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_solution_run_template**
> delete_solution_run_template(organization_id, solution_id, run_template_id)

Remove the specified Solution Run Template

### Example


```python
import cosmotech_api
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    run_template_id = 'run_template_id_example' # str | the Run Template identifier

    try:
        # Remove the specified Solution Run Template
        api_instance.delete_solution_run_template(organization_id, solution_id, run_template_id)
    except Exception as e:
        print("Exception when calling SolutionApi->delete_solution_run_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **run_template_id** | **str**| the Run Template identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | the operation succeeded |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_solutions**
> List[Solution] find_all_solutions(organization_id, page=page, size=size)

List all Solutions

### Example


```python
import cosmotech_api
from cosmotech_api.models.solution import Solution
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    page = 56 # int | page number to query (optional)
    size = 56 # int | amount of result by page (optional)

    try:
        # List all Solutions
        api_response = api_instance.find_all_solutions(organization_id, page=page, size=size)
        print("The response of SolutionApi->find_all_solutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->find_all_solutions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **page** | **int**| page number to query | [optional] 
 **size** | **int**| amount of result by page | [optional] 

### Return type

[**List[Solution]**](Solution.md)

### Authorization

No authorization required

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


```python
import cosmotech_api
from cosmotech_api.models.solution import Solution
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier

    try:
        # Get the details of a solution
        api_response = api_instance.find_solution_by_id(organization_id, solution_id)
        print("The response of SolutionApi->find_solution_by_id:\n")
        pprint(api_response)
    except Exception as e:
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Solution details |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solution_access_control**
> SolutionAccessControl get_solution_access_control(organization_id, solution_id, identity_id)

Get a control access for the Solution

### Example


```python
import cosmotech_api
from cosmotech_api.models.solution_access_control import SolutionAccessControl
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    identity_id = 'identity_id_example' # str | the User identifier

    try:
        # Get a control access for the Solution
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
 **identity_id** | **str**| the User identifier | 

### Return type

[**SolutionAccessControl**](SolutionAccessControl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Solution access |  -  |
**404** | The Solution or user specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solution_security**
> SolutionSecurity get_solution_security(organization_id, solution_id)

Get the Solution security information

### Example


```python
import cosmotech_api
from cosmotech_api.models.solution_security import SolutionSecurity
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier

    try:
        # Get the Solution security information
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Solution security |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solution_security_users**
> List[str] get_solution_security_users(organization_id, solution_id)

Get the Solution security users list

### Example


```python
import cosmotech_api
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier

    try:
        # Get the Solution security users list
        api_response = api_instance.get_solution_security_users(organization_id, solution_id)
        print("The response of SolutionApi->get_solution_security_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->get_solution_security_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Solution security users list |  -  |
**404** | the Solution or the User specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_run_templates**
> remove_all_run_templates(organization_id, solution_id)

Remove all Run Templates from the Solution specified

### Example


```python
import cosmotech_api
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier

    try:
        # Remove all Run Templates from the Solution specified
        api_instance.remove_all_run_templates(organization_id, solution_id)
    except Exception as e:
        print("Exception when calling SolutionApi->remove_all_run_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | the operation succeeded |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_solution_parameter_groups**
> remove_all_solution_parameter_groups(organization_id, solution_id)

Remove all Parameter Groups from the Solution specified

### Example


```python
import cosmotech_api
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier

    try:
        # Remove all Parameter Groups from the Solution specified
        api_instance.remove_all_solution_parameter_groups(organization_id, solution_id)
    except Exception as e:
        print("Exception when calling SolutionApi->remove_all_solution_parameter_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | the operation succeeded |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_solution_parameters**
> remove_all_solution_parameters(organization_id, solution_id)

Remove all Parameters from the Solution specified

### Example


```python
import cosmotech_api
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier

    try:
        # Remove all Parameters from the Solution specified
        api_instance.remove_all_solution_parameters(organization_id, solution_id)
    except Exception as e:
        print("Exception when calling SolutionApi->remove_all_solution_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | the operation succeeded |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_solution_access_control**
> remove_solution_access_control(organization_id, solution_id, identity_id)

Remove the specified access from the given Organization Solution

### Example


```python
import cosmotech_api
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    identity_id = 'identity_id_example' # str | the User identifier

    try:
        # Remove the specified access from the given Organization Solution
        api_instance.remove_solution_access_control(organization_id, solution_id, identity_id)
    except Exception as e:
        print("Exception when calling SolutionApi->remove_solution_access_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **identity_id** | **str**| the User identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request succeeded |  -  |
**404** | The Solution or the user specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_solution_default_security**
> SolutionSecurity set_solution_default_security(organization_id, solution_id, solution_role)

Set the Solution default security

### Example


```python
import cosmotech_api
from cosmotech_api.models.solution_role import SolutionRole
from cosmotech_api.models.solution_security import SolutionSecurity
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    solution_role = cosmotech_api.SolutionRole() # SolutionRole | This change the solution default security. The default security is the role assigned to any person not on the Access Control List. If the default security is None, then nobody outside of the ACL can access the solution.

    try:
        # Set the Solution default security
        api_response = api_instance.set_solution_default_security(organization_id, solution_id, solution_role)
        print("The response of SolutionApi->set_solution_default_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolutionApi->set_solution_default_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **solution_id** | **str**| the Solution identifier | 
 **solution_role** | [**SolutionRole**](SolutionRole.md)| This change the solution default security. The default security is the role assigned to any person not on the Access Control List. If the default security is None, then nobody outside of the ACL can access the solution. | 

### Return type

[**SolutionSecurity**](SolutionSecurity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Solution default visibility |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_solution**
> Solution update_solution(organization_id, solution_id, solution)

Update a solution

### Example


```python
import cosmotech_api
from cosmotech_api.models.solution import Solution
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    solution = cosmotech_api.Solution() # Solution | the new Solution details. This endpoint can't be used to update security

    try:
        # Update a solution
        api_response = api_instance.update_solution(organization_id, solution_id, solution)
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
 **solution** | [**Solution**](Solution.md)| the new Solution details. This endpoint can&#39;t be used to update security | 

### Return type

[**Solution**](Solution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the solution details |  -  |
**400** | Bad request |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_solution_access_control**
> SolutionAccessControl update_solution_access_control(organization_id, solution_id, identity_id, solution_role)

Update the specified access to User for a Solution

### Example


```python
import cosmotech_api
from cosmotech_api.models.solution_access_control import SolutionAccessControl
from cosmotech_api.models.solution_role import SolutionRole
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    identity_id = 'identity_id_example' # str | the User identifier
    solution_role = cosmotech_api.SolutionRole() # SolutionRole | The new Solution Access Control

    try:
        # Update the specified access to User for a Solution
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
 **identity_id** | **str**| the User identifier | 
 **solution_role** | [**SolutionRole**](SolutionRole.md)| The new Solution Access Control | 

### Return type

[**SolutionAccessControl**](SolutionAccessControl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Solution access |  -  |
**404** | The Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_solution_run_template**
> List[RunTemplate] update_solution_run_template(organization_id, solution_id, run_template_id, run_template)

Update the specified Solution Run Template

### Example


```python
import cosmotech_api
from cosmotech_api.models.run_template import RunTemplate
from cosmotech_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cosmotech_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.SolutionApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    solution_id = 'solution_id_example' # str | the Solution identifier
    run_template_id = 'run_template_id_example' # str | the Run Template identifier
    run_template = cosmotech_api.RunTemplate() # RunTemplate | the Run Templates

    try:
        # Update the specified Solution Run Template
        api_response = api_instance.update_solution_run_template(organization_id, solution_id, run_template_id, run_template)
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
 **run_template_id** | **str**| the Run Template identifier | 
 **run_template** | [**RunTemplate**](RunTemplate.md)| the Run Templates | 

### Return type

[**List[RunTemplate]**](RunTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Parameters |  -  |
**400** | Bad request |  -  |
**404** | the Solution or Run Template specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

