# ClusterNodeConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerator** | [**AcceleratorConfig**](AcceleratorConfig.md) |  | 
**cpus** | **int** |  | [optional] 
**cpu_generation** | **str** |  | [optional] 
**cores_per_cpu** | **int** |  | [optional] 
**threads_per_core** | **int** |  | [optional] [readonly] 
**memory** | **str** |  | [optional] [readonly] 

## Example

```python
from epiccore.models.cluster_node_config import ClusterNodeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodeConfig from a JSON string
cluster_node_config_instance = ClusterNodeConfig.from_json(json)
# print the JSON string representation of the object
print ClusterNodeConfig.to_json()

# convert the object into a dict
cluster_node_config_dict = cluster_node_config_instance.to_dict()
# create an instance of ClusterNodeConfig from a dict
cluster_node_config_form_dict = cluster_node_config.from_dict(cluster_node_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


