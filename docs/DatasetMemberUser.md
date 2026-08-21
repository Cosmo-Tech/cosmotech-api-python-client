# DatasetMemberUser

A user member of the dataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user id | 
**role** | **str** | The user role in the dataset | 

## Example

```python
from cosmotech_api.models.dataset_member_user import DatasetMemberUser

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetMemberUser from a JSON string
dataset_member_user_instance = DatasetMemberUser.from_json(json)
# print the JSON string representation of the object
print(DatasetMemberUser.to_json())

# convert the object into a dict
dataset_member_user_dict = dataset_member_user_instance.to_dict()
# create an instance of DatasetMemberUser from a dict
dataset_member_user_from_dict = DatasetMemberUser.from_dict(dataset_member_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


