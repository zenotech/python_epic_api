# PriceQuote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | [**Cost**](Cost.md) |  | [optional] 
**valid** | **bool** | Whether the requested spec represents a valid configuration that could be launched | [optional] [readonly] 
**reason** | **str** | If the configuration is invalid this string will contain the reason why the configuration is not valid | [optional] [readonly] 

## Example

```python
from epiccore.models.price_quote import PriceQuote

# TODO update the JSON string below
json = "{}"
# create an instance of PriceQuote from a JSON string
price_quote_instance = PriceQuote.from_json(json)
# print the JSON string representation of the object
print PriceQuote.to_json()

# convert the object into a dict
price_quote_dict = price_quote_instance.to_dict()
# create an instance of PriceQuote from a dict
price_quote_form_dict = price_quote.from_dict(price_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


