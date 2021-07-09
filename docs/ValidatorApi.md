# cosmotech_api.ValidatorApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_validator**](ValidatorApi.md#create_validator) | **POST** /organizations/{organization_id}/datasets/validators | Register a new validator
[**create_validator_run**](ValidatorApi.md#create_validator_run) | **POST** /organizations/{organization_id}/datasets/validators/{validator_id}/history | Register a new validator run
[**delete_validator**](ValidatorApi.md#delete_validator) | **DELETE** /organizations/{organization_id}/datasets/validators/{validator_id} | Delete a validator
[**delete_validator_run**](ValidatorApi.md#delete_validator_run) | **DELETE** /organizations/{organization_id}/datasets/validators/{validator_id}/history/{validatorrun_id} | Delete a validator run
[**find_all_validator_runs**](ValidatorApi.md#find_all_validator_runs) | **GET** /organizations/{organization_id}/datasets/validators/{validator_id}/history | List all Validator Runs
[**find_all_validators**](ValidatorApi.md#find_all_validators) | **GET** /organizations/{organization_id}/datasets/validators | List all Validators
[**find_validator_by_id**](ValidatorApi.md#find_validator_by_id) | **GET** /organizations/{organization_id}/datasets/validators/{validator_id} | Get the details of a validator
[**find_validator_run_by_id**](ValidatorApi.md#find_validator_run_by_id) | **GET** /organizations/{organization_id}/datasets/validators/{validator_id}/history/{validatorrun_id} | Get the details of a validator run
[**run_validator**](ValidatorApi.md#run_validator) | **POST** /organizations/{organization_id}/datasets/validators/{validator_id}/run | Run a Validator


# **create_validator**
> Validator create_validator(organization_id, validator)

Register a new validator

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import validator_api
from cosmotech_api.model.validator import Validator
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
    api_instance = validator_api.ValidatorApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    validator = Validator(
        name="name_example",
        description="description_example",
        repository="repository_example",
        version="version_example",
        url="url_example",
        tags=[
            "tags_example",
        ],
    ) # Validator | the Validator to create

    # example passing only required values which don't have defaults set
    try:
        # Register a new validator
        api_response = api_instance.create_validator(organization_id, validator)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ValidatorApi->create_validator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **validator** | [**Validator**](Validator.md)| the Validator to create |

### Return type

[**Validator**](Validator.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the validator details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_validator_run**
> ValidatorRun create_validator_run(organization_id, validator_id, validator_run)

Register a new validator run

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import validator_api
from cosmotech_api.model.validator_run import ValidatorRun
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
    api_instance = validator_api.ValidatorApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    validator_id = "validator_id_example" # str | the ValidatorRun identifier
    validator_run = ValidatorRun(
        dataset_id="dataset_id_example",
    ) # ValidatorRun | the Validator Run to create

    # example passing only required values which don't have defaults set
    try:
        # Register a new validator run
        api_response = api_instance.create_validator_run(organization_id, validator_id, validator_run)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ValidatorApi->create_validator_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **validator_id** | **str**| the ValidatorRun identifier |
 **validator_run** | [**ValidatorRun**](ValidatorRun.md)| the Validator Run to create |

### Return type

[**ValidatorRun**](ValidatorRun.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the validator run details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_validator**
> delete_validator(organization_id, validator_id)

Delete a validator

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import validator_api
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
    api_instance = validator_api.ValidatorApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    validator_id = "validator_id_example" # str | the Validator identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete a validator
        api_instance.delete_validator(organization_id, validator_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ValidatorApi->delete_validator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **validator_id** | **str**| the Validator identifier |

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
**404** | the Validator specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_validator_run**
> delete_validator_run(organization_id, validator_id, validatorrun_id)

Delete a validator run

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import validator_api
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
    api_instance = validator_api.ValidatorApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    validator_id = "validator_id_example" # str | the Validator identifier
    validatorrun_id = "validatorrun_id_example" # str | the Validator Run identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete a validator run
        api_instance.delete_validator_run(organization_id, validator_id, validatorrun_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ValidatorApi->delete_validator_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **validator_id** | **str**| the Validator identifier |
 **validatorrun_id** | **str**| the Validator Run identifier |

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
**404** | the ValidatorRun specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_validator_runs**
> [ValidatorRun] find_all_validator_runs(organization_id, validator_id)

List all Validator Runs

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import validator_api
from cosmotech_api.model.validator_run import ValidatorRun
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
    api_instance = validator_api.ValidatorApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    validator_id = "validator_id_example" # str | the ValidatorRun identifier

    # example passing only required values which don't have defaults set
    try:
        # List all Validator Runs
        api_response = api_instance.find_all_validator_runs(organization_id, validator_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ValidatorApi->find_all_validator_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **validator_id** | **str**| the ValidatorRun identifier |

### Return type

[**[ValidatorRun]**](ValidatorRun.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the validator run details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_validators**
> [Validator] find_all_validators(organization_id)

List all Validators

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import validator_api
from cosmotech_api.model.validator import Validator
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
    api_instance = validator_api.ValidatorApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier

    # example passing only required values which don't have defaults set
    try:
        # List all Validators
        api_response = api_instance.find_all_validators(organization_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ValidatorApi->find_all_validators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |

### Return type

[**[Validator]**](Validator.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the validator details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_validator_by_id**
> Validator find_validator_by_id(organization_id, validator_id)

Get the details of a validator

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import validator_api
from cosmotech_api.model.validator import Validator
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
    api_instance = validator_api.ValidatorApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    validator_id = "validator_id_example" # str | the Validator identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a validator
        api_response = api_instance.find_validator_by_id(organization_id, validator_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ValidatorApi->find_validator_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **validator_id** | **str**| the Validator identifier |

### Return type

[**Validator**](Validator.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Validator details |  -  |
**404** | the Validator specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_validator_run_by_id**
> ValidatorRun find_validator_run_by_id(organization_id, validator_id, validatorrun_id)

Get the details of a validator run

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import validator_api
from cosmotech_api.model.validator_run import ValidatorRun
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
    api_instance = validator_api.ValidatorApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    validator_id = "validator_id_example" # str | the Validator identifier
    validatorrun_id = "validatorrun_id_example" # str | the Validator Run identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a validator run
        api_response = api_instance.find_validator_run_by_id(organization_id, validator_id, validatorrun_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ValidatorApi->find_validator_run_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **validator_id** | **str**| the Validator identifier |
 **validatorrun_id** | **str**| the Validator Run identifier |

### Return type

[**ValidatorRun**](ValidatorRun.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Validator Run details |  -  |
**404** | the ValidatorRun specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_validator**
> ValidatorRun run_validator(organization_id, validator_id, validator_run)

Run a Validator

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import validator_api
from cosmotech_api.model.validator_run import ValidatorRun
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
    api_instance = validator_api.ValidatorApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    validator_id = "validator_id_example" # str | the ValidatorRun identifier
    validator_run = ValidatorRun(
        dataset_id="dataset_id_example",
    ) # ValidatorRun | the Validator to run

    # example passing only required values which don't have defaults set
    try:
        # Run a Validator
        api_response = api_instance.run_validator(organization_id, validator_id, validator_run)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling ValidatorApi->run_validator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **validator_id** | **str**| the ValidatorRun identifier |
 **validator_run** | [**ValidatorRun**](ValidatorRun.md)| the Validator to run |

### Return type

[**ValidatorRun**](ValidatorRun.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the validator run details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

