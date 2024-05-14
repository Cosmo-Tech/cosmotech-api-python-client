# QueryResult

the result of a SQL Query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **List[Dict[str, object]]** | the list of results | [optional] 

## Example

```python
from cosmotech_api.models.query_result import QueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResult from a JSON string
query_result_instance = QueryResult.from_json(json)
# print the JSON string representation of the object
print QueryResult.to_json()

# convert the object into a dict
query_result_dict = query_result_instance.to_dict()
# create an instance of QueryResult from a dict
query_result_form_dict = query_result.from_dict(query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


