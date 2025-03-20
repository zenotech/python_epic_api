# JobauthList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[JobAuthStatus]**](JobAuthStatus.md) |  | 

## Example

```python
from epiccore.models.jobauth_list200_response import JobauthList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of JobauthList200Response from a JSON string
jobauth_list200_response_instance = JobauthList200Response.from_json(json)
# print the JSON string representation of the object
print JobauthList200Response.to_json()

# convert the object into a dict
jobauth_list200_response_dict = jobauth_list200_response_instance.to_dict()
# create an instance of JobauthList200Response from a dict
jobauth_list200_response_form_dict = jobauth_list200_response.from_dict(jobauth_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


