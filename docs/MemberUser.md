# MemberUser

A user member of the IAM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user id | 
**role** | **str** | The user role in the IAM | 

## Example

```python
from cosmotech_api.models.member_user import MemberUser

# TODO update the JSON string below
json = "{}"
# create an instance of MemberUser from a JSON string
member_user_instance = MemberUser.from_json(json)
# print the JSON string representation of the object
print(MemberUser.to_json())

# convert the object into a dict
member_user_dict = member_user_instance.to_dict()
# create an instance of MemberUser from a dict
member_user_from_dict = MemberUser.from_dict(member_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


