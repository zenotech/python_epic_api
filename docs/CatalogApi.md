# epiccore.CatalogApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_applications_list**](CatalogApi.md#catalog_applications_list) | **GET** /catalog/applications/ | 
[**catalog_applications_read**](CatalogApi.md#catalog_applications_read) | **GET** /catalog/applications/{application}/ | 
[**catalog_clusters_list**](CatalogApi.md#catalog_clusters_list) | **GET** /catalog/clusters/ | 
[**catalog_clusters_read**](CatalogApi.md#catalog_clusters_read) | **GET** /catalog/clusters/{queue_code}/ | 
[**catalog_desktop_list**](CatalogApi.md#catalog_desktop_list) | **GET** /catalog/desktop/ | 
[**catalog_desktop_read**](CatalogApi.md#catalog_desktop_read) | **GET** /catalog/desktop/{node_code}/ | 


# **catalog_applications_list**
> InlineResponse200 catalog_applications_list(product_name=product_name, limit=limit, offset=offset)



List all available applications and the versions for that application

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
    api_instance = epiccore.CatalogApi(api_client)
    product_name = 'product_name_example' # str | Filter by application name (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.catalog_applications_list(product_name=product_name, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CatalogApi->catalog_applications_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_name** | **str**| Filter by application name | [optional] 
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
> BatchApplicationDetails catalog_applications_read(application)



Retreive the details for the application with the application product name {product}

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
    api_instance = epiccore.CatalogApi(api_client)
    application = 'application_example' # str | 

    try:
        api_response = api_instance.catalog_applications_read(application)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CatalogApi->catalog_applications_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**|  | 

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

# **catalog_clusters_list**
> InlineResponse2001 catalog_clusters_list(cluster_name=cluster_name, queue_name=queue_name, allowed_apps=allowed_apps, limit=limit, offset=offset)



View available cluster queues

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
    api_instance = epiccore.CatalogApi(api_client)
    cluster_name = 'cluster_name_example' # str | Filter by cluster name (optional)
queue_name = 'queue_name_example' # str | Filter by queue name (optional)
allowed_apps = 'allowed_apps_example' # str | Filter by application code available on queue (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.catalog_clusters_list(cluster_name=cluster_name, queue_name=queue_name, allowed_apps=allowed_apps, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CatalogApi->catalog_clusters_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Filter by cluster name | [optional] 
 **queue_name** | **str**| Filter by queue name | [optional] 
 **allowed_apps** | **str**| Filter by application code available on queue | [optional] 
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

# **catalog_clusters_read**
> BatchQueueDetails catalog_clusters_read(queue_code)



Retreive the details for the cluster queue with queue code {queue_code}

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
    api_instance = epiccore.CatalogApi(api_client)
    queue_code = 'queue_code_example' # str | 

    try:
        api_response = api_instance.catalog_clusters_read(queue_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CatalogApi->catalog_clusters_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_code** | **str**|  | 

### Return type

[**BatchQueueDetails**](BatchQueueDetails.md)

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

# **catalog_desktop_list**
> InlineResponse2002 catalog_desktop_list(limit=limit, offset=offset)



List the available node types for desktop instances

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
    api_instance = epiccore.CatalogApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.catalog_desktop_list(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CatalogApi->catalog_desktop_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **catalog_desktop_read**
> DesktopNodeType catalog_desktop_read(node_code)



Get the details of the desktop node type with code node_code

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
    api_instance = epiccore.CatalogApi(api_client)
    node_code = 'node_code_example' # str | 

    try:
        api_response = api_instance.catalog_desktop_read(node_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CatalogApi->catalog_desktop_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_code** | **str**|  | 

### Return type

[**DesktopNodeType**](DesktopNodeType.md)

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

