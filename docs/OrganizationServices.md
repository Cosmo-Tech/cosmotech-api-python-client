# OrganizationServices

the cloud service resources of the Organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_credentials** | **Dict[str, object]** | a freeform credentials object for the Organization tenant. Structure depends on cloud provider | [optional] 
**storage** | [**OrganizationService**](OrganizationService.md) |  | [optional] 
**solutions_container_registry** | [**OrganizationService**](OrganizationService.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.organization_services import OrganizationServices

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationServices from a JSON string
organization_services_instance = OrganizationServices.from_json(json)
# print the JSON string representation of the object
print(OrganizationServices.to_json())

# convert the object into a dict
organization_services_dict = organization_services_instance.to_dict()
# create an instance of OrganizationServices from a dict
organization_services_from_dict = OrganizationServices.from_dict(organization_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


