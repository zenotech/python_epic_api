# SoftwareCost

The cost of the application.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the currency | 
**currency** | **str** | Type of currency | 
**currency_symbol** | **str** | Symbol to be used for this currency | 

## Example

```python
from epiccore.models.software_cost import SoftwareCost

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareCost from a JSON string
software_cost_instance = SoftwareCost.from_json(json)
# print the JSON string representation of the object
print SoftwareCost.to_json()

# convert the object into a dict
software_cost_dict = software_cost_instance.to_dict()
# create an instance of SoftwareCost from a dict
software_cost_form_dict = software_cost.from_dict(software_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


