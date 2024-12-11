# RunTemplateParameterValue

the value of Analysis parameter for a Runner for this Run

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_id** | **str** | the parameter Id | 
**var_type** | **str** | the parameter value type | [optional] [readonly] 
**value** | **str** | the parameter value | 

## Example

```python
from cosmotech_api.models.run_template_parameter_value import RunTemplateParameterValue

# TODO update the JSON string below
json = "{}"
# create an instance of RunTemplateParameterValue from a JSON string
run_template_parameter_value_instance = RunTemplateParameterValue.from_json(json)
# print the JSON string representation of the object
print(RunTemplateParameterValue.to_json())

# convert the object into a dict
run_template_parameter_value_dict = run_template_parameter_value_instance.to_dict()
# create an instance of RunTemplateParameterValue from a dict
run_template_parameter_value_from_dict = RunTemplateParameterValue.from_dict(run_template_parameter_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


