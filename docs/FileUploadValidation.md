# FileUploadValidation

files read on upload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[FileUploadMetadata]**](FileUploadMetadata.md) | list of filename found on nodes folder | [optional] 
**edges** | [**List[FileUploadMetadata]**](FileUploadMetadata.md) | list of filename found on edges folder | [optional] 

## Example

```python
from cosmotech_api.models.file_upload_validation import FileUploadValidation

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadValidation from a JSON string
file_upload_validation_instance = FileUploadValidation.from_json(json)
# print the JSON string representation of the object
print FileUploadValidation.to_json()

# convert the object into a dict
file_upload_validation_dict = file_upload_validation_instance.to_dict()
# create an instance of FileUploadValidation from a dict
file_upload_validation_form_dict = file_upload_validation.from_dict(file_upload_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


