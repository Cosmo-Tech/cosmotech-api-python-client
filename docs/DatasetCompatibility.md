# DatasetCompatibility

a Dataset compatibility constraint to a Solution version open range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solution_key** | **str** | the Solution key which group Solution versions | 
**minimum_version** | **str** | the Solution minimum version compatibility (version included) | [optional] 
**maximum_version** | **str** | the Solution maximum version compatibility (version included) | [optional] 

## Example

```python
from cosmotech_api.models.dataset_compatibility import DatasetCompatibility

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetCompatibility from a JSON string
dataset_compatibility_instance = DatasetCompatibility.from_json(json)
# print the JSON string representation of the object
print DatasetCompatibility.to_json()

# convert the object into a dict
dataset_compatibility_dict = dataset_compatibility_instance.to_dict()
# create an instance of DatasetCompatibility from a dict
dataset_compatibility_form_dict = dataset_compatibility.from_dict(dataset_compatibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


