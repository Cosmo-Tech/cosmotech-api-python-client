# SolutionMemberGroup

A group member of the solution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The group id | 
**role** | **str** | The group role in the solution | 
**users** | **List[str]** | The list of users in the group | 

## Example

```python
from cosmotech_api.models.solution_member_group import SolutionMemberGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SolutionMemberGroup from a JSON string
solution_member_group_instance = SolutionMemberGroup.from_json(json)
# print the JSON string representation of the object
print(SolutionMemberGroup.to_json())

# convert the object into a dict
solution_member_group_dict = solution_member_group_instance.to_dict()
# create an instance of SolutionMemberGroup from a dict
solution_member_group_from_dict = SolutionMemberGroup.from_dict(solution_member_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


