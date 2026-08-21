# RunnerMemberGroup

A group member of the runner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The group id | 
**role** | **str** | The group role in the runner | 
**users** | **List[str]** | The list of users in the group | 

## Example

```python
from cosmotech_api.models.runner_member_group import RunnerMemberGroup

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerMemberGroup from a JSON string
runner_member_group_instance = RunnerMemberGroup.from_json(json)
# print the JSON string representation of the object
print(RunnerMemberGroup.to_json())

# convert the object into a dict
runner_member_group_dict = runner_member_group_instance.to_dict()
# create an instance of RunnerMemberGroup from a dict
runner_member_group_from_dict = RunnerMemberGroup.from_dict(runner_member_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


