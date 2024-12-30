# RunDataQuery

a data result query in SQL

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | the query in SQL | 

## Example

```python
from cosmotech_api.models.run_data_query import RunDataQuery

# TODO update the JSON string below
json = "{}"
# create an instance of RunDataQuery from a JSON string
run_data_query_instance = RunDataQuery.from_json(json)
# print the JSON string representation of the object
print RunDataQuery.to_json()

# convert the object into a dict
run_data_query_dict = run_data_query_instance.to_dict()
# create an instance of RunDataQuery from a dict
run_data_query_form_dict = run_data_query.from_dict(run_data_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


