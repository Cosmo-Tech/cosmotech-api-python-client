# DeleteHistoricalData

Configuration of scenario runs deletion automatic mecanism

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Activate or Deactivate historical data deletion | [default to True]
**poll_frequency** | **int** | define the polling frequency of scenario run status (in millis) | [optional] [default to 10000]
**time_out** | **int** | define the polling timeout | [optional] [default to 28800]

## Example

```python
from cosmotech_api.models.delete_historical_data import DeleteHistoricalData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteHistoricalData from a JSON string
delete_historical_data_instance = DeleteHistoricalData.from_json(json)
# print the JSON string representation of the object
print(DeleteHistoricalData.to_json())

# convert the object into a dict
delete_historical_data_dict = delete_historical_data_instance.to_dict()
# create an instance of DeleteHistoricalData from a dict
delete_historical_data_from_dict = DeleteHistoricalData.from_dict(delete_historical_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


