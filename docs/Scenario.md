# Scenario

a Scenario with base information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Scenario unique identifier | [optional] [readonly] 
**name** | **str** | the Scenario name | [optional] 
**description** | **str** | the Scenario description | [optional] 
**tags** | **List[str]** | the list of tags | [optional] 
**parent_id** | **str** | the Scenario parent id | [optional] 
**owner_id** | **str** | the user id which own this Scenario | [optional] [readonly] 
**root_id** | **str** | the scenario root id | [optional] [readonly] 
**solution_id** | **str** | the Solution Id associated with this Scenario | [optional] [readonly] 
**run_template_id** | **str** | the Solution Run Template Id associated with this Scenario | [optional] 
**organization_id** | **str** | the associated Organization Id | [optional] [readonly] 
**workspace_id** | **str** | the associated Workspace Id | [optional] [readonly] 
**state** | [**ScenarioJobState**](ScenarioJobState.md) |  | [optional] 
**creation_date** | **int** | the Scenario creation date | [optional] [readonly] 
**last_update** | **int** | the last time a Scenario was updated | [optional] [readonly] 
**owner_name** | **str** | the name of the owner | [optional] [readonly] 
**solution_name** | **str** | the Solution name | [optional] [readonly] 
**run_template_name** | **str** | the Solution Run Template name associated with this Scenario | [optional] [readonly] 
**dataset_list** | **List[str]** | the list of Dataset Id associated to this Scenario Run Template | [optional] 
**run_sizing** | [**ScenarioResourceSizing**](ScenarioResourceSizing.md) |  | [optional] 
**parameters_values** | [**List[ScenarioRunTemplateParameterValue]**](ScenarioRunTemplateParameterValue.md) | the list of Solution Run Template parameters values | [optional] 
**last_run** | [**ScenarioLastRun**](ScenarioLastRun.md) |  | [optional] 
**parent_last_run** | [**ScenarioLastRun**](ScenarioLastRun.md) |  | [optional] 
**root_last_run** | [**ScenarioLastRun**](ScenarioLastRun.md) |  | [optional] 
**validation_status** | [**ScenarioValidationStatus**](ScenarioValidationStatus.md) |  | [optional] 
**security** | [**ScenarioSecurity**](ScenarioSecurity.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.scenario import Scenario

# TODO update the JSON string below
json = "{}"
# create an instance of Scenario from a JSON string
scenario_instance = Scenario.from_json(json)
# print the JSON string representation of the object
print Scenario.to_json()

# convert the object into a dict
scenario_dict = scenario_instance.to_dict()
# create an instance of Scenario from a dict
scenario_form_dict = scenario.from_dict(scenario_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


