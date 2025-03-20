# JobDataBinding

List of job specs to launch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for this job | 
**spec** | [**JobSpec**](JobSpec.md) |  | 
**app_options** | **object** | Application specific options | 
**cluster** | [**JobClusterSpec**](JobClusterSpec.md) |  | 
**input_data** | [**DataSpec**](DataSpec.md) |  | [optional] 

## Example

```python
from epiccore.models.job_data_binding import JobDataBinding

# TODO update the JSON string below
json = "{}"
# create an instance of JobDataBinding from a JSON string
job_data_binding_instance = JobDataBinding.from_json(json)
# print the JSON string representation of the object
print JobDataBinding.to_json()

# convert the object into a dict
job_data_binding_dict = job_data_binding_instance.to_dict()
# create an instance of JobDataBinding from a dict
job_data_binding_form_dict = job_data_binding.from_dict(job_data_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


