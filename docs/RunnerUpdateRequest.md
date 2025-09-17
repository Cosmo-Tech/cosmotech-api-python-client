# RunnerUpdateRequest

Request object for updating a runner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the Runner name | [optional] 
**description** | **str** | the Runner description | [optional] 
**tags** | **List[str]** | the list of tags | [optional] 
**run_template_id** | **str** | the Solution Run Template Id associated with this Runner | [optional] 
**dataset_list** | **List[str]** | the list of Dataset Id associated to this Runner Run Template | [optional] 
**run_sizing** | [**RunnerResourceSizing**](RunnerResourceSizing.md) |  | [optional] 
**parameters_values** | [**List[RunnerRunTemplateParameterValue]**](RunnerRunTemplateParameterValue.md) | the list of Solution Run Template parameters values | [optional] 
**owner_name** | **str** | the name of the owner | [optional] 
**solution_name** | **str** | the Solution name | [optional] 
**run_template_name** | **str** | the Solution Run Template name associated with this Runner | [optional] 

## Example

```python
from cosmotech_api.models.runner_update_request import RunnerUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerUpdateRequest from a JSON string
runner_update_request_instance = RunnerUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(RunnerUpdateRequest.to_json())

# convert the object into a dict
runner_update_request_dict = runner_update_request_instance.to_dict()
# create an instance of RunnerUpdateRequest from a dict
runner_update_request_from_dict = RunnerUpdateRequest.from_dict(runner_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


