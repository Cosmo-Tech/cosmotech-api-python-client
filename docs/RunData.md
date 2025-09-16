# RunData

Run Data stored

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_name** | **str** | Database name | [optional] 
**table_name** | **str** | Table name | [optional] 
**data** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from cosmotech_api.models.run_data import RunData

# TODO update the JSON string below
json = "{}"
# create an instance of RunData from a JSON string
run_data_instance = RunData.from_json(json)
# print the JSON string representation of the object
print(RunData.to_json())

# convert the object into a dict
run_data_dict = run_data_instance.to_dict()
# create an instance of RunData from a dict
run_data_from_dict = RunData.from_dict(run_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


