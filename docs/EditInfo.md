# EditInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | The timestamp of the modification in millisecond | 
**user_id** | **str** | The id of the user who did the modification | 

## Example

```python
from cosmotech_api.models.edit_info import EditInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EditInfo from a JSON string
edit_info_instance = EditInfo.from_json(json)
# print the JSON string representation of the object
print(EditInfo.to_json())

# convert the object into a dict
edit_info_dict = edit_info_instance.to_dict()
# create an instance of EditInfo from a dict
edit_info_from_dict = EditInfo.from_dict(edit_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


