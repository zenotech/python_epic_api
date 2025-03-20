# ProjectDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [optional] [readonly] 
**project_id** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] 
**closed** | **bool** |  | [optional] 
**all_users** | **bool** |  | [optional] 
**authorized_user_profiles** | **List[int]** |  | [optional] 
**has_budget** | **bool** |  | [optional] [readonly] 
**spend_limit** | [**SpendLimit**](SpendLimit.md) |  | [optional] 
**current_spend** | [**CurrentSpend**](CurrentSpend.md) |  | [optional] 

## Example

```python
from epiccore.models.project_details import ProjectDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDetails from a JSON string
project_details_instance = ProjectDetails.from_json(json)
# print the JSON string representation of the object
print ProjectDetails.to_json()

# convert the object into a dict
project_details_dict = project_details_instance.to_dict()
# create an instance of ProjectDetails from a dict
project_details_form_dict = project_details.from_dict(project_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


