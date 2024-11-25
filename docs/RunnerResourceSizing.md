# RunnerResourceSizing

a description object for resource requests and limits (default same configuration as basic sizing)

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
print RunnerResourceSizing.to_json()

# convert the object into a dict
runner_resource_sizing_dict = runner_resource_sizing_instance.to_dict()
# create an instance of RunnerResourceSizing from a dict
runner_resource_sizing_form_dict = runner_resource_sizing.from_dict(runner_resource_sizing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


