# DesktopNodeLaunchSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_code** | **str** | node_code of the node type to launch. Valid values are obtained from the catalog/desktop/ endpoint | 
**runtime** | **int** | Runtime in hours to run this desktop node for. This is the maximum runtime as the viz node can be stopped earlier and you will only be charged for the elapsed time | 
**secure_ip** | **bool** | Should we restrict which IPs can connect to this node? | [optional] [default to False]
**ip_address** | **str** | IPv4 Address to restrict connections to this node from | [optional] 
**invoice_reference** | **str** | Invoice reference - this text will appear on the monthly invoice against this nodes charges | [optional] 
**data_path** | [**DataSpec**](DataSpec.md) |  | 
**mount_type** | **str** | How should the data folder be mounted to the desktop. Offline takes a copy of the data and will not be automatically synced back to the data store. | 
**project** | **int** | Project ID to bill this desktop node against | [optional] 

## Example

```python
from epiccore.models.desktop_node_launch_spec import DesktopNodeLaunchSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DesktopNodeLaunchSpec from a JSON string
desktop_node_launch_spec_instance = DesktopNodeLaunchSpec.from_json(json)
# print the JSON string representation of the object
print DesktopNodeLaunchSpec.to_json()

# convert the object into a dict
desktop_node_launch_spec_dict = desktop_node_launch_spec_instance.to_dict()
# create an instance of DesktopNodeLaunchSpec from a dict
desktop_node_launch_spec_form_dict = desktop_node_launch_spec.from_dict(desktop_node_launch_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


