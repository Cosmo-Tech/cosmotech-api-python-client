# DatasetTwinGraphQuery

a twin graph query in cypher language

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | the query in cypher language | 

## Example

```python
from cosmotech_api.models.dataset_twin_graph_query import DatasetTwinGraphQuery

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetTwinGraphQuery from a JSON string
dataset_twin_graph_query_instance = DatasetTwinGraphQuery.from_json(json)
# print the JSON string representation of the object
print DatasetTwinGraphQuery.to_json()

# convert the object into a dict
dataset_twin_graph_query_dict = dataset_twin_graph_query_instance.to_dict()
# create an instance of DatasetTwinGraphQuery from a dict
dataset_twin_graph_query_form_dict = dataset_twin_graph_query.from_dict(dataset_twin_graph_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


