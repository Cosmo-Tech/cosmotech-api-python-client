# ScenarioRun

a ScenarioRun with only base properties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the ScenarioRun | [optional] [readonly] 
**job_id** | **str** | the Platform compute cluster Job Id | [optional] [readonly] 
**owner_id** | **str** | the user id which own this scenariorun | [optional] [readonly] 
**workspace_id** | **str** | the Workspace Id | [optional] [readonly] 
**workspace_name** | **str** | the Workspace name | [optional] [readonly] 
**scenario_id** | **str** | the Scenario Id | [optional] [readonly] 
**scenario_name** | **str** | the Scenario name | [optional] [readonly] 
**solution_id** | **str** | the Solution Id | [optional] [readonly] 
**solution_name** | **str** | the Solution name | [optional] [readonly] 
**solution_version** | **str** | the Solution version | [optional] [readonly] 
**run_template_id** | **str** | the Solution Run Template id | [optional] [readonly] 
**run_template_name** | **str** | the Run Template name | [optional] [readonly] 
**compute_size** | **str** | the compute size needed for this Analysis. Standard sizes are basic and highcpu. Default is basic | [optional] [readonly] 
**state** | **str** | the ScenarioRun state | [optional] [readonly] 
**failed_step** | **str** | the failed step if state is Failed | [optional] [readonly] 
**failed_container_id** | **str** | the failed container Id if state is Failed | [optional] [readonly] 
**start_time** | **str** | the ScenarioRun start Date Time | [optional] [readonly] 
**end_time** | **str** | the ScenarioRun end Date Time | [optional] [readonly] 
**dataset_list** | **[str]** | the list of Dataset Id associated to this Analysis | [optional] [readonly] 
**parameters_values** | [**[RunTemplateParameterValue]**](RunTemplateParameterValue.md) | the list of Run Template parameters values | [optional] [readonly] 
**send_input_to_data_warehouse** | **bool** | whether or not the Dataset values and the input parameters values are send to the DataWarehouse prior to ScenarioRun Run | [optional] [readonly] 
**data_warehouse_db** | **str** | the DataWarehouse database name to send data if sendInputToDataWarehouse is set | [optional] 
**results_event_bus_resource_uri** | **str** | the event bus which receive Workspace ScenarioRun results messages. Message won&#39;t be send if this is not set | [optional] 
**scenariorun_event_bus_resource_uri** | **str** | the event bus which receive Workspace ScenarioRun events messages. Message won&#39;t be send if this is not set | [optional] 
**node_label** | **str** | the node label request | [optional] [readonly] 
**fetch_dataset_containers** | [**[ScenarioRunContainer]**](ScenarioRunContainer.md) | the containers which fetch the Scenario Datasets | [optional] [readonly] 
**fetch_scenario_parameters_container** | [**ScenarioRunContainer**](ScenarioRunContainer.md) |  | [optional] 
**apply_parameters_container** | [**ScenarioRunContainer**](ScenarioRunContainer.md) |  | [optional] 
**validate_data_container** | [**ScenarioRunContainer**](ScenarioRunContainer.md) |  | [optional] 
**send_data_warehouse_container** | [**ScenarioRunContainer**](ScenarioRunContainer.md) |  | [optional] 
**pre_run_container** | [**ScenarioRunContainer**](ScenarioRunContainer.md) |  | [optional] 
**run_container** | [**ScenarioRunContainer**](ScenarioRunContainer.md) |  | [optional] 
**post_run_container** | [**ScenarioRunContainer**](ScenarioRunContainer.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


