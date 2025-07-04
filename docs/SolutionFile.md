# SolutionFile

A Solution File resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | The Solution File name | 

## Example

```python
from cosmotech_api.models.solution_file import SolutionFile

# TODO update the JSON string below
json = "{}"
# create an instance of SolutionFile from a JSON string
solution_file_instance = SolutionFile.from_json(json)
# print the JSON string representation of the object
print(SolutionFile.to_json())

# convert the object into a dict
solution_file_dict = solution_file_instance.to_dict()
# create an instance of SolutionFile from a dict
solution_file_from_dict = SolutionFile.from_dict(solution_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


