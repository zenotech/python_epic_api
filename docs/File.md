# File


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID for this folder | [optional] [readonly] 
**created** | **datetime** | Creation time | [optional] [readonly] 
**modified** | **datetime** |  | [optional] [readonly] 
**name** | **str** | File name | [optional] [readonly] 
**obj_key** | **str** | S3 key reference | [optional] [readonly] 
**size** | **int** |  | [optional] 
**last_modified** | **datetime** | Last modified time | [optional] [readonly] 
**folder** | **int** | Folder name | [optional] [readonly] 

## Example

```python
from epiccore.models.file import File

# TODO update the JSON string below
json = "{}"
# create an instance of File from a JSON string
file_instance = File.from_json(json)
# print the JSON string representation of the object
print File.to_json()

# convert the object into a dict
file_dict = file_instance.to_dict()
# create an instance of File from a dict
file_form_dict = file.from_dict(file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


