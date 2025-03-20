# JobTaskSpec

List of task definitions that make up this job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | A reference to help you identify this task | 
**partitions** | **int** | How many partitions/tasks will this task be submitted as. | 
**runtime** | **int** | Maximum runtime for this task in whole hours. | 
**task_distribution** | **str** | How should the partitions be distributed on the HPC cluster | 
**tasks_per_device** | **int** | How many tasks should be scheduled per device. | [optional] 
**hyperthreading** | **bool** | Make use of hyperthreaded core where available | [optional] [default to True]

## Example

```python
from epiccore.models.job_task_spec import JobTaskSpec

# TODO update the JSON string below
json = "{}"
# create an instance of JobTaskSpec from a JSON string
job_task_spec_instance = JobTaskSpec.from_json(json)
# print the JSON string representation of the object
print JobTaskSpec.to_json()

# convert the object into a dict
job_task_spec_dict = job_task_spec_instance.to_dict()
# create an instance of JobTaskSpec from a dict
job_task_spec_form_dict = job_task_spec.from_dict(job_task_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


