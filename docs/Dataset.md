# Dataset

a Dataset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Dataset unique identifier | [optional] [readonly] 
**name** | **str** | the Dataset name | [optional] 
**description** | **str** | the Dataset description | [optional] 
**owner_id** | **str** | the User id which own this Dataset | [optional] [readonly] 
**tags** | **[str]** | the list of tags | [optional] 
**connector** | [**DatasetConnector**](DatasetConnector.md) |  | [optional] 
**fragments_ids** | **[str]** | the list of other Datasets ids to compose as fragments | [optional] 
**validator_id** | **str** | the validator id | [optional] 
**compatibility** | [**[DatasetCompatibility]**](DatasetCompatibility.md) | the list of compatible Solutions versions | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


