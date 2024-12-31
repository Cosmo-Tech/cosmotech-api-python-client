# ScenarioResourceSizing

a description object for resource requests and limits (default same configuration as basic sizing)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**ResourceSizeInfo**](ResourceSizeInfo.md) |  | 
**limits** | [**ResourceSizeInfo**](ResourceSizeInfo.md) |  | 

## Example

```python
from cosmotech_api.models.scenario_resource_sizing import ScenarioResourceSizing

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioResourceSizing from a JSON string
scenario_resource_sizing_instance = ScenarioResourceSizing.from_json(json)
# print the JSON string representation of the object
print(ScenarioResourceSizing.to_json())

# convert the object into a dict
scenario_resource_sizing_dict = scenario_resource_sizing_instance.to_dict()
# create an instance of ScenarioResourceSizing from a dict
scenario_resource_sizing_from_dict = ScenarioResourceSizing.from_dict(scenario_resource_sizing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


