# MaxLimit

Maximum monthly spend limit for the current user's billing profile. The sum of all user/team limits may not exceed this value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the currency | 
**currency** | **str** | Type of currency | 

## Example

```python
from epiccore.models.max_limit import MaxLimit

# TODO update the JSON string below
json = "{}"
# create an instance of MaxLimit from a JSON string
max_limit_instance = MaxLimit.from_json(json)
# print the JSON string representation of the object
print MaxLimit.to_json()

# convert the object into a dict
max_limit_dict = max_limit_instance.to_dict()
# create an instance of MaxLimit from a dict
max_limit_form_dict = max_limit.from_dict(max_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


