# WorkspaceWebApp

a Workspace Web Application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | the Workspace Web Application URL | 
**iframes** | **Dict[str, object]** | a map of iframeKey/iframeURL | [optional] 
**options** | **Dict[str, object]** | free form options for Web Application | [optional] 

## Example

```python
from cosmotech_api.models.workspace_web_app import WorkspaceWebApp

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceWebApp from a JSON string
workspace_web_app_instance = WorkspaceWebApp.from_json(json)
# print the JSON string representation of the object
print WorkspaceWebApp.to_json()

# convert the object into a dict
workspace_web_app_dict = workspace_web_app_instance.to_dict()
# create an instance of WorkspaceWebApp from a dict
workspace_web_app_form_dict = workspace_web_app.from_dict(workspace_web_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


