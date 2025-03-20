# DesktopInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**status** | **str** | Current desktop status | [optional] [readonly] 
**connection_string** | **str** | The URL or hostname of the desktop | [optional] [readonly] 
**node_type** | [**DesktopNodeType**](DesktopNodeType.md) |  | [optional] 
**launched_by** | **str** | Full name of user that launched the desktop | [optional] [readonly] 
**team** | **str** | ID of the active Team for the desktop | [optional] [readonly] 
**created** | **datetime** |  | [optional] [readonly] 
**runtime** | **str** | The requested runtime in hours | [optional] [readonly] 

## Example

```python
from epiccore.models.desktop_instance import DesktopInstance

# TODO update the JSON string below
json = "{}"
# create an instance of DesktopInstance from a JSON string
desktop_instance_instance = DesktopInstance.from_json(json)
# print the JSON string representation of the object
print DesktopInstance.to_json()

# convert the object into a dict
desktop_instance_dict = desktop_instance_instance.to_dict()
# create an instance of DesktopInstance from a dict
desktop_instance_form_dict = desktop_instance.from_dict(desktop_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


