# GraphProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | the type of the relationship | [optional] 
**source** | **str** | the source node of the relationship | [optional] 
**target** | **str** | the target node of the relationship | [optional] 
**name** | **str** | the name of the graph data object | [optional] 
**params** | **str** | the parameters of the graph data object | [optional] 

## Example

```python
from cosmotech_api.models.graph_properties import GraphProperties

# TODO update the JSON string below
json = "{}"
# create an instance of GraphProperties from a JSON string
graph_properties_instance = GraphProperties.from_json(json)
# print the JSON string representation of the object
print GraphProperties.to_json()

# convert the object into a dict
graph_properties_dict = graph_properties_instance.to_dict()
# create an instance of GraphProperties from a dict
graph_properties_form_dict = graph_properties.from_dict(graph_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


