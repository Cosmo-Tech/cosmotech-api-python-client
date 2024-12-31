# ScenarioRunContainer

a ScenarioRun container description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the container Id | [optional] [readonly] 
**name** | **str** | the container name | 
**labels** | **Dict[str, str]** | the metadata labels | [optional] 
**env_vars** | **Dict[str, str]** | environment variable map | [optional] 
**image** | **str** | the container image URI | 
**entrypoint** | **str** | the container entry point | [optional] 
**run_args** | **List[str]** | the list of run arguments for the container | [optional] 
**dependencies** | **List[str]** | the list of dependencies container name to run this container | [optional] 
**solution_container** | **bool** | whether or not this container is a Cosmo Tech solution container | [optional] [readonly] 
**node_label** | **str** | the node label request | [optional] 
**run_sizing** | [**ContainerResourceSizing**](ContainerResourceSizing.md) |  | [optional] 
**artifacts** | [**List[ScenarioRunContainerArtifact]**](ScenarioRunContainerArtifact.md) | the list of artifacts | [optional] 

## Example

```python
from cosmotech_api.models.scenario_run_container import ScenarioRunContainer

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioRunContainer from a JSON string
scenario_run_container_instance = ScenarioRunContainer.from_json(json)
# print the JSON string representation of the object
print(ScenarioRunContainer.to_json())

# convert the object into a dict
scenario_run_container_dict = scenario_run_container_instance.to_dict()
# create an instance of ScenarioRunContainer from a dict
scenario_run_container_from_dict = ScenarioRunContainer.from_dict(scenario_run_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


