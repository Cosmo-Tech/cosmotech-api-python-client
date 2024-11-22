# ScenarioRunStartContainers

the parameters to run directly containers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generate_name** | **str** | the base name for workflow name generation | [optional] 
**csm_simulation_id** | **str** | Cosmo Tech Simulation Run Id | 
**node_label** | **str** | the node label request | [optional] 
**labels** | **Dict[str, str]** | the workflow labels | [optional] 
**containers** | [**List[ScenarioRunContainer]**](ScenarioRunContainer.md) | the containerslist | 

## Example

```python
from cosmotech_api.models.scenario_run_start_containers import ScenarioRunStartContainers

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioRunStartContainers from a JSON string
scenario_run_start_containers_instance = ScenarioRunStartContainers.from_json(json)
# print the JSON string representation of the object
print ScenarioRunStartContainers.to_json()

# convert the object into a dict
scenario_run_start_containers_dict = scenario_run_start_containers_instance.to_dict()
# create an instance of ScenarioRunStartContainers from a dict
scenario_run_start_containers_form_dict = scenario_run_start_containers.from_dict(scenario_run_start_containers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


