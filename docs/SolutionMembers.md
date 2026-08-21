# SolutionMembers

The Solution members, including users and groups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[SolutionMemberUser]**](SolutionMemberUser.md) | The list of users in the solution | [default to []]
**groups** | [**List[SolutionMemberGroup]**](SolutionMemberGroup.md) | The list of groups in the solution | [default to []]

## Example

```python
from cosmotech_api.models.solution_members import SolutionMembers

# TODO update the JSON string below
json = "{}"
# create an instance of SolutionMembers from a JSON string
solution_members_instance = SolutionMembers.from_json(json)
# print the JSON string representation of the object
print(SolutionMembers.to_json())

# convert the object into a dict
solution_members_dict = solution_members_instance.to_dict()
# create an instance of SolutionMembers from a dict
solution_members_from_dict = SolutionMembers.from_dict(solution_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


