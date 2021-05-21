# RunTemplateParameter

a Run Template Parameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the Parameter id | 
**labels** | [**TranslatedLabels**](TranslatedLabels.md) |  | 
**var_type** | **str** | the variable type for the parameter. Basic types or special type %DATASETID% | 
**default_value** | **str** | the default value for this parameter | [optional] 
**min_value** | **str** | the minimum value for this parameter | [optional] 
**max_value** | **str** | the maximum value for this parameter | [optional] 
**regex_validation** | **str** | a regex to validate the value | [optional] 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | freeform options | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


