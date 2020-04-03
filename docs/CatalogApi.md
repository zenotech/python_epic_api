# epic_api.CatalogApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_applications_list**](CatalogApi.md#catalog_applications_list) | **GET** /catalog/applications/ | 
[**catalog_applications_read**](CatalogApi.md#catalog_applications_read) | **GET** /catalog/applications/{id}/ | 
[**catalog_viz_list**](CatalogApi.md#catalog_viz_list) | **GET** /catalog/viz/ | 
[**catalog_viz_read**](CatalogApi.md#catalog_viz_read) | **GET** /catalog/viz/{id}/ | 
[**catalog_viznodetype_read**](CatalogApi.md#catalog_viznodetype_read) | **GET** /catalog/viznodetype/{viz_application_version_id}/ | 


# **catalog_applications_list**
> InlineResponse200 catalog_applications_list(limit=limit, offset=offset)



View available applications

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
    api_instance = epic_api.CatalogApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.catalog_applications_list(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CatalogApi->catalog_applications_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **catalog_applications_read**
> BatchApplicationDetails catalog_applications_read(id)



View available applications

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
    api_instance = epic_api.CatalogApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.catalog_applications_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CatalogApi->catalog_applications_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BatchApplicationDetails**](BatchApplicationDetails.md)

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

# **catalog_viz_list**
> InlineResponse2001 catalog_viz_list(limit=limit, offset=offset)



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
    api_instance = epic_api.CatalogApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.catalog_viz_list(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CatalogApi->catalog_viz_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

# **catalog_viz_read**
> VizNodeApp catalog_viz_read(id)



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
    api_instance = epic_api.CatalogApi(api_client)
    id = 56 # int | A unique integer value identifying this viz node application.

    try:
        api_response = api_instance.catalog_viz_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CatalogApi->catalog_viz_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this viz node application. | 

### Return type

[**VizNodeApp**](VizNodeApp.md)

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

# **catalog_viznodetype_read**
> InlineResponse2002 catalog_viznodetype_read(viz_application_version_id, limit=limit, offset=offset)



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
    api_instance = epic_api.CatalogApi(api_client)
    viz_application_version_id = 'viz_application_version_id_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.catalog_viznodetype_read(viz_application_version_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CatalogApi->catalog_viznodetype_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viz_application_version_id** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

