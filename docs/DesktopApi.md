# epiccore.DesktopApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**desktop_create**](DesktopApi.md#desktop_create) | **POST** /desktop/ | 
[**desktop_list**](DesktopApi.md#desktop_list) | **GET** /desktop/ | 
[**desktop_quote**](DesktopApi.md#desktop_quote) | **POST** /desktop/quote/ | 
[**desktop_read**](DesktopApi.md#desktop_read) | **GET** /desktop/{id}/ | 
[**desktop_terminate**](DesktopApi.md#desktop_terminate) | **POST** /desktop/{id}/terminate/ | 


# **desktop_create**
> DesktopInstance desktop_create(data)



Launch a new desktop instance.

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.desktop_instance import DesktopInstance
from epiccore.models.desktop_node_launch_spec import DesktopNodeLaunchSpec
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
    api_instance = epiccore.DesktopApi(api_client)
    data = epiccore.DesktopNodeLaunchSpec() # DesktopNodeLaunchSpec | 

    try:
        api_response = api_instance.desktop_create(data)
        print("The response of DesktopApi->desktop_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesktopApi->desktop_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesktopNodeLaunchSpec**](DesktopNodeLaunchSpec.md)|  | 

### Return type

[**DesktopInstance**](DesktopInstance.md)

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
> DesktopList200Response desktop_list(limit=limit, offset=offset)



List Desktop instances

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.desktop_list200_response import DesktopList200Response
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
    api_instance = epiccore.DesktopApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.desktop_list(limit=limit, offset=offset)
        print("The response of DesktopApi->desktop_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesktopApi->desktop_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**DesktopList200Response**](DesktopList200Response.md)

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
import os
import epiccore
from epiccore.models.desktop_node_quote import DesktopNodeQuote
from epiccore.models.price_quote import PriceQuote
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
    api_instance = epiccore.DesktopApi(api_client)
    data = epiccore.DesktopNodeQuote() # DesktopNodeQuote | 

    try:
        api_response = api_instance.desktop_quote(data)
        print("The response of DesktopApi->desktop_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesktopApi->desktop_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesktopNodeQuote**](DesktopNodeQuote.md)|  | 

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
> DesktopInstance desktop_read(id)



### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.desktop_instance import DesktopInstance
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
    api_instance = epiccore.DesktopApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.desktop_read(id)
        print("The response of DesktopApi->desktop_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesktopApi->desktop_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DesktopInstance**](DesktopInstance.md)

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

# **desktop_terminate**
> desktop_terminate(id, data)



Terminate the desktop with step with ID {id}

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
    api_instance = epiccore.DesktopApi(api_client)
    id = 'id_example' # str | 
    data = None # object | 

    try:
        api_instance.desktop_terminate(id, data)
    except Exception as e:
        print("Exception when calling DesktopApi->desktop_terminate: %s\n" % e)
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
**204** | Terminate request received |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

