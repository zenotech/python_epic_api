# FileDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID for this folder | [optional] [readonly] 
**meta_data** | **object** | File meta-data | [optional] [readonly] 
**created** | **datetime** | Creation time | [optional] [readonly] 
**modified** | **datetime** |  | [optional] [readonly] 
**name** | **str** | File name | [optional] [readonly] 
**obj_key** | **str** | S3 key reference | [optional] [readonly] 
**size** | **int** |  | [optional] 
**last_modified** | **datetime** | Last modified time | [optional] [readonly] 
**folder** | **int** | Folder name | [optional] [readonly] 

## Example

```python
from epiccore.models.file_details import FileDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FileDetails from a JSON string
file_details_instance = FileDetails.from_json(json)
# print the JSON string representation of the object
print FileDetails.to_json()

# convert the object into a dict
file_details_dict = file_details_instance.to_dict()
# create an instance of FileDetails from a dict
file_details_form_dict = file_details.from_dict(file_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


