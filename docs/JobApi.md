# epiccore.JobApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_auth_read**](JobApi.md#job_auth_read) | **GET** /job/{id}/auth/ | 
[**job_auth_update**](JobApi.md#job_auth_update) | **PUT** /job/{id}/auth/ | 
[**job_cancel**](JobApi.md#job_cancel) | **POST** /job/{id}/cancel/ | 
[**job_create**](JobApi.md#job_create) | **POST** /job/ | 
[**job_list**](JobApi.md#job_list) | **GET** /job/ | 
[**job_partial_update**](JobApi.md#job_partial_update) | **PATCH** /job/{id}/ | 
[**job_quote**](JobApi.md#job_quote) | **POST** /job/quote/ | 
[**job_read**](JobApi.md#job_read) | **GET** /job/{id}/ | 
[**job_residuals_read**](JobApi.md#job_residuals_read) | **GET** /job/{id}/residuals/ | 


# **job_auth_read**
> JobAuthStatus job_auth_read(id)



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
    api_instance = epiccore.JobApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.job_auth_read(id)
        print("The response of JobApi->job_auth_read:\n")
        pprint(api_response)
    except Exception as e:
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
    api_instance = epiccore.JobApi(api_client)
    id = 'id_example' # str | 
    data = epiccore.JobAuthStatus() # JobAuthStatus | 

    try:
        api_response = api_instance.job_auth_update(id, data)
        print("The response of JobApi->job_auth_update:\n")
        pprint(api_response)
    except Exception as e:
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

# **job_cancel**
> job_cancel(id, data)



Cancel a job

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
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
    api_instance = epiccore.JobApi(api_client)
    id = 'id_example' # str | 
    data = None # object | 

    try:
        api_instance.job_cancel(id, data)
    except Exception as e:
        print("Exception when calling JobApi->job_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | **object**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Cancel request received |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_create**
> List[Job] job_create(data)



Create a new job bssased on the submitted job specification. App and Queue codes can be retreived from the catalog endpoints.

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.job import Job
from epiccore.models.job_array_spec import JobArraySpec
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
    api_instance = epiccore.JobApi(api_client)
    data = epiccore.JobArraySpec() # JobArraySpec | 

    try:
        api_response = api_instance.job_create(data)
        print("The response of JobApi->job_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->job_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**JobArraySpec**](JobArraySpec.md)|  | 

### Return type

[**List[Job]**](Job.md)

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
> JobList200Response job_list(job_array=job_array, limit=limit, offset=offset)



List the jobs instances in EPIC

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.job_list200_response import JobList200Response
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
    api_instance = epiccore.JobApi(api_client)
    job_array = 'job_array_example' # str | Filter by ID of the parent Job Array (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.job_list(job_array=job_array, limit=limit, offset=offset)
        print("The response of JobApi->job_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->job_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_array** | **str**| Filter by ID of the parent Job Array | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**JobList200Response**](JobList200Response.md)

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

# **job_partial_update**
> JobAppOptions job_partial_update(id, data)



Update the job options for job instance with ID {id}

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.job_app_options import JobAppOptions
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
    api_instance = epiccore.JobApi(api_client)
    id = 'id_example' # str | 
    data = epiccore.JobAppOptions() # JobAppOptions | 

    try:
        api_response = api_instance.job_partial_update(id, data)
        print("The response of JobApi->job_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->job_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**JobAppOptions**](JobAppOptions.md)|  | 

### Return type

[**JobAppOptions**](JobAppOptions.md)

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

# **job_quote**
> JobQuote job_quote(data)



Provides a price quote based upon the given BatchJobLaunchSpec. Quotes will be returned for clusters that the user/team has permission to use and that support the requested application, task distribution and runtime. When submitting multiple steps in a the job specification then the task reference may be used to identify individual steps.

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.job_quote import JobQuote
from epiccore.models.job_spec import JobSpec
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
    api_instance = epiccore.JobApi(api_client)
    data = epiccore.JobSpec() # JobSpec | 

    try:
        api_response = api_instance.job_quote(data)
        print("The response of JobApi->job_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->job_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**JobSpec**](JobSpec.md)|  | 

### Return type

[**JobQuote**](JobQuote.md)

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



See the details for the job instance with ID {id}

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.job import Job
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
    api_instance = epiccore.JobApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.job_read(id)
        print("The response of JobApi->job_read:\n")
        pprint(api_response)
    except Exception as e:
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

# **job_residuals_read**
> JobResidual job_residuals_read(id, variables=variables)



Retreive the residuals for job with ID {id}

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.job_residual import JobResidual
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
    api_instance = epiccore.JobApi(api_client)
    id = 56 # int | A unique integer value identifying this batch job instance.
    variables = ['variables_example'] # List[str] | Return data values for these variable names (optional)

    try:
        api_response = api_instance.job_residuals_read(id, variables=variables)
        print("The response of JobApi->job_residuals_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->job_residuals_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this batch job instance. | 
 **variables** | [**List[str]**](str.md)| Return data values for these variable names | [optional] 

### Return type

[**JobResidual**](JobResidual.md)

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

