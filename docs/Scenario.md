# Scenario

a Scenario with base information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Scenario unique identifier | [optional] [readonly] 
**name** | **str** | the Scenario name | [optional] 
**description** | **str** | the Scenario description | [optional] 
**tags** | **[str]** | the list of tags | [optional] 
**parent_id** | **str** | the Scenario parent id | [optional] 
**owner_id** | **str** | the user id which own this Scenario | [optional] [readonly] 
**root_id** | **str** | the scenario root id | [optional] [readonly] 
**solution_id** | **str** | the Solution Id associated with this Scenario | [optional] [readonly] 
**run_template_id** | **str** | the Solution Run Template Id associated with this Scenario | [optional] 
**workspace_id** | **str** | the associated Workspace Id | [optional] [readonly] 
**users** | [**[ScenarioUser]**](ScenarioUser.md) | the list of users Id with their role | [optional] 
**state** | [**ScenarioJobState**](ScenarioJobState.md) |  | [optional] 
**creation_date** | **datetime** | the Scenario creation date | [optional] [readonly] 
**last_update** | **datetime** | the last time a Scenario was updated | [optional] [readonly] 
**owner_name** | **str** | the name of the owner | [optional] [readonly] 
**solution_name** | **str** | the Solution name | [optional] [readonly] 
**run_template_name** | **str** | the Solution Run Template name associated with this Scenario | [optional] [readonly] 
**dataset_list** | **[str]** | the list of Dataset Id associated to this Scenario Run Template | [optional] 
**parameters_values** | [**[ScenarioRunTemplateParameterValue]**](ScenarioRunTemplateParameterValue.md) | the list of Solution Run Template parameters values | [optional] 
**last_run** | **dict** |  | [optional] 
**parent_last_run** | **dict** |  | [optional] 
**root_last_run** | **dict** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


