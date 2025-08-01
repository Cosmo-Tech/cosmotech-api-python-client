# DatasetPartUpdateRequest

Dataset part update request object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_name** | **str** | the source data name (e.g. filename associated to the dataset part) | [optional] 
**description** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from cosmotech_api.models.dataset_part_update_request import DatasetPartUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetPartUpdateRequest from a JSON string
dataset_part_update_request_instance = DatasetPartUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DatasetPartUpdateRequest.to_json())

# convert the object into a dict
dataset_part_update_request_dict = dataset_part_update_request_instance.to_dict()
# create an instance of DatasetPartUpdateRequest from a dict
dataset_part_update_request_from_dict = DatasetPartUpdateRequest.from_dict(dataset_part_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


