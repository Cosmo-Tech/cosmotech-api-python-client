# RunnerMemberUser

A user member of the runner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user id | 
**role** | **str** | The user role in the runner | 

## Example

```python
from cosmotech_api.models.runner_member_user import RunnerMemberUser

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerMemberUser from a JSON string
runner_member_user_instance = RunnerMemberUser.from_json(json)
# print the JSON string representation of the object
print(RunnerMemberUser.to_json())

# convert the object into a dict
runner_member_user_dict = runner_member_user_instance.to_dict()
# create an instance of RunnerMemberUser from a dict
runner_member_user_from_dict = RunnerMemberUser.from_dict(runner_member_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


