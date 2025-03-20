# Team

Team for which this limit applies. Is Null if this is the user's limits

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID for this team | [optional] [readonly] 
**name** | **str** | Name of this team | [optional] [readonly] 
**number_of_members** | **int** | Number of members in this team | [optional] [readonly] 
**user_role** | **str** | Your role in this team | [optional] [readonly] 

## Example

```python
from epiccore.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print Team.to_json()

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_form_dict = team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


