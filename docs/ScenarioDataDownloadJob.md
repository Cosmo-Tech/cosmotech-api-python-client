# ScenarioDataDownloadJob

Scenario data download job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Scenario Data Download job identifier | [optional] [readonly] 

## Example

```python
from cosmotech_api.models.scenario_data_download_job import ScenarioDataDownloadJob

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioDataDownloadJob from a JSON string
scenario_data_download_job_instance = ScenarioDataDownloadJob.from_json(json)
# print the JSON string representation of the object
print(ScenarioDataDownloadJob.to_json())

# convert the object into a dict
scenario_data_download_job_dict = scenario_data_download_job_instance.to_dict()
# create an instance of ScenarioDataDownloadJob from a dict
scenario_data_download_job_from_dict = ScenarioDataDownloadJob.from_dict(scenario_data_download_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


