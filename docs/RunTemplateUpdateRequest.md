# RunTemplateUpdateRequest

A Solution Run Template Create Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Run Template name | [optional] 
**labels** | **Dict[str, str]** | A translated label with key as ISO 639-1 code | [optional] 
**description** | **str** | The Run Template description | [optional] 
**tags** | **List[str]** | The list of Run Template tags | [optional] 
**compute_size** | **str** | The compute size needed for this Run Template | [optional] 
**run_sizing** | [**RunTemplateResourceSizing**](RunTemplateResourceSizing.md) |  | [optional] 
**parameter_groups** | **List[str]** | The ordered list of parameters groups for the Run Template | [optional] 
**execution_timeout** | **int** | An optional duration in seconds in which a workflow is allowed to run | [optional] 

## Example

```python
from cosmotech_api.models.run_template_update_request import RunTemplateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunTemplateUpdateRequest from a JSON string
run_template_update_request_instance = RunTemplateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(RunTemplateUpdateRequest.to_json())

# convert the object into a dict
run_template_update_request_dict = run_template_update_request_instance.to_dict()
# create an instance of RunTemplateUpdateRequest from a dict
run_template_update_request_from_dict = RunTemplateUpdateRequest.from_dict(run_template_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


