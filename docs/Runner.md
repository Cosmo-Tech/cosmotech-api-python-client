# Runner

a Runner with base information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Runner unique identifier | [optional] [readonly] 
**name** | **str** | the Runner name | [optional] 
**description** | **str** | the Runner description | [optional] 
**tags** | **[str]** | the list of tags | [optional] 
**parent_id** | **str** | the Runner parent id | [optional] 
**owner_id** | **str** | the user id which own this Runner | [optional] [readonly] 
**root_id** | **str** | the runner root id | [optional] [readonly] 
**solution_id** | **str** | the Solution Id associated with this Runner | [optional] [readonly] 
**run_template_id** | **str** | the Solution Run Template Id associated with this Runner | [optional] 
**organization_id** | **str** | the associated Organization Id | [optional] [readonly] 
**workspace_id** | **str** | the associated Workspace Id | [optional] [readonly] 
**creation_date** | **int** | the Runner creation date | [optional] [readonly] 
**last_update** | **int** | the last time a Runner was updated | [optional] [readonly] 
**owner_name** | **str** | the name of the owner | [optional] [readonly] 
**solution_name** | **str** | the Solution name | [optional] [readonly] 
**run_template_name** | **str** | the Solution Run Template name associated with this Runner | [optional] [readonly] 
**dataset_list** | **[str]** | the list of Dataset Id associated to this Runner Run Template | [optional] 
**run_sizing** | [**RunnerResourceSizing**](RunnerResourceSizing.md) |  | [optional] 
**parameters_values** | [**[RunnerRunTemplateParameterValue]**](RunnerRunTemplateParameterValue.md) | the list of Solution Run Template parameters values | [optional] 
**last_run_id** | **str** | last run id from current runner | [optional] 
**validation_status** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**security** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


