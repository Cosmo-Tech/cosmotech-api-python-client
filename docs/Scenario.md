# Scenario


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the Scenario name | 
**id** | **str** | the Scenario unique identifier | [optional] [readonly] 
**description** | **str** | the Scenario description | [optional] 
**tags** | **[str]** | the list of tags | [optional] 
**parent_id** | **str** | the Scenario parent id | [optional] 
**owner_id** | **str** | the user id which own this Scenario | [optional] [readonly] 
**user_list** | [**[ScenarioUser]**](ScenarioUser.md) | the list of users Id with their role | [optional] 
**simulator_id** | **str** | the Simulator Id associated with this Scenario | [optional] [readonly] 
**analysis** | [**[ScenarioAnalysis]**](ScenarioAnalysis.md) | the configuration for Analysis | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


