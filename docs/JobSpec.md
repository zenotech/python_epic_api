# JobSpec

Job specification for this job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_code** | **str** | The App Code of the application_version to launch. Valid values are obtained from the catalog/applications/ endpoint | 
**project** | **int** | Project ID to bill this job against | [optional] 
**tasks** | [**List[JobTaskSpec]**](JobTaskSpec.md) | List of task definitions that make up this job | 
**queue_code** | **str** | (Optional) Code of cluster queue for the quote. This will just return the quotes for that queue. If not present the quote will be for all available queues | [optional] 

## Example

```python
from epiccore.models.job_spec import JobSpec

# TODO update the JSON string below
json = "{}"
# create an instance of JobSpec from a JSON string
job_spec_instance = JobSpec.from_json(json)
# print the JSON string representation of the object
print JobSpec.to_json()

# convert the object into a dict
job_spec_dict = job_spec_instance.to_dict()
# create an instance of JobSpec from a dict
job_spec_form_dict = job_spec.from_dict(job_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


