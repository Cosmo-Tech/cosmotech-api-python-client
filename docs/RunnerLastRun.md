# RunnerLastRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runner_run_id** | **str** | the last Runner Run id | [optional] 
**csm_simulation_run** | **str** | the last Cosmo Tech Simulation Run id | [optional] 
**workflow_id** | **str** | the last Workflow Id | [optional] 
**workflow_name** | **str** | the last Workflow name | [optional] 

## Example

```python
from cosmotech_api.models.runner_last_run import RunnerLastRun

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerLastRun from a JSON string
runner_last_run_instance = RunnerLastRun.from_json(json)
# print the JSON string representation of the object
print(RunnerLastRun.to_json())

# convert the object into a dict
runner_last_run_dict = runner_last_run_instance.to_dict()
# create an instance of RunnerLastRun from a dict
runner_last_run_from_dict = RunnerLastRun.from_dict(runner_last_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


