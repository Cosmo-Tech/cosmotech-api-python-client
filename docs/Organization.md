# Organization

An Organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Organization unique identifier | [readonly] 
**name** | **str** | The Organization name | 
**create_info** | [**OrganizationEditInfo**](OrganizationEditInfo.md) | The details of the Organization creation | 
**update_info** | [**OrganizationEditInfo**](OrganizationEditInfo.md) | The details of the Organization last update | 
**security** | [**OrganizationSecurity**](OrganizationSecurity.md) |  | 

## Example

```python
from cosmotech_api.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_from_dict = Organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


