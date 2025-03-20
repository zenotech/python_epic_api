# ProductName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**image** | **str** |  | [optional] [readonly] 
**description** | **str** |  | 
**small_print** | **str** |  | 

## Example

```python
from epiccore.models.product_name import ProductName

# TODO update the JSON string below
json = "{}"
# create an instance of ProductName from a JSON string
product_name_instance = ProductName.from_json(json)
# print the JSON string representation of the object
print ProductName.to_json()

# convert the object into a dict
product_name_dict = product_name_instance.to_dict()
# create an instance of ProductName from a dict
product_name_form_dict = product_name.from_dict(product_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


