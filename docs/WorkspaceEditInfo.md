# WorkspaceEditInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | The timestamp of the modification in millisecond | 
**user_id** | **str** | The id of the user who did the modification | 

## Example

```python
from cosmotech_api.models.workspace_edit_info import WorkspaceEditInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceEditInfo from a JSON string
workspace_edit_info_instance = WorkspaceEditInfo.from_json(json)
# print the JSON string representation of the object
print(WorkspaceEditInfo.to_json())

# convert the object into a dict
workspace_edit_info_dict = workspace_edit_info_instance.to_dict()
# create an instance of WorkspaceEditInfo from a dict
workspace_edit_info_from_dict = WorkspaceEditInfo.from_dict(workspace_edit_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


