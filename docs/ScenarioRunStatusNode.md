# ScenarioRunStatusNode

status of a ScenarioRun Node

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the node id | [optional] 
**name** | **str** | the node unique name | [optional] 
**container_name** | **str** | the ScenarioRun container name | [optional] 
**outbound_nodes** | **[str]** | the list of outbound nodes | [optional] [readonly] 
**resources_duration** | [**ScenarioRunResourceRequested**](ScenarioRunResourceRequested.md) |  | [optional] 
**estimated_duration** | **int** | estimatedDuration in seconds | [optional] 
**host_node_name** | **str** | HostNodeName name of the Kubernetes node on which the Pod is running, if applicable | [optional] 
**message** | **str** | a human readable message indicating details about why the node is in this condition | [optional] 
**phase** | **str** | high-level summary of where the node is in its lifecycle | [optional] 
**progress** | **str** | progress to completion | [optional] 
**start_time** | **str** | the node start time | [optional] 
**end_time** | **str** | the node end time | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


