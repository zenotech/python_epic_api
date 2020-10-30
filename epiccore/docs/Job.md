# Job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID for this job | [optional] [readonly] 
**name** | **str** | Name of this job | [optional] [readonly] 
**app** | **str** | Name of the application that this job uses | [optional] [readonly] 
**application_version** | **int** | Application version ID | [optional] [readonly] 
**cost** | **str** | Maximum cost for running this job | [optional] [readonly] 
**status** | **str** | Current status of this job | [optional] [readonly] 
**submitted_by** | **str** | Name of the user who submitted this job | [optional] [readonly] 
**submitted_at** | **str** | Date at which this job was submitted | [optional] [readonly] 
**finished** | **bool** | Has this job finished? | [optional] [readonly] 
**resource** | [**BatchQueueDetails**](BatchQueueDetails.md) |  | [optional] 
**project** | **int** | Project ID to bill this job against | [optional] 
**invoice_reference** | **str** | Invoice reference - this text will appear on the monthly invoice against this jobs charges | [optional] 
**config** | [**JobConfiguration**](JobConfiguration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


