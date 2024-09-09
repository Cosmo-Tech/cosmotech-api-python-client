# DatasetCopyParameters

the Dataset Copy Parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | the source Dataset id | [optional] 
**target_id** | **str** | the target Dataset id | [optional] 
**options** | **Dict[str, object]** | freeform options to path to connectors | [optional] 

## Example

```python
from cosmotech_api.models.dataset_copy_parameters import DatasetCopyParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetCopyParameters from a JSON string
dataset_copy_parameters_instance = DatasetCopyParameters.from_json(json)
# print the JSON string representation of the object
print(DatasetCopyParameters.to_json())

# convert the object into a dict
dataset_copy_parameters_dict = dataset_copy_parameters_instance.to_dict()
# create an instance of DatasetCopyParameters from a dict
dataset_copy_parameters_from_dict = DatasetCopyParameters.from_dict(dataset_copy_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


