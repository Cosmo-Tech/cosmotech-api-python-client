# DatasetPart

Dataset part object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**source_name** | **str** | the source data name (e.g. filename associated to the dataset part) | 
**description** | **str** |  | [optional] 
**tags** | **List[str]** |  | 
**additional_data** | **Dict[str, object]** | Free form additional data | [optional] 
**type** | [**DatasetPartTypeEnum**](DatasetPartTypeEnum.md) |  | [default to DatasetPartTypeEnum.FILE]
**organization_id** | **str** | the associated Organization Id | [readonly] 
**workspace_id** | **str** | the associated Workspace Id | [readonly] 
**dataset_id** | **str** | the associated Dataset Id | [readonly] 
**create_info** | [**EditInfo**](EditInfo.md) | The details of the Dataset creation | 
**update_info** | [**EditInfo**](EditInfo.md) | The details of the Dataset last update | 

## Example

```python
from cosmotech_api.models.dataset_part import DatasetPart

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetPart from a JSON string
dataset_part_instance = DatasetPart.from_json(json)
# print the JSON string representation of the object
print(DatasetPart.to_json())

# convert the object into a dict
dataset_part_dict = dataset_part_instance.to_dict()
# create an instance of DatasetPart from a dict
dataset_part_from_dict = DatasetPart.from_dict(dataset_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


