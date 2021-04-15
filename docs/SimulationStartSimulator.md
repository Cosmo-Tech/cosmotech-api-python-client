# SimulationStartSimulator

the parameters to run directly a Simulator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**simulator_id** | **str** | the Simulator Id | [optional] 
**simulator_analysis_id** | **str** | the Simulator Analysis id | [optional] 
**dataset_list** | **[str]** | the list of Dataset Id associated to this Analysis | [optional] 
**parameters_values** | [**[SimulationAnalysisParameterValue]**](SimulationAnalysisParameterValue.md) | the list of Simulator Analysis parameters values | [optional] 
**send_input_to_data_warehouse** | **bool** | whether or not the Dataset values and the input parameters values are send to the DataWarehouse prior to Simulation Run | [optional] 
**data_warehouse_db** | **str** | the DataWarehouse database name to send data if sendInputToDataWarehouse is set | [optional] 
**results_event_bus_resource_uri** | **str** | the event bus which receive Workspace Simulation results messages. Message won&#39;t be send if this is not set | [optional] 
**simulation_event_bus_resource_uri** | **str** | the event bus which receive Workspace Simulation events messages. Message won&#39;t be send if this is not set | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


