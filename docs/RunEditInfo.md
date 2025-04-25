# RunEditInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | The timestamp of the modification in millisecond | 
**user_id** | **str** | The id of the user who did the modification | 

## Example

```python
from cosmotech_api.models.run_edit_info import RunEditInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RunEditInfo from a JSON string
run_edit_info_instance = RunEditInfo.from_json(json)
# print the JSON string representation of the object
print(RunEditInfo.to_json())

# convert the object into a dict
run_edit_info_dict = run_edit_info_instance.to_dict()
# create an instance of RunEditInfo from a dict
run_edit_info_from_dict = RunEditInfo.from_dict(run_edit_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


