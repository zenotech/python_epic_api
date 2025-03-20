# JobArraySpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of job array - only required for more than one job | [optional] [default to 'Job Array']
**config** | [**JobConfiguration**](JobConfiguration.md) |  | 
**jobs** | [**List[JobDataBinding]**](JobDataBinding.md) | List of job specs to launch | 
**common_data** | [**DataSpec**](DataSpec.md) |  | [optional] 

## Example

```python
from epiccore.models.job_array_spec import JobArraySpec

# TODO update the JSON string below
json = "{}"
# create an instance of JobArraySpec from a JSON string
job_array_spec_instance = JobArraySpec.from_json(json)
# print the JSON string representation of the object
print JobArraySpec.to_json()

# convert the object into a dict
job_array_spec_dict = job_array_spec_instance.to_dict()
# create an instance of JobArraySpec from a dict
job_array_spec_form_dict = job_array_spec.from_dict(job_array_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


