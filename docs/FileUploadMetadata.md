# FileUploadMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from cosmotech_api.models.file_upload_metadata import FileUploadMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadMetadata from a JSON string
file_upload_metadata_instance = FileUploadMetadata.from_json(json)
# print the JSON string representation of the object
print(FileUploadMetadata.to_json())

# convert the object into a dict
file_upload_metadata_dict = file_upload_metadata_instance.to_dict()
# create an instance of FileUploadMetadata from a dict
file_upload_metadata_from_dict = FileUploadMetadata.from_dict(file_upload_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


