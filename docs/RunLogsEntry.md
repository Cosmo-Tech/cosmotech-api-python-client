# RunLogsEntry

single run log entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | **str** | log line data | 

## Example

```python
from cosmotech_api.models.run_logs_entry import RunLogsEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RunLogsEntry from a JSON string
run_logs_entry_instance = RunLogsEntry.from_json(json)
# print the JSON string representation of the object
print RunLogsEntry.to_json()

# convert the object into a dict
run_logs_entry_dict = run_logs_entry_instance.to_dict()
# create an instance of RunLogsEntry from a dict
run_logs_entry_form_dict = run_logs_entry.from_dict(run_logs_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


