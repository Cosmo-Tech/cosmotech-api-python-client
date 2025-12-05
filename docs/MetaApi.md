# cosmotech_api.MetaApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**about**](MetaApi.md#about) | **GET** /about | Get various information about the API


# **about**
> AboutInfo about()

Get various information about the API

### Example

* OAuth Authentication (oAuth2AuthCode):

```python
import cosmotech_api
from cosmotech_api.models.about_info import AboutInfo
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
    api_instance = cosmotech_api.MetaApi(api_client)

    try:
        # Get various information about the API
        api_response = api_instance.about()
        print("The response of MetaApi->about:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->about: %s\n" % e)
```


### Parameters

This endpoint does not need any parameter.

### Return type

[**AboutInfo**](AboutInfo.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API information details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

