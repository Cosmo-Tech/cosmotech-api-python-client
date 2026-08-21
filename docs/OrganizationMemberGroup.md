# OrganizationMemberGroup

A group member of the organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The group id | 
**role** | **str** | The user role in the organization | 
**users** | **List[str]** | The list of users in the group | 

## Example

```python
from cosmotech_api.models.organization_member_group import OrganizationMemberGroup

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMemberGroup from a JSON string
organization_member_group_instance = OrganizationMemberGroup.from_json(json)
# print the JSON string representation of the object
print(OrganizationMemberGroup.to_json())

# convert the object into a dict
organization_member_group_dict = organization_member_group_instance.to_dict()
# create an instance of OrganizationMemberGroup from a dict
organization_member_group_from_dict = OrganizationMemberGroup.from_dict(organization_member_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


