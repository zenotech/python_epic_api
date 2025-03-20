# DesktopNodeType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_code** | **str** | The code for this node type to be used in DesktopNodeLaunchSpec | [optional] 
**name** | **str** | This provides the name of this node type | [optional] [readonly] 
**description** | **str** | This provides a detailed description of this node type | [optional] [readonly] 
**cores** | **int** | Number of cores that this desktop node has | [optional] [readonly] 
**gpus** | **int** | Number of gpus that this desktop node has | [optional] [readonly] 

## Example

```python
from epiccore.models.desktop_node_type import DesktopNodeType

# TODO update the JSON string below
json = "{}"
# create an instance of DesktopNodeType from a JSON string
desktop_node_type_instance = DesktopNodeType.from_json(json)
# print the JSON string representation of the object
print DesktopNodeType.to_json()

# convert the object into a dict
desktop_node_type_dict = desktop_node_type_instance.to_dict()
# create an instance of DesktopNodeType from a dict
desktop_node_type_form_dict = desktop_node_type.from_dict(desktop_node_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


