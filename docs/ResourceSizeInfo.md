# ResourceSizeInfo

define cpus and memory needs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **str** | define cpu needs | 
**memory** | **str** | define memory needs | 

## Example

```python
from cosmotech_api.models.resource_size_info import ResourceSizeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSizeInfo from a JSON string
resource_size_info_instance = ResourceSizeInfo.from_json(json)
# print the JSON string representation of the object
print ResourceSizeInfo.to_json()

# convert the object into a dict
resource_size_info_dict = resource_size_info_instance.to_dict()
# create an instance of ResourceSizeInfo from a dict
resource_size_info_form_dict = resource_size_info.from_dict(resource_size_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


