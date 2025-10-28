# Dataset

Dataset object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**organization_id** | **str** | the associated Organization Id | [readonly] 
**workspace_id** | **str** | the associated Workspace Id | [readonly] 
**tags** | **List[str]** | the list of tags | 
**additional_data** | **Dict[str, object]** | Free form additional data | [optional] 
**parts** | [**List[DatasetPart]**](DatasetPart.md) |  | 
**create_info** | [**CreateInfo**](CreateInfo.md) | The details of the Dataset creation | 
**update_info** | [**EditInfo**](EditInfo.md) | The details of the Dataset last update | 
**security** | [**DatasetSecurity**](DatasetSecurity.md) |  | 

## Example

```python
from cosmotech_api.models.dataset import Dataset

# TODO update the JSON string below
json = "{}"
# create an instance of Dataset from a JSON string
dataset_instance = Dataset.from_json(json)
# print the JSON string representation of the object
print(Dataset.to_json())

# convert the object into a dict
dataset_dict = dataset_instance.to_dict()
# create an instance of Dataset from a dict
dataset_from_dict = Dataset.from_dict(dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


