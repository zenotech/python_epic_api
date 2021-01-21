# JobSpec

Job specification for this job
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_version** | **int** | ID of the application_version to launch. Valid values are obtained from the catalog/applications/ endpoint | 
**project** | **int** | Project ID to bill this job against | [optional] 
**tasks** | [**list[JobTaskSpec]**](JobTaskSpec.md) | List of task definitions that make up this job | 
**queue** | **int** | (Optional) ID of cluster queue for the quote. This will just return the quotes for that queue. If not present the quote will be for all available queues | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


