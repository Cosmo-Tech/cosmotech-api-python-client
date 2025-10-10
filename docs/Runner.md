# Runner

a Runner with complete information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Runner unique identifier | [readonly] 
**name** | **str** | the Runner name | 
**description** | **str** | the Runner description | [optional] 
**tags** | **List[str]** | the list of tags | [optional] 
**parent_id** | **str** | the Runner parent id | [optional] 
**create_info** | [**RunnerEditInfo**](RunnerEditInfo.md) | The details of the Runner creation | 
**update_info** | [**RunnerEditInfo**](RunnerEditInfo.md) | The details of the Runner last update | 
**root_id** | **str** | the runner root id | [optional] [readonly] 
**solution_id** | **str** | the Solution Id associated with this Runner | [readonly] 
**run_template_id** | **str** | the Solution Run Template Id associated with this Runner | 
**organization_id** | **str** | the associated Organization Id | [readonly] 
**workspace_id** | **str** | the associated Workspace Id | [readonly] 
**owner_name** | **str** | the name of the owner | [readonly] 
**solution_name** | **str** | the Solution name | [optional] [readonly] 
**run_template_name** | **str** | the Solution Run Template name associated with this Runner | [optional] [readonly] 
**datasets** | [**RunnerDatasets**](RunnerDatasets.md) |  | 
**run_sizing** | [**RunnerResourceSizing**](RunnerResourceSizing.md) |  | [optional] 
**parameters_values** | [**List[RunnerRunTemplateParameterValue]**](RunnerRunTemplateParameterValue.md) | the list of Solution Run Template parameters values | 
**last_run_info** | [**LastRunInfo**](LastRunInfo.md) |  | 
**validation_status** | [**RunnerValidationStatus**](RunnerValidationStatus.md) |  | 
**security** | [**RunnerSecurity**](RunnerSecurity.md) |  | 

## Example

```python
from cosmotech_api.models.runner import Runner

# TODO update the JSON string below
json = "{}"
# create an instance of Runner from a JSON string
runner_instance = Runner.from_json(json)
# print the JSON string representation of the object
print(Runner.to_json())

# convert the object into a dict
runner_dict = runner_instance.to_dict()
# create an instance of Runner from a dict
runner_from_dict = Runner.from_dict(runner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


