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
**nodes** | [**List[ScenarioRunStatusNode]**](ScenarioRunStatusNode.md) | status of ScenarioRun nodes | [optional] 
**state** | [**ScenarioRunState**](ScenarioRunState.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.scenario_run_status import ScenarioRunStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioRunStatus from a JSON string
scenario_run_status_instance = ScenarioRunStatus.from_json(json)
# print the JSON string representation of the object
print(ScenarioRunStatus.to_json())

# convert the object into a dict
scenario_run_status_dict = scenario_run_status_instance.to_dict()
# create an instance of ScenarioRunStatus from a dict
scenario_run_status_from_dict = ScenarioRunStatus.from_dict(scenario_run_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


