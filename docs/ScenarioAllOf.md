# ScenarioAllOf

a Scenario with detailed information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solution_name** | **str** | the Solution name | [optional] [readonly] 
**run_template_name** | **str** | the Solution Run Template name associated with this Scenario | [optional] [readonly] 
**dataset_list** | **[str]** | the list of Dataset Id associated to this Scenario Run Template | [optional] 
**parameters_values** | [**[ScenarioRunTemplateParameterValue]**](ScenarioRunTemplateParameterValue.md) | the list of Solution Run Template parameters values | [optional] 
**send_input_to_data_warehouse** | **bool** | whether or not the Dataset values and the input parameters values are send to the DataWarehouse prior to Simulation Run | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


