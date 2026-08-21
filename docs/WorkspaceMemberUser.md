# WorkspaceMemberUser

A user member of the workspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user id | 
**role** | **str** | The user role in the workspace | 

## Example

```python
from cosmotech_api.models.workspace_member_user import WorkspaceMemberUser

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMemberUser from a JSON string
workspace_member_user_instance = WorkspaceMemberUser.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMemberUser.to_json())

# convert the object into a dict
workspace_member_user_dict = workspace_member_user_instance.to_dict()
# create an instance of WorkspaceMemberUser from a dict
workspace_member_user_from_dict = WorkspaceMemberUser.from_dict(workspace_member_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


