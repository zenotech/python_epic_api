# TeamDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID for this team | [optional] [readonly] 
**name** | **str** | Name of this team | [optional] [readonly] 
**number_of_members** | **int** | Number of members in this team | [optional] [readonly] 
**user_role** | **str** | Your role in this team | [optional] [readonly] 
**members** | **str** | List of user ids and roles for members of this team | [optional] [readonly] 

## Example

```python
from epiccore.models.team_details import TeamDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TeamDetails from a JSON string
team_details_instance = TeamDetails.from_json(json)
# print the JSON string representation of the object
print TeamDetails.to_json()

# convert the object into a dict
team_details_dict = team_details_instance.to_dict()
# create an instance of TeamDetails from a dict
team_details_form_dict = team_details.from_dict(team_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


