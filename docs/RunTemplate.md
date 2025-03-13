# RunTemplate

A Solution Run Template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Solution Run Template id | 
**name** | **str** | The Run Template name | [optional] 
**labels** | **Dict[str, str]** | a translated label with key as ISO 639-1 code | [optional] 
**description** | **str** | The Run Template description | [optional] 
**tags** | **List[str]** | The list of Run Template tags | [optional] 
**compute_size** | **str** | The compute size needed for this Run Template | [optional] 
**run_sizing** | [**RunTemplateResourceSizing**](RunTemplateResourceSizing.md) |  | [optional] 
**parameter_groups** | **List[str]** | The ordered list of parameters groups for the Run Template | [optional] 
**execution_timeout** | **int** | An optional duration in seconds in which a workflow is allowed to run | [optional] 

## Example

```python
from cosmotech_api.models.run_template import RunTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of RunTemplate from a JSON string
run_template_instance = RunTemplate.from_json(json)
# print the JSON string representation of the object
print(RunTemplate.to_json())

# convert the object into a dict
run_template_dict = run_template_instance.to_dict()
# create an instance of RunTemplate from a dict
run_template_from_dict = RunTemplate.from_dict(run_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


