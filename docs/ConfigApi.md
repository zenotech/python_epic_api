# epiccore.ConfigApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_read**](ConfigApi.md#config_read) | **GET** /config/{app_code}/{queue_code}/ | 


# **config_read**
> SiteConfigurationSerialiser config_read(app_code, queue_code)



Fetch the application configuration for <app_code> running on <queue_code>. Only accessable to authorised users.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
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
    api_instance = epiccore.ConfigApi(api_client)
    app_code = 'app_code_example' # str | 
queue_code = 'queue_code_example' # str | 

    try:
        api_response = api_instance.config_read(app_code, queue_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_code** | **str**|  | 
 **queue_code** | **str**|  | 

### Return type

[**SiteConfigurationSerialiser**](SiteConfigurationSerialiser.md)

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

