# CreatedRun

Newly created Run info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Run id | 

## Example

```python
from cosmotech_api.models.created_run import CreatedRun

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedRun from a JSON string
created_run_instance = CreatedRun.from_json(json)
# print the JSON string representation of the object
print(CreatedRun.to_json())

# convert the object into a dict
created_run_dict = created_run_instance.to_dict()
# create an instance of CreatedRun from a dict
created_run_from_dict = CreatedRun.from_dict(created_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


