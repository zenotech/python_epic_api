# TaskQuote

List of job quotes for individual tasks in this request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | The reference given in the quote request, to help you identify this task. | [optional] [readonly] 
**queue_code** | **str** | The Queue code of the queue for this quote | [optional] 
**iaas_cost** | [**IaasCost**](IaasCost.md) |  | [optional] 
**software_cost** | [**SoftwareCost**](SoftwareCost.md) |  | [optional] 
**service_charge** | [**ServiceCharge**](ServiceCharge.md) |  | [optional] 
**discount** | [**Discount**](Discount.md) |  | [optional] 
**tax** | [**Tax**](Tax.md) |  | [optional] 
**total** | [**Total1**](Total1.md) |  | [optional] 

## Example

```python
from epiccore.models.task_quote import TaskQuote

# TODO update the JSON string below
json = "{}"
# create an instance of TaskQuote from a JSON string
task_quote_instance = TaskQuote.from_json(json)
# print the JSON string representation of the object
print TaskQuote.to_json()

# convert the object into a dict
task_quote_dict = task_quote_instance.to_dict()
# create an instance of TaskQuote from a dict
task_quote_form_dict = task_quote.from_dict(task_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


