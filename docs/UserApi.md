# cosmotech_api.UserApi

All URIs are relative to *https://dev.api.cosmotech.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_user**](UserApi.md#authorize_user) | **GET** /oauth2/authorize | Authorize an User with OAuth2. Delegated to configured OAuth2 service
[**find_all_users**](UserApi.md#find_all_users) | **GET** /users | List all Users
[**find_user_by_id**](UserApi.md#find_user_by_id) | **GET** /users/{user_id} | Get the details of an user
[**get_current_user**](UserApi.md#get_current_user) | **GET** /users/me | Get the details of the logged-in User
[**get_organization_current_user**](UserApi.md#get_organization_current_user) | **GET** /organizations/{organization_id}/me | Get the details of a logged-in User with roles for an Organization
[**get_workspace_current_user**](UserApi.md#get_workspace_current_user) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/me | Get the details of the logged-in user with roles for a Workspace
[**register_user**](UserApi.md#register_user) | **POST** /users | Register a new user
[**test_platform**](UserApi.md#test_platform) | **GET** /test | test platform API call
[**unregister_user**](UserApi.md#unregister_user) | **DELETE** /users/{user_id} | Unregister an user
[**update_user**](UserApi.md#update_user) | **PATCH** /users/{user_id} | Update a User


# **authorize_user**
> authorize_user()

Authorize an User with OAuth2. Delegated to configured OAuth2 service

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import user_api
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Authorize an User with OAuth2. Delegated to configured OAuth2 service
        api_instance.authorize_user()
    except cosmotech_api.ApiException as e:
        print("Exception when calling UserApi->authorize_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**302** | Redirection response |  * Location -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_users**
> [User] find_all_users()

List all Users

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import user_api
from cosmotech_api.model.user import User
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all Users
        api_response = api_instance.find_all_users()
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling UserApi->find_all_users: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[User]**](User.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the user details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_user_by_id**
> User find_user_by_id(user_id)

Get the details of an user

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import user_api
from cosmotech_api.model.user import User
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
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | the User identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of an user
        api_response = api_instance.find_user_by_id(user_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling UserApi->find_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the User identifier |

### Return type

[**User**](User.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the User details |  -  |
**404** | the User specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> User get_current_user()

Get the details of the logged-in User

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import user_api
from cosmotech_api.model.user import User
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the details of the logged-in User
        api_response = api_instance.get_current_user()
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling UserApi->get_current_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the User details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_current_user**
> User get_organization_current_user(organization_id)

Get the details of a logged-in User with roles for an Organization

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import user_api
from cosmotech_api.model.user import User
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
    api_instance = user_api.UserApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of a logged-in User with roles for an Organization
        api_response = api_instance.get_organization_current_user(organization_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling UserApi->get_organization_current_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |

### Return type

[**User**](User.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the User details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_current_user**
> User get_workspace_current_user(organization_id, workspace_id)

Get the details of the logged-in user with roles for a Workspace

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import user_api
from cosmotech_api.model.user import User
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
    api_instance = user_api.UserApi(api_client)
    organization_id = "organization_id_example" # str | the Organization identifier
    workspace_id = "workspace_id_example" # str | the Workspace identifier

    # example passing only required values which don't have defaults set
    try:
        # Get the details of the logged-in user with roles for a Workspace
        api_response = api_instance.get_workspace_current_user(organization_id, workspace_id)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling UserApi->get_workspace_current_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| the Organization identifier |
 **workspace_id** | **str**| the Workspace identifier |

### Return type

[**User**](User.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the User details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user**
> User register_user(user)

Register a new user

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import user_api
from cosmotech_api.model.user import User
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
    api_instance = user_api.UserApi(api_client)
    user = User(
        name="name_example",
        platform_roles=[
            "Admin",
        ],
    ) # User | the User to register

    # example passing only required values which don't have defaults set
    try:
        # Register a new user
        api_response = api_instance.register_user(user)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling UserApi->register_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| the User to register |

### Return type

[**User**](User.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the user details |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_platform**
> str test_platform()

test platform API call

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import user_api
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # test platform API call
        api_response = api_instance.test_platform()
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling UserApi->test_platform: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | test string |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_user**
> unregister_user(user_id)

Unregister an user

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | the User identifier

    # example passing only required values which don't have defaults set
    try:
        # Unregister an user
        api_instance.unregister_user(user_id)
    except cosmotech_api.ApiException as e:
        print("Exception when calling UserApi->unregister_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**404** | the User specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(user_id, user)

Update a User

### Example

* OAuth Authentication (oAuth2AuthCode):
```python
import time
import cosmotech_api
from cosmotech_api.api import user_api
from cosmotech_api.model.user import User
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
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | the User identifier
    user = User(
        name="name_example",
        platform_roles=[
            "Admin",
        ],
    ) # User | the new User details. Organization membership is handled via the /organizations endpoint.

    # example passing only required values which don't have defaults set
    try:
        # Update a User
        api_response = api_instance.update_user(user_id, user)
        pprint(api_response)
    except cosmotech_api.ApiException as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the User identifier |
 **user** | [**User**](User.md)| the new User details. Organization membership is handled via the /organizations endpoint. |

### Return type

[**User**](User.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the user details |  -  |
**400** | Bad request |  -  |
**404** | the User specified is unknown or you don&#39;t have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

