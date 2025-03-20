# IaasCost

The cost of the HPC resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the currency | 
**currency** | **str** | Type of currency | 
**currency_symbol** | **str** | Symbol to be used for this currency | 

## Example

```python
from epiccore.models.iaas_cost import IaasCost

# TODO update the JSON string below
json = "{}"
# create an instance of IaasCost from a JSON string
iaas_cost_instance = IaasCost.from_json(json)
# print the JSON string representation of the object
print IaasCost.to_json()

# convert the object into a dict
iaas_cost_dict = iaas_cost_instance.to_dict()
# create an instance of IaasCost from a dict
iaas_cost_form_dict = iaas_cost.from_dict(iaas_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


