# SpendLimit

Maximum monthly spend limit for this project code.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the currency | 
**currency** | **str** | Type of currency | 
**currency_symbol** | **str** | Symbol to be used for this currency | 

## Example

```python
from epiccore.models.spend_limit import SpendLimit

# TODO update the JSON string below
json = "{}"
# create an instance of SpendLimit from a JSON string
spend_limit_instance = SpendLimit.from_json(json)
# print the JSON string representation of the object
print SpendLimit.to_json()

# convert the object into a dict
spend_limit_dict = spend_limit_instance.to_dict()
# create an instance of SpendLimit from a dict
spend_limit_form_dict = spend_limit.from_dict(spend_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


