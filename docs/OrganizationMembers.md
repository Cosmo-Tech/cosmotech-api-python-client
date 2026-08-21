# OrganizationMembers

The Organization members, including users and groups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[OrganizationMemberUser]**](OrganizationMemberUser.md) | The list of users in the organization | [default to []]
**groups** | [**List[OrganizationMemberGroup]**](OrganizationMemberGroup.md) | The list of groups in the organization | [default to []]

## Example

```python
from cosmotech_api.models.organization_members import OrganizationMembers

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMembers from a JSON string
organization_members_instance = OrganizationMembers.from_json(json)
# print the JSON string representation of the object
print(OrganizationMembers.to_json())

# convert the object into a dict
organization_members_dict = organization_members_instance.to_dict()
# create an instance of OrganizationMembers from a dict
organization_members_from_dict = OrganizationMembers.from_dict(organization_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


