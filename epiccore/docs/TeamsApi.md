# epiccore.TeamsApi

All URIs are relative to *https://epic-qa.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_memberships_list**](TeamsApi.md#teams_memberships_list) | **GET** /teams/memberships/ | 
[**teams_memberships_read**](TeamsApi.md#teams_memberships_read) | **GET** /teams/memberships/{id}/ | 
[**teams_userteams_list**](TeamsApi.md#teams_userteams_list) | **GET** /teams/userteams/ | 
[**teams_userteams_read**](TeamsApi.md#teams_userteams_read) | **GET** /teams/userteams/{id}/ | 


# **teams_memberships_list**
> InlineResponse20012 teams_memberships_list(limit=limit, offset=offset)



List the team memberships for your user account

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import epiccore
from epiccore.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://epic-qa.zenotech.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = epiccore.Configuration(
    host = "https://epic-qa.zenotech.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = epiccore.Configuration(
    host = "https://epic-qa.zenotech.com/api/v2",
    api_key = {
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = epiccore.TeamsApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.teams_memberships_list(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->teams_memberships_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_memberships_read**
> TeamMembership teams_memberships_read(id)



See the details for a team membership. Memberships of all teams you are a of member of will be visable.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import epiccore
from epiccore.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://epic-qa.zenotech.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = epiccore.Configuration(
    host = "https://epic-qa.zenotech.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = epiccore.Configuration(
    host = "https://epic-qa.zenotech.com/api/v2",
    api_key = {
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = epiccore.TeamsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.teams_memberships_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->teams_memberships_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TeamMembership**](TeamMembership.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_userteams_list**
> InlineResponse20013 teams_userteams_list(limit=limit, offset=offset)



List the teams you are a member of.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import epiccore
from epiccore.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://epic-qa.zenotech.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = epiccore.Configuration(
    host = "https://epic-qa.zenotech.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = epiccore.Configuration(
    host = "https://epic-qa.zenotech.com/api/v2",
    api_key = {
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = epiccore.TeamsApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.teams_userteams_list(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->teams_userteams_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_userteams_read**
> TeamDetails teams_userteams_read(id)



See the details for a team. You must be a member of the team to see the details.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import epiccore
from epiccore.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://epic-qa.zenotech.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = epiccore.Configuration(
    host = "https://epic-qa.zenotech.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = epiccore.Configuration(
    host = "https://epic-qa.zenotech.com/api/v2",
    api_key = {
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = epiccore.TeamsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.teams_userteams_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->teams_userteams_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TeamDetails**](TeamDetails.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

