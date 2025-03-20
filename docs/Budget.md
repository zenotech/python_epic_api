# Budget

Monthly budget for this team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_limit** | [**MonthlyLimit**](MonthlyLimit.md) |  | 

## Example

```python
from epiccore.models.budget import Budget

# TODO update the JSON string below
json = "{}"
# create an instance of Budget from a JSON string
budget_instance = Budget.from_json(json)
# print the JSON string representation of the object
print Budget.to_json()

# convert the object into a dict
budget_dict = budget_instance.to_dict()
# create an instance of Budget from a dict
budget_form_dict = budget.from_dict(budget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


