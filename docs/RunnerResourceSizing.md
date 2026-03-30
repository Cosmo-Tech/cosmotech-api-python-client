# RunnerResourceSizing

A description object for resource requests and limits. Values must follow the Kubernetes resource requirements/limits syntax:  See https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes Default configuration is basic sizing 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**ResourceSizeInfo**](ResourceSizeInfo.md) |  | 
**limits** | [**ResourceSizeInfo**](ResourceSizeInfo.md) |  | 

## Example

```python
from cosmotech_api.models.runner_resource_sizing import RunnerResourceSizing

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerResourceSizing from a JSON string
runner_resource_sizing_instance = RunnerResourceSizing.from_json(json)
# print the JSON string representation of the object
print(RunnerResourceSizing.to_json())

# convert the object into a dict
runner_resource_sizing_dict = runner_resource_sizing_instance.to_dict()
# create an instance of RunnerResourceSizing from a dict
runner_resource_sizing_from_dict = RunnerResourceSizing.from_dict(runner_resource_sizing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


