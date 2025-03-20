# BatchApplicationVersionDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_code** | **str** |  | 
**version** | **str** |  | 
**available_on** | **List[str]** | List of the batch cluster queue codes with the application available | [optional] [readonly] 

## Example

```python
from epiccore.models.batch_application_version_details import BatchApplicationVersionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BatchApplicationVersionDetails from a JSON string
batch_application_version_details_instance = BatchApplicationVersionDetails.from_json(json)
# print the JSON string representation of the object
print BatchApplicationVersionDetails.to_json()

# convert the object into a dict
batch_application_version_details_dict = batch_application_version_details_instance.to_dict()
# create an instance of BatchApplicationVersionDetails from a dict
batch_application_version_details_form_dict = batch_application_version_details.from_dict(batch_application_version_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


