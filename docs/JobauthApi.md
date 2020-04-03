# epic_api.JobauthApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobauth_list**](JobauthApi.md#jobauth_list) | **GET** /jobauth/ | 
[**jobauth_read**](JobauthApi.md#jobauth_read) | **GET** /jobauth/{job}/ | 
[**jobauth_update**](JobauthApi.md#jobauth_update) | **PUT** /jobauth/{job}/ | 


# **jobauth_list**
> InlineResponse2004 jobauth_list(limit=limit, offset=offset)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import epic_api
from epic_api.rest import ApiException
from pprint import pprint
configuration = epic_api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://epic.zenotech.com/api/v2
configuration.host = "https://epic.zenotech.com/api/v2"

# Enter a context with an instance of the API client
with epic_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = epic_api.JobauthApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.jobauth_list(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobauthApi->jobauth_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **jobauth_read**
> JobAuthStatus jobauth_read(job)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import epic_api
from epic_api.rest import ApiException
from pprint import pprint
configuration = epic_api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://epic.zenotech.com/api/v2
configuration.host = "https://epic.zenotech.com/api/v2"

# Enter a context with an instance of the API client
with epic_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = epic_api.JobauthApi(api_client)
    job = 'job_example' # str | A unique value identifying this job authorisation.

    try:
        api_response = api_instance.jobauth_read(job)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobauthApi->jobauth_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | **str**| A unique value identifying this job authorisation. | 

### Return type

[**JobAuthStatus**](JobAuthStatus.md)

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

# **jobauth_update**
> JobAuthStatus jobauth_update(job, data)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import epic_api
from epic_api.rest import ApiException
from pprint import pprint
configuration = epic_api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://epic.zenotech.com/api/v2
configuration.host = "https://epic.zenotech.com/api/v2"

# Enter a context with an instance of the API client
with epic_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = epic_api.JobauthApi(api_client)
    job = 'job_example' # str | A unique value identifying this job authorisation.
data = epic_api.JobAuthStatus() # JobAuthStatus | 

    try:
        api_response = api_instance.jobauth_update(job, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobauthApi->jobauth_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | **str**| A unique value identifying this job authorisation. | 
 **data** | [**JobAuthStatus**](JobAuthStatus.md)|  | 

### Return type

[**JobAuthStatus**](JobAuthStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

