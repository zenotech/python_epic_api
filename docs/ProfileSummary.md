# ProfileSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**display_currency** | **str** |  | [optional] 
**display_currency_symbol** | **str** |  | [optional] [readonly] 

## Example

```python
from epiccore.models.profile_summary import ProfileSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileSummary from a JSON string
profile_summary_instance = ProfileSummary.from_json(json)
# print the JSON string representation of the object
print ProfileSummary.to_json()

# convert the object into a dict
profile_summary_dict = profile_summary_instance.to_dict()
# create an instance of ProfileSummary from a dict
profile_summary_form_dict = profile_summary.from_dict(profile_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


