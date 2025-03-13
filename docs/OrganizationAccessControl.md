# OrganizationAccessControl

Response object for organization access control

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the identity id | 
**role** | **str** | a role | 

## Example

```python
from cosmotech_api.models.organization_access_control import OrganizationAccessControl

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAccessControl from a JSON string
organization_access_control_instance = OrganizationAccessControl.from_json(json)
# print the JSON string representation of the object
print(OrganizationAccessControl.to_json())

# convert the object into a dict
organization_access_control_dict = organization_access_control_instance.to_dict()
# create an instance of OrganizationAccessControl from a dict
organization_access_control_from_dict = OrganizationAccessControl.from_dict(organization_access_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


