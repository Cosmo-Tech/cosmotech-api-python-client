# ScenarioRunAllOf

a ScenarioRun

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_list** | **[str]** | the list of Dataset Id associated to this Analysis | [optional] [readonly] 
**parameters_values** | [**[RunTemplateParameterValue]**](RunTemplateParameterValue.md) | the list of Run Template parameters values | [optional] [readonly] 
**send_input_to_data_warehouse** | **bool** | whether or not the Dataset values and the input parameters values are send to the DataWarehouse prior to ScenarioRun Run | [optional] [readonly] 
**data_warehouse_db** | **str** | the DataWarehouse database name to send data if sendInputToDataWarehouse is set | [optional] 
**results_event_bus_resource_uri** | **str** | the event bus which receive Workspace ScenarioRun results messages. Message won&#39;t be send if this is not set | [optional] 
**scenariorun_event_bus_resource_uri** | **str** | the event bus which receive Workspace ScenarioRun events messages. Message won&#39;t be send if this is not set | [optional] 
**node_label** | **str** | the node label request | [optional] [readonly] 
**init_containers** | [**[ScenarioRunContainers]**](ScenarioRunContainers.md) | the list of init containers | [optional] [readonly] 
**main_container** | [**ScenarioRunContainers**](ScenarioRunContainers.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


