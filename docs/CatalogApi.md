# epiccore.CatalogApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_applications_list**](CatalogApi.md#catalog_applications_list) | **GET** /catalog/applications/ | 
[**catalog_applications_read**](CatalogApi.md#catalog_applications_read) | **GET** /catalog/applications/{id}/ | 
[**catalog_applications_versions_list**](CatalogApi.md#catalog_applications_versions_list) | **GET** /catalog/applications/{app_pk}/versions/ | 
[**catalog_applications_versions_read**](CatalogApi.md#catalog_applications_versions_read) | **GET** /catalog/applications/{app_pk}/versions/{id}/ | 
[**catalog_applications_versions_resources_list**](CatalogApi.md#catalog_applications_versions_resources_list) | **GET** /catalog/applications/{app_pk}/versions/{app_version_pk}/resources/ | 
[**catalog_applications_versions_resources_read**](CatalogApi.md#catalog_applications_versions_resources_read) | **GET** /catalog/applications/{app_pk}/versions/{app_version_pk}/resources/{id}/ | 
[**catalog_desktop_applications_list**](CatalogApi.md#catalog_desktop_applications_list) | **GET** /catalog/desktop/applications/ | 
[**catalog_desktop_applications_read**](CatalogApi.md#catalog_desktop_applications_read) | **GET** /catalog/desktop/applications/{id}/ | 
[**catalog_desktop_list**](CatalogApi.md#catalog_desktop_list) | **GET** /catalog/desktop/ | 
[**catalog_desktop_read**](CatalogApi.md#catalog_desktop_read) | **GET** /catalog/desktop/{id}/ | 
[**catalog_viz_applications_list**](CatalogApi.md#catalog_viz_applications_list) | **GET** /catalog/viz/applications/ | 
[**catalog_viz_applications_read**](CatalogApi.md#catalog_viz_applications_read) | **GET** /catalog/viz/applications/{id}/ | 
[**catalog_viz_list**](CatalogApi.md#catalog_viz_list) | **GET** /catalog/viz/ | 
[**catalog_viz_read**](CatalogApi.md#catalog_viz_read) | **GET** /catalog/viz/{id}/ | 
[**catalog_viznodetype_read**](CatalogApi.md#catalog_viznodetype_read) | **GET** /catalog/viznodetype/{viz_application_version_id}/ | 


# **catalog_applications_list**
> InlineResponse200 catalog_applications_list()



View available applications

### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import catalog_api
from epiccore.model.inline_response200 import InlineResponse200
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
    api_instance = catalog_api.CatalogApi(api_client)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.catalog_applications_list(limit=limit, offset=offset)
        pprint(api_response)
    except epiccore.ApiException as e:
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
import time
import epiccore
from epiccore.api import catalog_api
from epiccore.model.batch_application_details import BatchApplicationDetails
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
    api_instance = catalog_api.CatalogApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.catalog_applications_read(id)
        pprint(api_response)
    except epiccore.ApiException as e:
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

# **catalog_applications_versions_list**
> InlineResponse2001 catalog_applications_versions_list(app_pk)



View details on application versions

### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import catalog_api
from epiccore.model.inline_response2001 import InlineResponse2001
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
    api_instance = catalog_api.CatalogApi(api_client)
    app_pk = "app_pk_example" # str | 
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.catalog_applications_versions_list(app_pk)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_applications_versions_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.catalog_applications_versions_list(app_pk, limit=limit, offset=offset)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_applications_versions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_pk** | **str**|  |
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

# **catalog_applications_versions_read**
> BatchApplicationVersionResourceDetails catalog_applications_versions_read(app_pk, id)



View details on application versions

### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import catalog_api
from epiccore.model.batch_application_version_resource_details import BatchApplicationVersionResourceDetails
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
    api_instance = catalog_api.CatalogApi(api_client)
    app_pk = "app_pk_example" # str | 
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.catalog_applications_versions_read(app_pk, id)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_applications_versions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_pk** | **str**|  |
 **id** | **str**|  |

### Return type

[**BatchApplicationVersionResourceDetails**](BatchApplicationVersionResourceDetails.md)

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

# **catalog_applications_versions_resources_list**
> InlineResponse2002 catalog_applications_versions_resources_list(app_pk, app_version_pk)



View details on resources available for a given application version

### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import catalog_api
from epiccore.model.inline_response2002 import InlineResponse2002
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
    api_instance = catalog_api.CatalogApi(api_client)
    app_pk = "app_pk_example" # str | 
    app_version_pk = "app_version_pk_example" # str | 
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.catalog_applications_versions_resources_list(app_pk, app_version_pk)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_applications_versions_resources_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.catalog_applications_versions_resources_list(app_pk, app_version_pk, limit=limit, offset=offset)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_applications_versions_resources_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_pk** | **str**|  |
 **app_version_pk** | **str**|  |
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

# **catalog_applications_versions_resources_read**
> BatchApplicationVersionResource catalog_applications_versions_resources_read(app_pk, app_version_pk, id)



View details on resources available for a given application version

### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import catalog_api
from epiccore.model.batch_application_version_resource import BatchApplicationVersionResource
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
    api_instance = catalog_api.CatalogApi(api_client)
    app_pk = "app_pk_example" # str | 
    app_version_pk = "app_version_pk_example" # str | 
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.catalog_applications_versions_resources_read(app_pk, app_version_pk, id)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_applications_versions_resources_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_pk** | **str**|  |
 **app_version_pk** | **str**|  |
 **id** | **str**|  |

### Return type

[**BatchApplicationVersionResource**](BatchApplicationVersionResource.md)

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

# **catalog_desktop_applications_list**
> InlineResponse2004 catalog_desktop_applications_list()



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import catalog_api
from epiccore.model.inline_response2004 import InlineResponse2004
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
    api_instance = catalog_api.CatalogApi(api_client)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.catalog_desktop_applications_list(limit=limit, offset=offset)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_desktop_applications_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **catalog_desktop_applications_read**
> DesktopNodeApplication catalog_desktop_applications_read(id)



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import catalog_api
from epiccore.model.desktop_node_application import DesktopNodeApplication
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
    api_instance = catalog_api.CatalogApi(api_client)
    id = "id_example" # str | A UUID string identifying this efs access point app.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.catalog_desktop_applications_read(id)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_desktop_applications_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this efs access point app. |

### Return type

[**DesktopNodeApplication**](DesktopNodeApplication.md)

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
> InlineResponse2003 catalog_desktop_list()



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import catalog_api
from epiccore.model.inline_response2003 import InlineResponse2003
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
    api_instance = catalog_api.CatalogApi(api_client)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.catalog_desktop_list(limit=limit, offset=offset)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_desktop_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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
> DesktopNodeApp catalog_desktop_read(id)



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import catalog_api
from epiccore.model.desktop_node_app import DesktopNodeApp
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
    api_instance = catalog_api.CatalogApi(api_client)
    id = 1 # int | A unique integer value identifying this viz node application.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.catalog_desktop_read(id)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_desktop_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this viz node application. |

### Return type

[**DesktopNodeApp**](DesktopNodeApp.md)

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

# **catalog_viz_applications_list**
> InlineResponse2004 catalog_viz_applications_list()



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import catalog_api
from epiccore.model.inline_response2004 import InlineResponse2004
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
    api_instance = catalog_api.CatalogApi(api_client)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.catalog_viz_applications_list(limit=limit, offset=offset)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_viz_applications_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **catalog_viz_applications_read**
> DesktopNodeApplication catalog_viz_applications_read(id)



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import catalog_api
from epiccore.model.desktop_node_application import DesktopNodeApplication
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
    api_instance = catalog_api.CatalogApi(api_client)
    id = "id_example" # str | A UUID string identifying this efs access point app.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.catalog_viz_applications_read(id)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_viz_applications_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this efs access point app. |

### Return type

[**DesktopNodeApplication**](DesktopNodeApplication.md)

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
> InlineResponse2003 catalog_viz_list()



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import catalog_api
from epiccore.model.inline_response2003 import InlineResponse2003
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
    api_instance = catalog_api.CatalogApi(api_client)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.catalog_viz_list(limit=limit, offset=offset)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_viz_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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
> DesktopNodeApp catalog_viz_read(id)



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import catalog_api
from epiccore.model.desktop_node_app import DesktopNodeApp
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
    api_instance = catalog_api.CatalogApi(api_client)
    id = 1 # int | A unique integer value identifying this viz node application.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.catalog_viz_read(id)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_viz_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this viz node application. |

### Return type

[**DesktopNodeApp**](DesktopNodeApp.md)

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
> InlineResponse2005 catalog_viznodetype_read(viz_application_version_id)



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import catalog_api
from epiccore.model.inline_response2005 import InlineResponse2005
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
    api_instance = catalog_api.CatalogApi(api_client)
    viz_application_version_id = "viz_application_version_id_example" # str | 
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.catalog_viznodetype_read(viz_application_version_id)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_viznodetype_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.catalog_viznodetype_read(viz_application_version_id, limit=limit, offset=offset)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling CatalogApi->catalog_viznodetype_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viz_application_version_id** | **str**|  |
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

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

