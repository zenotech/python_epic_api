# CostThreshold

If job authorisation is enabled and all_jobs is false, jobs costing above this value will require authorisation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the currency | 
**currency** | **str** | Type of currency | 
**currency_symbol** | **str** | Symbol to be used for this currency | 

## Example

```python
from epiccore.models.cost_threshold import CostThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of CostThreshold from a JSON string
cost_threshold_instance = CostThreshold.from_json(json)
# print the JSON string representation of the object
print CostThreshold.to_json()

# convert the object into a dict
cost_threshold_dict = cost_threshold_instance.to_dict()
# create an instance of CostThreshold from a dict
cost_threshold_form_dict = cost_threshold.from_dict(cost_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


