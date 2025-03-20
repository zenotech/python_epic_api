# JobConfiguration

Job configuration options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload** | **List[str]** | When should data be uploaded? | [optional] 
**overwrite_existing** | **bool** | Should uploads overwrite existing data files? | [optional] [default to True]
**data_sync_interval** | **int** | How frequently should the data be uploaded back to the EPIC data store? | [optional] 
**local_submission** | **bool** | Is this job being submitted locally? | [optional] [default to False]

## Example

```python
from epiccore.models.job_configuration import JobConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of JobConfiguration from a JSON string
job_configuration_instance = JobConfiguration.from_json(json)
# print the JSON string representation of the object
print JobConfiguration.to_json()

# convert the object into a dict
job_configuration_dict = job_configuration_instance.to_dict()
# create an instance of JobConfiguration from a dict
job_configuration_form_dict = job_configuration.from_dict(job_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


