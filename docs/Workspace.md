# Workspace

a Workspace

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the Workspace name | 
**simulator** | [**WorkspaceSimulator**](WorkspaceSimulator.md) |  | 
**id** | **str** | the Workspace version unique identifier | [optional] [readonly] 
**description** | **str** | the Workspace description | [optional] 
**version** | **str** | the Workspace version MAJOR.MINOR.PATCH. | [optional] 
**tags** | **[str]** | the list of tags | [optional] 
**owner_id** | **str** | the user id which own this workspace | [optional] [readonly] 
**simulator_analysis_filter** | **[str]** | a filter list of available Simulator Analysis | [optional] 
**users** | [**[WorkspaceUser]**](WorkspaceUser.md) | the list of users Id with their role | [optional] 
**web_app** | [**WorkspaceWebApp**](WorkspaceWebApp.md) |  | [optional] 
**services** | [**WorkspaceServices**](WorkspaceServices.md) |  | [optional] 
**send_input_to_data_warehouse** | **bool** | default setting for all Scenarios and Analysis to set whether or not the Dataset values and the input parameters values are send to the DataWarehouse prior to Simulation Run | [optional]  if omitted the server will use the default value of True

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


