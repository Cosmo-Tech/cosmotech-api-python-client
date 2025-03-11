# RunnerCreateRequest

Request object for creating a new runner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the Runner name | 
**description** | **str** | the Runner description | [optional] 
**tags** | **List[str]** | the list of tags | [optional] 
**solution_id** | **str** | the Solution Id associated with this Runner | [readonly] 
**parent_id** | **str** | the Runner parent id | [optional] 
**run_template_id** | **str** | the Solution Run Template Id associated with this Runner | 
**dataset_list** | **List[str]** | the list of Dataset Id associated to this Runner Run Template | [optional] [default to []]
**run_sizing** | [**RunnerResourceSizing**](RunnerResourceSizing.md) |  | [optional] 
**parameters_values** | [**List[RunnerRunTemplateParameterValue]**](RunnerRunTemplateParameterValue.md) | the list of Solution Run Template parameters values | [optional] [default to []]
**owner_name** | **str** | the name of the owner | [readonly] 
**solution_name** | **str** | the Solution name | [optional] [readonly] 
**run_template_name** | **str** | the Solution Run Template name associated with this Runner | [optional] [readonly] 
**security** | [**RunnerSecurity**](RunnerSecurity.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.runner_create_request import RunnerCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerCreateRequest from a JSON string
runner_create_request_instance = RunnerCreateRequest.from_json(json)
# print the JSON string representation of the object
print(RunnerCreateRequest.to_json())

# convert the object into a dict
runner_create_request_dict = runner_create_request_instance.to_dict()
# create an instance of RunnerCreateRequest from a dict
runner_create_request_from_dict = RunnerCreateRequest.from_dict(runner_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


