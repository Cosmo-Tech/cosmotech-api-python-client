# ScenarioRunSearch

the search options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solution_id** | **str** | the Solution Id to search | [optional] 
**run_template_id** | **str** | the Solution Analysis Id to search | [optional] 
**workspace_id** | **str** | the Workspace Id to search | [optional] 
**scenario_id** | **str** | the Scenario Id to search | [optional] 
**state** | [**ScenarioRunSearchState**](ScenarioRunSearchState.md) |  | [optional] 
**workflow_id** | **str** | the Cosmo Tech compute cluster Argo Workflow Id to search | [optional] 
**workflow_name** | **str** | the Cosmo Tech compute cluster Argo Workflow Name | [optional] 
**owner_id** | **str** | the owner Id to search | [optional] 

## Example

```python
from cosmotech_api.models.scenario_run_search import ScenarioRunSearch

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioRunSearch from a JSON string
scenario_run_search_instance = ScenarioRunSearch.from_json(json)
# print the JSON string representation of the object
print(ScenarioRunSearch.to_json())

# convert the object into a dict
scenario_run_search_dict = scenario_run_search_instance.to_dict()
# create an instance of ScenarioRunSearch from a dict
scenario_run_search_from_dict = ScenarioRunSearch.from_dict(scenario_run_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


