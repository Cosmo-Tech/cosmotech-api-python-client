# RunLogs

the run logs returned by all containers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | the Run Id | [optional] [readonly] 
**containers** | [**Dict[str, RunContainerLogs]**](RunContainerLogs.md) | the container map of logs | [optional] [readonly] 

## Example

```python
from cosmotech_api.models.run_logs import RunLogs

# TODO update the JSON string below
json = "{}"
# create an instance of RunLogs from a JSON string
run_logs_instance = RunLogs.from_json(json)
# print the JSON string representation of the object
print RunLogs.to_json()

# convert the object into a dict
run_logs_dict = run_logs_instance.to_dict()
# create an instance of RunLogs from a dict
run_logs_form_dict = run_logs.from_dict(run_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


