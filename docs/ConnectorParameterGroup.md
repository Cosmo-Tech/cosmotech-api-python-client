# ConnectorParameterGroup

a connector parameters group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the connector parameter group id | 
**label** | **str** | the list of translated parameter group labels | 
**parameters** | [**List[ConnectorParameter]**](ConnectorParameter.md) | the list of parameters | 

## Example

```python
from cosmotech_api.models.connector_parameter_group import ConnectorParameterGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorParameterGroup from a JSON string
connector_parameter_group_instance = ConnectorParameterGroup.from_json(json)
# print the JSON string representation of the object
print(ConnectorParameterGroup.to_json())

# convert the object into a dict
connector_parameter_group_dict = connector_parameter_group_instance.to_dict()
# create an instance of ConnectorParameterGroup from a dict
connector_parameter_group_from_dict = ConnectorParameterGroup.from_dict(connector_parameter_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


