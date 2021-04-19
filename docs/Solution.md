# Solution

a version of a Solution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solution_key** | **str** | the Solution key which group Solution versions | 
**name** | **str** | the Solution name | 
**repository** | **str** | the registry repository containing the image | 
**version** | **str** | the Solution version MAJOR.MINOR.PATCH. Must be aligned with an existing repository tag | 
**id** | **str** | the Solution version unique identifier | [optional] [readonly] 
**description** | **str** | the Solution description | [optional] 
**simulator** | **str** | the main simulator name used in standard Run Template | [optional] 
**owner_id** | **str** | the User id which own this Solution | [optional] [readonly] 
**url** | **str** | an optional URL link to solution page | [optional] 
**tags** | **[str]** | the list of tags | [optional] 
**run_templates** | [**[RunTemplate]**](RunTemplate.md) | list of Run Template | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


