# epiccore.LicensesApi

All URIs are relative to *https://epic.zenotech.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**licenses_ansys**](LicensesApi.md#licenses_ansys) | **POST** /licenses/ansys/ | 
[**licenses_create**](LicensesApi.md#licenses_create) | **POST** /licenses/ | 
[**licenses_list**](LicensesApi.md#licenses_list) | **GET** /licenses/ | 
[**licenses_read**](LicensesApi.md#licenses_read) | **GET** /licenses/{id}/ | 
[**licenses_update**](LicensesApi.md#licenses_update) | **PUT** /licenses/{id}/ | 
[**licenses_zcad**](LicensesApi.md#licenses_zcad) | **POST** /licenses/zcad/ | 
[**licenses_zcfd**](LicensesApi.md#licenses_zcfd) | **POST** /licenses/zcfd/ | 


# **licenses_ansys**
> AnsysLicense licenses_ansys(data)



Creates a Ansys License server configuration

### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import licenses_api
from epiccore.model.ansys_license import AnsysLicense
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
    api_instance = licenses_api.LicensesApi(api_client)
    data = AnsysLicense(
        display_name="display_name_example",
        flexlm_host="flexlm_host_example",
        flexlm_port=1024,
        ansysli_host="ansysli_host_example",
        ansysli_port=1024,
    ) # AnsysLicense | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.licenses_ansys(data)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling LicensesApi->licenses_ansys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AnsysLicense**](AnsysLicense.md)|  |

### Return type

[**AnsysLicense**](AnsysLicense.md)

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

# **licenses_create**
> License licenses_create(data)



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import licenses_api
from epiccore.model.license import License
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
    api_instance = licenses_api.LicensesApi(api_client)
    data = License(
        teams="teams_example",
        license_type="zenotech_zcfd",
        id="id_example",
        display_name="display_name_example",
    ) # License | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.licenses_create(data)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling LicensesApi->licenses_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**License**](License.md)|  |

### Return type

[**License**](License.md)

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

# **licenses_list**
> InlineResponse20011 licenses_list()



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import licenses_api
from epiccore.model.inline_response20011 import InlineResponse20011
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
    api_instance = licenses_api.LicensesApi(api_client)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.licenses_list(limit=limit, offset=offset)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling LicensesApi->licenses_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

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

# **licenses_read**
> License licenses_read(id)



### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import licenses_api
from epiccore.model.license import License
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
    api_instance = licenses_api.LicensesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.licenses_read(id)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling LicensesApi->licenses_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**License**](License.md)

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

# **licenses_update**
> TeamSelect licenses_update(id, data)



Grant a team access to this license

### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import licenses_api
from epiccore.model.team_select import TeamSelect
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
    api_instance = licenses_api.LicensesApi(api_client)
    id = "id_example" # str | 
    data = TeamSelect(
        id=1,
    ) # TeamSelect | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.licenses_update(id, data)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling LicensesApi->licenses_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **data** | [**TeamSelect**](TeamSelect.md)|  |

### Return type

[**TeamSelect**](TeamSelect.md)

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

# **licenses_zcad**
> ZenotechLicense licenses_zcad(data)



Creates a ZCAD License server configuration

### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import licenses_api
from epiccore.model.zenotech_license import ZenotechLicense
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
    api_instance = licenses_api.LicensesApi(api_client)
    data = ZenotechLicense(
        display_name="display_name_example",
        license_password="license_password_example",
    ) # ZenotechLicense | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.licenses_zcad(data)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling LicensesApi->licenses_zcad: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ZenotechLicense**](ZenotechLicense.md)|  |

### Return type

[**ZenotechLicense**](ZenotechLicense.md)

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

# **licenses_zcfd**
> ZenotechLicense licenses_zcfd(data)



Creates a ZCFD License server configuration

### Example

* Api Key Authentication (Bearer):
```python
import time
import epiccore
from epiccore.api import licenses_api
from epiccore.model.zenotech_license import ZenotechLicense
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
    api_instance = licenses_api.LicensesApi(api_client)
    data = ZenotechLicense(
        display_name="display_name_example",
        license_password="license_password_example",
    ) # ZenotechLicense | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.licenses_zcfd(data)
        pprint(api_response)
    except epiccore.ApiException as e:
        print("Exception when calling LicensesApi->licenses_zcfd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ZenotechLicense**](ZenotechLicense.md)|  |

### Return type

[**ZenotechLicense**](ZenotechLicense.md)

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

