# SolutionUpdateRequest

Request object for updating a solution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | technical key for resource name convention and version grouping. Must be unique | [optional] 
**name** | **str** | The Solution name | [optional] 
**description** | **str** | The Solution description | [optional] 
**repository** | **str** | The registry repository containing the image | [optional] 
**always_pull** | **bool** | Set to true if the runtemplate wants to always pull the image | [optional] [default to False]
**csm_simulator** | **str** | The main Cosmo Tech simulator name used in standard Run Template | [optional] 
**version** | **str** | The Solution version MAJOR.MINOR.PATCH. Must be aligned with an existing repository tag | [optional] 
**sdk_version** | **str** | The MAJOR.MINOR version used to build this solution | [optional] 
**url** | **str** | An optional URL link to solution page | [optional] 
**tags** | **List[str]** | The list of tags | [optional] 
**parameters** | [**List[RunTemplateParameter]**](RunTemplateParameter.md) | The list of Run Template Parameters | [optional] 
**parameter_groups** | [**List[RunTemplateParameterGroup]**](RunTemplateParameterGroup.md) | The list of parameters groups for the Run Templates | [optional] 

## Example

```python
from cosmotech_api.models.solution_update_request import SolutionUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SolutionUpdateRequest from a JSON string
solution_update_request_instance = SolutionUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SolutionUpdateRequest.to_json())

# convert the object into a dict
solution_update_request_dict = solution_update_request_instance.to_dict()
# create an instance of SolutionUpdateRequest from a dict
solution_update_request_from_dict = SolutionUpdateRequest.from_dict(solution_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


