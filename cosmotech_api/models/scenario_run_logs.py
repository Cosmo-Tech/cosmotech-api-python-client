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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cosmotech_api.models.scenario_run_container_logs import ScenarioRunContainerLogs
from typing import Optional, Set
from typing_extensions import Self

class ScenarioRunLogs(BaseModel):
    """
    the scenariorun logs returned by all containers
    """ # noqa: E501
    scenariorun_id: Optional[StrictStr] = Field(default=None, description="the ScenarioRun Id", alias="scenariorunId")
    containers: Optional[Dict[str, ScenarioRunContainerLogs]] = Field(default=None, description="the container map of logs")
    __properties: ClassVar[List[str]] = ["scenariorunId", "containers"]

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
        """Create an instance of ScenarioRunLogs from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "scenariorun_id",
            "containers",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each value in containers (dict)
        _field_dict = {}
        if self.containers:
            for _key in self.containers:
                if self.containers[_key]:
                    _field_dict[_key] = self.containers[_key].to_dict()
            _dict['containers'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioRunLogs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "scenariorunId": obj.get("scenariorunId"),
            "containers": dict(
                (_k, ScenarioRunContainerLogs.from_dict(_v))
                for _k, _v in obj["containers"].items()
            )
            if obj.get("containers") is not None
            else None
        })
        return _obj

