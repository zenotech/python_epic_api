# epiccore.JobauthApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobauth_list**](JobauthApi.md#jobauth_list) | **GET** /jobauth/ | 
[**jobauth_read**](JobauthApi.md#jobauth_read) | **GET** /jobauth/{job}/ | 
[**jobauth_update**](JobauthApi.md#jobauth_update) | **PUT** /jobauth/{job}/ | 


# **jobauth_list**
> InlineResponse20010 jobauth_list()



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import jobauth_api
from epiccore.model.inline_response20010 import InlineResponse20010
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
    api_instance = jobauth_api.JobauthApi(api_client)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobauth_list(limit=limit, offset=offset)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling JobauthApi->jobauth_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

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
import time
import epiccore
from epiccore.api import jobauth_api
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
    api_instance = jobauth_api.JobauthApi(api_client)
    job = "job_example" # str | A unique value identifying this job authorisation.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobauth_read(job)
        pprint(api_response)
    except epiccore.ApiException as e:
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
import time
import epiccore
from epiccore.api import jobauth_api
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
    api_instance = jobauth_api.JobauthApi(api_client)
    job = "job_example" # str | A unique value identifying this job authorisation.
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
        api_response = api_instance.jobauth_update(job, data)
        pprint(api_response)
    except epiccore.ApiException as e:
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

