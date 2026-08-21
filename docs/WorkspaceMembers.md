# WorkspaceMembers

The Workspace members, including users and groups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[WorkspaceMemberUser]**](WorkspaceMemberUser.md) | The list of users in the workspace | [default to []]
**groups** | [**List[WorkspaceMemberGroup]**](WorkspaceMemberGroup.md) | The list of groups in the workspace | [default to []]

## Example

```python
from cosmotech_api.models.workspace_members import WorkspaceMembers

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMembers from a JSON string
workspace_members_instance = WorkspaceMembers.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMembers.to_json())

# convert the object into a dict
workspace_members_dict = workspace_members_instance.to_dict()
# create an instance of WorkspaceMembers from a dict
workspace_members_from_dict = WorkspaceMembers.from_dict(workspace_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


