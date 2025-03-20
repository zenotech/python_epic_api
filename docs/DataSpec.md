# DataSpec

Input data specification for this desktop

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path to the folder containing the data for this job | 

## Example

```python
from epiccore.models.data_spec import DataSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DataSpec from a JSON string
data_spec_instance = DataSpec.from_json(json)
# print the JSON string representation of the object
print DataSpec.to_json()

# convert the object into a dict
data_spec_dict = data_spec_instance.to_dict()
# create an instance of DataSpec from a dict
data_spec_form_dict = data_spec.from_dict(data_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


