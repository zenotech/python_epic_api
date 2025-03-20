# DesktopList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DesktopInstance]**](DesktopInstance.md) |  | 

## Example

```python
from epiccore.models.desktop_list200_response import DesktopList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DesktopList200Response from a JSON string
desktop_list200_response_instance = DesktopList200Response.from_json(json)
# print the JSON string representation of the object
print DesktopList200Response.to_json()

# convert the object into a dict
desktop_list200_response_dict = desktop_list200_response_instance.to_dict()
# create an instance of DesktopList200Response from a dict
desktop_list200_response_form_dict = desktop_list200_response.from_dict(desktop_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


