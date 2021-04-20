# ScenarioRunContainerLogs

logs for a given container

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_id** | **str** | container ID for log source as seen by Docker engine | [optional] [readonly] 
**computer** | **str** | computer/node that&#39;s generating the log | [optional] [readonly] 
**logs** | [**[ScenarioRunContainerLog]**](ScenarioRunContainerLog.md) | the list of container logs in structured format | [optional] [readonly] 
**text_log** | **str** | the plain text log if plainText option has been set | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


