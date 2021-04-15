# SimulatorAnalysis

a Simulator Analysis run template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Simulator Analysis id | 
**name** | **str** | the Simulator Analysis name | 
**description** | **str** | the Simulator Analysis description | [optional] 
**simulation** | **str** | the simulation name | [optional] 
**tags** | **[str]** | the list of Simulator Analysis tags | [optional] 
**compute_size** | **str** | the compute size needed for this Analysis. Standard sizes are basic and highcpu. Default is basic | [optional] 
**parameters_handler_resource** | [**AnalysisResourceStorage**](AnalysisResourceStorage.md) |  | [optional] 
**dataset_validator_resource** | [**AnalysisResourceStorage**](AnalysisResourceStorage.md) |  | [optional] 
**custom_driver_resource** | [**AnalysisResourceStorage**](AnalysisResourceStorage.md) |  | [optional] 
**dataset_schema_resource** | [**AnalysisResourceStorage**](AnalysisResourceStorage.md) |  | [optional] 
**parameter_groups** | [**[AnalysisParameterGroup]**](AnalysisParameterGroup.md) | the list of parameters groups for the Analysis | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


