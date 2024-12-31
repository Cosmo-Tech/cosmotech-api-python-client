# DatasetSecurity

the dataset security information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | the role by default | 
**access_control_list** | [**List[DatasetAccessControl]**](DatasetAccessControl.md) | the list which can access this Dataset with detailed access control information | 

## Example

```python
from cosmotech_api.models.dataset_security import DatasetSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetSecurity from a JSON string
dataset_security_instance = DatasetSecurity.from_json(json)
# print the JSON string representation of the object
print(DatasetSecurity.to_json())

# convert the object into a dict
dataset_security_dict = dataset_security_instance.to_dict()
# create an instance of DatasetSecurity from a dict
dataset_security_from_dict = DatasetSecurity.from_dict(dataset_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


