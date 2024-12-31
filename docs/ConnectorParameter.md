# ConnectorParameter

a connector parameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the connector parameter id | 
**label** | **str** | the list of translated parameter group labels | 
**value_type** | **str** | the parameter value type | [optional] 
**options** | **List[str]** | the list of available and valid values for the parameter | [optional] 
**default** | **str** | the default value | [optional] 
**env_var** | **str** | associated environment variable in connector image | [optional] 

## Example

```python
from cosmotech_api.models.connector_parameter import ConnectorParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorParameter from a JSON string
connector_parameter_instance = ConnectorParameter.from_json(json)
# print the JSON string representation of the object
print(ConnectorParameter.to_json())

# convert the object into a dict
connector_parameter_dict = connector_parameter_instance.to_dict()
# create an instance of ConnectorParameter from a dict
connector_parameter_from_dict = ConnectorParameter.from_dict(connector_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


