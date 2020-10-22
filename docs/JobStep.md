# JobStep

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_name** | **str** | The name of this job step | 
**id** | **int** | jobstep id | [optional] [readonly] 
**run_if_previous_step_fails** | **bool** | Whether this job step will run if the previous step fails | [optional] 
**node_count** | **int** | Number of nodes this job step will run on | [optional] 
**num_tasks** | **int** | Number of tasks that will run for this job step | [optional] 
**tasks_per_node** | **int** | Number of tasks that will run on each node | [optional] 
**threads_per_task** | **int** | Number of threads assigned to each task | [optional] 
**max_runtime** | **int** | Maximum runtime in hours that this job step will run for | [optional] 
**status** | **str, none_type** | Status of this jobstep | [optional] 
**exit_code** | **int, none_type** | Unix exit code for this job step | [optional] 
**start_time** | **datetime, none_type** | Time this job step started running | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


