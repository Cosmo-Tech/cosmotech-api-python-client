# SendRunDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**data** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from cosmotech_api.models.send_run_data_request import SendRunDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendRunDataRequest from a JSON string
send_run_data_request_instance = SendRunDataRequest.from_json(json)
# print the JSON string representation of the object
print(SendRunDataRequest.to_json())

# convert the object into a dict
send_run_data_request_dict = send_run_data_request_instance.to_dict()
# create an instance of SendRunDataRequest from a dict
send_run_data_request_from_dict = SendRunDataRequest.from_dict(send_run_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


