# ScenarioRunLogs

the scenariorun logs returned by all containers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenariorun_id** | **str** | the ScenarioRun Id | [optional] [readonly] 
**options** | [**ScenarioRunLogsOptions**](ScenarioRunLogsOptions.md) |  | [optional] 
**fetch_dataset_logs** | [**[ScenarioRunContainerLogs]**](ScenarioRunContainerLogs.md) | logs for the containers which fetch the Scenario Datasets | [optional] [readonly] 
**fetch_scenario_parameters_log** | [**ScenarioRunContainerLogs**](ScenarioRunContainerLogs.md) |  | [optional] 
**apply_parameters_logs** | [**ScenarioRunContainerLogs**](ScenarioRunContainerLogs.md) |  | [optional] 
**validate_data_logs** | [**ScenarioRunContainerLogs**](ScenarioRunContainerLogs.md) |  | [optional] 
**send_data_warehouse_logs** | [**ScenarioRunContainerLogs**](ScenarioRunContainerLogs.md) |  | [optional] 
**pre_run_logs** | [**ScenarioRunContainerLogs**](ScenarioRunContainerLogs.md) |  | [optional] 
**run_logs** | [**ScenarioRunContainerLogs**](ScenarioRunContainerLogs.md) |  | [optional] 
**post_run_logs** | [**ScenarioRunContainerLogs**](ScenarioRunContainerLogs.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


