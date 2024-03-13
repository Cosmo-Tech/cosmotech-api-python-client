# ScenarioRunTemplateParameterValue

the value of a Solution Run Template parameter for a Scenario

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_id** | **str** | the parameter Id | 
**var_type** | **str** | the parameter value type | [optional] [readonly] 
**value** | **str** | the parameter value | 
**is_inherited** | **bool** | whether or not the value is inherited from parent or has been changed | [optional] 

## Example

```python
from cosmotech_api.models.scenario_run_template_parameter_value import ScenarioRunTemplateParameterValue

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioRunTemplateParameterValue from a JSON string
scenario_run_template_parameter_value_instance = ScenarioRunTemplateParameterValue.from_json(json)
# print the JSON string representation of the object
print ScenarioRunTemplateParameterValue.to_json()

# convert the object into a dict
scenario_run_template_parameter_value_dict = scenario_run_template_parameter_value_instance.to_dict()
# create an instance of ScenarioRunTemplateParameterValue from a dict
scenario_run_template_parameter_value_form_dict = scenario_run_template_parameter_value.from_dict(scenario_run_template_parameter_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


