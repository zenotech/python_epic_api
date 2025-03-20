# BatchApplicationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**product** | [**ProductName**](ProductName.md) |  | 
**versions** | [**List[BatchApplicationVersionDetails]**](BatchApplicationVersionDetails.md) |  | [optional] [readonly] 
**permission_to_use** | **bool** | Does your account have permission to use this application? | [optional] [readonly] 
**supports_cases** | **bool** |  | [optional] 

## Example

```python
from epiccore.models.batch_application_list import BatchApplicationList

# TODO update the JSON string below
json = "{}"
# create an instance of BatchApplicationList from a JSON string
batch_application_list_instance = BatchApplicationList.from_json(json)
# print the JSON string representation of the object
print BatchApplicationList.to_json()

# convert the object into a dict
batch_application_list_dict = batch_application_list_instance.to_dict()
# create an instance of BatchApplicationList from a dict
batch_application_list_form_dict = batch_application_list.from_dict(batch_application_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


