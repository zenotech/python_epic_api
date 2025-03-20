# License


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**active** | **bool** |  | [optional] 
**display_name** | **str** |  | 
**description** | **str** |  | [optional] 
**environment** | [**List[EnvVar]**](EnvVar.md) |  | [optional] [readonly] 
**application** | [**Application**](Application.md) |  | [optional] 

## Example

```python
from epiccore.models.license import License

# TODO update the JSON string below
json = "{}"
# create an instance of License from a JSON string
license_instance = License.from_json(json)
# print the JSON string representation of the object
print License.to_json()

# convert the object into a dict
license_dict = license_instance.to_dict()
# create an instance of License from a dict
license_form_dict = license.from_dict(license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


