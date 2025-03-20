# ApplicationConfigurationSerialiser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_script** | [**Template**](Template.md) |  | 
**stop_script** | [**Template**](Template.md) |  | 
**created** | **datetime** |  | [optional] [readonly] 
**modified** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 

## Example

```python
from epiccore.models.application_configuration_serialiser import ApplicationConfigurationSerialiser

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationConfigurationSerialiser from a JSON string
application_configuration_serialiser_instance = ApplicationConfigurationSerialiser.from_json(json)
# print the JSON string representation of the object
print ApplicationConfigurationSerialiser.to_json()

# convert the object into a dict
application_configuration_serialiser_dict = application_configuration_serialiser_instance.to_dict()
# create an instance of ApplicationConfigurationSerialiser from a dict
application_configuration_serialiser_form_dict = application_configuration_serialiser.from_dict(application_configuration_serialiser_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


