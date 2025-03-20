# JobstepResponseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID for this refresh request | [optional] [readonly] 
**job_step** | **int** | The ID of the running job step to refresh | 
**response_recieved** | **bool** | Has the refresh completed? | [optional] 

## Example

```python
from epiccore.models.jobstep_response_request import JobstepResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobstepResponseRequest from a JSON string
jobstep_response_request_instance = JobstepResponseRequest.from_json(json)
# print the JSON string representation of the object
print JobstepResponseRequest.to_json()

# convert the object into a dict
jobstep_response_request_dict = jobstep_response_request_instance.to_dict()
# create an instance of JobstepResponseRequest from a dict
jobstep_response_request_form_dict = jobstep_response_request.from_dict(jobstep_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


