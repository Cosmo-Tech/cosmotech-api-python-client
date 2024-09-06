# DatasetConnector

the Connector setup bound to a Dataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Connector id | [optional] 
**name** | **str** | the Connector name | [optional] 
**version** | **str** | the Connector version | [optional] 
**parameters_values** | **Dict[str, str]** |  | [optional] 

## Example

```python
from cosmotech_api.models.dataset_connector import DatasetConnector

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetConnector from a JSON string
dataset_connector_instance = DatasetConnector.from_json(json)
# print the JSON string representation of the object
print DatasetConnector.to_json()

# convert the object into a dict
dataset_connector_dict = dataset_connector_instance.to_dict()
# create an instance of DatasetConnector from a dict
dataset_connector_form_dict = dataset_connector.from_dict(dataset_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


