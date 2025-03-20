# LicensesList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[License]**](License.md) |  | 

## Example

```python
from epiccore.models.licenses_list200_response import LicensesList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LicensesList200Response from a JSON string
licenses_list200_response_instance = LicensesList200Response.from_json(json)
# print the JSON string representation of the object
print LicensesList200Response.to_json()

# convert the object into a dict
licenses_list200_response_dict = licenses_list200_response_instance.to_dict()
# create an instance of LicensesList200Response from a dict
licenses_list200_response_form_dict = licenses_list200_response.from_dict(licenses_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


