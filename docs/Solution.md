# Solution

a version of a Solution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Solution version unique identifier | [optional] [readonly] 
**organization_id** | **str** | the Organization unique identifier | [optional] [readonly] 
**key** | **str** | the Solution key which group Solution versions | [optional] 
**name** | **str** | the Solution name | [optional] 
**description** | **str** | the Solution description | [optional] 
**repository** | **str** | the registry repository containing the image | [optional] 
**always_pull** | **bool** | set to true if the runtemplate wants to always pull the image | [optional] [default to False]
**csm_simulator** | **str** | the main Cosmo Tech simulator name used in standard Run Template | [optional] 
**version** | **str** | the Solution version MAJOR.MINOR.PATCH. Must be aligned with an existing repository tag | [optional] 
**owner_id** | **str** | the User id which own this Solution | [optional] [readonly] 
**sdk_version** | **str** | the MAJOR.MINOR version used to build this solution | [optional] 
**url** | **str** | an optional URL link to solution page | [optional] 
**tags** | **List[str]** | the list of tags | [optional] 
**parameters** | [**List[RunTemplateParameter]**](RunTemplateParameter.md) | the list of Run Template Parameters | [optional] 
**parameter_groups** | [**List[RunTemplateParameterGroup]**](RunTemplateParameterGroup.md) | the list of parameters groups for the Run Templates | [optional] 
**run_templates** | [**List[RunTemplate]**](RunTemplate.md) | list of Run Template | [default to []]
**security** | [**SolutionSecurity**](SolutionSecurity.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.solution import Solution

# TODO update the JSON string below
json = "{}"
# create an instance of Solution from a JSON string
solution_instance = Solution.from_json(json)
# print the JSON string representation of the object
print(Solution.to_json())

# convert the object into a dict
solution_dict = solution_instance.to_dict()
# create an instance of Solution from a dict
solution_from_dict = Solution.from_dict(solution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


