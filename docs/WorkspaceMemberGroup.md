# WorkspaceMemberGroup

A group member of the workspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The group id | 
**role** | **str** | The group role in the workspace | 
**users** | **List[str]** | The list of users in the group | 

## Example

```python
from cosmotech_api.models.workspace_member_group import WorkspaceMemberGroup

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMemberGroup from a JSON string
workspace_member_group_instance = WorkspaceMemberGroup.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMemberGroup.to_json())

# convert the object into a dict
workspace_member_group_dict = workspace_member_group_instance.to_dict()
# create an instance of WorkspaceMemberGroup from a dict
workspace_member_group_from_dict = WorkspaceMemberGroup.from_dict(workspace_member_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


