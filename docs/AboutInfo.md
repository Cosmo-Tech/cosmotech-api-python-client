# AboutInfo

Misc information about the api

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**AboutInfoVersion**](AboutInfoVersion.md) |  | 

## Example

```python
from cosmotech_api.models.about_info import AboutInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AboutInfo from a JSON string
about_info_instance = AboutInfo.from_json(json)
# print the JSON string representation of the object
print(AboutInfo.to_json())

# convert the object into a dict
about_info_dict = about_info_instance.to_dict()
# create an instance of AboutInfo from a dict
about_info_from_dict = AboutInfo.from_dict(about_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


