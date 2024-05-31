# ScenarioDataDownloadInfo

Scenario data download job info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | the Scenario Data Download URL | [optional] [readonly] 
**state** | [**ScenarioJobState**](ScenarioJobState.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.scenario_data_download_info import ScenarioDataDownloadInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioDataDownloadInfo from a JSON string
scenario_data_download_info_instance = ScenarioDataDownloadInfo.from_json(json)
# print the JSON string representation of the object
print ScenarioDataDownloadInfo.to_json()

# convert the object into a dict
scenario_data_download_info_dict = scenario_data_download_info_instance.to_dict()
# create an instance of ScenarioDataDownloadInfo from a dict
scenario_data_download_info_form_dict = scenario_data_download_info.from_dict(scenario_data_download_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


