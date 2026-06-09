# ContainerResourceSizeInfo

Define cpus and memory needs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **str** | Define cpu needs | 
**memory** | **str** | Define memory needs | 

## Example

```python
from cosmotech_api.models.container_resource_size_info import ContainerResourceSizeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerResourceSizeInfo from a JSON string
container_resource_size_info_instance = ContainerResourceSizeInfo.from_json(json)
# print the JSON string representation of the object
print(ContainerResourceSizeInfo.to_json())

# convert the object into a dict
container_resource_size_info_dict = container_resource_size_info_instance.to_dict()
# create an instance of ContainerResourceSizeInfo from a dict
container_resource_size_info_from_dict = ContainerResourceSizeInfo.from_dict(container_resource_size_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


