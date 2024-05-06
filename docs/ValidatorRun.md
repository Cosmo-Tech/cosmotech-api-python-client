# ValidatorRun

a Validator Run

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Validator Run id | [optional] [readonly] 
**validator_id** | **str** | the Validator id | [optional] [readonly] 
**validator_name** | **str** | the validator name | [optional] [readonly] 
**dataset_id** | **str** | the Dataset id to run the validator on | 
**dataset_name** | **str** | the Dataset name | [optional] [readonly] 
**state** | **str** | the Validator Run state | [optional] [readonly] 
**container_id** | **str** | the Validator Run container id | [optional] [readonly] 
**logs** | **str** | the Validator Run logs | [optional] [readonly] 

## Example

```python
from cosmotech_api.models.validator_run import ValidatorRun

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatorRun from a JSON string
validator_run_instance = ValidatorRun.from_json(json)
# print the JSON string representation of the object
print ValidatorRun.to_json()

# convert the object into a dict
validator_run_dict = validator_run_instance.to_dict()
# create an instance of ValidatorRun from a dict
validator_run_form_dict = validator_run.from_dict(validator_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


