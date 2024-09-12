# SolutionSecurity

the Solution security information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | the role by default | 
**access_control_list** | [**List[SolutionAccessControl]**](SolutionAccessControl.md) | the list which can access this Solution with detailed access control information | 

## Example

```python
from cosmotech_api.models.solution_security import SolutionSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of SolutionSecurity from a JSON string
solution_security_instance = SolutionSecurity.from_json(json)
# print the JSON string representation of the object
print SolutionSecurity.to_json()

# convert the object into a dict
solution_security_dict = solution_security_instance.to_dict()
# create an instance of SolutionSecurity from a dict
solution_security_form_dict = solution_security.from_dict(solution_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


