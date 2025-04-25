# OrganizationEditInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | The timestamp of the modification in millisecond | 
**user_id** | **str** | The id of the user who did the modification | 

## Example

```python
from cosmotech_api.models.organization_edit_info import OrganizationEditInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationEditInfo from a JSON string
organization_edit_info_instance = OrganizationEditInfo.from_json(json)
# print the JSON string representation of the object
print(OrganizationEditInfo.to_json())

# convert the object into a dict
organization_edit_info_dict = organization_edit_info_instance.to_dict()
# create an instance of OrganizationEditInfo from a dict
organization_edit_info_from_dict = OrganizationEditInfo.from_dict(organization_edit_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


