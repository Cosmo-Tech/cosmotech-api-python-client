# Solution

a version of a Solution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Solution version unique identifier | [optional] [readonly] 
**organization_id** | **str** | the Organization unique identifier | [optional] [readonly] 
**key** | **str** | the Solution key which group Solution versions | [optional] 
**name** | **str** | the Solution name | [optional] 
**description** | **str** | the Solution description | [optional] 
**repository** | **str** | the registry repository containing the image | [optional] 
**csm_simulator** | **str** | the main Cosmo Tech simulator name used in standard Run Template | [optional] 
**version** | **str** | the Solution version MAJOR.MINOR.PATCH. Must be aligned with an existing repository tag | [optional] 
**owner_id** | **str** | the User id which own this Solution | [optional] [readonly] 
**sdk_version** | **str** | the MAJOR.MINOR version used to build this solution | [optional] 
**url** | **str** | an optional URL link to solution page | [optional] 
**tags** | **[str]** | the list of tags | [optional] 
**parameters** | [**[RunTemplateParameter]**](RunTemplateParameter.md) | the list of Run Template Parameters | [optional] 
**parameter_groups** | [**[RunTemplateParameterGroup]**](RunTemplateParameterGroup.md) | the list of parameters groups for the Run Templates | [optional] 
**run_templates** | [**[RunTemplate]**](RunTemplate.md) | list of Run Template | [optional] 
**security** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


