# SessionToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_key_id** | **str** | AWS Access Key | [optional] [readonly] 
**aws_secret_key** | **str** | AWS Secret Key | [optional] [readonly] 
**aws_session_token** | **str** |  | [optional] [readonly] 
**expiration** | **datetime** | Expiration time of token | [optional] [readonly] 

## Example

```python
from epiccore.models.session_token import SessionToken

# TODO update the JSON string below
json = "{}"
# create an instance of SessionToken from a JSON string
session_token_instance = SessionToken.from_json(json)
# print the JSON string representation of the object
print SessionToken.to_json()

# convert the object into a dict
session_token_dict = session_token_instance.to_dict()
# create an instance of SessionToken from a dict
session_token_form_dict = session_token.from_dict(session_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


