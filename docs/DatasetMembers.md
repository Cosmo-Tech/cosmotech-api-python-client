# DatasetMembers

The Dataset members, including users and groups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[DatasetMemberUser]**](DatasetMemberUser.md) | The list of users in the dataset | [default to []]
**groups** | [**List[DatasetMemberGroup]**](DatasetMemberGroup.md) | The list of groups in the dataset | [default to []]

## Example

```python
from cosmotech_api.models.dataset_members import DatasetMembers

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetMembers from a JSON string
dataset_members_instance = DatasetMembers.from_json(json)
# print the JSON string representation of the object
print(DatasetMembers.to_json())

# convert the object into a dict
dataset_members_dict = dataset_members_instance.to_dict()
# create an instance of DatasetMembers from a dict
dataset_members_from_dict = DatasetMembers.from_dict(dataset_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


