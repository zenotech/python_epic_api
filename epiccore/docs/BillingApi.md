# epiccore.BillingApi

All URIs are relative to *https://epic-qa.zenotech.com/api/v2*

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
    api_instance = epiccore.BillingApi(api_client)
    
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
    api_instance = epiccore.BillingApi(api_client)
    data = epiccore.Limits() # Limits | 

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

