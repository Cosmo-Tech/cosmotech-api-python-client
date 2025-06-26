# CreateInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | The timestamp of the creation in millisecond | 
**user_id** | **str** | The id of the user who did the creation | 
**runner_id** | **str** | The runner id which has created the dataset (nullable) | [optional] 

## Example

```python
from cosmotech_api.models.create_info import CreateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInfo from a JSON string
create_info_instance = CreateInfo.from_json(json)
# print the JSON string representation of the object
print(CreateInfo.to_json())

# convert the object into a dict
create_info_dict = create_info_instance.to_dict()
# create an instance of CreateInfo from a dict
create_info_from_dict = CreateInfo.from_dict(create_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


