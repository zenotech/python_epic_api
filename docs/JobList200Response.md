# JobList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Job]**](Job.md) |  | 

## Example

```python
from epiccore.models.job_list200_response import JobList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of JobList200Response from a JSON string
job_list200_response_instance = JobList200Response.from_json(json)
# print the JSON string representation of the object
print JobList200Response.to_json()

# convert the object into a dict
job_list200_response_dict = job_list200_response_instance.to_dict()
# create an instance of JobList200Response from a dict
job_list200_response_form_dict = job_list200_response.from_dict(job_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


