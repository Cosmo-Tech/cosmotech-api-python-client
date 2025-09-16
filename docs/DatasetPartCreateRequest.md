# DatasetPartCreateRequest

Dataset part create request object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**source_name** | **str** | the source data name (e.g. filename associated to the dataset part) | 
**description** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] [default to []]
**type** | [**DatasetPartTypeEnum**](DatasetPartTypeEnum.md) |  | [optional] [default to DatasetPartTypeEnum.FILE]

## Example

```python
from cosmotech_api.models.dataset_part_create_request import DatasetPartCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetPartCreateRequest from a JSON string
dataset_part_create_request_instance = DatasetPartCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DatasetPartCreateRequest.to_json())

# convert the object into a dict
dataset_part_create_request_dict = dataset_part_create_request_instance.to_dict()
# create an instance of DatasetPartCreateRequest from a dict
dataset_part_create_request_from_dict = DatasetPartCreateRequest.from_dict(dataset_part_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


