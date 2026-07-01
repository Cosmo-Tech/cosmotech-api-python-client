# ComponentRolePermissions

A RBAC by component

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | 
**roles** | **Dict[str, List[str]]** |  | 

## Example

```python
from cosmotech_api.models.component_role_permissions import ComponentRolePermissions

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentRolePermissions from a JSON string
component_role_permissions_instance = ComponentRolePermissions.from_json(json)
# print the JSON string representation of the object
print(ComponentRolePermissions.to_json())

# convert the object into a dict
component_role_permissions_dict = component_role_permissions_instance.to_dict()
# create an instance of ComponentRolePermissions from a dict
component_role_permissions_from_dict = ComponentRolePermissions.from_dict(component_role_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


