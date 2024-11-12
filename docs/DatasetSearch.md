# DatasetSearch

the search options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_tags** | **List[str]** | the dataset tag list to search | 

## Example

```python
from cosmotech_api.models.dataset_search import DatasetSearch

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetSearch from a JSON string
dataset_search_instance = DatasetSearch.from_json(json)
# print the JSON string representation of the object
print(DatasetSearch.to_json())

# convert the object into a dict
dataset_search_dict = dataset_search_instance.to_dict()
# create an instance of DatasetSearch from a dict
dataset_search_from_dict = DatasetSearch.from_dict(dataset_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


