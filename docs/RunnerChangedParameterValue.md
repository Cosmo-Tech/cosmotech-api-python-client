# RunnerChangedParameterValue

the difference between the values of a parameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_id** | **str** | the parameter id the values refer to | [optional] [readonly] 
**var_type** | **str** | the parameter value type | [optional] [readonly] 
**value** | **str** | the parameter value for the reference Runner | [optional] [readonly] 
**compared_value** | **str** | the parameter value for the compared Runner | [optional] [readonly] 

## Example

```python
from cosmotech_api.models.runner_changed_parameter_value import RunnerChangedParameterValue

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerChangedParameterValue from a JSON string
runner_changed_parameter_value_instance = RunnerChangedParameterValue.from_json(json)
# print the JSON string representation of the object
print(RunnerChangedParameterValue.to_json())

# convert the object into a dict
runner_changed_parameter_value_dict = runner_changed_parameter_value_instance.to_dict()
# create an instance of RunnerChangedParameterValue from a dict
runner_changed_parameter_value_from_dict = RunnerChangedParameterValue.from_dict(runner_changed_parameter_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


