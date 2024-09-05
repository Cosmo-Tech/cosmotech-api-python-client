# DatasetTwinGraphInfo

a twin graph query in cypher language

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | the import job id | [optional] 
**dataset_id** | **str** | the Dataset id | [optional] 
**status** | **str** | Twingraph status | [optional] 

## Example

```python
from cosmotech_api.models.dataset_twin_graph_info import DatasetTwinGraphInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetTwinGraphInfo from a JSON string
dataset_twin_graph_info_instance = DatasetTwinGraphInfo.from_json(json)
# print the JSON string representation of the object
print(DatasetTwinGraphInfo.to_json())

# convert the object into a dict
dataset_twin_graph_info_dict = dataset_twin_graph_info_instance.to_dict()
# create an instance of DatasetTwinGraphInfo from a dict
dataset_twin_graph_info_from_dict = DatasetTwinGraphInfo.from_dict(dataset_twin_graph_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


