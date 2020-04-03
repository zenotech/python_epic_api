# JobAuth

Job Authorisation criteria for this team
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Is job authorisation enabled? | [optional] [default to False]
**all_jobs** | **bool** | If authorisation is enabled, then does it apply to all jobs? | [optional] [default to False]
**cost_threshold** | **str** | If job authorisation is enabled and all_jobs is false, jobs costing above this value will require authorisation. | [optional] 
**description_str** | **str** | A user readable description of the state of the job authorisation criteria | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


