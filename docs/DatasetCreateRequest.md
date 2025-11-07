# DatasetCreateRequest

Dataset creation request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] [default to []]
**additional_data** | **Dict[str, object]** | Free form additional data | [optional] 
**parts** | [**List[DatasetPartCreateRequest]**](DatasetPartCreateRequest.md) |  | [optional] [default to []]
**security** | [**DatasetSecurity**](DatasetSecurity.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.dataset_create_request import DatasetCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetCreateRequest from a JSON string
dataset_create_request_instance = DatasetCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DatasetCreateRequest.to_json())

# convert the object into a dict
dataset_create_request_dict = dataset_create_request_instance.to_dict()
# create an instance of DatasetCreateRequest from a dict
dataset_create_request_from_dict = DatasetCreateRequest.from_dict(dataset_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


