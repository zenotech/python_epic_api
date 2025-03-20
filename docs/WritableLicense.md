# WritableLicense


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**display_name** | **str** |  | 
**description** | **str** |  | [optional] 
**environment** | [**List[EnvVar]**](EnvVar.md) |  | 
**application** | **int** |  | [optional] 

## Example

```python
from epiccore.models.writable_license import WritableLicense

# TODO update the JSON string below
json = "{}"
# create an instance of WritableLicense from a JSON string
writable_license_instance = WritableLicense.from_json(json)
# print the JSON string representation of the object
print WritableLicense.to_json()

# convert the object into a dict
writable_license_dict = writable_license_instance.to_dict()
# create an instance of WritableLicense from a dict
writable_license_form_dict = writable_license.from_dict(writable_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


