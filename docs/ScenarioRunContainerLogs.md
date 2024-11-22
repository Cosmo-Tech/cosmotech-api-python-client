# ScenarioRunContainerLogs

logs for a given container

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | the node Id which has executed this log | [optional] [readonly] 
**container_name** | **str** | the container name | [optional] [readonly] 
**children** | **List[str]** | the list of children node id | [optional] [readonly] 
**logs** | **str** | the node logs in plain text | [optional] [readonly] 

## Example

```python
from cosmotech_api.models.scenario_run_container_logs import ScenarioRunContainerLogs

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioRunContainerLogs from a JSON string
scenario_run_container_logs_instance = ScenarioRunContainerLogs.from_json(json)
# print the JSON string representation of the object
print ScenarioRunContainerLogs.to_json()

# convert the object into a dict
scenario_run_container_logs_dict = scenario_run_container_logs_instance.to_dict()
# create an instance of ScenarioRunContainerLogs from a dict
scenario_run_container_logs_form_dict = scenario_run_container_logs.from_dict(scenario_run_container_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


