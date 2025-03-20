# Folder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID for this folder | [optional] [readonly] 
**created** | **datetime** | Creation time | [optional] [readonly] 
**modified** | **datetime** | Last modified time | [optional] [readonly] 
**name** | **str** | Folder name | [optional] [readonly] 
**obj_key** | **str** | S3 key reference | [optional] [readonly] 
**last_modified** | **datetime** | Last modified time | [optional] 

## Example

```python
from epiccore.models.folder import Folder

# TODO update the JSON string below
json = "{}"
# create an instance of Folder from a JSON string
folder_instance = Folder.from_json(json)
# print the JSON string representation of the object
print Folder.to_json()

# convert the object into a dict
folder_dict = folder_instance.to_dict()
# create an instance of Folder from a dict
folder_form_dict = folder.from_dict(folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


