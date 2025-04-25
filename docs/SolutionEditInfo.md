# SolutionEditInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | The timestamp of the modification in millisecond | 
**user_id** | **str** | The id of the user who did the modification | 

## Example

```python
from cosmotech_api.models.solution_edit_info import SolutionEditInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SolutionEditInfo from a JSON string
solution_edit_info_instance = SolutionEditInfo.from_json(json)
# print the JSON string representation of the object
print(SolutionEditInfo.to_json())

# convert the object into a dict
solution_edit_info_dict = solution_edit_info_instance.to_dict()
# create an instance of SolutionEditInfo from a dict
solution_edit_info_from_dict = SolutionEditInfo.from_dict(solution_edit_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


