# DatasetCreateInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | The timestamp of the creation in millisecond | 
**user_id** | **str** | The id of the user who did the creation | 
**runner_id** | **str** | The runner id which has created the dataset (nullable) | [optional] 

## Example

```python
from cosmotech_api.models.dataset_create_info import DatasetCreateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetCreateInfo from a JSON string
dataset_create_info_instance = DatasetCreateInfo.from_json(json)
# print the JSON string representation of the object
print(DatasetCreateInfo.to_json())

# convert the object into a dict
dataset_create_info_dict = dataset_create_info_instance.to_dict()
# create an instance of DatasetCreateInfo from a dict
dataset_create_info_from_dict = DatasetCreateInfo.from_dict(dataset_create_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


