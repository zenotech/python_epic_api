# JobLog

The step logs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stdout** | **str** |  | [optional] [readonly] 
**stderr** | **str** |  | [optional] [readonly] 
**app** | **str** |  | [optional] [readonly] 
**last_update** | **str** | Last time the logs were updated | [optional] [readonly] 

## Example

```python
from epiccore.models.job_log import JobLog

# TODO update the JSON string below
json = "{}"
# create an instance of JobLog from a JSON string
job_log_instance = JobLog.from_json(json)
# print the JSON string representation of the object
print JobLog.to_json()

# convert the object into a dict
job_log_dict = job_log_instance.to_dict()
# create an instance of JobLog from a dict
job_log_form_dict = job_log.from_dict(job_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


