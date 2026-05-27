# OrganizationRole

the Organization Role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | the Organization Role | 

## Example

```python
from cosmotech_api.models.organization_role import OrganizationRole

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationRole from a JSON string
organization_role_instance = OrganizationRole.from_json(json)
# print the JSON string representation of the object
print(OrganizationRole.to_json())

# convert the object into a dict
organization_role_dict = organization_role_instance.to_dict()
# create an instance of OrganizationRole from a dict
organization_role_from_dict = OrganizationRole.from_dict(organization_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


