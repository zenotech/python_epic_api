# Job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID for this Job | [optional] [readonly] 
**name** | **str** | Name of this job | [optional] [readonly] 
**app** | **str** | Name of the application that this job uses | [optional] [readonly] 
**cost** | **str** | Maximum cost for running this job | [optional] [readonly] 
**submitted_by** | **str** | Name of the user who submitted this job | [optional] [readonly] 
**submitted_at** | **str** | Date at which this job was submitted | [optional] [readonly] 
**finished** | **bool** | Has this job finished? | [optional] [readonly] 
**project** | **int** | Project ID to bill this job against | [optional] 
**invoice_reference** | **str** | Invoice reference - this text will appear on the monthly invoice against this jobs charges | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


