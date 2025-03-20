# Limits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | [**List[Limit]**](Limit.md) | List of limits for all teams linked to the current user&#39;s billing profile | 
**max_limit** | [**MaxLimit**](MaxLimit.md) |  | [optional] 
**max_limit_str** | **str** | Maximum monthly spend limit for the current user&#39;s billing profile as a string in user&#39;s display currency | [optional] [readonly] 
**total** | [**Total**](Total.md) |  | [optional] 
**total_str** | **str** | Current total monthly spend limit as a string | [optional] [readonly] 

## Example

```python
from epiccore.models.limits import Limits

# TODO update the JSON string below
json = "{}"
# create an instance of Limits from a JSON string
limits_instance = Limits.from_json(json)
# print the JSON string representation of the object
print Limits.to_json()

# convert the object into a dict
limits_dict = limits_instance.to_dict()
# create an instance of Limits from a dict
limits_form_dict = limits.from_dict(limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


