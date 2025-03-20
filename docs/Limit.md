# Limit

List of limits for all teams linked to the current user's billing profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | [**Team**](Team.md) |  | [optional] 
**budget** | [**Budget**](Budget.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**jobauth** | [**JobAuth**](JobAuth.md) |  | [optional] 
**id** | **int** | Team id for this limit. -1 signifies the user&#39;s limits | 

## Example

```python
from epiccore.models.limit import Limit

# TODO update the JSON string below
json = "{}"
# create an instance of Limit from a JSON string
limit_instance = Limit.from_json(json)
# print the JSON string representation of the object
print Limit.to_json()

# convert the object into a dict
limit_dict = limit_instance.to_dict()
# create an instance of Limit from a dict
limit_form_dict = limit.from_dict(limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


