# BatchApplicationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**product** | [**ProductName**](ProductName.md) |  | 
**version** | [**List[BatchApplicationVersionDetails]**](BatchApplicationVersionDetails.md) |  | [optional] [readonly] 
**permission_to_use** | **bool** | Does your account have permission to use this application? | [optional] [readonly] 

## Example

```python
from epiccore.models.batch_application_details import BatchApplicationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BatchApplicationDetails from a JSON string
batch_application_details_instance = BatchApplicationDetails.from_json(json)
# print the JSON string representation of the object
print BatchApplicationDetails.to_json()

# convert the object into a dict
batch_application_details_dict = batch_application_details_instance.to_dict()
# create an instance of BatchApplicationDetails from a dict
batch_application_details_form_dict = batch_application_details.from_dict(batch_application_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


