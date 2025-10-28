# WorkspaceUpdateRequest

Request object for updating a workspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Technical key for resource name convention and version grouping. Must be unique | [optional] 
**name** | **str** | Workspace name | [optional] 
**description** | **str** | The Workspace description | [optional] 
**tags** | **List[str]** | The list of tags | [optional] 
**solution** | [**WorkspaceSolution**](WorkspaceSolution.md) |  | [optional] 
**additional_data** | **Dict[str, object]** | Free form additional data | [optional] 
**dataset_copy** | **bool** | Activate the copy of dataset on scenario creation | [optional] 

## Example

```python
from cosmotech_api.models.workspace_update_request import WorkspaceUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceUpdateRequest from a JSON string
workspace_update_request_instance = WorkspaceUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceUpdateRequest.to_json())

# convert the object into a dict
workspace_update_request_dict = workspace_update_request_instance.to_dict()
# create an instance of WorkspaceUpdateRequest from a dict
workspace_update_request_from_dict = WorkspaceUpdateRequest.from_dict(workspace_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


