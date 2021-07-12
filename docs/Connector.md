# Connector

a version of a Connector

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | the Connector key which group Connector versions | 
**name** | **str** | the Connector name | 
**repository** | **str** | the registry repository containing the image | 
**version** | **str** | the Connector version MAJOR.MINOR.PATCH. Must be aligned with an existing repository tag | 
**io_types** | **[str]** |  | 
**id** | **str** | the Connector version unique identifier | [optional] [readonly] 
**description** | **str** | the Connector description | [optional] 
**tags** | **[str]** | the list of tags | [optional] 
**owner_id** | **str** | the user id which own this connector version | [optional] [readonly] 
**url** | **str** | an optional URL link to connector page | [optional] 
**parameter_groups** | [**[ConnectorParameterGroup]**](ConnectorParameterGroup.md) | the list of connector parameters groups | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


