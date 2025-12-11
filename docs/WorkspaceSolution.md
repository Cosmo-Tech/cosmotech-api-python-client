# WorkspaceSolution

The Workspace Solution configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solution_id** | **str** | The Solution Id attached to this workspace | 
**dataset_id** | **str** | The Dataset Id attached to this workspace. This dataset will be used to store default values for Solution parameters with file&#39;s varType.  | [optional] 
**default_parameter_values** | **Dict[str, str]** | A map of parameterId/value to set default values for Solution parameters with simple varType (int, string, ...) | [optional] 

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


