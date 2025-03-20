# JobAuthStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | **bool** | Is authorisation required for this job? | [optional] [readonly] 
**state** | **str** |  | [optional] 
**job** | [**JobSummary**](JobSummary.md) |  | [optional] 
**user_profile** | [**UserName**](UserName.md) |  | [optional] 
**permissions** | **str** |  | [optional] [readonly] 

## Example

```python
from epiccore.models.job_auth_status import JobAuthStatus

# TODO update the JSON string below
json = "{}"
# create an instance of JobAuthStatus from a JSON string
job_auth_status_instance = JobAuthStatus.from_json(json)
# print the JSON string representation of the object
print JobAuthStatus.to_json()

# convert the object into a dict
job_auth_status_dict = job_auth_status_instance.to_dict()
# create an instance of JobAuthStatus from a dict
job_auth_status_form_dict = job_auth_status.from_dict(job_auth_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


