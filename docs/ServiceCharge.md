# ServiceCharge

The EPIC service charge for the job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the currency | 
**currency** | **str** | Type of currency | 
**currency_symbol** | **str** | Symbol to be used for this currency | 

## Example

```python
from epiccore.models.service_charge import ServiceCharge

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCharge from a JSON string
service_charge_instance = ServiceCharge.from_json(json)
# print the JSON string representation of the object
print ServiceCharge.to_json()

# convert the object into a dict
service_charge_dict = service_charge_instance.to_dict()
# create an instance of ServiceCharge from a dict
service_charge_form_dict = service_charge.from_dict(service_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


