# Job


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID for this job | [optional] [readonly] 
**name** | **str** | Name of this job | [optional] [readonly] 
**app** | **str** | Name of the application that this job uses | [optional] [readonly] 
**app_options** | **object** | Job app options | [optional] [readonly] 
**application_version** | **str** | Application version ID | [optional] [readonly] 
**cost** | **str** | Maximum cost for running this job | [optional] [readonly] 
**status** | **str** | Current status of this job | [optional] [readonly] 
**submitted_by** | **str** | Name of the user who submitted this job | [optional] [readonly] 
**submitted_at** | **str** | Date at which this job was submitted | [optional] [readonly] 
**finished** | **bool** | Has this job finished? | [optional] [readonly] 
**resource** | [**BatchQueueDetails**](BatchQueueDetails.md) |  | [optional] 
**project** | **int** | Project ID to bill this job against | [optional] 
**invoice_reference** | **str** | Invoice reference - this text will appear on the monthly invoice against this jobs charges | [optional] 
**config** | [**JobConfiguration**](JobConfiguration.md) |  | [optional] 
**job_steps** | [**List[JobStep]**](JobStep.md) | The job steps associated with this Job | [optional] [readonly] 
**input_data** | [**DataSpec**](DataSpec.md) |  | [optional] 
**requires_auth** | **bool** | Does this job require additional authorisation? | [optional] [readonly] 
**array** | **int** | ID of associated Job Array | [optional] [readonly] 

## Example

```python
from epiccore.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print Job.to_json()

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_form_dict = job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


