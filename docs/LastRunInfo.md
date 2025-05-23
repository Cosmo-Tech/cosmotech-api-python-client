# LastRunInfo

last run info from current runner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_run_id** | **str** | last run id from current runner | [optional] 
**last_run_status** | **str** | last run status from current runner | [optional] 

## Example

```python
from cosmotech_api.models.last_run_info import LastRunInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LastRunInfo from a JSON string
last_run_info_instance = LastRunInfo.from_json(json)
# print the JSON string representation of the object
print(LastRunInfo.to_json())

# convert the object into a dict
last_run_info_dict = last_run_info_instance.to_dict()
# create an instance of LastRunInfo from a dict
last_run_info_from_dict = LastRunInfo.from_dict(last_run_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


