# JobSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID for this job | [optional] [readonly] 
**name** | **str** | Name of this job | [optional] [readonly] 
**app** | **str** | Name of the application that this job uses | [optional] [readonly] 
**cost** | **str** | Maximum cost for running this job | [optional] [readonly] 
**submitted_by** | **str** | Name of the user who submitted this job | [optional] [readonly] 
**submitted_at** | **str** | Date at which this job was submitted | [optional] [readonly] 

## Example

```python
from epiccore.models.job_summary import JobSummary

# TODO update the JSON string below
json = "{}"
# create an instance of JobSummary from a JSON string
job_summary_instance = JobSummary.from_json(json)
# print the JSON string representation of the object
print JobSummary.to_json()

# convert the object into a dict
job_summary_dict = job_summary_instance.to_dict()
# create an instance of JobSummary from a dict
job_summary_form_dict = job_summary.from_dict(job_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


