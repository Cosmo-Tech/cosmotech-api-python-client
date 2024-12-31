# ScenarioRunLogs

the scenariorun logs returned by all containers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenariorun_id** | **str** | the ScenarioRun Id | [optional] [readonly] 
**containers** | [**Dict[str, ScenarioRunContainerLogs]**](ScenarioRunContainerLogs.md) | the container map of logs | [optional] [readonly] 

## Example

```python
from cosmotech_api.models.scenario_run_logs import ScenarioRunLogs

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioRunLogs from a JSON string
scenario_run_logs_instance = ScenarioRunLogs.from_json(json)
# print the JSON string representation of the object
print(ScenarioRunLogs.to_json())

# convert the object into a dict
scenario_run_logs_dict = scenario_run_logs_instance.to_dict()
# create an instance of ScenarioRunLogs from a dict
scenario_run_logs_from_dict = ScenarioRunLogs.from_dict(scenario_run_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


