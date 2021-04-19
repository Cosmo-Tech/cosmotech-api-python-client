# PlatformServices

the list of Platform services

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | the Cloud Provider for the services | defaults to "Azure"
**credentials** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | a freeform credentials object for the Platform. Structure depends on cloud provider | [optional] 
**storage** | [**PlatformService**](PlatformService.md) |  | [optional] 
**core_container_registry** | [**PlatformService**](PlatformService.md) |  | [optional] 
**solutions_container_registry** | [**PlatformService**](PlatformService.md) |  | [optional] 
**event_bus_cluster** | [**PlatformService**](PlatformService.md) |  | [optional] 
**data_warehouse_cluster** | [**PlatformService**](PlatformService.md) |  | [optional] 
**database_cluster** | [**PlatformService**](PlatformService.md) |  | [optional] 
**key_vault** | [**PlatformService**](PlatformService.md) |  | [optional] 
**kubernetes_cluster** | [**PlatformService**](PlatformService.md) |  | [optional] 
**directory** | [**PlatformService**](PlatformService.md) |  | [optional] 
**monitoring** | [**PlatformService**](PlatformService.md) |  | [optional] 
**analytic** | [**PlatformService**](PlatformService.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


