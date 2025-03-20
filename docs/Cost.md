# Cost

The cost of the requested resource. May only be present if the valid field is true.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the currency | 
**currency** | **str** | Type of currency | 

## Example

```python
from epiccore.models.cost import Cost

# TODO update the JSON string below
json = "{}"
# create an instance of Cost from a JSON string
cost_instance = Cost.from_json(json)
# print the JSON string representation of the object
print Cost.to_json()

# convert the object into a dict
cost_dict = cost_instance.to_dict()
# create an instance of Cost from a dict
cost_form_dict = cost.from_dict(cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


