# CatalogDesktopList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DesktopNodeType]**](DesktopNodeType.md) |  | 

## Example

```python
from epiccore.models.catalog_desktop_list200_response import CatalogDesktopList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogDesktopList200Response from a JSON string
catalog_desktop_list200_response_instance = CatalogDesktopList200Response.from_json(json)
# print the JSON string representation of the object
print CatalogDesktopList200Response.to_json()

# convert the object into a dict
catalog_desktop_list200_response_dict = catalog_desktop_list200_response_instance.to_dict()
# create an instance of CatalogDesktopList200Response from a dict
catalog_desktop_list200_response_form_dict = catalog_desktop_list200_response.from_dict(catalog_desktop_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


