# JobClusterSpec

Cluster configuration to launch the job on

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queue_code** | **str** | Queue code of cluster queue to run this job on | 

## Example

```python
from epiccore.models.job_cluster_spec import JobClusterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of JobClusterSpec from a JSON string
job_cluster_spec_instance = JobClusterSpec.from_json(json)
# print the JSON string representation of the object
print JobClusterSpec.to_json()

# convert the object into a dict
job_cluster_spec_dict = job_cluster_spec_instance.to_dict()
# create an instance of JobClusterSpec from a dict
job_cluster_spec_form_dict = job_cluster_spec.from_dict(job_cluster_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


