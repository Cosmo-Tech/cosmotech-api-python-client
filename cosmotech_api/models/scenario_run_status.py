# coding: utf-8

"""
    Cosmo Tech Platform API

    Cosmo Tech Platform API

    The version of the OpenAPI document: 3.1.3
    Contact: platform@cosmotech.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cosmotech_api.models.scenario_run_state import ScenarioRunState
from cosmotech_api.models.scenario_run_status_node import ScenarioRunStatusNode
from typing import Optional, Set
from typing_extensions import Self

class ScenarioRunStatus(BaseModel):
    """
    a ScenarioRun status
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="the ScenarioRun id")
    organization_id: Optional[StrictStr] = Field(default=None, description="the ScenarioRun id", alias="organizationId")
    workflow_id: Optional[StrictStr] = Field(default=None, description="the Cosmo Tech compute cluster Argo Workflow Id to search", alias="workflowId")
    workflow_name: Optional[StrictStr] = Field(default=None, description="the Cosmo Tech compute cluster Argo Workflow Name", alias="workflowName")
    start_time: Optional[StrictStr] = Field(default=None, description="the ScenarioRun start Date Time", alias="startTime")
    end_time: Optional[StrictStr] = Field(default=None, description="the ScenarioRun end Date Time", alias="endTime")
    phase: Optional[StrictStr] = Field(default=None, description="high-level summary of where the workflow is in its lifecycle")
    progress: Optional[StrictStr] = Field(default=None, description="progress to completion")
    message: Optional[StrictStr] = Field(default=None, description="a  human readable message indicating details about why the workflow is in this condition")
    estimated_duration: Optional[StrictInt] = Field(default=None, description="estimatedDuration in seconds", alias="estimatedDuration")
    nodes: Optional[List[ScenarioRunStatusNode]] = Field(default=None, description="status of ScenarioRun nodes")
    state: Optional[ScenarioRunState] = None
    __properties: ClassVar[List[str]] = ["id", "organizationId", "workflowId", "workflowName", "startTime", "endTime", "phase", "progress", "message", "estimatedDuration", "nodes", "state"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ScenarioRunStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in nodes (list)
        _items = []
        if self.nodes:
            for _item in self.nodes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nodes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioRunStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "organizationId": obj.get("organizationId"),
            "workflowId": obj.get("workflowId"),
            "workflowName": obj.get("workflowName"),
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime"),
            "phase": obj.get("phase"),
            "progress": obj.get("progress"),
            "message": obj.get("message"),
            "estimatedDuration": obj.get("estimatedDuration"),
            "nodes": [ScenarioRunStatusNode.from_dict(_item) for _item in obj["nodes"]] if obj.get("nodes") is not None else None,
            "state": obj.get("state")
        })
        return _obj

