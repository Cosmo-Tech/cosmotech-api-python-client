# RunTemplate

a Solution Run Template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Solution Run Template id | 
**name** | **str** | the Run Template name | 
**description** | **str** | the Run Template description | [optional] 
**use_direct_csm_simulator** | **bool** | whether or not the Run Template use the main standard csmSimulator directly. False if there is an Engine set | [optional] [readonly] 
**csm_simulation** | **str** | the Cosmo Tech simulation name. This information is send to the Engine. Mandatory information if no Engine is defined | [optional] 
**tags** | **[str]** | the list of Run Template tags | [optional] 
**compute_size** | **str** | the compute size needed for this Run Template. Standard sizes are basic and highcpu. Default is basic | [optional] 
**parameters_handler_resource** | [**RunTemplateResourceStorage**](RunTemplateResourceStorage.md) |  | [optional] 
**dataset_validator_resource** | [**RunTemplateResourceStorage**](RunTemplateResourceStorage.md) |  | [optional] 
**engine_resource** | [**RunTemplateResourceStorage**](RunTemplateResourceStorage.md) |  | [optional] 
**dataset_schema_resource** | [**RunTemplateResourceStorage**](RunTemplateResourceStorage.md) |  | [optional] 
**parameter_groups** | [**[RunTemplateParameterGroup]**](RunTemplateParameterGroup.md) | the list of parameters groups for the Run Template | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


