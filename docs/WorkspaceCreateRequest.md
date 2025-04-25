# WorkspaceCreateRequest

Request object for creating a new workspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Technical key for resource name convention and version grouping. Must be unique | 
**name** | **str** | Workspace name. This name is displayed in the sample webApp | 
**description** | **str** | The Workspace description | [optional] 
**version** | **str** | The Workspace version MAJOR.MINOR.PATCH. | [optional] 
**tags** | **List[str]** | The list of tags | [optional] 
**solution** | [**WorkspaceSolution**](WorkspaceSolution.md) |  | 
**web_app** | [**WorkspaceWebApp**](WorkspaceWebApp.md) |  | [optional] 
**dataset_copy** | **bool** | Activate the copy of dataset on scenario creation | [optional] [default to True]
**security** | [**WorkspaceSecurity**](WorkspaceSecurity.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.workspace_create_request import WorkspaceCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCreateRequest from a JSON string
workspace_create_request_instance = WorkspaceCreateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceCreateRequest.to_json())

# convert the object into a dict
workspace_create_request_dict = workspace_create_request_instance.to_dict()
# create an instance of WorkspaceCreateRequest from a dict
workspace_create_request_from_dict = WorkspaceCreateRequest.from_dict(workspace_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


