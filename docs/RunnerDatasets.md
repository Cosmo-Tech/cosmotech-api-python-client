# RunnerDatasets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bases** | **List[str]** | a list of Dataset Id used to build the Runner | 
**parameter** | **str** | The dataset id used for dataset parameters on current Runner | 
**parameters** | **List[object]** | The dataset parts retrieved from the parameter property (programmatically fulfilled) | [optional] 

## Example

```python
from cosmotech_api.models.runner_datasets import RunnerDatasets

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerDatasets from a JSON string
runner_datasets_instance = RunnerDatasets.from_json(json)
# print the JSON string representation of the object
print(RunnerDatasets.to_json())

# convert the object into a dict
runner_datasets_dict = runner_datasets_instance.to_dict()
# create an instance of RunnerDatasets from a dict
runner_datasets_from_dict = RunnerDatasets.from_dict(runner_datasets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


