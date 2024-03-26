# ScenarioRun

a ScenarioRun with only base properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the ScenarioRun | [optional] [readonly] 
**state** | [**ScenarioRunState**](ScenarioRunState.md) |  | [optional] 
**organization_id** | **str** | the Organization id | [optional] 
**workflow_id** | **str** | the Cosmo Tech compute cluster Argo Workflow Id to search | [optional] 
**csm_simulation_run** | **str** | the Cosmo Tech Simulation Run Id | [optional] [readonly] 
**generate_name** | **str** | the base name for workflow name generation | [optional] 
**workflow_name** | **str** | the Cosmo Tech compute cluster Argo Workflow Name | [optional] 
**owner_id** | **str** | the user id which own this scenariorun | [optional] [readonly] 
**workspace_id** | **str** | the Workspace Id | [optional] [readonly] 
**workspace_key** | **str** | technical key for resource name convention and version grouping. Must be unique | [optional] [readonly] 
**scenario_id** | **str** | the Scenario Id | [optional] [readonly] 
**solution_id** | **str** | the Solution Id | [optional] [readonly] 
**run_template_id** | **str** | the Solution Run Template id | [optional] [readonly] 
**compute_size** | **str** | the compute size needed for this Analysis. Standard sizes are basic and highcpu. Default is basic | [optional] [readonly] 
**sdk_version** | **str** | the MAJOR.MINOR version used to build the solution solution | [optional] 
**created_at** | **str** | the ScenarioRun creation date | [optional] [readonly] 
**no_data_ingestion_state** | **bool** | set to true if the run template does not use any Datawarehouse consumers (AMQP consumers for Azure) | [optional] 
**dataset_list** | **List[str]** | the list of Dataset Id associated to this Analysis | [optional] [readonly] 
**parameters_values** | [**List[RunTemplateParameterValue]**](RunTemplateParameterValue.md) | the list of Run Template parameters values | [optional] [readonly] 
**send_datasets_to_data_warehouse** | **bool** | whether or not the Datasets values are send to the DataWarehouse prior to Simulation Run. If not set follow the Workspace setting | [optional] [readonly] 
**send_input_parameters_to_data_warehouse** | **bool** | whether or not the input parameters values are send to the DataWarehouse prior to Simulation Run. If not set follow the Workspace setting | [optional] [readonly] 
**node_label** | **str** | the node label request | [optional] [readonly] 
**containers** | [**List[ScenarioRunContainer]**](ScenarioRunContainer.md) | the containers list. This information is not returned by the API. | [optional] 

## Example

```python
from cosmotech_api.models.scenario_run import ScenarioRun

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioRun from a JSON string
scenario_run_instance = ScenarioRun.from_json(json)
# print the JSON string representation of the object
print ScenarioRun.to_json()

# convert the object into a dict
scenario_run_dict = scenario_run_instance.to_dict()
# create an instance of ScenarioRun from a dict
scenario_run_form_dict = scenario_run.from_dict(scenario_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


