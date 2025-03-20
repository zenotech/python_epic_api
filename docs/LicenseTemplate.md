# LicenseTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**application** | [**Application**](Application.md) |  | [optional] 
**environment** | [**List[EnvVarTemplate]**](EnvVarTemplate.md) |  | [optional] [readonly] 

## Example

```python
from epiccore.models.license_template import LicenseTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseTemplate from a JSON string
license_template_instance = LicenseTemplate.from_json(json)
# print the JSON string representation of the object
print LicenseTemplate.to_json()

# convert the object into a dict
license_template_dict = license_template_instance.to_dict()
# create an instance of LicenseTemplate from a dict
license_template_form_dict = license_template.from_dict(license_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


