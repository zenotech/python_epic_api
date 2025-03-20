# epiccore.JobrefreshApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobrefresh_create**](JobrefreshApi.md#jobrefresh_create) | **POST** /jobrefresh/ | 
[**jobrefresh_read**](JobrefreshApi.md#jobrefresh_read) | **GET** /jobrefresh/{id}/ | 


# **jobrefresh_create**
> JobstepResponseRequest jobrefresh_create(data)



Create a request to refresh the logs for a running job step with ID {job_step}.

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.jobstep_response_request import JobstepResponseRequest
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
    api_instance = epiccore.JobrefreshApi(api_client)
    data = epiccore.JobstepResponseRequest() # JobstepResponseRequest | 

    try:
        api_response = api_instance.jobrefresh_create(data)
        print("The response of JobrefreshApi->jobrefresh_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobrefreshApi->jobrefresh_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**JobstepResponseRequest**](JobstepResponseRequest.md)|  | 

### Return type

[**JobstepResponseRequest**](JobstepResponseRequest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobrefresh_read**
> JobstepResponseRequest jobrefresh_read(id)



Check the progress of a refresh request

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.jobstep_response_request import JobstepResponseRequest
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
    api_instance = epiccore.JobrefreshApi(api_client)
    id = 56 # int | A unique integer value identifying this jobstep response request.

    try:
        api_response = api_instance.jobrefresh_read(id)
        print("The response of JobrefreshApi->jobrefresh_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobrefreshApi->jobrefresh_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jobstep response request. | 

### Return type

[**JobstepResponseRequest**](JobstepResponseRequest.md)

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

