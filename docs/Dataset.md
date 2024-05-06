# Dataset

a Dataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Dataset unique identifier | [optional] [readonly] 
**name** | **str** | the Dataset name | [optional] 
**description** | **str** | the Dataset description | [optional] 
**owner_id** | **str** | the User id which own this Dataset | [optional] [readonly] 
**owner_name** | **str** | the name of the owner | [optional] [readonly] 
**organization_id** | **str** | the Organization Id related to this Dataset | [optional] [readonly] 
**parent_id** | **str** | the Dataset id which is the parent of this Dataset | [optional] 
**linked_workspace_id_list** | **List[str]** | list of workspace linked to this dataset | [optional] 
**twingraph_id** | **str** | the twin graph id | [optional] 
**main** | **bool** | is this the main dataset | [optional] 
**creation_date** | **int** | the Dataset creation date | [optional] [readonly] 
**refresh_date** | **int** | the last time a refresh was done | [optional] [readonly] 
**source_type** | [**DatasetSourceType**](DatasetSourceType.md) |  | [optional] 
**source** | [**SourceInfo**](SourceInfo.md) |  | [optional] 
**ingestion_status** | **str** | the Dataset ingestion status | [optional] 
**twincache_status** | **str** | the twincache data status | [optional] 
**queries** | **List[str]** | the list of queries | [optional] 
**tags** | **List[str]** | the list of tags | [optional] 
**connector** | [**DatasetConnector**](DatasetConnector.md) |  | [optional] 
**fragments_ids** | **List[str]** | the list of other Datasets ids to compose as fragments | [optional] 
**validator_id** | **str** | the validator id | [optional] 
**compatibility** | [**List[DatasetCompatibility]**](DatasetCompatibility.md) | the list of compatible Solutions versions | [optional] 
**security** | [**DatasetSecurity**](DatasetSecurity.md) |  | [optional] 

## Example

```python
from cosmotech_api.models.dataset import Dataset

# TODO update the JSON string below
json = "{}"
# create an instance of Dataset from a JSON string
dataset_instance = Dataset.from_json(json)
# print the JSON string representation of the object
print Dataset.to_json()

# convert the object into a dict
dataset_dict = dataset_instance.to_dict()
# create an instance of Dataset from a dict
dataset_form_dict = dataset.from_dict(dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


