# Solution

A version of a Solution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Solution version unique identifier | 
**organization_id** | **str** | The Organization unique identifier | 
**key** | **str** | The Solution key which groups Solution versions | 
**name** | **str** | The Solution name | 
**description** | **str** | The Solution description | [optional] 
**repository** | **str** | The registry repository containing the image | 
**always_pull** | **bool** | Set to true if the runtemplate wants to always pull the image | [optional] [default to False]
**version** | **str** | The Solution version MAJOR.MINOR.PATCH. Must be aligned with an existing repository tag | 
**create_info** | [**SolutionEditInfo**](SolutionEditInfo.md) | The details of the Solution creation | 
**update_info** | [**SolutionEditInfo**](SolutionEditInfo.md) | The details of the Solution last update | 
**sdk_version** | **str** | The full SDK version used to build this solution, if available | [optional] 
**url** | **str** | An optional URL link to solution page | [optional] 
**tags** | **List[str]** | The list of tags | [optional] 
**parameters** | [**List[RunTemplateParameter]**](RunTemplateParameter.md) | The list of Run Template Parameters | 
**parameter_groups** | [**List[RunTemplateParameterGroup]**](RunTemplateParameterGroup.md) | The list of parameters groups for the Run Templates | 
**run_templates** | [**List[RunTemplate]**](RunTemplate.md) | List of Run Templates | [default to []]
**security** | [**SolutionSecurity**](SolutionSecurity.md) |  | 

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


