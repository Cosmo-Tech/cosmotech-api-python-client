# ScenarioBase

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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


