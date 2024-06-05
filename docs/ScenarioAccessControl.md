# ScenarioAccessControl

a Scenario access control item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the identity id | 
**role** | **str** | a role | 

## Example

```python
from cosmotech_api.models.scenario_access_control import ScenarioAccessControl

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioAccessControl from a JSON string
scenario_access_control_instance = ScenarioAccessControl.from_json(json)
# print the JSON string representation of the object
print ScenarioAccessControl.to_json()

# convert the object into a dict
scenario_access_control_dict = scenario_access_control_instance.to_dict()
# create an instance of ScenarioAccessControl from a dict
scenario_access_control_form_dict = scenario_access_control.from_dict(scenario_access_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


