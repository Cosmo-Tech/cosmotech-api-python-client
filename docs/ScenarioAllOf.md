# ScenarioAllOf

a Scenario with detailed information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**simulator_id** | **str** | the Simulator Id associated with this Scenario | [optional] [readonly] 
**analyses** | [**[ScenarioAnalysis]**](ScenarioAnalysis.md) | the configuration for next Analysis | [optional] 
**successful_analyses** | [**[ScenarioSuccessfulAnalysis]**](ScenarioSuccessfulAnalysis.md) | the configuration and information for last successful Analyses Runs | [optional] [readonly] 
**failed_analyses** | [**[ScenarioFailedAnalysis]**](ScenarioFailedAnalysis.md) | the configuration and information for last failed Analyses Runs | [optional] [readonly] 
**running_analyses** | [**[ScenarioRunningAnalysis]**](ScenarioRunningAnalysis.md) | the configuration and information for currently running Analyses Runs | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


