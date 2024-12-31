# ScenarioLastRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenario_run_id** | **str** | the last Scenario Run id | [optional] 
**csm_simulation_run** | **str** | the last Cosmo Tech Simulation Run id | [optional] 
**workflow_id** | **str** | the last Workflow Id | [optional] 
**workflow_name** | **str** | the last Workflow name | [optional] 

## Example

```python
from cosmotech_api.models.scenario_last_run import ScenarioLastRun

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioLastRun from a JSON string
scenario_last_run_instance = ScenarioLastRun.from_json(json)
# print the JSON string representation of the object
print(ScenarioLastRun.to_json())

# convert the object into a dict
scenario_last_run_dict = scenario_last_run_instance.to_dict()
# create an instance of ScenarioLastRun from a dict
scenario_last_run_from_dict = ScenarioLastRun.from_dict(scenario_last_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


