# Connector

a version of a Connector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Connector version unique identifier | [optional] [readonly] 
**key** | **str** | the Connector key which group Connector versions | [optional] 
**name** | **str** | the Connector name | [optional] 
**description** | **str** | the Connector description | [optional] 
**repository** | **str** | the registry repository containing the image | [optional] 
**version** | **str** | the Connector version MAJOR.MINOR.PATCH. Must be aligned with an existing repository tag | [optional] 
**tags** | **List[str]** | the list of tags | [optional] 
**owner_id** | **str** | the user id which own this connector version | [optional] [readonly] 
**url** | **str** | an optional URL link to connector page | [optional] 
**azure_managed_identity** | **bool** | whether or not the connector uses Azure Managed Identity | [optional] 
**azure_authentication_with_customer_app_registration** | **bool** | whether to authenticate against Azure using the app registration credentials provided by the customer | [optional] 
**io_types** | **List[str]** |  | [optional] 
**parameter_groups** | [**List[ConnectorParameterGroup]**](ConnectorParameterGroup.md) | the list of connector parameters groups | [optional] 

## Example

```python
from cosmotech_api.models.connector import Connector

# TODO update the JSON string below
json = "{}"
# create an instance of Connector from a JSON string
connector_instance = Connector.from_json(json)
# print the JSON string representation of the object
print Connector.to_json()

# convert the object into a dict
connector_dict = connector_instance.to_dict()
# create an instance of Connector from a dict
connector_form_dict = connector.from_dict(connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


