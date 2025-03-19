# SolutionCreateRequest

Request object for creating a new solution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | technical key for resource name convention and version grouping. Must be unique | 
**name** | **str** | Solution name. This name is displayed in the sample webApp | 
**description** | **str** | The Solution description | [optional] 
**repository** | **str** | The registry repository containing the image | 
**version** | **str** | The Solution version MAJOR.MINOR.PATCH | 
**always_pull** | **bool** | Set to true if the runtemplate wants to always pull the image | [optional] [default to False]
**csm_simulator** | **str** | The main Cosmo Tech simulator name used in standard Run Template | 
**tags** | **List[str]** | The list of tags | [optional] 
**parameters** | [**List[RunTemplateParameterCreateRequest]**](RunTemplateParameterCreateRequest.md) | The list of Run Template Parameters | [optional] [default to []]
**parameter_groups** | [**List[RunTemplateParameterGroup]**](RunTemplateParameterGroup.md) | The list of parameters groups for the Run Templates | [optional] [default to []]
**run_templates** | [**List[RunTemplate]**](RunTemplate.md) | List of Run Templates | [optional] [default to []]
**url** | **str** | An optional URL link to solution page | [optional] 
**security** | [**SolutionSecurity**](SolutionSecurity.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.solution_create_request import SolutionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SolutionCreateRequest from a JSON string
solution_create_request_instance = SolutionCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SolutionCreateRequest.to_json())

# convert the object into a dict
solution_create_request_dict = solution_create_request_instance.to_dict()
# create an instance of SolutionCreateRequest from a dict
solution_create_request_from_dict = SolutionCreateRequest.from_dict(solution_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


