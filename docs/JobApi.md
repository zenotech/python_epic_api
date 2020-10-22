# epiccore.JobApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_auth_read**](JobApi.md#job_auth_read) | **GET** /job/{id}/auth/ | 
[**job_auth_update**](JobApi.md#job_auth_update) | **PUT** /job/{id}/auth/ | 
[**job_cancel**](JobApi.md#job_cancel) | **POST** /job/{id}/cancel/ | 
[**job_create**](JobApi.md#job_create) | **POST** /job/ | 
[**job_list**](JobApi.md#job_list) | **GET** /job/ | 
[**job_quote**](JobApi.md#job_quote) | **POST** /job/quote/ | 
[**job_read**](JobApi.md#job_read) | **GET** /job/{id}/ | 
[**job_steps_cancel**](JobApi.md#job_steps_cancel) | **POST** /job/{job_pk}/steps/{id}/cancel/ | 
[**job_steps_list**](JobApi.md#job_steps_list) | **GET** /job/{job_pk}/steps/ | 
[**job_steps_logs**](JobApi.md#job_steps_logs) | **GET** /job/{job_pk}/steps/{id}/logs/ | 
[**job_steps_read**](JobApi.md#job_steps_read) | **GET** /job/{job_pk}/steps/{id}/ | 


# **job_auth_read**
> JobAuthStatus job_auth_read(id)



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import job_api
from epiccore.model.job_auth_status import JobAuthStatus
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
configuration = epiccore.Configuration(
    host = "https://epic.zenotech.com/api/v2",
    api_key = {
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.job_auth_read(id)
        pprint(api_response)
    except epiccore.ApiException as e:
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
import time
import epiccore
from epiccore.api import job_api
from epiccore.model.job_auth_status import JobAuthStatus
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
configuration = epiccore.Configuration(
    host = "https://epic.zenotech.com/api/v2",
    api_key = {
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)
    id = "id_example" # str | 
    data = JobAuthStatus(
        required=True,
        state="state_example",
        job=Job(
            id=1,
            name="name_example",
            app="app_example",
            application_version=1,
            cost="cost_example",
            status="status_example",
            submitted_by="submitted_by_example",
            submitted_at="submitted_at_example",
            finished=True,
            resource=BatchQueueDetails(
                id=1,
                display_name="display_name_example",
                display_description="display_description_example",
                max_runtime=0,
                max_allocation=0,
                reported_avail_tasks=0,
                reported_max_tasks=0,
                sla=SLA(
                    name="name_example",
                    description="description_example",
                ),
                maintenance_mode="maintenance_mode_example",
                resource_config="resource_config_example",
            ),
            project=1,
            invoice_reference="invoice_reference_example",
            config=JobConfiguration(
                upload=[
                    "complete",
                ],
                overwrite_existing=True,
                data_sync_interval=0,
            ),
        ),
        user_profile=UserName(
            display_name="display_name_example",
        ),
        permissions="permissions_example",
    ) # JobAuthStatus | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.job_auth_update(id, data)
        pprint(api_response)
    except epiccore.ApiException as e:
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
import epiccore
from epiccore.api import job_api
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
configuration = epiccore.Configuration(
    host = "https://epic.zenotech.com/api/v2",
    api_key = {
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)
    id = "id_example" # str | 
    data = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.job_cancel(id, data)
    except epiccore.ApiException as e:
        print("Exception when calling JobApi->job_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

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
> [Job] job_create(data)



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import job_api
from epiccore.model.job import Job
from epiccore.model.job_array_spec import JobArraySpec
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
configuration = epiccore.Configuration(
    host = "https://epic.zenotech.com/api/v2",
    api_key = {
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)
    data = JobArraySpec(
        name="Job Array",
        config=JobConfiguration(
            upload=[
                "complete",
            ],
            overwrite_existing=True,
            data_sync_interval=0,
        ),
        jobs=[
            JobDataBinding(
                name="name_example",
                spec=JobSpec(
                    application_version=1,
                    project=-1,
                    tasks=[
                        JobTaskSpec(
                            reference="reference_example",
                            partitions=1,
                            runtime=1,
                            task_distribution="core",
                            hyperthreading=True,
                        ),
                    ],
                ),
                app_options={},
                cluster=JobClusterSpec(
                    queue=1,
                ),
                input_data=DataSpec(
                    path="path_example",
                ),
            ),
        ],
        common_data=DataSpec(
            path="path_example",
        ),
    ) # JobArraySpec | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.job_create(data)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling JobApi->job_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**JobArraySpec**](JobArraySpec.md)|  |

### Return type

[**[Job]**](Job.md)

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
> InlineResponse2008 job_list()



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import job_api
from epiccore.model.inline_response2008 import InlineResponse2008
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
configuration = epiccore.Configuration(
    host = "https://epic.zenotech.com/api/v2",
    api_key = {
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.job_list(limit=limit, offset=offset)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling JobApi->job_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

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
> JobQuote job_quote(data)



Provides a price quote based upon the given BatchJobLaunchSpec. Quotes will be returned for clusters that the user/team has permission to use and that support the requested application, task distribution and runtime. When submitting muliple tasks in a the job specification then the task reference may be used to identify individual tasks.

### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import job_api
from epiccore.model.job_quote import JobQuote
from epiccore.model.job_spec import JobSpec
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
configuration = epiccore.Configuration(
    host = "https://epic.zenotech.com/api/v2",
    api_key = {
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)
    data = JobSpec(
        application_version=1,
        project=-1,
        tasks=[
            JobTaskSpec(
                reference="reference_example",
                partitions=1,
                runtime=1,
                task_distribution="core",
                hyperthreading=True,
            ),
        ],
    ) # JobSpec | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.job_quote(data)
        pprint(api_response)
    except epiccore.ApiException as e:
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



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import job_api
from epiccore.model.job import Job
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
configuration = epiccore.Configuration(
    host = "https://epic.zenotech.com/api/v2",
    api_key = {
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.job_read(id)
        pprint(api_response)
    except epiccore.ApiException as e:
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

# **job_steps_cancel**
> job_steps_cancel(id, job_pk, data)



Cancel a job step

### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import job_api
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
configuration = epiccore.Configuration(
    host = "https://epic.zenotech.com/api/v2",
    api_key = {
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)
    id = "id_example" # str | 
    job_pk = "job_pk_example" # str | 
    data = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.job_steps_cancel(id, job_pk, data)
    except epiccore.ApiException as e:
        print("Exception when calling JobApi->job_steps_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **job_pk** | **str**|  |
 **data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

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

# **job_steps_list**
> InlineResponse2009 job_steps_list(job_pk)



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import job_api
from epiccore.model.inline_response2009 import InlineResponse2009
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
configuration = epiccore.Configuration(
    host = "https://epic.zenotech.com/api/v2",
    api_key = {
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)
    job_pk = "job_pk_example" # str | 
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.job_steps_list(job_pk)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling JobApi->job_steps_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.job_steps_list(job_pk, limit=limit, offset=offset)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling JobApi->job_steps_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_pk** | **str**|  |
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

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

# **job_steps_logs**
> JobLog job_steps_logs(id, job_pk)



Fetch logs for a job step

### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import job_api
from epiccore.model.job_log import JobLog
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
configuration = epiccore.Configuration(
    host = "https://epic.zenotech.com/api/v2",
    api_key = {
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)
    id = "id_example" # str | 
    job_pk = "job_pk_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.job_steps_logs(id, job_pk)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling JobApi->job_steps_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **job_pk** | **str**|  |

### Return type

[**JobLog**](JobLog.md)

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

# **job_steps_read**
> JobStep job_steps_read(id, job_pk)



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import job_api
from epiccore.model.job_step import JobStep
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
configuration = epiccore.Configuration(
    host = "https://epic.zenotech.com/api/v2",
    api_key = {
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with epiccore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)
    id = "id_example" # str | 
    job_pk = "job_pk_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.job_steps_read(id, job_pk)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling JobApi->job_steps_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **job_pk** | **str**|  |

### Return type

[**JobStep**](JobStep.md)

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

