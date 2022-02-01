# ScenarioRunStatus

a ScenarioRun status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the ScenarioRun id | [optional] 
**organization_id** | **str** | the ScenarioRun id | [optional] 
**workflow_id** | **str** | the Cosmo Tech compute cluster Argo Workflow Id to search | [optional] 
**workflow_name** | **str** | the Cosmo Tech compute cluster Argo Workflow Name | [optional] 
**start_time** | **str** | the ScenarioRun start Date Time | [optional] 
**end_time** | **str** | the ScenarioRun end Date Time | [optional] 
**phase** | **str** | high-level summary of where the workflow is in its lifecycle | [optional] 
**progress** | **str** | progress to completion | [optional] 
**message** | **str** | a  human readable message indicating details about why the workflow is in this condition | [optional] 
**estimated_duration** | **int** | estimatedDuration in seconds | [optional] 
**nodes** | [**[ScenarioRunStatusNode]**](ScenarioRunStatusNode.md) | status of ScenarioRun nodes | [optional] 
**state** | [**ScenarioRunState**](ScenarioRunState.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


