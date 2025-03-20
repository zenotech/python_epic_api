# CatalogApplicationsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[BatchApplicationList]**](BatchApplicationList.md) |  | 

## Example

```python
from epiccore.models.catalog_applications_list200_response import CatalogApplicationsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogApplicationsList200Response from a JSON string
catalog_applications_list200_response_instance = CatalogApplicationsList200Response.from_json(json)
# print the JSON string representation of the object
print CatalogApplicationsList200Response.to_json()

# convert the object into a dict
catalog_applications_list200_response_dict = catalog_applications_list200_response_instance.to_dict()
# create an instance of CatalogApplicationsList200Response from a dict
catalog_applications_list200_response_form_dict = catalog_applications_list200_response.from_dict(catalog_applications_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


