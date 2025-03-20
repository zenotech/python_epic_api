# epiccore.JobauthApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobauth_list**](JobauthApi.md#jobauth_list) | **GET** /jobauth/ | 
[**jobauth_read**](JobauthApi.md#jobauth_read) | **GET** /jobauth/{job}/ | 
[**jobauth_update**](JobauthApi.md#jobauth_update) | **PUT** /jobauth/{job}/ | 


# **jobauth_list**
> JobauthList200Response jobauth_list(limit=limit, offset=offset)



### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.jobauth_list200_response import JobauthList200Response
from epiccore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://epic.zenotech.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = epiccore.Configuration(
    host = "https://epic.zenotech.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = epiccore.JobauthApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.jobauth_list(limit=limit, offset=offset)
        print("The response of JobauthApi->jobauth_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobauthApi->jobauth_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**JobauthList200Response**](JobauthList200Response.md)

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



Get the authorisation status for job with ID {id}

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.job_auth_status import JobAuthStatus
from epiccore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://epic.zenotech.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = epiccore.Configuration(
    host = "https://epic.zenotech.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = epiccore.JobauthApi(api_client)
    job = 'job_example' # str | A unique value identifying this job authorisation.

    try:
        api_response = api_instance.jobauth_read(job)
        print("The response of JobauthApi->jobauth_read:\n")
        pprint(api_response)
    except Exception as e:
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



Update the authorisation status for job  with ID {id}

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.job_auth_status import JobAuthStatus
from epiccore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://epic.zenotech.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = epiccore.Configuration(
    host = "https://epic.zenotech.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = epiccore.JobauthApi(api_client)
    job = 'job_example' # str | A unique value identifying this job authorisation.
    data = epiccore.JobAuthStatus() # JobAuthStatus | 

    try:
        api_response = api_instance.jobauth_update(job, data)
        print("The response of JobauthApi->jobauth_update:\n")
        pprint(api_response)
    except Exception as e:
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

