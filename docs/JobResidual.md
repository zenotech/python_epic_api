# JobResidual


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variables** | **List[str]** | A list of the available residual variable names | 
**residual_values** | [**List[JobResidualData]**](JobResidualData.md) | The values of an individual residual variable, including xaxis data | [optional] [readonly] 

## Example

```python
from epiccore.models.job_residual import JobResidual

# TODO update the JSON string below
json = "{}"
# create an instance of JobResidual from a JSON string
job_residual_instance = JobResidual.from_json(json)
# print the JSON string representation of the object
print JobResidual.to_json()

# convert the object into a dict
job_residual_dict = job_residual_instance.to_dict()
# create an instance of JobResidual from a dict
job_residual_form_dict = job_residual.from_dict(job_residual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


