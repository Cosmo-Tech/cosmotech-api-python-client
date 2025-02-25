# RunTemplate

A Solution Run Template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Solution Run Template id | 
**name** | **str** | The Run Template name | [optional] 
**labels** | **Dict[str, str]** | a translated label with key as ISO 639-1 code | [optional] 
**description** | **str** | The Run Template description | [optional] 
**csm_simulation** | **str** | The Cosmo Tech simulation name | [optional] 
**tags** | **List[str]** | The list of Run Template tags | [optional] 
**compute_size** | **str** | The compute size needed for this Run Template | [optional] 
**run_sizing** | [**RunTemplateResourceSizing**](RunTemplateResourceSizing.md) |  | [optional] 
**no_data_ingestion_state** | **bool** | Set to true if the run template does not want to check data ingestion state | [optional] 
**parameters_handler_source** | [**RunTemplateStepSource**](RunTemplateStepSource.md) |  | [optional] 
**dataset_validator_source** | [**RunTemplateStepSource**](RunTemplateStepSource.md) |  | [optional] 
**pre_run_source** | [**RunTemplateStepSource**](RunTemplateStepSource.md) |  | [optional] 
**run_source** | [**RunTemplateStepSource**](RunTemplateStepSource.md) |  | [optional] 
**post_run_source** | [**RunTemplateStepSource**](RunTemplateStepSource.md) |  | [optional] 
**scenariodata_transform_source** | [**RunTemplateStepSource**](RunTemplateStepSource.md) |  | [optional] 
**parameter_groups** | **List[str]** | The ordered list of parameters groups for the Run Template | [optional] 
**stack_steps** | **bool** | Whether or not to stack adjacent scenario run steps | [optional] 
**git_repository_url** | **str** | An optional URL to the git repository | [optional] 
**git_branch_name** | **str** | An optional git branch name | [optional] 
**run_template_source_dir** | **str** | An optional directory where to find the run template source | [optional] 
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


