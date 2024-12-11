# RunStatus

a Run status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Run id | [optional] 
**organization_id** | **str** | the Organization id | [optional] 
**workspace_id** | **str** | the Workspace id | [optional] 
**runner_id** | **str** | the Runner id | [optional] 
**workflow_id** | **str** | the Cosmo Tech compute cluster Argo Workflow Id to search | [optional] 
**workflow_name** | **str** | the Cosmo Tech compute cluster Argo Workflow Name | [optional] 
**start_time** | **str** | the Run start Date Time | [optional] 
**end_time** | **str** | the Run end Date Time | [optional] 
**phase** | **str** | high-level summary of where the workflow is in its lifecycle | [optional] 
**progress** | **str** | progress to completion | [optional] 
**message** | **str** | a  human readable message indicating details about why the workflow is in this condition | [optional] 
**estimated_duration** | **int** | estimatedDuration in seconds | [optional] 
**nodes** | [**List[RunStatusNode]**](RunStatusNode.md) | status of Run nodes | [optional] 
**state** | [**RunState**](RunState.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.run_status import RunStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RunStatus from a JSON string
run_status_instance = RunStatus.from_json(json)
# print the JSON string representation of the object
print(RunStatus.to_json())

# convert the object into a dict
run_status_dict = run_status_instance.to_dict()
# create an instance of RunStatus from a dict
run_status_from_dict = RunStatus.from_dict(run_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


