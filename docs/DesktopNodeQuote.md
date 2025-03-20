# DesktopNodeQuote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_code** | **str** | node_code of the node type to launch. Valid values are obtained from the catalog/desktop/ endpoint | 
**runtime** | **int** | Runtime in hours to run this desktop node for. This is the maximum runtime as the viz node can be stopped earlier and you will only be charged for the elapsed time | 

## Example

```python
from epiccore.models.desktop_node_quote import DesktopNodeQuote

# TODO update the JSON string below
json = "{}"
# create an instance of DesktopNodeQuote from a JSON string
desktop_node_quote_instance = DesktopNodeQuote.from_json(json)
# print the JSON string representation of the object
print DesktopNodeQuote.to_json()

# convert the object into a dict
desktop_node_quote_dict = desktop_node_quote_instance.to_dict()
# create an instance of DesktopNodeQuote from a dict
desktop_node_quote_form_dict = desktop_node_quote.from_dict(desktop_node_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


