# DeleteHistoricalData

Configuration of scenario runs deletion automatic mecanism

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Activate or Deactivate historical data deletion | defaults to True
**poll_frequency** | **int** | define the polling frequency of scenario run status (in millis) | [optional]  if omitted the server will use the default value of 10000
**time_out** | **int** | define the polling timeout | [optional]  if omitted the server will use the default value of 28800
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


