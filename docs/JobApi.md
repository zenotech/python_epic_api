# epic_api.JobApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_auth_read**](JobApi.md#job_auth_read) | **GET** /job/{id}/auth/ | 
[**job_auth_update**](JobApi.md#job_auth_update) | **PUT** /job/{id}/auth/ | 
[**job_create**](JobApi.md#job_create) | **POST** /job/ | 
[**job_list**](JobApi.md#job_list) | **GET** /job/ | 
[**job_quote**](JobApi.md#job_quote) | **POST** /job/quote/ | 
[**job_read**](JobApi.md#job_read) | **GET** /job/{id}/ | 


# **job_auth_read**
> JobAuthStatus job_auth_read(id)



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
    api_instance = epic_api.JobApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.job_auth_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->job_auth_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **job_auth_update**
> JobAuthStatus job_auth_update(id, data)



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
    api_instance = epic_api.JobApi(api_client)
    id = 'id_example' # str | 
data = epic_api.JobAuthStatus() # JobAuthStatus | 

    try:
        api_response = api_instance.job_auth_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->job_auth_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **job_create**
> Job job_create(data)



Method not yet implemented

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
    api_instance = epic_api.JobApi(api_client)
    data = epic_api.Job() # Job | 

    try:
        api_response = api_instance.job_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->job_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Job**](Job.md)|  | 

### Return type

[**Job**](Job.md)

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

# **job_list**
> InlineResponse2003 job_list(limit=limit, offset=offset)



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
    api_instance = epic_api.JobApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.job_list(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->job_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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

# **job_quote**
> PriceQuote job_quote(data)



Provides a price quote based upon the given BatchJobLaunchSpec. Quotes will be returned for clusters that the user/team has permission to use and that support the requested application, task distribution and runtime. When submitting muliple tasks in a the job specification then the task reference may be used to identify individual tasks.

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
    api_instance = epic_api.JobApi(api_client)
    data = epic_api.BatchJobSpec() # BatchJobSpec | 

    try:
        api_response = api_instance.job_quote(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->job_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**BatchJobSpec**](BatchJobSpec.md)|  | 

### Return type

[**PriceQuote**](PriceQuote.md)

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

# **job_read**
> Job job_read(id)



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
    api_instance = epic_api.JobApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.job_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->job_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Job**](Job.md)

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

