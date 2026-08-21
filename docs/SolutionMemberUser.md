# SolutionMemberUser

A user member of the solution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user id | 
**role** | **str** | The user role in the solution | 

## Example

```python
from cosmotech_api.models.solution_member_user import SolutionMemberUser

# TODO update the JSON string below
json = "{}"
# create an instance of SolutionMemberUser from a JSON string
solution_member_user_instance = SolutionMemberUser.from_json(json)
# print the JSON string representation of the object
print(SolutionMemberUser.to_json())

# convert the object into a dict
solution_member_user_dict = solution_member_user_instance.to_dict()
# create an instance of SolutionMemberUser from a dict
solution_member_user_from_dict = SolutionMemberUser.from_dict(solution_member_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


