# CurrentSpend

Current monthly spend for this project code.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the currency | 
**currency** | **str** | Type of currency | 
**currency_symbol** | **str** | Symbol to be used for this currency | 

## Example

```python
from epiccore.models.current_spend import CurrentSpend

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentSpend from a JSON string
current_spend_instance = CurrentSpend.from_json(json)
# print the JSON string representation of the object
print CurrentSpend.to_json()

# convert the object into a dict
current_spend_dict = current_spend_instance.to_dict()
# create an instance of CurrentSpend from a dict
current_spend_form_dict = current_spend.from_dict(current_spend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


