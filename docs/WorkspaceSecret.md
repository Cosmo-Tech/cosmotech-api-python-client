# WorkspaceSecret

the secret definition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dedicated_event_hub_key** | **str** | the dedicated event hub shared access key | [optional] 

## Example

```python
from cosmotech_api.models.workspace_secret import WorkspaceSecret

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSecret from a JSON string
workspace_secret_instance = WorkspaceSecret.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSecret.to_json())

# convert the object into a dict
workspace_secret_dict = workspace_secret_instance.to_dict()
# create an instance of WorkspaceSecret from a dict
workspace_secret_from_dict = WorkspaceSecret.from_dict(workspace_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


