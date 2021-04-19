# RunTemplate

a Solution Run Template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Solution Run Template id | 
**name** | **str** | the Run Template name | 
**description** | **str** | the Run Template description | [optional] 
**is_standard_simulator** | **bool** | whether or not the Run Template use the main standard Simulator directly. False if there is a Custom Simulator set | [optional] [readonly] 
**simulation** | **str** | the simulation name. This information is send to the Simulator | [optional] 
**tags** | **[str]** | the list of Run Template tags | [optional] 
**compute_size** | **str** | the compute size needed for this Run Template. Standard sizes are basic and highcpu. Default is basic | [optional] 
**parameters_handler_resource** | [**RunTemplateResourceStorage**](RunTemplateResourceStorage.md) |  | [optional] 
**dataset_validator_resource** | [**RunTemplateResourceStorage**](RunTemplateResourceStorage.md) |  | [optional] 
**custom_simulator_resource** | [**RunTemplateResourceStorage**](RunTemplateResourceStorage.md) |  | [optional] 
**dataset_schema_resource** | [**RunTemplateResourceStorage**](RunTemplateResourceStorage.md) |  | [optional] 
**parameter_groups** | [**[RunTemplateParameterGroup]**](RunTemplateParameterGroup.md) | the list of parameters groups for the Run Template | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


