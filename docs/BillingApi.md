# epic_api.BillingApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_limits_list**](BillingApi.md#billing_limits_list) | **GET** /billing/limits/ | 
[**billing_limits_partial_update**](BillingApi.md#billing_limits_partial_update) | **PATCH** /billing/limits/ | 


# **billing_limits_list**
> Limits billing_limits_list()



Return the current limits for the users billing profile

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
    api_instance = epic_api.BillingApi(api_client)
    
    try:
        api_response = api_instance.billing_limits_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->billing_limits_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Limits**](Limits.md)

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

# **billing_limits_partial_update**
> Limits billing_limits_partial_update(data)



Update billing limits for the users billing profile and associated teams

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
    api_instance = epic_api.BillingApi(api_client)
    data = epic_api.Limits() # Limits | 

    try:
        api_response = api_instance.billing_limits_partial_update(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->billing_limits_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Limits**](Limits.md)|  | 

### Return type

[**Limits**](Limits.md)

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

