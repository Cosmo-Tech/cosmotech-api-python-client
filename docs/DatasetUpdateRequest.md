# DatasetUpdateRequest

Dataset creation request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**additional_data** | **Dict[str, object]** | Free form additional data | [optional] 
**parts** | [**List[DatasetPartCreateRequest]**](DatasetPartCreateRequest.md) |  | [optional] 
**security** | [**DatasetSecurity**](DatasetSecurity.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.dataset_update_request import DatasetUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetUpdateRequest from a JSON string
dataset_update_request_instance = DatasetUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DatasetUpdateRequest.to_json())

# convert the object into a dict
dataset_update_request_dict = dataset_update_request_instance.to_dict()
# create an instance of DatasetUpdateRequest from a dict
dataset_update_request_from_dict = DatasetUpdateRequest.from_dict(dataset_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


