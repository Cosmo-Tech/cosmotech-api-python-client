# RunnerComparisonResult

the result of the comparison of two runners

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runner_id** | **str** | the Runner Id which is the reference for the comparison | [optional] [readonly] 
**compared_runner_id** | **str** | the Runner Id the reference Runner is compared to | [optional] [readonly] 
**changed_values** | [**List[RunnerChangedParameterValue]**](RunnerChangedParameterValue.md) | the list of changed values for parameters | [optional] [readonly] 

## Example

```python
from cosmotech_api.models.runner_comparison_result import RunnerComparisonResult

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerComparisonResult from a JSON string
runner_comparison_result_instance = RunnerComparisonResult.from_json(json)
# print the JSON string representation of the object
print(RunnerComparisonResult.to_json())

# convert the object into a dict
runner_comparison_result_dict = runner_comparison_result_instance.to_dict()
# create an instance of RunnerComparisonResult from a dict
runner_comparison_result_from_dict = RunnerComparisonResult.from_dict(runner_comparison_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


