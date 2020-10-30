# epiccore.ProfileApi

All URIs are relative to *https://epic-qa.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profile_settings_list**](ProfileApi.md#profile_settings_list) | **GET** /profile/settings/ | 


# **profile_settings_list**
> ProfileSummary profile_settings_list()



Return details about the settings for the users billing profile

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
    api_instance = epiccore.ProfileApi(api_client)
    
    try:
        api_response = api_instance.profile_settings_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProfileApi->profile_settings_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProfileSummary**](ProfileSummary.md)

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

