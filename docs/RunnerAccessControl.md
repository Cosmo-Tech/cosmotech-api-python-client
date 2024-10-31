# RunnerAccessControl

a Runner access control item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the identity id | 
**role** | **str** | a role | 

## Example

```python
from cosmotech_api.models.runner_access_control import RunnerAccessControl

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerAccessControl from a JSON string
runner_access_control_instance = RunnerAccessControl.from_json(json)
# print the JSON string representation of the object
print RunnerAccessControl.to_json()

# convert the object into a dict
runner_access_control_dict = runner_access_control_instance.to_dict()
# create an instance of RunnerAccessControl from a dict
runner_access_control_form_dict = runner_access_control.from_dict(runner_access_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


