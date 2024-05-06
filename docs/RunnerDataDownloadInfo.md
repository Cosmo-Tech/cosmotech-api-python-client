# RunnerDataDownloadInfo

Runner data download job info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | the Runner Data Download URL | [optional] [readonly] 
**state** | [**RunnerJobState**](RunnerJobState.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.runner_data_download_info import RunnerDataDownloadInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerDataDownloadInfo from a JSON string
runner_data_download_info_instance = RunnerDataDownloadInfo.from_json(json)
# print the JSON string representation of the object
print RunnerDataDownloadInfo.to_json()

# convert the object into a dict
runner_data_download_info_dict = runner_data_download_info_instance.to_dict()
# create an instance of RunnerDataDownloadInfo from a dict
runner_data_download_info_form_dict = runner_data_download_info.from_dict(runner_data_download_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


