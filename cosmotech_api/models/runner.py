# coding: utf-8

"""
    Cosmo Tech Platform API

    Cosmo Tech Platform API

    The version of the OpenAPI document: 5.0.1-SNAPSHOT
    Contact: platform@cosmotech.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cosmotech_api.models.last_run_info import LastRunInfo
from cosmotech_api.models.runner_edit_info import RunnerEditInfo
from cosmotech_api.models.runner_resource_sizing import RunnerResourceSizing
from cosmotech_api.models.runner_run_template_parameter_value import RunnerRunTemplateParameterValue
from cosmotech_api.models.runner_security import RunnerSecurity
from cosmotech_api.models.runner_validation_status import RunnerValidationStatus
from typing import Optional, Set
from typing_extensions import Self

class Runner(BaseModel):
    """
    a Runner with complete information
    """ # noqa: E501
    id: StrictStr = Field(description="the Runner unique identifier")
    name: StrictStr = Field(description="the Runner name")
    description: Optional[StrictStr] = Field(default=None, description="the Runner description")
    tags: Optional[List[StrictStr]] = Field(default=None, description="the list of tags")
    parent_id: Optional[StrictStr] = Field(default=None, description="the Runner parent id", alias="parentId")
    create_info: RunnerEditInfo = Field(description="The details of the Runner creation", alias="createInfo")
    update_info: RunnerEditInfo = Field(description="The details of the Runner last update", alias="updateInfo")
    root_id: Optional[StrictStr] = Field(default=None, description="the runner root id", alias="rootId")
    solution_id: StrictStr = Field(description="the Solution Id associated with this Runner", alias="solutionId")
    run_template_id: StrictStr = Field(description="the Solution Run Template Id associated with this Runner", alias="runTemplateId")
    organization_id: StrictStr = Field(description="the associated Organization Id", alias="organizationId")
    workspace_id: StrictStr = Field(description="the associated Workspace Id", alias="workspaceId")
    owner_name: StrictStr = Field(description="the name of the owner", alias="ownerName")
    solution_name: Optional[StrictStr] = Field(default=None, description="the Solution name", alias="solutionName")
    run_template_name: Optional[StrictStr] = Field(default=None, description="the Solution Run Template name associated with this Runner", alias="runTemplateName")
    dataset_list: List[StrictStr] = Field(description="the list of Dataset Id associated to this Runner Run Template", alias="datasetList")
    run_sizing: Optional[RunnerResourceSizing] = Field(default=None, alias="runSizing")
    parameters_values: List[RunnerRunTemplateParameterValue] = Field(description="the list of Solution Run Template parameters values", alias="parametersValues")
    last_run_info: LastRunInfo = Field(alias="lastRunInfo")
    validation_status: RunnerValidationStatus = Field(alias="validationStatus")
    security: RunnerSecurity
    __properties: ClassVar[List[str]] = ["id", "name", "description", "tags", "parentId", "createInfo", "updateInfo", "rootId", "solutionId", "runTemplateId", "organizationId", "workspaceId", "ownerName", "solutionName", "runTemplateName", "datasetList", "runSizing", "parametersValues", "lastRunInfo", "validationStatus", "security"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Runner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "root_id",
            "solution_id",
            "organization_id",
            "workspace_id",
            "owner_name",
            "solution_name",
            "run_template_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of create_info
        if self.create_info:
            _dict['createInfo'] = self.create_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of update_info
        if self.update_info:
            _dict['updateInfo'] = self.update_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of run_sizing
        if self.run_sizing:
            _dict['runSizing'] = self.run_sizing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in parameters_values (list)
        _items = []
        if self.parameters_values:
            for _item_parameters_values in self.parameters_values:
                if _item_parameters_values:
                    _items.append(_item_parameters_values.to_dict())
            _dict['parametersValues'] = _items
        # override the default output from pydantic by calling `to_dict()` of last_run_info
        if self.last_run_info:
            _dict['lastRunInfo'] = self.last_run_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security
        if self.security:
            _dict['security'] = self.security.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Runner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "tags": obj.get("tags"),
            "parentId": obj.get("parentId"),
            "createInfo": RunnerEditInfo.from_dict(obj["createInfo"]) if obj.get("createInfo") is not None else None,
            "updateInfo": RunnerEditInfo.from_dict(obj["updateInfo"]) if obj.get("updateInfo") is not None else None,
            "rootId": obj.get("rootId"),
            "solutionId": obj.get("solutionId"),
            "runTemplateId": obj.get("runTemplateId"),
            "organizationId": obj.get("organizationId"),
            "workspaceId": obj.get("workspaceId"),
            "ownerName": obj.get("ownerName"),
            "solutionName": obj.get("solutionName"),
            "runTemplateName": obj.get("runTemplateName"),
            "datasetList": obj.get("datasetList"),
            "runSizing": RunnerResourceSizing.from_dict(obj["runSizing"]) if obj.get("runSizing") is not None else None,
            "parametersValues": [RunnerRunTemplateParameterValue.from_dict(_item) for _item in obj["parametersValues"]] if obj.get("parametersValues") is not None else None,
            "lastRunInfo": LastRunInfo.from_dict(obj["lastRunInfo"]) if obj.get("lastRunInfo") is not None else None,
            "validationStatus": obj.get("validationStatus"),
            "security": RunnerSecurity.from_dict(obj["security"]) if obj.get("security") is not None else None
        })
        return _obj


