# Total1

The total cost of the job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the currency | 
**currency** | **str** | Type of currency | 
**currency_symbol** | **str** | Symbol to be used for this currency | 

## Example

```python
from epiccore.models.total1 import Total1

# TODO update the JSON string below
json = "{}"
# create an instance of Total1 from a JSON string
total1_instance = Total1.from_json(json)
# print the JSON string representation of the object
print Total1.to_json()

# convert the object into a dict
total1_dict = total1_instance.to_dict()
# create an instance of Total1 from a dict
total1_form_dict = total1.from_dict(total1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


