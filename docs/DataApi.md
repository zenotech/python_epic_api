# epiccore.DataApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_file_list**](DataApi.md#data_file_list) | **GET** /data/file/ | 
[**data_file_read**](DataApi.md#data_file_read) | **GET** /data/file/{id}/ | 
[**data_folder_list**](DataApi.md#data_folder_list) | **GET** /data/folder/ | 
[**data_folder_read**](DataApi.md#data_folder_read) | **GET** /data/folder/{id}/ | 
[**data_session_list**](DataApi.md#data_session_list) | **GET** /data/session/ | 


# **data_file_list**
> DataFileList200Response data_file_list(name=name, path=path, limit=limit, offset=offset)



List all files your user has access to

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.data_file_list200_response import DataFileList200Response
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
    api_instance = epiccore.DataApi(api_client)
    name = 'name_example' # str | Filter by file name (optional)
    path = 'path_example' # str | Filter by folder path (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.data_file_list(name=name, path=path, limit=limit, offset=offset)
        print("The response of DataApi->data_file_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->data_file_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter by file name | [optional] 
 **path** | **str**| Filter by folder path | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**DataFileList200Response**](DataFileList200Response.md)

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

# **data_file_read**
> FileDetails data_file_read(id)



See the details for a particular file

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.file_details import FileDetails
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
    api_instance = epiccore.DataApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.data_file_read(id)
        print("The response of DataApi->data_file_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->data_file_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FileDetails**](FileDetails.md)

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

# **data_folder_list**
> DataFolderList200Response data_folder_list(name=name, path=path, limit=limit, offset=offset)



List all folders your user has access to

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.data_folder_list200_response import DataFolderList200Response
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
    api_instance = epiccore.DataApi(api_client)
    name = 'name_example' # str | Filter by folder name (optional)
    path = 'path_example' # str | Filter by folder path (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.data_folder_list(name=name, path=path, limit=limit, offset=offset)
        print("The response of DataApi->data_folder_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->data_folder_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter by folder name | [optional] 
 **path** | **str**| Filter by folder path | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**DataFolderList200Response**](DataFolderList200Response.md)

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

# **data_folder_read**
> FolderDetails data_folder_read(id)



See the details for a particular folder

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.folder_details import FolderDetails
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
    api_instance = epiccore.DataApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.data_folder_read(id)
        print("The response of DataApi->data_folder_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->data_folder_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FolderDetails**](FolderDetails.md)

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

# **data_session_list**
> DataLocation data_session_list()



Get connection details for accessing the EPIC data store. Returns a temporary credenital to upload and download data to EPIC

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import epiccore
from epiccore.models.data_location import DataLocation
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
    api_instance = epiccore.DataApi(api_client)

    try:
        api_response = api_instance.data_session_list()
        print("The response of DataApi->data_session_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->data_session_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DataLocation**](DataLocation.md)

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

