# RunStatusNode

status of a Run Node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the node id | [optional] 
**name** | **str** | the node unique name | [optional] 
**container_name** | **str** | the Run container name | [optional] 
**outbound_nodes** | **List[str]** | the list of outbound nodes | [optional] [readonly] 
**resources_duration** | [**RunResourceRequested**](RunResourceRequested.md) |  | [optional] 
**estimated_duration** | **int** | estimatedDuration in seconds | [optional] 
**host_node_name** | **str** | HostNodeName name of the Kubernetes node on which the Pod is running, if applicable | [optional] 
**message** | **str** | a human readable message indicating details about why the node is in this condition | [optional] 
**phase** | **str** | high-level summary of where the node is in its lifecycle | [optional] 
**progress** | **str** | progress to completion | [optional] 
**start_time** | **str** | the node start time | [optional] 
**end_time** | **str** | the node end time | [optional] 

## Example

```python
from cosmotech_api.models.run_status_node import RunStatusNode

# TODO update the JSON string below
json = "{}"
# create an instance of RunStatusNode from a JSON string
run_status_node_instance = RunStatusNode.from_json(json)
# print the JSON string representation of the object
print RunStatusNode.to_json()

# convert the object into a dict
run_status_node_dict = run_status_node_instance.to_dict()
# create an instance of RunStatusNode from a dict
run_status_node_form_dict = run_status_node.from_dict(run_status_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


