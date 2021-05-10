# ScenarioRunContainer

a ScenarioRun container description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the container name | 
**image** | **str** | the container image URI | 
**id** | **str** | the container Id | [optional] [readonly] 
**env_vars** | **{str: (str,)}** | environment variable map | [optional] 
**entrypoint** | **str** | the container entry point | [optional] 
**run_args** | **[str]** | the list of run arguments for the container | [optional] 
**dependencies** | **[str]** | the list of dependencies container name to run this container | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


