# SiteConfigurationSerialiser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_configuration** | [**ApplicationConfigurationSerialiser**](ApplicationConfigurationSerialiser.md) |  | 
**environment_script** | [**Template**](Template.md) |  | 
**env_variables** | [**List[EnvironmentVariable]**](EnvironmentVariable.md) |  | 
**created** | **datetime** |  | [optional] [readonly] 
**modified** | **datetime** |  | [optional] [readonly] 

## Example

```python
from epiccore.models.site_configuration_serialiser import SiteConfigurationSerialiser

# TODO update the JSON string below
json = "{}"
# create an instance of SiteConfigurationSerialiser from a JSON string
site_configuration_serialiser_instance = SiteConfigurationSerialiser.from_json(json)
# print the JSON string representation of the object
print SiteConfigurationSerialiser.to_json()

# convert the object into a dict
site_configuration_serialiser_dict = site_configuration_serialiser_instance.to_dict()
# create an instance of SiteConfigurationSerialiser from a dict
site_configuration_serialiser_form_dict = site_configuration_serialiser.from_dict(site_configuration_serialiser_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


