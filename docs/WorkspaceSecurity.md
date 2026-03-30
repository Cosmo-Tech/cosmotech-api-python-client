# WorkspaceSecurity

The workspace security information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | The role by default | 
**access_control_list** | [**List[WorkspaceAccessControl]**](WorkspaceAccessControl.md) | The list which can access this Workspace with detailed access control information | 

## Example

```python
from cosmotech_api.models.workspace_security import WorkspaceSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSecurity from a JSON string
workspace_security_instance = WorkspaceSecurity.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSecurity.to_json())

# convert the object into a dict
workspace_security_dict = workspace_security_instance.to_dict()
# create an instance of WorkspaceSecurity from a dict
workspace_security_from_dict = WorkspaceSecurity.from_dict(workspace_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


