# JobAppOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_options** | **object** | Application specific options to update | 
**config** | [**JobConfiguration**](JobConfiguration.md) |  | 

## Example

```python
from epiccore.models.job_app_options import JobAppOptions

# TODO update the JSON string below
json = "{}"
# create an instance of JobAppOptions from a JSON string
job_app_options_instance = JobAppOptions.from_json(json)
# print the JSON string representation of the object
print JobAppOptions.to_json()

# convert the object into a dict
job_app_options_dict = job_app_options_instance.to_dict()
# create an instance of JobAppOptions from a dict
job_app_options_form_dict = job_app_options.from_dict(job_app_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


