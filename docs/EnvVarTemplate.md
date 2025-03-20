# EnvVarTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable_name** | **str** |  | 
**help_text** | **str** |  | 
**var_type** | **str** |  | 
**default** | **str** |  | [optional] 

## Example

```python
from epiccore.models.env_var_template import EnvVarTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of EnvVarTemplate from a JSON string
env_var_template_instance = EnvVarTemplate.from_json(json)
# print the JSON string representation of the object
print EnvVarTemplate.to_json()

# convert the object into a dict
env_var_template_dict = env_var_template_instance.to_dict()
# create an instance of EnvVarTemplate from a dict
env_var_template_form_dict = env_var_template.from_dict(env_var_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


