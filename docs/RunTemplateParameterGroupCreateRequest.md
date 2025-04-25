# RunTemplateParameterGroupCreateRequest

A Parameter Group Create Request for a Run Template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Parameter Group id | 
**description** | **str** | A description of the parameter group | [optional] 
**labels** | **Dict[str, str]** | A translated label with key as ISO 639-1 code | [optional] 
**is_table** | **bool** | Does the group define a table | [optional] [default to False]
**options** | **Dict[str, object]** | Freeform options | [optional] 
**parent_id** | **str** | The Run Template Group parent Id | [optional] 
**parameters** | **List[str]** | An ordered list of Run Template Parameters | [optional] [default to []]

## Example

```python
from cosmotech_api.models.run_template_parameter_group_create_request import RunTemplateParameterGroupCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunTemplateParameterGroupCreateRequest from a JSON string
run_template_parameter_group_create_request_instance = RunTemplateParameterGroupCreateRequest.from_json(json)
# print the JSON string representation of the object
print(RunTemplateParameterGroupCreateRequest.to_json())

# convert the object into a dict
run_template_parameter_group_create_request_dict = run_template_parameter_group_create_request_instance.to_dict()
# create an instance of RunTemplateParameterGroupCreateRequest from a dict
run_template_parameter_group_create_request_from_dict = RunTemplateParameterGroupCreateRequest.from_dict(run_template_parameter_group_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


