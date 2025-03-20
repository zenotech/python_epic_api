# SLA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from epiccore.models.sla import SLA

# TODO update the JSON string below
json = "{}"
# create an instance of SLA from a JSON string
sla_instance = SLA.from_json(json)
# print the JSON string representation of the object
print SLA.to_json()

# convert the object into a dict
sla_dict = sla_instance.to_dict()
# create an instance of SLA from a dict
sla_form_dict = sla.from_dict(sla_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


