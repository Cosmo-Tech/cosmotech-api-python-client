# Workspace

a Workspace

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the Workspace name | 
**id** | **str** | the Workspace version unique identifier | [optional] [readonly] 
**description** | **str** | the Workspace description | [optional] 
**version** | **str** | the Workspace version MAJOR.MINOR.PATCH. | [optional] 
**tags** | **[str]** | the list of tags | [optional] 
**owner_id** | **str** | the user id which own this workspace | [optional] [readonly] 
**simulator** | [**WorkspaceSimulator**](WorkspaceSimulator.md) |  | [optional] 
**user_list** | [**[WorkspaceUser]**](WorkspaceUser.md) | the list of user Id which have | [optional] 
**web_app** | [**WorkspaceWebApp**](WorkspaceWebApp.md) |  | [optional] 
**resources** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | a list of resources for the Workspace with resourceName/resourceUrl | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


