# epiccore.DesktopApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**desktop_create**](DesktopApi.md#desktop_create) | **POST** /desktop/ | 
[**desktop_list**](DesktopApi.md#desktop_list) | **GET** /desktop/ | 
[**desktop_quote**](DesktopApi.md#desktop_quote) | **POST** /desktop/quote/ | 
[**desktop_read**](DesktopApi.md#desktop_read) | **GET** /desktop/{id}/ | 


# **desktop_create**
> DesktopNodeLaunchSpec desktop_create(data)



Launch a Desktop Node given a DesktopNodeLaunchSpec

### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import desktop_api
from epiccore.model.desktop_node_launch_spec import DesktopNodeLaunchSpec
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
    api_instance = desktop_api.DesktopApi(api_client)
    data = DesktopNodeLaunchSpec(
        node_type=1,
        application_version=1,
        connection=1,
        folder=1,
        project=-1,
        runtime=1,
        mount_type="mount_type_example",
        secure_ip=False,
        ip_address="ip_address_example",
        invoice_reference="invoice_reference_example",
    ) # DesktopNodeLaunchSpec | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.desktop_create(data)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling DesktopApi->desktop_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesktopNodeLaunchSpec**](DesktopNodeLaunchSpec.md)|  |

### Return type

[**DesktopNodeLaunchSpec**](DesktopNodeLaunchSpec.md)

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

# **desktop_list**
> InlineResponse2007 desktop_list()



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import desktop_api
from epiccore.model.inline_response2007 import InlineResponse2007
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
    api_instance = desktop_api.DesktopApi(api_client)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.desktop_list(limit=limit, offset=offset)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling DesktopApi->desktop_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

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

# **desktop_quote**
> PriceQuote desktop_quote(data)



Provides a price quote based upon the given VizNodeLaunchSpec. This will also provide information as to whether it meets billing budget criteria for the given team / project combination

### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import desktop_api
from epiccore.model.price_quote import PriceQuote
from epiccore.model.desktop_node_launch_spec import DesktopNodeLaunchSpec
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
    api_instance = desktop_api.DesktopApi(api_client)
    data = DesktopNodeLaunchSpec(
        node_type=1,
        application_version=1,
        connection=1,
        folder=1,
        project=-1,
        runtime=1,
        mount_type="mount_type_example",
        secure_ip=False,
        ip_address="ip_address_example",
        invoice_reference="invoice_reference_example",
    ) # DesktopNodeLaunchSpec | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.desktop_quote(data)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling DesktopApi->desktop_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesktopNodeLaunchSpec**](DesktopNodeLaunchSpec.md)|  |

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

# **desktop_read**
> DesktopNode desktop_read(id)



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import desktop_api
from epiccore.model.desktop_node import DesktopNode
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
    api_instance = desktop_api.DesktopApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.desktop_read(id)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling DesktopApi->desktop_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**DesktopNode**](DesktopNode.md)

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

