# RunnerRunTemplateParameterValue

the value of a Solution Run Template parameter for a Runner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_id** | **str** | the parameter Id | 
**var_type** | **str** | the parameter value type | [optional] 
**value** | **str** | the parameter value | 
**is_inherited** | **bool** | whether or not the value is inherited from parent or has been changed | [optional] 

## Example

```python
from cosmotech_api.models.runner_run_template_parameter_value import RunnerRunTemplateParameterValue

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerRunTemplateParameterValue from a JSON string
runner_run_template_parameter_value_instance = RunnerRunTemplateParameterValue.from_json(json)
# print the JSON string representation of the object
print(RunnerRunTemplateParameterValue.to_json())

# convert the object into a dict
runner_run_template_parameter_value_dict = runner_run_template_parameter_value_instance.to_dict()
# create an instance of RunnerRunTemplateParameterValue from a dict
runner_run_template_parameter_value_from_dict = RunnerRunTemplateParameterValue.from_dict(runner_run_template_parameter_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


