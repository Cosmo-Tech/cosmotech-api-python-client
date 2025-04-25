# RunnerEditInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | The timestamp of the modification in millisecond | 
**user_id** | **str** | The id of the user who did the modification | 

## Example

```python
from cosmotech_api.models.runner_edit_info import RunnerEditInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerEditInfo from a JSON string
runner_edit_info_instance = RunnerEditInfo.from_json(json)
# print the JSON string representation of the object
print(RunnerEditInfo.to_json())

# convert the object into a dict
runner_edit_info_dict = runner_edit_info_instance.to_dict()
# create an instance of RunnerEditInfo from a dict
runner_edit_info_from_dict = RunnerEditInfo.from_dict(runner_edit_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


