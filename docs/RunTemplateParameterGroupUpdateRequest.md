# RunTemplateParameterGroupUpdateRequest

A Parameter Group Update Request for a Run Template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the parameter group | [optional] 
**labels** | **Dict[str, str]** | A translated label with key as ISO 639-1 code | [optional] 
**additional_data** | **Dict[str, object]** | Free form additional data | [optional] 
**parameters** | **List[str]** | An ordered list of Run Template Parameters | [optional] 

## Example

```python
from cosmotech_api.models.run_template_parameter_group_update_request import RunTemplateParameterGroupUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunTemplateParameterGroupUpdateRequest from a JSON string
run_template_parameter_group_update_request_instance = RunTemplateParameterGroupUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(RunTemplateParameterGroupUpdateRequest.to_json())

# convert the object into a dict
run_template_parameter_group_update_request_dict = run_template_parameter_group_update_request_instance.to_dict()
# create an instance of RunTemplateParameterGroupUpdateRequest from a dict
run_template_parameter_group_update_request_from_dict = RunTemplateParameterGroupUpdateRequest.from_dict(run_template_parameter_group_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


