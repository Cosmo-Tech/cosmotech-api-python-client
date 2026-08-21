# RunnerMembers

The Runner members, including users and groups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[RunnerMemberUser]**](RunnerMemberUser.md) | The list of users in the runner | [default to []]
**groups** | [**List[RunnerMemberGroup]**](RunnerMemberGroup.md) | The list of groups in the runner | [default to []]

## Example

```python
from cosmotech_api.models.runner_members import RunnerMembers

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerMembers from a JSON string
runner_members_instance = RunnerMembers.from_json(json)
# print the JSON string representation of the object
print(RunnerMembers.to_json())

# convert the object into a dict
runner_members_dict = runner_members_instance.to_dict()
# create an instance of RunnerMembers from a dict
runner_members_from_dict = RunnerMembers.from_dict(runner_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


