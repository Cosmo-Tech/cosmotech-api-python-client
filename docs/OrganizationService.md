# OrganizationService

a cloud service resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_service** | **str** | the cloud service name | [optional] 
**base_uri** | **str** | the platform base uri for this service | [optional] 
**platform_service** | **str** | the Platform service associated to the resource | [optional] 
**resource_uri** | **str** | the Organization specific uri for this service resource | [optional] 
**credentials** | **Dict[str, object]** | a freeform credentials object. Structure depends on service | [optional] 

## Example

```python
from cosmotech_api.models.organization_service import OrganizationService

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationService from a JSON string
organization_service_instance = OrganizationService.from_json(json)
# print the JSON string representation of the object
print OrganizationService.to_json()

# convert the object into a dict
organization_service_dict = organization_service_instance.to_dict()
# create an instance of OrganizationService from a dict
organization_service_form_dict = organization_service.from_dict(organization_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


