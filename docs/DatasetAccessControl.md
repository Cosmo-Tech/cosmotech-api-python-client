# DatasetAccessControl

a Dataset access control item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the identity id | 
**role** | **str** | a role | 

## Example

```python
from cosmotech_api.models.dataset_access_control import DatasetAccessControl

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetAccessControl from a JSON string
dataset_access_control_instance = DatasetAccessControl.from_json(json)
# print the JSON string representation of the object
print DatasetAccessControl.to_json()

# convert the object into a dict
dataset_access_control_dict = dataset_access_control_instance.to_dict()
# create an instance of DatasetAccessControl from a dict
dataset_access_control_form_dict = dataset_access_control.from_dict(dataset_access_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


