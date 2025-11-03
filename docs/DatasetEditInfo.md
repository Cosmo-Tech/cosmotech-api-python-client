# DatasetEditInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | The timestamp of the modification in millisecond | 
**user_id** | **str** | The id of the user who did the modification | 

## Example

```python
from cosmotech_api.models.dataset_edit_info import DatasetEditInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetEditInfo from a JSON string
dataset_edit_info_instance = DatasetEditInfo.from_json(json)
# print the JSON string representation of the object
print(DatasetEditInfo.to_json())

# convert the object into a dict
dataset_edit_info_dict = dataset_edit_info_instance.to_dict()
# create an instance of DatasetEditInfo from a dict
dataset_edit_info_from_dict = DatasetEditInfo.from_dict(dataset_edit_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


