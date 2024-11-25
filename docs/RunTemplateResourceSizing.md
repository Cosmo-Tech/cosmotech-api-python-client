# RunTemplateResourceSizing

a description object for resource requests and limits (default same configuration as basic sizing)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**ResourceSizeInfo**](ResourceSizeInfo.md) |  | 
**limits** | [**ResourceSizeInfo**](ResourceSizeInfo.md) |  | 

## Example

```python
from cosmotech_api.models.run_template_resource_sizing import RunTemplateResourceSizing

# TODO update the JSON string below
json = "{}"
# create an instance of RunTemplateResourceSizing from a JSON string
run_template_resource_sizing_instance = RunTemplateResourceSizing.from_json(json)
# print the JSON string representation of the object
print RunTemplateResourceSizing.to_json()

# convert the object into a dict
run_template_resource_sizing_dict = run_template_resource_sizing_instance.to_dict()
# create an instance of RunTemplateResourceSizing from a dict
run_template_resource_sizing_form_dict = run_template_resource_sizing.from_dict(run_template_resource_sizing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


