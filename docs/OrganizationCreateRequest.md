# OrganizationCreateRequest

Request object for creating a new organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the Organization name | 
**security** | [**OrganizationSecurity**](OrganizationSecurity.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.organization_create_request import OrganizationCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCreateRequest from a JSON string
organization_create_request_instance = OrganizationCreateRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationCreateRequest.to_json())

# convert the object into a dict
organization_create_request_dict = organization_create_request_instance.to_dict()
# create an instance of OrganizationCreateRequest from a dict
organization_create_request_from_dict = OrganizationCreateRequest.from_dict(organization_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


