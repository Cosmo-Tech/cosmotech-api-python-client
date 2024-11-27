# RunContainerLogs

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
from cosmotech_api.models.run_container_logs import RunContainerLogs

# TODO update the JSON string below
json = "{}"
# create an instance of RunContainerLogs from a JSON string
run_container_logs_instance = RunContainerLogs.from_json(json)
# print the JSON string representation of the object
print RunContainerLogs.to_json()

# convert the object into a dict
run_container_logs_dict = run_container_logs_instance.to_dict()
# create an instance of RunContainerLogs from a dict
run_container_logs_form_dict = run_container_logs.from_dict(run_container_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


