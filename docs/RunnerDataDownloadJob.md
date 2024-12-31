# RunnerDataDownloadJob

Runner data download job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Runner Data Download job identifier | [optional] [readonly] 

## Example

```python
from cosmotech_api.models.runner_data_download_job import RunnerDataDownloadJob

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerDataDownloadJob from a JSON string
runner_data_download_job_instance = RunnerDataDownloadJob.from_json(json)
# print the JSON string representation of the object
print(RunnerDataDownloadJob.to_json())

# convert the object into a dict
runner_data_download_job_dict = runner_data_download_job_instance.to_dict()
# create an instance of RunnerDataDownloadJob from a dict
runner_data_download_job_from_dict = RunnerDataDownloadJob.from_dict(runner_data_download_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


