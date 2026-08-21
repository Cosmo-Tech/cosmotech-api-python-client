# DatasetMemberGroup

A group member of the dataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The group id | 
**role** | **str** | The group role in the dataset | 
**users** | **List[str]** | The list of users in the group | 

## Example

```python
from cosmotech_api.models.dataset_member_group import DatasetMemberGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetMemberGroup from a JSON string
dataset_member_group_instance = DatasetMemberGroup.from_json(json)
# print the JSON string representation of the object
print(DatasetMemberGroup.to_json())

# convert the object into a dict
dataset_member_group_dict = dataset_member_group_instance.to_dict()
# create an instance of DatasetMemberGroup from a dict
dataset_member_group_from_dict = DatasetMemberGroup.from_dict(dataset_member_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


