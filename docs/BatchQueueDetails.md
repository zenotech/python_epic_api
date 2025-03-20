# BatchQueueDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queue_code** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**cluster_name** | **str** |  | [optional] [readonly] 
**max_runtime** | **int** |  | [optional] 
**max_allocation** | **int** |  | [optional] 
**reported_avail_tasks** | **int** |  | [optional] 
**reported_max_tasks** | **int** |  | [optional] 
**sla** | [**SLA**](SLA.md) |  | 
**maintenance_mode** | **bool** |  | [optional] [readonly] 
**resource_config** | [**ClusterNodeConfig**](ClusterNodeConfig.md) |  | 
**supports_local_submission** | **bool** |  | [optional] [readonly] 

## Example

```python
from epiccore.models.batch_queue_details import BatchQueueDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BatchQueueDetails from a JSON string
batch_queue_details_instance = BatchQueueDetails.from_json(json)
# print the JSON string representation of the object
print BatchQueueDetails.to_json()

# convert the object into a dict
batch_queue_details_dict = batch_queue_details_instance.to_dict()
# create an instance of BatchQueueDetails from a dict
batch_queue_details_form_dict = batch_queue_details.from_dict(batch_queue_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


