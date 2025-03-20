# JobQuote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_quotes** | [**List[TaskQuote]**](TaskQuote.md) | List of job quotes for individual tasks in this request | [optional] 
**totals** | [**List[TaskQuote]**](TaskQuote.md) | List of job quote totals for this request | [optional] 

## Example

```python
from epiccore.models.job_quote import JobQuote

# TODO update the JSON string below
json = "{}"
# create an instance of JobQuote from a JSON string
job_quote_instance = JobQuote.from_json(json)
# print the JSON string representation of the object
print JobQuote.to_json()

# convert the object into a dict
job_quote_dict = job_quote_instance.to_dict()
# create an instance of JobQuote from a dict
job_quote_form_dict = job_quote.from_dict(job_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


