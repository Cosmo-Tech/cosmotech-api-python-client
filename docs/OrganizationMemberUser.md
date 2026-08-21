# OrganizationMemberUser

A user member of the organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user id | 
**role** | **str** | The user role in the organization | 

## Example

```python
from cosmotech_api.models.organization_member_user import OrganizationMemberUser

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMemberUser from a JSON string
organization_member_user_instance = OrganizationMemberUser.from_json(json)
# print the JSON string representation of the object
print(OrganizationMemberUser.to_json())

# convert the object into a dict
organization_member_user_dict = organization_member_user_instance.to_dict()
# create an instance of OrganizationMemberUser from a dict
organization_member_user_from_dict = OrganizationMemberUser.from_dict(organization_member_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


