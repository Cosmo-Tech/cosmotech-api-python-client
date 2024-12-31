# ScenarioComparisonResult

the result of the comparison of two scenarios

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenario_id** | **str** | the Scenario Id which is the reference for the comparison | [optional] [readonly] 
**compared_scenario_id** | **str** | the Scenario Id the reference Scenario is compared to | [optional] [readonly] 
**changed_values** | [**List[ScenarioChangedParameterValue]**](ScenarioChangedParameterValue.md) | the list of changed values for parameters | [optional] [readonly] 

## Example

```python
from cosmotech_api.models.scenario_comparison_result import ScenarioComparisonResult

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioComparisonResult from a JSON string
scenario_comparison_result_instance = ScenarioComparisonResult.from_json(json)
# print the JSON string representation of the object
print(ScenarioComparisonResult.to_json())

# convert the object into a dict
scenario_comparison_result_dict = scenario_comparison_result_instance.to_dict()
# create an instance of ScenarioComparisonResult from a dict
scenario_comparison_result_from_dict = ScenarioComparisonResult.from_dict(scenario_comparison_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


