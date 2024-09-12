# OrganizationSecurity

the Organization security information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | the role by default | 
**access_control_list** | [**List[OrganizationAccessControl]**](OrganizationAccessControl.md) | the list which can access this Organization with detailed access control information | 

## Example

```python
from cosmotech_api.models.organization_security import OrganizationSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSecurity from a JSON string
organization_security_instance = OrganizationSecurity.from_json(json)
# print the JSON string representation of the object
print OrganizationSecurity.to_json()

# convert the object into a dict
organization_security_dict = organization_security_instance.to_dict()
# create an instance of OrganizationSecurity from a dict
organization_security_form_dict = organization_security.from_dict(organization_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


