# cosmotech_api.ScenariorunresultApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_scenario_run_result**](ScenariorunresultApi.md#get_scenario_run_result) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/scenarioruns/{scenariorun_id}/probes/{probe_id} | Get a ScenarioRunResult in the Organization
[**send_scenario_run_result**](ScenariorunresultApi.md#send_scenario_run_result) | **POST** /organizations/{organization_id}/workspaces/{workspace_id}/scenarios/{scenario_id}/scenarioruns/{scenariorun_id}/probes/{probe_id} | Create a new ScenarioRunResult in the Organization


# **get_scenario_run_result**
> ScenarioRunResult get_scenario_run_result(organization_id, workspace_id, scenario_id, scenariorun_id, probe_id)

Get a ScenarioRunResult in the Organization

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorunresult_api
from cosmotech_api.model.scenario_run_result import ScenarioRunResult
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
    api_instance = scenariorunresult_api.ScenariorunresultApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier
    scenariorun_id = "scenariorun_id_example" # str | the ScenarioRun identifier
    probe_id = "probe_id_example" # str | the Probe identifier

    # example passing only required values which don't have defaults set
    try:
        # Get a ScenarioRunResult in the Organization
        api_response = api_instance.get_scenario_run_result(organization_id, workspace_id, scenario_id, scenariorun_id, probe_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunresultApi->get_scenario_run_result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |
 **scenariorun_id** | **str**| the ScenarioRun identifier |
 **probe_id** | **str**| the Probe identifier |

### Return type

[**ScenarioRunResult**](ScenarioRunResult.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Organization details |  -  |
**404** | the ScenarioRunResult specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_scenario_run_result**
> ScenarioRunResult send_scenario_run_result(organization_id, workspace_id, scenario_id, scenariorun_id, probe_id, request_body)

Create a new ScenarioRunResult in the Organization

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import scenariorunresult_api
from cosmotech_api.model.scenario_run_result import ScenarioRunResult
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
    api_instance = scenariorunresult_api.ScenariorunresultApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier
    scenario_id = "scenario_id_example" # str | the Scenario identifier
    scenariorun_id = "scenariorun_id_example" # str | the ScenarioRun identifier
    probe_id = "probe_id_example" # str | the Probe identifier
    request_body = {
        "key": "key_example",
    } # {str: (str,)} | the ScenarioRunResult to register

    # example passing only required values which don't have defaults set
    try:
        # Create a new ScenarioRunResult in the Organization
        api_response = api_instance.send_scenario_run_result(organization_id, workspace_id, scenario_id, scenariorun_id, probe_id, request_body)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ScenariorunresultApi->send_scenario_run_result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |
 **scenario_id** | **str**| the Scenario identifier |
 **scenariorun_id** | **str**| the ScenarioRun identifier |
 **probe_id** | **str**| the Probe identifier |
 **request_body** | **{str: (str,)}**| the ScenarioRunResult to register |

### Return type

[**ScenarioRunResult**](ScenarioRunResult.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Organization details |  -  |
**400** | the ScenarioRunResult specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

