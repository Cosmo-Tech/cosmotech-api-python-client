# WorkspaceSolution

the Workspace Solution configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solution_id** | **str** | the Solution Id attached to this workspace | [optional] 
**run_template_filter** | **List[str]** | the list of Solution Run Template Id to filter | [optional] 
**default_run_template_dataset** | **Dict[str, object]** | a map of RunTemplateId/DatasetId to set a default dataset for a Run Template | [optional] 

## Example

```python
from cosmotech_api.models.workspace_solution import WorkspaceSolution

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSolution from a JSON string
workspace_solution_instance = WorkspaceSolution.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSolution.to_json())

# convert the object into a dict
workspace_solution_dict = workspace_solution_instance.to_dict()
# create an instance of WorkspaceSolution from a dict
workspace_solution_from_dict = WorkspaceSolution.from_dict(workspace_solution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


