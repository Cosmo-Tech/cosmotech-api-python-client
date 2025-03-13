# RunTemplateParameter

A Run Template Parameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Parameter id | 
**labels** | **Dict[str, str]** | a translated label with key as ISO 639-1 code | [optional] 
**var_type** | **str** | the variable type for the parameter. Basic types or special type %DATASETID% | [optional] 
**default_value** | **str** | The default value for this parameter | [optional] 
**min_value** | **str** | The minimum value for this parameter | [optional] 
**max_value** | **str** | The maximum value for this parameter | [optional] 
**regex_validation** | **str** | A regex to validate the value | [optional] 
**options** | **Dict[str, object]** | Freeform options | [optional] 

## Example

```python
from cosmotech_api.models.run_template_parameter import RunTemplateParameter

# TODO update the JSON string below
json = "{}"
# create an instance of RunTemplateParameter from a JSON string
run_template_parameter_instance = RunTemplateParameter.from_json(json)
# print the JSON string representation of the object
print(RunTemplateParameter.to_json())

# convert the object into a dict
run_template_parameter_dict = run_template_parameter_instance.to_dict()
# create an instance of RunTemplateParameter from a dict
run_template_parameter_from_dict = RunTemplateParameter.from_dict(run_template_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


