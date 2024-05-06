# ScenarioRunContainerArtifact

a scenario run container artifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the artifact name | [optional] 
**path** | **str** | the artifact path (relative to /var/csmoutput) | [optional] 

## Example

```python
from cosmotech_api.models.scenario_run_container_artifact import ScenarioRunContainerArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioRunContainerArtifact from a JSON string
scenario_run_container_artifact_instance = ScenarioRunContainerArtifact.from_json(json)
# print the JSON string representation of the object
print ScenarioRunContainerArtifact.to_json()

# convert the object into a dict
scenario_run_container_artifact_dict = scenario_run_container_artifact_instance.to_dict()
# create an instance of ScenarioRunContainerArtifact from a dict
scenario_run_container_artifact_form_dict = scenario_run_container_artifact.from_dict(scenario_run_container_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


