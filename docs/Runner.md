# Runner

a Runner with base information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Runner unique identifier | [optional] [readonly] 
**name** | **str** | the Runner name | [optional] 
**description** | **str** | the Runner description | [optional] 
**tags** | **List[str]** | the list of tags | [optional] 
**parent_id** | **str** | the Runner parent id | [optional] 
**owner_id** | **str** | the user id which own this Runner | [optional] [readonly] 
**root_id** | **str** | the runner root id | [optional] [readonly] 
**solution_id** | **str** | the Solution Id associated with this Runner | [optional] [readonly] 
**run_template_id** | **str** | the Solution Run Template Id associated with this Runner | [optional] 
**organization_id** | **str** | the associated Organization Id | [optional] [readonly] 
**workspace_id** | **str** | the associated Workspace Id | [optional] [readonly] 
**state** | [**RunnerJobState**](RunnerJobState.md) |  | [optional] 
**creation_date** | **int** | the Runner creation date | [optional] [readonly] 
**last_update** | **int** | the last time a Runner was updated | [optional] [readonly] 
**owner_name** | **str** | the name of the owner | [optional] [readonly] 
**solution_name** | **str** | the Solution name | [optional] [readonly] 
**run_template_name** | **str** | the Solution Run Template name associated with this Runner | [optional] [readonly] 
**dataset_list** | **List[str]** | the list of Dataset Id associated to this Runner Run Template | [optional] 
**run_sizing** | [**RunnerResourceSizing**](RunnerResourceSizing.md) |  | [optional] 
**parameters_values** | [**List[RunnerRunTemplateParameterValue]**](RunnerRunTemplateParameterValue.md) | the list of Solution Run Template parameters values | [optional] 
**last_run** | [**RunnerLastRun**](RunnerLastRun.md) |  | [optional] 
**parent_last_run** | [**RunnerParentLastRun**](RunnerParentLastRun.md) |  | [optional] 
**root_last_run** | [**RunnerRootLastRun**](RunnerRootLastRun.md) |  | [optional] 
**validation_status** | [**RunnerValidationStatus**](RunnerValidationStatus.md) |  | [optional] 
**security** | [**RunnerSecurity**](RunnerSecurity.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.runner import Runner

# TODO update the JSON string below
json = "{}"
# create an instance of Runner from a JSON string
runner_instance = Runner.from_json(json)
# print the JSON string representation of the object
print Runner.to_json()

# convert the object into a dict
runner_dict = runner_instance.to_dict()
# create an instance of Runner from a dict
runner_form_dict = runner.from_dict(runner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


