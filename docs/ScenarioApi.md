# cosmotech_api.ScenarioApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_or_replace_scenario_parameter_values**](ScenarioApi.md#add_or_replace_scenario_parameter_values) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/parameterValues | Add (or replace) Parameter Values for the Scenario specified
[**add_scenario_access_control**](ScenarioApi.md#add_scenario_access_control) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/security/access | Add a control access to the Scenario
[**compare_scenarios**](ScenarioApi.md#compare_scenarios) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/compare/{compared_scenario_id} | Compare the Scenario with another one and returns the difference for parameters values
[**create_scenario**](ScenarioApi.md#create_scenario) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios | Create a new Scenario
[**delete_all_scenarios**](ScenarioApi.md#delete_all_scenarios) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios | Delete all Scenarios of the Workspace
[**delete_scenario**](ScenarioApi.md#delete_scenario) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id} | Delete a scenario
[**download_scenario_data**](ScenarioApi.md#download_scenario_data) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/downloads | Download Scenario data
[**find_all_scenarios**](ScenarioApi.md#find_all_scenarios) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios | List all Scenarios
[**find_all_scenarios_by_validation_status**](ScenarioApi.md#find_all_scenarios_by_validation_status) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/{validationStatus} | List all Scenarios by validation status
[**find_scenario_by_id**](ScenarioApi.md#find_scenario_by_id) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id} | Get the details of an scenario
[**get_scenario_access_control**](ScenarioApi.md#get_scenario_access_control) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/security/access/{identity_id} | Get a control access for the Scenario
[**get_scenario_data_download_job_info**](ScenarioApi.md#get_scenario_data_download_job_info) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/downloads/{download_id} | Get Scenario data download URL
[**get_scenario_permissions**](ScenarioApi.md#get_scenario_permissions) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/permissions/{role} | Get the Scenario permission by given role
[**get_scenario_security**](ScenarioApi.md#get_scenario_security) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/security | Get the Scenario security information
[**get_scenario_security_users**](ScenarioApi.md#get_scenario_security_users) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/security/users | Get the Scenario security users list
[**get_scenario_validation_status_by_id**](ScenarioApi.md#get_scenario_validation_status_by_id) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/ValidationStatus | Get the validation status of an scenario
[**get_scenarios_tree**](ScenarioApi.md#get_scenarios_tree) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/tree | Get the Scenarios Tree
[**remove_all_scenario_parameter_values**](ScenarioApi.md#remove_all_scenario_parameter_values) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/parameterValues | Remove all Parameter Values from the Scenario specified
[**remove_scenario_access_control**](ScenarioApi.md#remove_scenario_access_control) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/security/access/{identity_id} | Remove the specified access from the given Organization Scenario
[**set_scenario_default_security**](ScenarioApi.md#set_scenario_default_security) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/security/default | Set the Scenario default security
[**update_scenario**](ScenarioApi.md#update_scenario) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id} | Update a scenario
[**update_scenario_access_control**](ScenarioApi.md#update_scenario_access_control) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/security/access/{identity_id} | Update the specified access to User for a Scenario


# **add_or_replace_scenario_parameter_values**
> List[ScenarioRunTemplateParameterValue] add_or_replace_scenario_parameter_values(organization_id, workspace_id, scenario_id, scenario_run_template_parameter_value)

Add (or replace) Parameter Values for the Scenario specified

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario_run_template_parameter_value import ScenarioRunTemplateParameterValue
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier
    scenario_run_template_parameter_value = [cosmotech_api.ScenarioRunTemplateParameterValue()] # List[ScenarioRunTemplateParameterValue] | the Parameter Value to add. Any Parameter Value with the same ID is overwritten

    try:
        # Add (or replace) Parameter Values for the Scenario specified
        api_response = api_instance.add_or_replace_scenario_parameter_values(organization_id, workspace_id, scenario_id, scenario_run_template_parameter_value)
        print("The response of ScenarioApi->add_or_replace_scenario_parameter_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->add_or_replace_scenario_parameter_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 
 **scenario_run_template_parameter_value** | [**List[ScenarioRunTemplateParameterValue]**](ScenarioRunTemplateParameterValue.md)| the Parameter Value to add. Any Parameter Value with the same ID is overwritten | 

### Return type

[**List[ScenarioRunTemplateParameterValue]**](ScenarioRunTemplateParameterValue.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the Parameter values |  -  |
**400** | Bad request |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_scenario_access_control**
> ScenarioAccessControl add_scenario_access_control(organization_id, workspace_id, scenario_id, scenario_access_control)

Add a control access to the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario_access_control import ScenarioAccessControl
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier
    scenario_access_control = cosmotech_api.ScenarioAccessControl() # ScenarioAccessControl | the new Scenario security access to add.

    try:
        # Add a control access to the Scenario
        api_response = api_instance.add_scenario_access_control(organization_id, workspace_id, scenario_id, scenario_access_control)
        print("The response of ScenarioApi->add_scenario_access_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->add_scenario_access_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 
 **scenario_access_control** | [**ScenarioAccessControl**](ScenarioAccessControl.md)| the new Scenario security access to add. | 

### Return type

[**ScenarioAccessControl**](ScenarioAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Scenario access |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compare_scenarios**
> ScenarioComparisonResult compare_scenarios(organization_id, workspace_id, scenario_id, compared_scenario_id)

Compare the Scenario with another one and returns the difference for parameters values

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario_comparison_result import ScenarioComparisonResult
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier
    compared_scenario_id = 'compared_scenario_id_example' # str | the Scenario identifier to compare to

    try:
        # Compare the Scenario with another one and returns the difference for parameters values
        api_response = api_instance.compare_scenarios(organization_id, workspace_id, scenario_id, compared_scenario_id)
        print("The response of ScenarioApi->compare_scenarios:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->compare_scenarios: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 
 **compared_scenario_id** | **str**| the Scenario identifier to compare to | 

### Return type

[**ScenarioComparisonResult**](ScenarioComparisonResult.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the comparison result for parameters values |  -  |
**404** | one of the Scenarios specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_scenario**
> Scenario create_scenario(organization_id, workspace_id, scenario)

Create a new Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario import Scenario
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario = cosmotech_api.Scenario() # Scenario | the Scenario to create

    try:
        # Create a new Scenario
        api_response = api_instance.create_scenario(organization_id, workspace_id, scenario)
        print("The response of ScenarioApi->create_scenario:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->create_scenario: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario** | [**Scenario**](Scenario.md)| the Scenario to create | 

### Return type

[**Scenario**](Scenario.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the scenario details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_scenarios**
> delete_all_scenarios(organization_id, workspace_id)

Delete all Scenarios of the Workspace

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier

    try:
        # Delete all Scenarios of the Workspace
        api_instance.delete_all_scenarios(organization_id, workspace_id)
    except Exception as e:
        print("Exception when calling ScenarioApi->delete_all_scenarios: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 

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
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scenario**
> delete_scenario(organization_id, workspace_id, scenario_id)

Delete a scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier

    try:
        # Delete a scenario
        api_instance.delete_scenario(organization_id, workspace_id, scenario_id)
    except Exception as e:
        print("Exception when calling ScenarioApi->delete_scenario: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 

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
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_scenario_data**
> ScenarioDataDownloadJob download_scenario_data(organization_id, workspace_id, scenario_id)

Download Scenario data

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario_data_download_job import ScenarioDataDownloadJob
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier

    try:
        # Download Scenario data
        api_response = api_instance.download_scenario_data(organization_id, workspace_id, scenario_id)
        print("The response of ScenarioApi->download_scenario_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->download_scenario_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 

### Return type

[**ScenarioDataDownloadJob**](ScenarioDataDownloadJob.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the Scenario Data response, once acknowledged. |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_scenarios**
> List[Scenario] find_all_scenarios(organization_id, workspace_id, page=page, size=size)

List all Scenarios

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario import Scenario
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    page = 56 # int | page number to query (optional)
    size = 56 # int | amount of result by page (optional)

    try:
        # List all Scenarios
        api_response = api_instance.find_all_scenarios(organization_id, workspace_id, page=page, size=size)
        print("The response of ScenarioApi->find_all_scenarios:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->find_all_scenarios: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **page** | **int**| page number to query | [optional] 
 **size** | **int**| amount of result by page | [optional] 

### Return type

[**List[Scenario]**](Scenario.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the list of Scenarios |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_scenarios_by_validation_status**
> List[Scenario] find_all_scenarios_by_validation_status(organization_id, workspace_id, validation_status, page=page, size=size)

List all Scenarios by validation status

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario import Scenario
from cosmotech_api.models.scenario_validation_status import ScenarioValidationStatus
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    validation_status = cosmotech_api.ScenarioValidationStatus() # ScenarioValidationStatus | the Scenario Validation Status
    page = 56 # int | page number to query (optional)
    size = 56 # int | amount of result by page (optional)

    try:
        # List all Scenarios by validation status
        api_response = api_instance.find_all_scenarios_by_validation_status(organization_id, workspace_id, validation_status, page=page, size=size)
        print("The response of ScenarioApi->find_all_scenarios_by_validation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->find_all_scenarios_by_validation_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **validation_status** | [**ScenarioValidationStatus**](.md)| the Scenario Validation Status | 
 **page** | **int**| page number to query | [optional] 
 **size** | **int**| amount of result by page | [optional] 

### Return type

[**List[Scenario]**](Scenario.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the list of Scenarios by a given validation status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_scenario_by_id**
> Scenario find_scenario_by_id(organization_id, workspace_id, scenario_id)

Get the details of an scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario import Scenario
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier

    try:
        # Get the details of an scenario
        api_response = api_instance.find_scenario_by_id(organization_id, workspace_id, scenario_id)
        print("The response of ScenarioApi->find_scenario_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->find_scenario_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 

### Return type

[**Scenario**](Scenario.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Scenario details |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_access_control**
> ScenarioAccessControl get_scenario_access_control(organization_id, workspace_id, scenario_id, identity_id)

Get a control access for the Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario_access_control import ScenarioAccessControl
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier
    identity_id = 'identity_id_example' # str | the User identifier

    try:
        # Get a control access for the Scenario
        api_response = api_instance.get_scenario_access_control(organization_id, workspace_id, scenario_id, identity_id)
        print("The response of ScenarioApi->get_scenario_access_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->get_scenario_access_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 
 **identity_id** | **str**| the User identifier | 

### Return type

[**ScenarioAccessControl**](ScenarioAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Scenario access |  -  |
**404** | the Scenario or user specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_data_download_job_info**
> ScenarioDataDownloadInfo get_scenario_data_download_job_info(organization_id, workspace_id, scenario_id, download_id)

Get Scenario data download URL

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario_data_download_info import ScenarioDataDownloadInfo
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier
    download_id = 'download_id_example' # str | the Scenario Download identifier

    try:
        # Get Scenario data download URL
        api_response = api_instance.get_scenario_data_download_job_info(organization_id, workspace_id, scenario_id, download_id)
        print("The response of ScenarioApi->get_scenario_data_download_job_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->get_scenario_data_download_job_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 
 **download_id** | **str**| the Scenario Download identifier | 

### Return type

[**ScenarioDataDownloadInfo**](ScenarioDataDownloadInfo.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the scenario data download URL. |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_permissions**
> List[str] get_scenario_permissions(organization_id, workspace_id, scenario_id, role)

Get the Scenario permission by given role

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier
    role = 'role_example' # str | the Role

    try:
        # Get the Scenario permission by given role
        api_response = api_instance.get_scenario_permissions(organization_id, workspace_id, scenario_id, role)
        print("The response of ScenarioApi->get_scenario_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->get_scenario_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 
 **role** | **str**| the Role | 

### Return type

**List[str]**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Scenarios security permission list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_security**
> ScenarioSecurity get_scenario_security(organization_id, workspace_id, scenario_id)

Get the Scenario security information

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario_security import ScenarioSecurity
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier

    try:
        # Get the Scenario security information
        api_response = api_instance.get_scenario_security(organization_id, workspace_id, scenario_id)
        print("The response of ScenarioApi->get_scenario_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->get_scenario_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 

### Return type

[**ScenarioSecurity**](ScenarioSecurity.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Scenario security |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_security_users**
> List[str] get_scenario_security_users(organization_id, workspace_id, scenario_id)

Get the Scenario security users list

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier

    try:
        # Get the Scenario security users list
        api_response = api_instance.get_scenario_security_users(organization_id, workspace_id, scenario_id)
        print("The response of ScenarioApi->get_scenario_security_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->get_scenario_security_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 

### Return type

**List[str]**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Scenario security users list |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_validation_status_by_id**
> ScenarioValidationStatus get_scenario_validation_status_by_id(organization_id, workspace_id, scenario_id)

Get the validation status of an scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario_validation_status import ScenarioValidationStatus
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier

    try:
        # Get the validation status of an scenario
        api_response = api_instance.get_scenario_validation_status_by_id(organization_id, workspace_id, scenario_id)
        print("The response of ScenarioApi->get_scenario_validation_status_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->get_scenario_validation_status_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 

### Return type

[**ScenarioValidationStatus**](ScenarioValidationStatus.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Scenario validation status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenarios_tree**
> List[Scenario] get_scenarios_tree(organization_id, workspace_id)

Get the Scenarios Tree

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario import Scenario
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier

    try:
        # Get the Scenarios Tree
        api_response = api_instance.get_scenarios_tree(organization_id, workspace_id)
        print("The response of ScenarioApi->get_scenarios_tree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->get_scenarios_tree: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 

### Return type

[**List[Scenario]**](Scenario.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the scenario tree |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_scenario_parameter_values**
> remove_all_scenario_parameter_values(organization_id, workspace_id, scenario_id)

Remove all Parameter Values from the Scenario specified

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier

    try:
        # Remove all Parameter Values from the Scenario specified
        api_instance.remove_all_scenario_parameter_values(organization_id, workspace_id, scenario_id)
    except Exception as e:
        print("Exception when calling ScenarioApi->remove_all_scenario_parameter_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 

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
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_scenario_access_control**
> remove_scenario_access_control(organization_id, workspace_id, scenario_id, identity_id)

Remove the specified access from the given Organization Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier
    identity_id = 'identity_id_example' # str | the User identifier

    try:
        # Remove the specified access from the given Organization Scenario
        api_instance.remove_scenario_access_control(organization_id, workspace_id, scenario_id, identity_id)
    except Exception as e:
        print("Exception when calling ScenarioApi->remove_scenario_access_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 
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
**404** | the Scenario or the user specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_scenario_default_security**
> ScenarioSecurity set_scenario_default_security(organization_id, workspace_id, scenario_id, scenario_role)

Set the Scenario default security

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario_role import ScenarioRole
from cosmotech_api.models.scenario_security import ScenarioSecurity
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier
    scenario_role = cosmotech_api.ScenarioRole() # ScenarioRole | This change the scenario default security. The default security is the role assigned to any person not on the Access Control List. If the default security is None, then nobody outside of the ACL can access the scenario.

    try:
        # Set the Scenario default security
        api_response = api_instance.set_scenario_default_security(organization_id, workspace_id, scenario_id, scenario_role)
        print("The response of ScenarioApi->set_scenario_default_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->set_scenario_default_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 
 **scenario_role** | [**ScenarioRole**](ScenarioRole.md)| This change the scenario default security. The default security is the role assigned to any person not on the Access Control List. If the default security is None, then nobody outside of the ACL can access the scenario. | 

### Return type

[**ScenarioSecurity**](ScenarioSecurity.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Scenario default visibility |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scenario**
> Scenario update_scenario(organization_id, workspace_id, scenario_id, scenario)

Update a scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario import Scenario
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier
    scenario = cosmotech_api.Scenario() # Scenario | The new Scenario details. This endpoint can't be used to update :   - id   - ownerId   - datasetList   - solutionId   - runTemplateId   - parametersValues   - security 

    try:
        # Update a scenario
        api_response = api_instance.update_scenario(organization_id, workspace_id, scenario_id, scenario)
        print("The response of ScenarioApi->update_scenario:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->update_scenario: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 
 **scenario** | [**Scenario**](Scenario.md)| The new Scenario details. This endpoint can&#39;t be used to update :   - id   - ownerId   - datasetList   - solutionId   - runTemplateId   - parametersValues   - security  | 

### Return type

[**Scenario**](Scenario.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the scenario details |  -  |
**400** | Bad request |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scenario_access_control**
> ScenarioAccessControl update_scenario_access_control(organization_id, workspace_id, scenario_id, identity_id, scenario_role)

Update the specified access to User for a Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.scenario_access_control import ScenarioAccessControl
from cosmotech_api.models.scenario_role import ScenarioRole
from cosmotech_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cosmotech_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cosmotech_api.ScenarioApi(api_client)
    organization_id = 'organization_id_example' # str | the Organization identifier
    workspace_id = 'workspace_id_example' # str | the Workspace identifier
    scenario_id = 'scenario_id_example' # str | the Scenario identifier
    identity_id = 'identity_id_example' # str | the User identifier
    scenario_role = cosmotech_api.ScenarioRole() # ScenarioRole | The new Scenario Access Control

    try:
        # Update the specified access to User for a Scenario
        api_response = api_instance.update_scenario_access_control(organization_id, workspace_id, scenario_id, identity_id, scenario_role)
        print("The response of ScenarioApi->update_scenario_access_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScenarioApi->update_scenario_access_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier | 
 **workspace_id** | **str**| the Workspace identifier | 
 **scenario_id** | **str**| the Scenario identifier | 
 **identity_id** | **str**| the User identifier | 
 **scenario_role** | [**ScenarioRole**](ScenarioRole.md)| The new Scenario Access Control | 

### Return type

[**ScenarioAccessControl**](ScenarioAccessControl.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Scenario access |  -  |
**404** | The Organization specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

