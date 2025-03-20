# MonthlyLimit

Monthly limit for this team / user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the currency | 
**currency** | **str** | Type of currency | 
**currency_symbol** | **str** | Symbol to be used for this currency | 

## Example

```python
from epiccore.models.monthly_limit import MonthlyLimit

# TODO update the JSON string below
json = "{}"
# create an instance of MonthlyLimit from a JSON string
monthly_limit_instance = MonthlyLimit.from_json(json)
# print the JSON string representation of the object
print MonthlyLimit.to_json()

# convert the object into a dict
monthly_limit_dict = monthly_limit_instance.to_dict()
# create an instance of MonthlyLimit from a dict
monthly_limit_form_dict = monthly_limit.from_dict(monthly_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


