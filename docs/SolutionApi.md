# cosmotech_api.SolutionApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_or_replace_parameter_groups**](SolutionApi.md#add_or_replace_parameter_groups) | **POST** /organizations/{organization_id}/solutions/{solution_id}/parameterGroups | Add Parameter Groups. Any item with the same ID will be overwritten
[**add_or_replace_parameters**](SolutionApi.md#add_or_replace_parameters) | **POST** /organizations/{organization_id}/solutions/{solution_id}/parameters | Add Parameters. Any item with the same ID will be overwritten
[**add_or_replace_run_templates**](SolutionApi.md#add_or_replace_run_templates) | **POST** /organizations/{organization_id}/solutions/{solution_id}/runTemplates | Add Run Templates. Any item with the same ID will be overwritten
[**add_solution_access_control**](SolutionApi.md#add_solution_access_control) | **POST** /organizations/{organization_id}/solutions/{solution_id}/security/access | Add a control access to the Solution
[**create_solution**](SolutionApi.md#create_solution) | **POST** /organizations/{organization_id}/solutions | Register a new solution
[**delete_solution**](SolutionApi.md#delete_solution) | **DELETE** /organizations/{organization_id}/solutions/{solution_id} | Delete a solution
[**delete_solution_run_template**](SolutionApi.md#delete_solution_run_template) | **DELETE** /organizations/{organization_id}/solutions/{solution_id}/runTemplates/{run_template_id} | Remove the specified Solution Run Template
[**download_run_template_handler**](SolutionApi.md#download_run_template_handler) | **GET** /organizations/{organization_id}/solutions/{solution_id}/runtemplates/{run_template_id}/handlers/{handler_id}/download | Download a Run Template step handler zip file
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
[**upload_run_template_handler**](SolutionApi.md#upload_run_template_handler) | **POST** /organizations/{organization_id}/solutions/{solution_id}/runtemplates/{run_template_id}/handlers/{handler_id}/upload | Upload a Run Template step handler zip file


# **add_or_replace_parameter_groups**
> [RunTemplateParameterGroup] add_or_replace_parameter_groups(organization_id, solution_id, run_template_parameter_group)

Add Parameter Groups. Any item with the same ID will be overwritten

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.run_template_parameter_group import RunTemplateParameterGroup
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier
    run_template_parameter_group = [
        RunTemplateParameterGroup(
            id="id_example",
            labels=TranslatedLabels(
                key="key_example",
            ),
            is_table=True,
            options={},
            parent_id="parent_id_example",
            parameters=[
                "parameters_example",
            ],
        ),
    ] # [RunTemplateParameterGroup] | the Parameter Groups

    # example passing only required values which don't have defaults set
    try:
        # Add Parameter Groups. Any item with the same ID will be overwritten
        api_response = api_instance.add_or_replace_parameter_groups(organization_id, solution_id, run_template_parameter_group)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SolutionApi->add_or_replace_parameter_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **solution_id** | **str**| the Solution identifier |
 **run_template_parameter_group** | [**[RunTemplateParameterGroup]**](RunTemplateParameterGroup.md)| the Parameter Groups |

### Return type

[**[RunTemplateParameterGroup]**](RunTemplateParameterGroup.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

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
> [RunTemplateParameter] add_or_replace_parameters(organization_id, solution_id, run_template_parameter)

Add Parameters. Any item with the same ID will be overwritten

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.run_template_parameter import RunTemplateParameter
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier
    run_template_parameter = [
        RunTemplateParameter(
            id="id_example",
            labels=TranslatedLabels(
                key="key_example",
            ),
            var_type="var_type_example",
            default_value="default_value_example",
            min_value="min_value_example",
            max_value="max_value_example",
            regex_validation="regex_validation_example",
            options={},
        ),
    ] # [RunTemplateParameter] | the Parameters

    # example passing only required values which don't have defaults set
    try:
        # Add Parameters. Any item with the same ID will be overwritten
        api_response = api_instance.add_or_replace_parameters(organization_id, solution_id, run_template_parameter)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SolutionApi->add_or_replace_parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **solution_id** | **str**| the Solution identifier |
 **run_template_parameter** | [**[RunTemplateParameter]**](RunTemplateParameter.md)| the Parameters |

### Return type

[**[RunTemplateParameter]**](RunTemplateParameter.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

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
> [RunTemplate] add_or_replace_run_templates(organization_id, solution_id, run_template)

Add Run Templates. Any item with the same ID will be overwritten

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.run_template import RunTemplate
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier
    run_template = [
        RunTemplate(
            id="id_example",
            name="name_example",
            labels=TranslatedLabels(
                key="key_example",
            ),
            description="description_example",
            csm_simulation="csm_simulation_example",
            tags=[
                "tags_example",
            ],
            compute_size="compute_size_example",
            run_sizing=RunTemplateResourceSizing(
                requests=ResourceSizeInfo(
                    cpu="cpu_example",
                    memory="memory_example",
                ),
                limits=ResourceSizeInfo(
                    cpu="cpu_example",
                    memory="memory_example",
                ),
            ),
            no_data_ingestion_state=True,
            fetch_datasets=True,
            scenario_data_download_transform=True,
            fetch_scenario_parameters=True,
            apply_parameters=True,
            validate_data=True,
            send_datasets_to_data_warehouse=True,
            send_input_parameters_to_data_warehouse=True,
            pre_run=True,
            run=True,
            post_run=True,
            parameters_json=True,
            parameters_handler_source=RunTemplateStepSource("cloud"),
            dataset_validator_source=RunTemplateStepSource("cloud"),
            pre_run_source=RunTemplateStepSource("cloud"),
            run_source=RunTemplateStepSource("cloud"),
            post_run_source=RunTemplateStepSource("cloud"),
            scenariodata_transform_source=RunTemplateStepSource("cloud"),
            parameter_groups=[
                "parameter_groups_example",
            ],
            stack_steps=True,
            git_repository_url="git_repository_url_example",
            git_branch_name="git_branch_name_example",
            run_template_source_dir="run_template_source_dir_example",
            orchestrator_type=RunTemplateOrchestrator("argoWorkflow"),
            execution_timeout=1,
            delete_historical_data=DeleteHistoricalData(
                enable=True,
                poll_frequency=10000,
                time_out=28800,
            ),
        ),
    ] # [RunTemplate] | the Run Templates

    # example passing only required values which don't have defaults set
    try:
        # Add Run Templates. Any item with the same ID will be overwritten
        api_response = api_instance.add_or_replace_run_templates(organization_id, solution_id, run_template)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SolutionApi->add_or_replace_run_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **solution_id** | **str**| the Solution identifier |
 **run_template** | [**[RunTemplate]**](RunTemplate.md)| the Run Templates |

### Return type

[**[RunTemplate]**](RunTemplate.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

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

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.solution_access_control import SolutionAccessControl
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier
    solution_access_control = SolutionAccessControl(
        id="id_example",
        role="role_example",
    ) # SolutionAccessControl | the new Solution security access to add.

    # example passing only required values which don't have defaults set
    try:
        # Add a control access to the Solution
        api_response = api_instance.add_solution_access_control(organization_id, solution_id, solution_access_control)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
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

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

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

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.solution import Solution
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution = Solution(
        key="key_example",
        name="name_example",
        description="description_example",
        repository="repository_example",
        csm_simulator="csm_simulator_example",
        version="version_example",
        sdk_version="sdk_version_example",
        url="url_example",
        tags=[
            "tags_example",
        ],
        parameters=[
            RunTemplateParameter(
                id="id_example",
                labels=TranslatedLabels(
                    key="key_example",
                ),
                var_type="var_type_example",
                default_value="default_value_example",
                min_value="min_value_example",
                max_value="max_value_example",
                regex_validation="regex_validation_example",
                options={},
            ),
        ],
        parameter_groups=[
            RunTemplateParameterGroup(
                id="id_example",
                labels=TranslatedLabels(
                    key="key_example",
                ),
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
                labels=TranslatedLabels(
                    key="key_example",
                ),
                description="description_example",
                csm_simulation="csm_simulation_example",
                tags=[
                    "tags_example",
                ],
                compute_size="compute_size_example",
                run_sizing=RunTemplateResourceSizing(
                    requests=ResourceSizeInfo(
                        cpu="cpu_example",
                        memory="memory_example",
                    ),
                    limits=ResourceSizeInfo(
                        cpu="cpu_example",
                        memory="memory_example",
                    ),
                ),
                no_data_ingestion_state=True,
                fetch_datasets=True,
                scenario_data_download_transform=True,
                fetch_scenario_parameters=True,
                apply_parameters=True,
                validate_data=True,
                send_datasets_to_data_warehouse=True,
                send_input_parameters_to_data_warehouse=True,
                pre_run=True,
                run=True,
                post_run=True,
                parameters_json=True,
                parameters_handler_source=RunTemplateStepSource("cloud"),
                dataset_validator_source=RunTemplateStepSource("cloud"),
                pre_run_source=RunTemplateStepSource("cloud"),
                run_source=RunTemplateStepSource("cloud"),
                post_run_source=RunTemplateStepSource("cloud"),
                scenariodata_transform_source=RunTemplateStepSource("cloud"),
                parameter_groups=[
                    "parameter_groups_example",
                ],
                stack_steps=True,
                git_repository_url="git_repository_url_example",
                git_branch_name="git_branch_name_example",
                run_template_source_dir="run_template_source_dir_example",
                orchestrator_type=RunTemplateOrchestrator("argoWorkflow"),
                execution_timeout=1,
                delete_historical_data=DeleteHistoricalData(
                    enable=True,
                    poll_frequency=10000,
                    time_out=28800,
                ),
            ),
        ],
        security=None,
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

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete a solution
        api_instance.delete_solution(organization_id, solution_id)
    except cosmotech_api.ApiException as e:
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
**204** | Request succeeded |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_solution_run_template**
> delete_solution_run_template(organization_id, solution_id, run_template_id)

Remove the specified Solution Run Template

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier
    run_template_id = "run_template_id_example" # str | the Run Template identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove the specified Solution Run Template
        api_instance.delete_solution_run_template(organization_id, solution_id, run_template_id)
    except cosmotech_api.ApiException as e:
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

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | the operation succeeded |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_run_template_handler**
> str download_run_template_handler(organization_id, solution_id, run_template_id, handler_id)

Download a Run Template step handler zip file

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.run_template_handler_id import RunTemplateHandlerId
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier
    run_template_id = "run_template_id_example" # str | the Run Template identifier
    handler_id = RunTemplateHandlerId("parameters_handler") # RunTemplateHandlerId | the Handler identifier

    # example passing only required values which don't have defaults set
    try:
        # Download a Run Template step handler zip file
        api_response = api_instance.download_run_template_handler(organization_id, solution_id, run_template_id, handler_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SolutionApi->download_run_template_handler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **solution_id** | **str**| the Solution identifier |
 **run_template_id** | **str**| the Run Template identifier |
 **handler_id** | **RunTemplateHandlerId**| the Handler identifier |

### Return type

**str**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the run template handle file as a resource |  * Content-Disposition - Run Template step handler zip file <br>  |
**404** | the Run Template Handler file specified is unknown or you don&#39;t have access to it |  -  |

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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    page = 1 # int | page number to query (optional)
    size = 1 # int | amount of result by page (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all Solutions
        api_response = api_instance.find_all_solutions(organization_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SolutionApi->find_all_solutions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all Solutions
        api_response = api_instance.find_all_solutions(organization_id, page=page, size=size)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SolutionApi->find_all_solutions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **page** | **int**| page number to query | [optional]
 **size** | **int**| amount of result by page | [optional]

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

# **get_solution_access_control**
> SolutionAccessControl get_solution_access_control(organization_id, solution_id, identity_id)

Get a control access for the Solution

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.solution_access_control import SolutionAccessControl
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier
    identity_id = "identity_id_example" # str | the User identifier

    # example passing only required values which don't have defaults set
    try:
        # Get a control access for the Solution
        api_response = api_instance.get_solution_access_control(organization_id, solution_id, identity_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
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

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

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

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.solution_security import SolutionSecurity
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the Solution security information
        api_response = api_instance.get_solution_security(organization_id, solution_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Solution security |  -  |
**404** | the Solution specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solution_security_users**
> [str] get_solution_security_users(organization_id, solution_id)

Get the Solution security users list

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the Solution security users list
        api_response = api_instance.get_solution_security_users(organization_id, solution_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SolutionApi->get_solution_security_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **solution_id** | **str**| the Solution identifier |

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
**200** | The Solution security users list |  -  |
**404** | the Solution or the User specified is unknown or you don&#39;t have access to them |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_run_templates**
> remove_all_run_templates(organization_id, solution_id)

Remove all Run Templates from the Solution specified

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove all Run Templates from the Solution specified
        api_instance.remove_all_run_templates(organization_id, solution_id)
    except cosmotech_api.ApiException as e:
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

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

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

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove all Parameter Groups from the Solution specified
        api_instance.remove_all_solution_parameter_groups(organization_id, solution_id)
    except cosmotech_api.ApiException as e:
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

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

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

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove all Parameters from the Solution specified
        api_instance.remove_all_solution_parameters(organization_id, solution_id)
    except cosmotech_api.ApiException as e:
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

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

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

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier
    identity_id = "identity_id_example" # str | the User identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove the specified access from the given Organization Solution
        api_instance.remove_solution_access_control(organization_id, solution_id, identity_id)
    except cosmotech_api.ApiException as e:
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

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

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

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.solution_role import SolutionRole
from cosmotech_api.model.solution_security import SolutionSecurity
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier
    solution_role = SolutionRole(
        role="role_example",
    ) # SolutionRole | This change the solution default security. The default security is the role assigned to any person not on the Access Control List. If the default security is None, then nobody outside of the ACL can access the solution.

    # example passing only required values which don't have defaults set
    try:
        # Set the Solution default security
        api_response = api_instance.set_solution_default_security(organization_id, solution_id, solution_role)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
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

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

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

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.solution import Solution
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier
    solution = Solution(
        key="key_example",
        name="name_example",
        description="description_example",
        repository="repository_example",
        csm_simulator="csm_simulator_example",
        version="version_example",
        sdk_version="sdk_version_example",
        url="url_example",
        tags=[
            "tags_example",
        ],
        parameters=[
            RunTemplateParameter(
                id="id_example",
                labels=TranslatedLabels(
                    key="key_example",
                ),
                var_type="var_type_example",
                default_value="default_value_example",
                min_value="min_value_example",
                max_value="max_value_example",
                regex_validation="regex_validation_example",
                options={},
            ),
        ],
        parameter_groups=[
            RunTemplateParameterGroup(
                id="id_example",
                labels=TranslatedLabels(
                    key="key_example",
                ),
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
                labels=TranslatedLabels(
                    key="key_example",
                ),
                description="description_example",
                csm_simulation="csm_simulation_example",
                tags=[
                    "tags_example",
                ],
                compute_size="compute_size_example",
                run_sizing=RunTemplateResourceSizing(
                    requests=ResourceSizeInfo(
                        cpu="cpu_example",
                        memory="memory_example",
                    ),
                    limits=ResourceSizeInfo(
                        cpu="cpu_example",
                        memory="memory_example",
                    ),
                ),
                no_data_ingestion_state=True,
                fetch_datasets=True,
                scenario_data_download_transform=True,
                fetch_scenario_parameters=True,
                apply_parameters=True,
                validate_data=True,
                send_datasets_to_data_warehouse=True,
                send_input_parameters_to_data_warehouse=True,
                pre_run=True,
                run=True,
                post_run=True,
                parameters_json=True,
                parameters_handler_source=RunTemplateStepSource("cloud"),
                dataset_validator_source=RunTemplateStepSource("cloud"),
                pre_run_source=RunTemplateStepSource("cloud"),
                run_source=RunTemplateStepSource("cloud"),
                post_run_source=RunTemplateStepSource("cloud"),
                scenariodata_transform_source=RunTemplateStepSource("cloud"),
                parameter_groups=[
                    "parameter_groups_example",
                ],
                stack_steps=True,
                git_repository_url="git_repository_url_example",
                git_branch_name="git_branch_name_example",
                run_template_source_dir="run_template_source_dir_example",
                orchestrator_type=RunTemplateOrchestrator("argoWorkflow"),
                execution_timeout=1,
                delete_historical_data=DeleteHistoricalData(
                    enable=True,
                    poll_frequency=10000,
                    time_out=28800,
                ),
            ),
        ],
        security=None,
    ) # Solution | the new Solution details. This endpoint can't be used to update security

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
 **solution** | [**Solution**](Solution.md)| the new Solution details. This endpoint can&#39;t be used to update security |

### Return type

[**Solution**](Solution.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

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

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.solution_role import SolutionRole
from cosmotech_api.model.solution_access_control import SolutionAccessControl
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier
    identity_id = "identity_id_example" # str | the User identifier
    solution_role = SolutionRole(
        role="role_example",
    ) # SolutionRole | The new Solution Access Control

    # example passing only required values which don't have defaults set
    try:
        # Update the specified access to User for a Solution
        api_response = api_instance.update_solution_access_control(organization_id, solution_id, identity_id, solution_role)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
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

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

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
> [RunTemplate] update_solution_run_template(organization_id, solution_id, run_template_id, run_template)

Update the specified Solution Run Template

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.run_template import RunTemplate
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier
    run_template_id = "run_template_id_example" # str | the Run Template identifier
    run_template = RunTemplate(
        id="id_example",
        name="name_example",
        labels=TranslatedLabels(
            key="key_example",
        ),
        description="description_example",
        csm_simulation="csm_simulation_example",
        tags=[
            "tags_example",
        ],
        compute_size="compute_size_example",
        run_sizing=RunTemplateResourceSizing(
            requests=ResourceSizeInfo(
                cpu="cpu_example",
                memory="memory_example",
            ),
            limits=ResourceSizeInfo(
                cpu="cpu_example",
                memory="memory_example",
            ),
        ),
        no_data_ingestion_state=True,
        fetch_datasets=True,
        scenario_data_download_transform=True,
        fetch_scenario_parameters=True,
        apply_parameters=True,
        validate_data=True,
        send_datasets_to_data_warehouse=True,
        send_input_parameters_to_data_warehouse=True,
        pre_run=True,
        run=True,
        post_run=True,
        parameters_json=True,
        parameters_handler_source=RunTemplateStepSource("cloud"),
        dataset_validator_source=RunTemplateStepSource("cloud"),
        pre_run_source=RunTemplateStepSource("cloud"),
        run_source=RunTemplateStepSource("cloud"),
        post_run_source=RunTemplateStepSource("cloud"),
        scenariodata_transform_source=RunTemplateStepSource("cloud"),
        parameter_groups=[
            "parameter_groups_example",
        ],
        stack_steps=True,
        git_repository_url="git_repository_url_example",
        git_branch_name="git_branch_name_example",
        run_template_source_dir="run_template_source_dir_example",
        orchestrator_type=RunTemplateOrchestrator("argoWorkflow"),
        execution_timeout=1,
        delete_historical_data=DeleteHistoricalData(
            enable=True,
            poll_frequency=10000,
            time_out=28800,
        ),
    ) # RunTemplate | the Run Templates

    # example passing only required values which don't have defaults set
    try:
        # Update the specified Solution Run Template
        api_response = api_instance.update_solution_run_template(organization_id, solution_id, run_template_id, run_template)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
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

[**[RunTemplate]**](RunTemplate.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

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

# **upload_run_template_handler**
> upload_run_template_handler(organization_id, solution_id, run_template_id, handler_id, body)

Upload a Run Template step handler zip file

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import time
import cosmotech_api
from cosmotech_api.api import solution_api
from cosmotech_api.model.run_template_handler_id import RunTemplateHandlerId
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
    api_instance = solution_api.SolutionApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    solution_id = "solution_id_example" # str | the Solution identifier
    run_template_id = "run_template_id_example" # str | the Run Template identifier
    handler_id = RunTemplateHandlerId("parameters_handler") # RunTemplateHandlerId | the Handler identifier
    body = open('/path/to/file', 'rb') # file_type | 
    overwrite = False # bool | whether to overwrite any existing handler resource (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Upload a Run Template step handler zip file
        api_instance.upload_run_template_handler(organization_id, solution_id, run_template_id, handler_id, body)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SolutionApi->upload_run_template_handler: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload a Run Template step handler zip file
        api_instance.upload_run_template_handler(organization_id, solution_id, run_template_id, handler_id, body, overwrite=overwrite)
    except cosmotech_api.ApiException as e:
        print("Exception when calling SolutionApi->upload_run_template_handler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **solution_id** | **str**| the Solution identifier |
 **run_template_id** | **str**| the Run Template identifier |
 **handler_id** | **RunTemplateHandlerId**| the Handler identifier |
 **body** | **file_type**|  |
 **overwrite** | **bool**| whether to overwrite any existing handler resource | [optional] if omitted the server will use the default value of False

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
**201** | zip file uploaded |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

