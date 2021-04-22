# RunTemplate

a Solution Run Template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Solution Run Template id | 
**name** | **str** | the Run Template name | 
**description** | **str** | the Run Template description | [optional] 
**csm_simulation** | **str** | the Cosmo Tech simulation name. This information is send to the Engine. Mandatory information if no Engine is defined | [optional] 
**tags** | **[str]** | the list of Run Template tags | [optional] 
**compute_size** | **str** | the compute size needed for this Run Template. Standard sizes are basic and highcpu. Default is basic | [optional] 
**parameters_handler_resource** | [**RunTemplateResourceStorage**](RunTemplateResourceStorage.md) |  | [optional] 
**dataset_validator_resource** | [**RunTemplateResourceStorage**](RunTemplateResourceStorage.md) |  | [optional] 
**pre_run_resource** | [**RunTemplateResourceStorage**](RunTemplateResourceStorage.md) |  | [optional] 
**engine_resource** | [**RunTemplateResourceStorage**](RunTemplateResourceStorage.md) |  | [optional] 
**post_run_resource** | [**RunTemplateResourceStorage**](RunTemplateResourceStorage.md) |  | [optional] 
**send_datasets_to_data_warehouse** | **bool** | whether or not the Datasets values are send to the DataWarehouse prior to Simulation Run | [optional]  if omitted the server will use the default value of True
**send_input_parameters_to_data_warehouse** | **bool** | whether or not the input parameters values are send to the DataWarehouse prior to Simulation Run | [optional]  if omitted the server will use the default value of True
**parameter_groups** | **[str]** | the ordered list of parameters groups for the Run Template | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


