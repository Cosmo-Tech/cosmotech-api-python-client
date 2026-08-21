# MemberGroup

A group member of the IAM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The group id | 
**role** | **str** | The user role in the IAM | 
**users** | **List[str]** | The list of users in the group | 

## Example

```python
from cosmotech_api.models.member_group import MemberGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MemberGroup from a JSON string
member_group_instance = MemberGroup.from_json(json)
# print the JSON string representation of the object
print(MemberGroup.to_json())

# convert the object into a dict
member_group_dict = member_group_instance.to_dict()
# create an instance of MemberGroup from a dict
member_group_from_dict = MemberGroup.from_dict(member_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


