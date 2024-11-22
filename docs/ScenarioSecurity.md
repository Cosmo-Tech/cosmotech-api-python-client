# ScenarioSecurity

the Scenario security information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | the role by default | 
**access_control_list** | [**List[ScenarioAccessControl]**](ScenarioAccessControl.md) | the list which can access this Scenario with detailed access control information | 

## Example

```python
from cosmotech_api.models.scenario_security import ScenarioSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioSecurity from a JSON string
scenario_security_instance = ScenarioSecurity.from_json(json)
# print the JSON string representation of the object
print ScenarioSecurity.to_json()

# convert the object into a dict
scenario_security_dict = scenario_security_instance.to_dict()
# create an instance of ScenarioSecurity from a dict
scenario_security_form_dict = scenario_security.from_dict(scenario_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


