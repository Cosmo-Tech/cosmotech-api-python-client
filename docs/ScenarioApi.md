# cosmotech_api.ScenarioApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_or_replace_scenario_parameter_values**](ScenarioApi.md#add_or_replace_scenario_parameter_values) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/parameterValues | Add (or replace) Parameter Values for the Scenario specified
[**add_or_replace_users_in_scenario**](ScenarioApi.md#add_or_replace_users_in_scenario) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/users | Add (or replace) users in the Scenario specified
[**compare_scenarios**](ScenarioApi.md#compare_scenarios) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/compare/{compared_scenario_id} | Compare the Scenario with another one and returns the difference for parameters values
[**create_scenario**](ScenarioApi.md#create_scenario) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios | Create a new Scenario
[**delete_all_scenarios**](ScenarioApi.md#delete_all_scenarios) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios | Delete all Scenarios of the Workspace
[**delete_scenario**](ScenarioApi.md#delete_scenario) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id} | Delete a scenario
[**find_all_scenarios**](ScenarioApi.md#find_all_scenarios) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios | List all Scenarios
[**find_scenario_by_id**](ScenarioApi.md#find_scenario_by_id) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id} | Get the details of an scenario
[**get_scenarios_tree**](ScenarioApi.md#get_scenarios_tree) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/tree | Get the Scenarios Tree
[**remove_all_scenario_parameter_values**](ScenarioApi.md#remove_all_scenario_parameter_values) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/parameterValues | Remove all Parameter Values from the Scenario specified
[**remove_all_users_of_scenario**](ScenarioApi.md#remove_all_users_of_scenario) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/users | Remove all users from the Scenario specified
[**remove_user_from_scenario**](ScenarioApi.md#remove_user_from_scenario) | **DELETE** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/users/{user_id} | Remove the specified user from the given Scenario
[**update_scenario**](ScenarioApi.md#update_scenario) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id} | Update a scenario


# **add_or_replace_scenario_parameter_values**
> [ScenarioRunTemplateParameterValue] add_or_replace_scenario_parameter_values(organization_id, workspace_id, scenario_id, scenario_run_template_parameter_value)

Add (or replace) Parameter Values for the Scenario specified

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenario_api
from cosmotech_api.model.scenario_run_template_parameter_value import ScenarioRunTemplateParameterValue
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
    api_instance = scenario_api.ScenarioApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier
    scenario_run_template_parameter_value = [
        ScenarioRunTemplateParameterValue(
            parameter_id="parameter_id_example",
            value="value_example",
            is_inherited=True,
        ),
    ] # [ScenarioRunTemplateParameterValue] | the Parameter Value to add. Any Parameter Value with the same ID is overwritten

    # example passing only required values which don't have defaults set
    try:
        # Add (or replace) Parameter Values for the Scenario specified
        api_response = api_instance.add_or_replace_scenario_parameter_values(organization_id, workspace_id, scenario_id, scenario_run_template_parameter_value)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenarioApi->add_or_replace_scenario_parameter_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |
 **scenario_run_template_parameter_value** | [**[ScenarioRunTemplateParameterValue]**](ScenarioRunTemplateParameterValue.md)| the Parameter Value to add. Any Parameter Value with the same ID is overwritten |

### Return type

[**[ScenarioRunTemplateParameterValue]**](ScenarioRunTemplateParameterValue.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the Parameter values |  -  |
**400** | Bad request |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_or_replace_users_in_scenario**
> [ScenarioUser] add_or_replace_users_in_scenario(organization_id, workspace_id, scenario_id, scenario_user)

Add (or replace) users in the Scenario specified

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenario_api
from cosmotech_api.model.scenario_user import ScenarioUser
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
    api_instance = scenario_api.ScenarioApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier
    scenario_user = [
        ScenarioUser(
            id="id_example",
            roles=[
                "Viewer",
            ],
        ),
    ] # [ScenarioUser] | the Users to add. Any User with the same ID is overwritten

    # example passing only required values which don't have defaults set
    try:
        # Add (or replace) users in the Scenario specified
        api_response = api_instance.add_or_replace_users_in_scenario(organization_id, workspace_id, scenario_id, scenario_user)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenarioApi->add_or_replace_users_in_scenario: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |
 **scenario_user** | [**[ScenarioUser]**](ScenarioUser.md)| the Users to add. Any User with the same ID is overwritten |

### Return type

[**[ScenarioUser]**](ScenarioUser.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the Scenario Users |  -  |
**400** | Bad request |  -  |
**404** | the Scenario specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compare_scenarios**
> ScenarioComparisonResult compare_scenarios(organization_id, workspace_id, scenario_id, compared_scenario_id)

Compare the Scenario with another one and returns the difference for parameters values

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenario_api
from cosmotech_api.model.scenario_comparison_result import ScenarioComparisonResult
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
    api_instance = scenario_api.ScenarioApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier
    compared_scenario_id = "compared_scenario_id_example" # str | the Scenario identifier to compare to

    # example passing only required values which don't have defaults set
    try:
        # Compare the Scenario with another one and returns the difference for parameters values
        api_response = api_instance.compare_scenarios(organization_id, workspace_id, scenario_id, compared_scenario_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
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
import time
import cosmotech_api
from cosmotech_api.api import scenario_api
from cosmotech_api.model.scenario import Scenario
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
    api_instance = scenario_api.ScenarioApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario = Scenario(
        name="name_example",
        description="description_example",
        tags=[
            "tags_example",
        ],
        parent_id="parent_id_example",
        run_template_id="run_template_id_example",
        users=[
            ScenarioUser(
                id="id_example",
                roles=[
                    "Viewer",
                ],
            ),
        ],
        dataset_list=[
            "dataset_list_example",
        ],
        parameters_values=[
            ScenarioRunTemplateParameterValue(
                parameter_id="parameter_id_example",
                value="value_example",
                is_inherited=True,
            ),
        ],
        last_run=ScenarioLastRun(
            scenario_run_id="scenario_run_id_example",
            csm_simulation_run="csm_simulation_run_example",
            workflow_id="workflow_id_example",
            workflow_name="workflow_name_example",
        ),
    ) # Scenario | the Scenario to create

    # example passing only required values which don't have defaults set
    try:
        # Create a new Scenario
        api_response = api_instance.create_scenario(organization_id, workspace_id, scenario)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
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
import time
import cosmotech_api
from cosmotech_api.api import scenario_api
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
    api_instance = scenario_api.ScenarioApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete all Scenarios of the Workspace
        api_instance.delete_all_scenarios(organization_id, workspace_id)
    except cosmotech_api.ApiException as e:
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
import time
import cosmotech_api
from cosmotech_api.api import scenario_api
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
    api_instance = scenario_api.ScenarioApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier
    wait_relationship_propagation = False # bool | whether to wait until child scenarios are effectively updated (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete a scenario
        api_instance.delete_scenario(organization_id, workspace_id, scenario_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenarioApi->delete_scenario: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a scenario
        api_instance.delete_scenario(organization_id, workspace_id, scenario_id, wait_relationship_propagation=wait_relationship_propagation)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenarioApi->delete_scenario: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |
 **wait_relationship_propagation** | **bool**| whether to wait until child scenarios are effectively updated | [optional] if omitted the server will use the default value of False

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

# **find_all_scenarios**
> [Scenario] find_all_scenarios(organization_id, workspace_id)

List all Scenarios

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenario_api
from cosmotech_api.model.scenario import Scenario
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
    api_instance = scenario_api.ScenarioApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier

    # example passing only required values which don't have defaults set
    try:
        # List all Scenarios
        api_response = api_instance.find_all_scenarios(organization_id, workspace_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenarioApi->find_all_scenarios: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |

### Return type

[**[Scenario]**](Scenario.md)

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

# **find_scenario_by_id**
> Scenario find_scenario_by_id(organization_id, workspace_id, scenario_id)

Get the details of an scenario

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenario_api
from cosmotech_api.model.scenario import Scenario
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
    api_instance = scenario_api.ScenarioApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of an scenario
        api_response = api_instance.find_scenario_by_id(organization_id, workspace_id, scenario_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
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

# **get_scenarios_tree**
> [Scenario] get_scenarios_tree(organization_id, workspace_id)

Get the Scenarios Tree

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenario_api
from cosmotech_api.model.scenario import Scenario
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
    api_instance = scenario_api.ScenarioApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the Scenarios Tree
        api_response = api_instance.get_scenarios_tree(organization_id, workspace_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenarioApi->get_scenarios_tree: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |

### Return type

[**[Scenario]**](Scenario.md)

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
import time
import cosmotech_api
from cosmotech_api.api import scenario_api
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
    api_instance = scenario_api.ScenarioApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove all Parameter Values from the Scenario specified
        api_instance.remove_all_scenario_parameter_values(organization_id, workspace_id, scenario_id)
    except cosmotech_api.ApiException as e:
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

# **remove_all_users_of_scenario**
> remove_all_users_of_scenario(organization_id, workspace_id, scenario_id)

Remove all users from the Scenario specified

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenario_api
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
    api_instance = scenario_api.ScenarioApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove all users from the Scenario specified
        api_instance.remove_all_users_of_scenario(organization_id, workspace_id, scenario_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenarioApi->remove_all_users_of_scenario: %s\n" % e)
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

# **remove_user_from_scenario**
> remove_user_from_scenario(organization_id, workspace_id, scenario_id, user_id)

Remove the specified user from the given Scenario

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenario_api
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
    api_instance = scenario_api.ScenarioApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier
    user_id = "user_id_example" # str | the User identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove the specified user from the given Scenario
        api_instance.remove_user_from_scenario(organization_id, workspace_id, scenario_id, user_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenarioApi->remove_user_from_scenario: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |
 **user_id** | **str**| the User identifier |

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
**404** | the Scenario or the User specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scenario**
> Scenario update_scenario(organization_id, workspace_id, scenario_id, scenario)

Update a scenario

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import scenario_api
from cosmotech_api.model.scenario import Scenario
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
    api_instance = scenario_api.ScenarioApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier
    scenario = Scenario(
        name="name_example",
        description="description_example",
        tags=[
            "tags_example",
        ],
        parent_id="parent_id_example",
        run_template_id="run_template_id_example",
        users=[
            ScenarioUser(
                id="id_example",
                roles=[
                    "Viewer",
                ],
            ),
        ],
        dataset_list=[
            "dataset_list_example",
        ],
        parameters_values=[
            ScenarioRunTemplateParameterValue(
                parameter_id="parameter_id_example",
                value="value_example",
                is_inherited=True,
            ),
        ],
        last_run=ScenarioLastRun(
            scenario_run_id="scenario_run_id_example",
            csm_simulation_run="csm_simulation_run_example",
            workflow_id="workflow_id_example",
            workflow_name="workflow_name_example",
        ),
    ) # Scenario | the new Scenario details.

    # example passing only required values which don't have defaults set
    try:
        # Update a scenario
        api_response = api_instance.update_scenario(organization_id, workspace_id, scenario_id, scenario)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenarioApi->update_scenario: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |
 **scenario** | [**Scenario**](Scenario.md)| the new Scenario details. |

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

