# RunTemplateParameterGroup

A Parameter Group for a Run Template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Parameter Group id | 
**description** | **str** | A description of the parameter group | [optional] 
**labels** | **Dict[str, str]** | a translated label with key as ISO 639-1 code | [optional] 
**is_table** | **bool** | Does the group define a table | 
**options** | **Dict[str, object]** | Freeform options | [optional] 
**parent_id** | **str** | The Run Template Group parent Id | [optional] 
**parameters** | **List[str]** | An ordered list of Run Template Parameters | 

## Example

```python
from cosmotech_api.models.run_template_parameter_group import RunTemplateParameterGroup

# TODO update the JSON string below
json = "{}"
# create an instance of RunTemplateParameterGroup from a JSON string
run_template_parameter_group_instance = RunTemplateParameterGroup.from_json(json)
# print the JSON string representation of the object
print(RunTemplateParameterGroup.to_json())

# convert the object into a dict
run_template_parameter_group_dict = run_template_parameter_group_instance.to_dict()
# create an instance of RunTemplateParameterGroup from a dict
run_template_parameter_group_from_dict = RunTemplateParameterGroup.from_dict(run_template_parameter_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


