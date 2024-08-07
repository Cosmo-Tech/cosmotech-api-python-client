# ScenarioRun

a ScenarioRun with only base properties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the ScenarioRun | [optional] [readonly] 
**state** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**organization_id** | **str** | the Organization id | [optional] 
**workflow_id** | **str** | the Cosmo Tech compute cluster Argo Workflow Id to search | [optional] 
**csm_simulation_run** | **str** | the Cosmo Tech Simulation Run Id | [optional] [readonly] 
**generate_name** | **str** | the base name for workflow name generation | [optional] 
**workflow_name** | **str** | the Cosmo Tech compute cluster Argo Workflow Name | [optional] 
**owner_id** | **str** | the user id which own this scenariorun | [optional] [readonly] 
**workspace_id** | **str** | the Workspace Id | [optional] [readonly] 
**workspace_key** | **str** | technical key for resource name convention and version grouping. Must be unique | [optional] [readonly] 
**scenario_id** | **str** | the Scenario Id | [optional] [readonly] 
**solution_id** | **str** | the Solution Id | [optional] [readonly] 
**run_template_id** | **str** | the Solution Run Template id | [optional] [readonly] 
**compute_size** | **str** | the compute size needed for this Analysis. Standard sizes are basic and highcpu. Default is basic | [optional] [readonly] 
**sdk_version** | **str** | the MAJOR.MINOR version used to build the solution solution | [optional] 
**created_at** | **str** | the ScenarioRun creation date | [optional] [readonly] 
**no_data_ingestion_state** | **bool** | set to true if the run template does not use any Datawarehouse consumers (AMQP consumers for Azure) | [optional] 
**dataset_list** | **[str]** | the list of Dataset Id associated to this Analysis | [optional] [readonly] 
**parameters_values** | [**[RunTemplateParameterValue]**](RunTemplateParameterValue.md) | the list of Run Template parameters values | [optional] [readonly] 
**send_datasets_to_data_warehouse** | **bool** | whether or not the Datasets values are send to the DataWarehouse prior to Simulation Run. If not set follow the Workspace setting | [optional] [readonly] 
**send_input_parameters_to_data_warehouse** | **bool** | whether or not the input parameters values are send to the DataWarehouse prior to Simulation Run. If not set follow the Workspace setting | [optional] [readonly] 
**node_label** | **str** | the node label request | [optional] [readonly] 
**containers** | [**[ScenarioRunContainer]**](ScenarioRunContainer.md) | the containers list. This information is not returned by the API. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


