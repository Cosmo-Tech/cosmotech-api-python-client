# TwinGraphBatchResult

Processing result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_lines** | **int** |  | 
**processed_lines** | **int** |  | 
**errors** | **List[str]** |  | 

## Example

```python
from cosmotech_api.models.twin_graph_batch_result import TwinGraphBatchResult

# TODO update the JSON string below
json = "{}"
# create an instance of TwinGraphBatchResult from a JSON string
twin_graph_batch_result_instance = TwinGraphBatchResult.from_json(json)
# print the JSON string representation of the object
print(TwinGraphBatchResult.to_json())

# convert the object into a dict
twin_graph_batch_result_dict = twin_graph_batch_result_instance.to_dict()
# create an instance of TwinGraphBatchResult from a dict
twin_graph_batch_result_from_dict = TwinGraphBatchResult.from_dict(twin_graph_batch_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


