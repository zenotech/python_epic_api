# JobAuth

Job Authorisation criteria for this team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Is job authorisation enabled? | [optional] [default to False]
**all_jobs** | **bool** | If authorisation is enabled, then does it apply to all jobs? | [optional] [default to False]
**cost_threshold** | [**CostThreshold**](CostThreshold.md) |  | [optional] 
**description_str** | **str** | A user readable description of the state of the job authorisation criteria | [optional] [readonly] 

## Example

```python
from epiccore.models.job_auth import JobAuth

# TODO update the JSON string below
json = "{}"
# create an instance of JobAuth from a JSON string
job_auth_instance = JobAuth.from_json(json)
# print the JSON string representation of the object
print JobAuth.to_json()

# convert the object into a dict
job_auth_dict = job_auth_instance.to_dict()
# create an instance of JobAuth from a dict
job_auth_form_dict = job_auth.from_dict(job_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


