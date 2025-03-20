# JobResidualData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable_name** | **str** | Name of the variable. | [optional] [readonly] 
**values** | **List[str]** | The residual values | [optional] 

## Example

```python
from epiccore.models.job_residual_data import JobResidualData

# TODO update the JSON string below
json = "{}"
# create an instance of JobResidualData from a JSON string
job_residual_data_instance = JobResidualData.from_json(json)
# print the JSON string representation of the object
print JobResidualData.to_json()

# convert the object into a dict
job_residual_data_dict = job_residual_data_instance.to_dict()
# create an instance of JobResidualData from a dict
job_residual_data_form_dict = job_residual_data.from_dict(job_residual_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


