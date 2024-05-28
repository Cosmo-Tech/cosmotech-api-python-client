# RunContainer

a Run container description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the container name | 
**image** | **str** | the container image URI | 
**id** | **str** | the container Id | [optional] [readonly] 
**labels** | **{str: (str,)}** | the metadata labels | [optional] 
**env_vars** | **{str: (str,)}** | environment variable map | [optional] 
**entrypoint** | **str** | the container entry point | [optional] 
**run_args** | **[str]** | the list of run arguments for the container | [optional] 
**dependencies** | **[str]** | the list of dependencies container name to run this container | [optional] 
**solution_container** | **bool** | whether or not this container is a Cosmo Tech solution container | [optional] [readonly] 
**node_label** | **str** | the node label request | [optional] 
**run_sizing** | [**ContainerResourceSizing**](ContainerResourceSizing.md) |  | [optional] 
**artifacts** | [**[RunContainerArtifact]**](RunContainerArtifact.md) | the list of artifacts | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


