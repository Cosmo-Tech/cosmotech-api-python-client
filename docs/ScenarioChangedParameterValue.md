# ScenarioChangedParameterValue

the difference between the values of a parameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_id** | **str** | the parameter id the values refer to | [optional] [readonly] 
**var_type** | **str** | the parameter value type | [optional] [readonly] 
**value** | **str** | the parameter value for the reference Scenario | [optional] [readonly] 
**compared_value** | **str** | the parameter value for the compared Scenario | [optional] [readonly] 

## Example

```python
from cosmotech_api.models.scenario_changed_parameter_value import ScenarioChangedParameterValue

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioChangedParameterValue from a JSON string
scenario_changed_parameter_value_instance = ScenarioChangedParameterValue.from_json(json)
# print the JSON string representation of the object
print ScenarioChangedParameterValue.to_json()

# convert the object into a dict
scenario_changed_parameter_value_dict = scenario_changed_parameter_value_instance.to_dict()
# create an instance of ScenarioChangedParameterValue from a dict
scenario_changed_parameter_value_form_dict = scenario_changed_parameter_value.from_dict(scenario_changed_parameter_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


