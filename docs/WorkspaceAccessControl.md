# WorkspaceAccessControl

A Workspace access control item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identity id | 
**role** | **str** | A role | 

## Example

```python
from cosmotech_api.models.workspace_access_control import WorkspaceAccessControl

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceAccessControl from a JSON string
workspace_access_control_instance = WorkspaceAccessControl.from_json(json)
# print the JSON string representation of the object
print(WorkspaceAccessControl.to_json())

# convert the object into a dict
workspace_access_control_dict = workspace_access_control_instance.to_dict()
# create an instance of WorkspaceAccessControl from a dict
workspace_access_control_from_dict = WorkspaceAccessControl.from_dict(workspace_access_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


