# ResourceSizeInfo

Define CPUs and memory needs. Values must follow the Kubernetes resource requirements/limits syntax:  See https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **str** | Define cpu needs | 
**memory** | **str** | Define memory needs | 

## Example

```python
from cosmotech_api.models.resource_size_info import ResourceSizeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSizeInfo from a JSON string
resource_size_info_instance = ResourceSizeInfo.from_json(json)
# print the JSON string representation of the object
print(ResourceSizeInfo.to_json())

# convert the object into a dict
resource_size_info_dict = resource_size_info_instance.to_dict()
# create an instance of ResourceSizeInfo from a dict
resource_size_info_from_dict = ResourceSizeInfo.from_dict(resource_size_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


