# ContainerResourceSizing

a description object for resource requests and limits (default same configuration as basic sizing)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**ContainerResourceSizeInfo**](ContainerResourceSizeInfo.md) |  | 
**limits** | [**ContainerResourceSizeInfo**](ContainerResourceSizeInfo.md) |  | 

## Example

```python
from cosmotech_api.models.container_resource_sizing import ContainerResourceSizing

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerResourceSizing from a JSON string
container_resource_sizing_instance = ContainerResourceSizing.from_json(json)
# print the JSON string representation of the object
print(ContainerResourceSizing.to_json())

# convert the object into a dict
container_resource_sizing_dict = container_resource_sizing_instance.to_dict()
# create an instance of ContainerResourceSizing from a dict
container_resource_sizing_from_dict = ContainerResourceSizing.from_dict(container_resource_sizing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


