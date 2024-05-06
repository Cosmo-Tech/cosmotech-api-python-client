# RunResourceRequested

the memory and CPU requested by the pod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **int** | the cpu requested | [optional] 
**memory** | **int** | the memory requested | [optional] 

## Example

```python
from cosmotech_api.models.run_resource_requested import RunResourceRequested

# TODO update the JSON string below
json = "{}"
# create an instance of RunResourceRequested from a JSON string
run_resource_requested_instance = RunResourceRequested.from_json(json)
# print the JSON string representation of the object
print RunResourceRequested.to_json()

# convert the object into a dict
run_resource_requested_dict = run_resource_requested_instance.to_dict()
# create an instance of RunResourceRequested from a dict
run_resource_requested_form_dict = run_resource_requested.from_dict(run_resource_requested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


