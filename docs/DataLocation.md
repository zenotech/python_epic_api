# DataLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s3_obj_key** | **str** | Root path for EPIC data store | [optional] [readonly] 
**s3_location** | **str** | S3 Bucket name for EPIC data store | [optional] [readonly] 
**aws_region** | **str** | AWS Region | [optional] [readonly] 
**session_token** | [**SessionToken**](SessionToken.md) |  | [optional] 

## Example

```python
from epiccore.models.data_location import DataLocation

# TODO update the JSON string below
json = "{}"
# create an instance of DataLocation from a JSON string
data_location_instance = DataLocation.from_json(json)
# print the JSON string representation of the object
print DataLocation.to_json()

# convert the object into a dict
data_location_dict = data_location_instance.to_dict()
# create an instance of DataLocation from a dict
data_location_form_dict = data_location.from_dict(data_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


