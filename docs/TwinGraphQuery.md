# TwinGraphQuery

a twin graph query in cypher language

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Twin graph version | [optional] 
**query** | **str** | the query in cypher language | 

## Example

```python
from cosmotech_api.models.twin_graph_query import TwinGraphQuery

# TODO update the JSON string below
json = "{}"
# create an instance of TwinGraphQuery from a JSON string
twin_graph_query_instance = TwinGraphQuery.from_json(json)
# print the JSON string representation of the object
print(TwinGraphQuery.to_json())

# convert the object into a dict
twin_graph_query_dict = twin_graph_query_instance.to_dict()
# create an instance of TwinGraphQuery from a dict
twin_graph_query_from_dict = TwinGraphQuery.from_dict(twin_graph_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


