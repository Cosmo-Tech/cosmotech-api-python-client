# RunContainerArtifact

a runner run container artifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the artifact name | [optional] 
**path** | **str** | the artifact path (relative to /var/csmoutput) | [optional] 

## Example

```python
from cosmotech_api.models.run_container_artifact import RunContainerArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of RunContainerArtifact from a JSON string
run_container_artifact_instance = RunContainerArtifact.from_json(json)
# print the JSON string representation of the object
print(RunContainerArtifact.to_json())

# convert the object into a dict
run_container_artifact_dict = run_container_artifact_instance.to_dict()
# create an instance of RunContainerArtifact from a dict
run_container_artifact_from_dict = RunContainerArtifact.from_dict(run_container_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


