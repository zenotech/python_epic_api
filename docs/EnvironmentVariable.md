# EnvironmentVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable_name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from epiccore.models.environment_variable import EnvironmentVariable

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentVariable from a JSON string
environment_variable_instance = EnvironmentVariable.from_json(json)
# print the JSON string representation of the object
print EnvironmentVariable.to_json()

# convert the object into a dict
environment_variable_dict = environment_variable_instance.to_dict()
# create an instance of EnvironmentVariable from a dict
environment_variable_form_dict = environment_variable.from_dict(environment_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


