# SubDatasetGraphQuery

a twin graph query in cypher language

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the name of the subdataset | [optional] 
**description** | **str** | the description of the subdataset | [optional] 
**queries** | **List[str]** | the query in cypher language | [optional] 
**main** | **bool** | is this the main dataset | [optional] 

## Example

```python
from cosmotech_api.models.sub_dataset_graph_query import SubDatasetGraphQuery

# TODO update the JSON string below
json = "{}"
# create an instance of SubDatasetGraphQuery from a JSON string
sub_dataset_graph_query_instance = SubDatasetGraphQuery.from_json(json)
# print the JSON string representation of the object
print SubDatasetGraphQuery.to_json()

# convert the object into a dict
sub_dataset_graph_query_dict = sub_dataset_graph_query_instance.to_dict()
# create an instance of SubDatasetGraphQuery from a dict
sub_dataset_graph_query_form_dict = sub_dataset_graph_query.from_dict(sub_dataset_graph_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


