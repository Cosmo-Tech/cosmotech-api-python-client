# Organization

an Organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Organization unique identifier | [optional] [readonly] 
**name** | **str** | the Organization name | [optional] 
**owner_id** | **str** | the Owner User Id | [optional] [readonly] 
**services** | [**OrganizationServices**](OrganizationServices.md) |  | [optional] 
**security** | [**OrganizationSecurity**](OrganizationSecurity.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print Organization.to_json()

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_form_dict = organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


