# Simulation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Simulation | [optional] [readonly] 
**job_id** | **str** | the Platform compute cluster Job Id | [optional] [readonly] 
**owner_id** | **str** | the user id which own this simulation | [optional] [readonly] 
**workspace_id** | **str** | the Workspace Id | [optional] [readonly] 
**workspace_name** | **str** | the Workspace name | [optional] [readonly] 
**scenario_id** | **str** | the Scenario Id | [optional] [readonly] 
**scenario_name** | **str** | the Scenario name | [optional] [readonly] 
**simulator_id** | **str** | the Simulator Id | [optional] [readonly] 
**simulator_name** | **str** | the Simulator name | [optional] [readonly] 
**simulator_version** | **str** | the Simulator version | [optional] [readonly] 
**simulator_analysis_id** | **str** | the Simulator Analysis id | [optional] [readonly] 
**simulator_analysis_name** | **str** | the Simulator Analysis name | [optional] [readonly] 
**compute_size** | **str** | the compute size needed for this Analysis. Standard sizes are basic and highcpu. Default is basic | [optional] [readonly] 
**state** | **str** | the Simulation state | [optional] [readonly] 
**start_time** | **str** | the Simulation start Date Time | [optional] [readonly] 
**end_time** | **str** | the Simulation end Date Time | [optional] [readonly] 
**dataset_list** | **[str]** | the list of Dataset Id associated to this Analysis | [optional] [readonly] 
**parameters_values** | [**[SimulationAnalysisParameterValue]**](SimulationAnalysisParameterValue.md) | the list of Simulator Analysis parameters values | [optional] [readonly] 
**send_input_to_data_warehouse** | **bool** | whether or not the Dataset values and the input parameters values are send to the DataWarehouse prior to Simulation Run | [optional] [readonly] 
**data_warehouse_db** | **str** | the DataWarehouse database name to send data if sendInputToDataWarehouse is set | [optional] 
**results_event_bus_resource_uri** | **str** | the event bus which receive Workspace Simulation results messages. Message won&#39;t be send if this is not set | [optional] 
**simulation_event_bus_resource_uri** | **str** | the event bus which receive Workspace Simulation events messages. Message won&#39;t be send if this is not set | [optional] 
**node_label** | **str** | the node label request | [optional] [readonly] 
**init_containers** | [**[SimulationContainers]**](SimulationContainers.md) | the list of init containers | [optional] [readonly] 
**main_container** | [**SimulationContainers**](SimulationContainers.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


