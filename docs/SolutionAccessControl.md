# SolutionAccessControl

A Solution access control item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identity id | 
**role** | **str** | The assigned role | 

## Example

```python
from cosmotech_api.models.solution_access_control import SolutionAccessControl

# TODO update the JSON string below
json = "{}"
# create an instance of SolutionAccessControl from a JSON string
solution_access_control_instance = SolutionAccessControl.from_json(json)
# print the JSON string representation of the object
print(SolutionAccessControl.to_json())

# convert the object into a dict
solution_access_control_dict = solution_access_control_instance.to_dict()
# create an instance of SolutionAccessControl from a dict
solution_access_control_from_dict = SolutionAccessControl.from_dict(solution_access_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


