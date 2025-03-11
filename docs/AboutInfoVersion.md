# AboutInfoVersion

API version details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full** | **str** | Full version representation | 
**release** | **str** | Release main version representation | 
**major** | **int** | Major version number | 
**minor** | **int** | Minor version number | 
**patch** | **int** | Patch version number | 
**label** | **str** | Label version, may be empty | 
**build** | **str** | Build VCS id | 

## Example

```python
from cosmotech_api.models.about_info_version import AboutInfoVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AboutInfoVersion from a JSON string
about_info_version_instance = AboutInfoVersion.from_json(json)
# print the JSON string representation of the object
print(AboutInfoVersion.to_json())

# convert the object into a dict
about_info_version_dict = about_info_version_instance.to_dict()
# create an instance of AboutInfoVersion from a dict
about_info_version_from_dict = AboutInfoVersion.from_dict(about_info_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


