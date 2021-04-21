# Scenario

a Scenario with base information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the Scenario name | 
**id** | **str** | the Scenario unique identifier | [optional] [readonly] 
**description** | **str** | the Scenario description | [optional] 
**tags** | **[str]** | the list of tags | [optional] 
**parent_id** | **str** | the Scenario parent id | [optional] 
**owner_id** | **str** | the user id which own this Scenario | [optional] [readonly] 
**solution_id** | **str** | the Solution Id associated with this Scenario | [optional] [readonly] 
**run_template_id** | **str** | the Solution Run Template Id associated with this Scenario | [optional] 
**users** | [**[ScenarioUser]**](ScenarioUser.md) | the list of users Id with their role | [optional] 
**state** | **str** | the Scenario state | [optional] [readonly] 
**creation_date** | **str** | the Scenario creation date | [optional] [readonly] 
**owner_name** | **str** | the name of the owner | [optional] [readonly] 
**solution_name** | **str** | the Solution name | [optional] [readonly] 
**run_template_name** | **str** | the Solution Run Template name associated with this Scenario | [optional] [readonly] 
**dataset_list** | **[str]** | the list of Dataset Id associated to this Scenario Run Template | [optional] 
**parameters_values** | [**[ScenarioRunTemplateParameterValue]**](ScenarioRunTemplateParameterValue.md) | the list of Solution Run Template parameters values | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


