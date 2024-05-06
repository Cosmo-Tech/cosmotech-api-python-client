# Validator

a Validator to validate a Dataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Validator id | [readonly] 
**name** | **str** | the Validator name | 
**description** | **str** | the Validator description | [optional] 
**repository** | **str** | the registry repository containing the Validator image | 
**version** | **str** | the Validator version MAJOR.MINOR.PATCH. Must be aligned with an existing repository tag | 
**owner_id** | **str** | the User id which own this Validator | [optional] [readonly] 
**url** | **str** | an optional URL link to Validator page | [optional] 
**tags** | **List[str]** | the list of tags | [optional] 

## Example

```python
from cosmotech_api.models.validator import Validator

# TODO update the JSON string below
json = "{}"
# create an instance of Validator from a JSON string
validator_instance = Validator.from_json(json)
# print the JSON string representation of the object
print Validator.to_json()

# convert the object into a dict
validator_dict = validator_instance.to_dict()
# create an instance of Validator from a dict
validator_form_dict = validator.from_dict(validator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


