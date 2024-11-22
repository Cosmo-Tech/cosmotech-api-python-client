# RunSearch

the search options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solution_id** | **str** | the Solution Id to search | [optional] 
**run_template_id** | **str** | the Solution Analysis Id to search | [optional] 
**workspace_id** | **str** | the Workspace Id to search | [optional] 
**runner_id** | **str** | the Runner Id to search | [optional] 
**state** | [**RunSearchState**](RunSearchState.md) |  | [optional] 
**workflow_id** | **str** | the Cosmo Tech compute cluster Argo Workflow Id to search | [optional] 
**workflow_name** | **str** | the Cosmo Tech compute cluster Argo Workflow Name | [optional] 
**owner_id** | **str** | the owner Id to search | [optional] 

## Example

```python
from cosmotech_api.models.run_search import RunSearch

# TODO update the JSON string below
json = "{}"
# create an instance of RunSearch from a JSON string
run_search_instance = RunSearch.from_json(json)
# print the JSON string representation of the object
print RunSearch.to_json()

# convert the object into a dict
run_search_dict = run_search_instance.to_dict()
# create an instance of RunSearch from a dict
run_search_form_dict = run_search.from_dict(run_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


