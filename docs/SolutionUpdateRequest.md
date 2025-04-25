# SolutionUpdateRequest

Request object for updating a solution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Technical key for resource name convention and version grouping. Must be unique | [optional] 
**name** | **str** | The Solution name | [optional] 
**description** | **str** | The Solution description | [optional] 
**repository** | **str** | The registry repository containing the image | [optional] 
**always_pull** | **bool** | Set to true if the runtemplate wants to always pull the image | [optional] 
**version** | **str** | The Solution version MAJOR.MINOR.PATCH. Must be aligned with an existing repository tag | [optional] 
**url** | **str** | An optional URL link to solution page | [optional] 
**tags** | **List[str]** | The list of tags | [optional] 
**parameters** | [**List[RunTemplateParameterCreateRequest]**](RunTemplateParameterCreateRequest.md) | The list of Run Template Parameters | [optional] 
**parameter_groups** | [**List[RunTemplateParameterGroupCreateRequest]**](RunTemplateParameterGroupCreateRequest.md) | The list of parameters groups for the Run Templates | [optional] 
**run_templates** | [**List[RunTemplateCreateRequest]**](RunTemplateCreateRequest.md) | List of Run Templates | [optional] 

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


