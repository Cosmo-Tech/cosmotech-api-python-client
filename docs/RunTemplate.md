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
**fetch_datasets** | **bool** | whether or not the fetch dataset step is done | [optional] 
**fetch_scenario_parameters** | **bool** | whether or not the fetch parameters step is done | [optional] 
**apply_parameters** | **bool** | whether or not the apply parameter step is done | [optional] 
**validate_data** | **bool** | whether or not the validate step is done | [optional] 
**send_datasets_to_data_warehouse** | **bool** | whether or not the Datasets values are send to the DataWarehouse prior to Simulation Run. If not set follow the Workspace setting | [optional] 
**send_input_parameters_to_data_warehouse** | **bool** | whether or not the input parameters values are send to the DataWarehouse prior to Simulation Run. If not set follow the Workspace setting | [optional] 
**pre_run** | **bool** | whether or not the pre-run step is done | [optional] 
**run** | **bool** | whether or not the run step is done | [optional] 
**post_run** | **bool** | whether or not the post-run step is done | [optional] 
**parameters_json** | **bool** | whether or not to store the scenario parameters in json instead of csv | [optional] 
**parameters_handler_source** | [**RunTemplateStepSource**](RunTemplateStepSource.md) |  | [optional] 
**dataset_validator_source** | [**RunTemplateStepSource**](RunTemplateStepSource.md) |  | [optional] 
**pre_run_source** | [**RunTemplateStepSource**](RunTemplateStepSource.md) |  | [optional] 
**run_source** | [**RunTemplateStepSource**](RunTemplateStepSource.md) |  | [optional] 
**post_run_source** | [**RunTemplateStepSource**](RunTemplateStepSource.md) |  | [optional] 
**parameter_groups** | **[str]** | the ordered list of parameters groups for the Run Template | [optional] 
**stack_steps** | **bool** | whether or not to stack adjacent scenario run steps in one container run which will chain steps | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


