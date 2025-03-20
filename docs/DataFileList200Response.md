# DataFileList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[File]**](File.md) |  | 

## Example

```python
from epiccore.models.data_file_list200_response import DataFileList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DataFileList200Response from a JSON string
data_file_list200_response_instance = DataFileList200Response.from_json(json)
# print the JSON string representation of the object
print DataFileList200Response.to_json()

# convert the object into a dict
data_file_list200_response_dict = data_file_list200_response_instance.to_dict()
# create an instance of DataFileList200Response from a dict
data_file_list200_response_form_dict = data_file_list200_response.from_dict(data_file_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


