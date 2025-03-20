# Total

The current total monthly spend limit for the current user's billing profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the currency | 
**currency** | **str** | Type of currency | 

## Example

```python
from epiccore.models.total import Total

# TODO update the JSON string below
json = "{}"
# create an instance of Total from a JSON string
total_instance = Total.from_json(json)
# print the JSON string representation of the object
print Total.to_json()

# convert the object into a dict
total_dict = total_instance.to_dict()
# create an instance of Total from a dict
total_form_dict = total.from_dict(total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


