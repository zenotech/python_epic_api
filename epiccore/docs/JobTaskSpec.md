# JobTaskSpec

List of task definitions that make up this job
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | A reference to help you identify this task | 
**partitions** | **int** | How many partitions/tasks will this task be submitted as. | 
**runtime** | **int** | Maximum runtime for this task in whole hours. | 
**task_distribution** | **str** | How should the partitions be distributed on the HPC cluster | 
**hyperthreading** | **bool** | Make use of hyperthreaded core where available | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


