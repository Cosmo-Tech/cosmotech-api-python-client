# RunnerSecurity

the Runner security information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | the role by default | 
**access_control_list** | [**List[RunnerAccessControl]**](RunnerAccessControl.md) | the list which can access this Runner with detailed access control information | 

## Example

```python
from cosmotech_api.models.runner_security import RunnerSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerSecurity from a JSON string
runner_security_instance = RunnerSecurity.from_json(json)
# print the JSON string representation of the object
print(RunnerSecurity.to_json())

# convert the object into a dict
runner_security_dict = runner_security_instance.to_dict()
# create an instance of RunnerSecurity from a dict
runner_security_from_dict = RunnerSecurity.from_dict(runner_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


