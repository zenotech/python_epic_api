# TeamsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Team]**](Team.md) |  | 

## Example

```python
from epiccore.models.teams_list200_response import TeamsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsList200Response from a JSON string
teams_list200_response_instance = TeamsList200Response.from_json(json)
# print the JSON string representation of the object
print TeamsList200Response.to_json()

# convert the object into a dict
teams_list200_response_dict = teams_list200_response_instance.to_dict()
# create an instance of TeamsList200Response from a dict
teams_list200_response_form_dict = teams_list200_response.from_dict(teams_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


