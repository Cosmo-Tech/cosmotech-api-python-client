# WorkspaceFile

A Workspace File resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | The Workspace File name | 

## Example

```python
from cosmotech_api.models.workspace_file import WorkspaceFile

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceFile from a JSON string
workspace_file_instance = WorkspaceFile.from_json(json)
# print the JSON string representation of the object
print(WorkspaceFile.to_json())

# convert the object into a dict
workspace_file_dict = workspace_file_instance.to_dict()
# create an instance of WorkspaceFile from a dict
workspace_file_from_dict = WorkspaceFile.from_dict(workspace_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


