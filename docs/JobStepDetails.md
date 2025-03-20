# JobStepDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | jobstep id | [optional] [readonly] 
**parent_job** | **int** | The id of the parent job for this step | [optional] [readonly] 
**run_if_previous_step_fails** | **bool** | Whether this job step will run if the previous step fails | [optional] 
**step_name** | **str** | The name of this job step | 
**node_count** | **int** | Number of nodes this job step will run on | [optional] 
**num_tasks** | **int** | Number of tasks that will run for this job step | [optional] 
**tasks_per_node** | **int** | Number of tasks that will run on each node | [optional] 
**threads_per_task** | **int** | Number of threads assigned to each task | [optional] 
**max_runtime** | **int** | Maximum runtime in hours that this job step will run for | [optional] 
**status** | **str** | Status of this jobstep | [optional] 
**exit_code** | **int** | Unix exit code for this job step | [optional] 
**start** | **datetime** | Time this job step started running | [optional] 
**end** | **datetime** | Time this job step finished running | [optional] 
**wallclock** | **str** |  | [optional] [readonly] 
**logs** | [**JobLog**](JobLog.md) |  | [optional] 

## Example

```python
from epiccore.models.job_step_details import JobStepDetails

# TODO update the JSON string below
json = "{}"
# create an instance of JobStepDetails from a JSON string
job_step_details_instance = JobStepDetails.from_json(json)
# print the JSON string representation of the object
print JobStepDetails.to_json()

# convert the object into a dict
job_step_details_dict = job_step_details_instance.to_dict()
# create an instance of JobStepDetails from a dict
job_step_details_form_dict = job_step_details.from_dict(job_step_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


