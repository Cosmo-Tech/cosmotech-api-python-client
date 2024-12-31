# ScenarioRunResourceRequested

the memory and CPU requested by the pod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **int** | the cpu requested | [optional] 
**memory** | **int** | the memory requested | [optional] 

## Example

```python
from cosmotech_api.models.scenario_run_resource_requested import ScenarioRunResourceRequested

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioRunResourceRequested from a JSON string
scenario_run_resource_requested_instance = ScenarioRunResourceRequested.from_json(json)
# print the JSON string representation of the object
print(ScenarioRunResourceRequested.to_json())

# convert the object into a dict
scenario_run_resource_requested_dict = scenario_run_resource_requested_instance.to_dict()
# create an instance of ScenarioRunResourceRequested from a dict
scenario_run_resource_requested_from_dict = ScenarioRunResourceRequested.from_dict(scenario_run_resource_requested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


