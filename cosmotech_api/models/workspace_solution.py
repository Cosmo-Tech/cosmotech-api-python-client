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
from typing import Optional, Set
from typing_extensions import Self

class WorkspaceSolution(BaseModel):
    """
    the Workspace Solution configuration
    """ # noqa: E501
    solution_id: Optional[StrictStr] = Field(default=None, description="the Solution Id attached to this workspace", alias="solutionId")
    run_template_filter: Optional[List[StrictStr]] = Field(default=None, description="the list of Solution Run Template Id to filter", alias="runTemplateFilter")
    default_run_template_dataset: Optional[Dict[str, Any]] = Field(default=None, description="a map of RunTemplateId/DatasetId to set a default dataset for a Run Template", alias="defaultRunTemplateDataset")
    __properties: ClassVar[List[str]] = ["solutionId", "runTemplateFilter", "defaultRunTemplateDataset"]

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
        """Create an instance of WorkspaceSolution from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkspaceSolution from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "solutionId": obj.get("solutionId"),
            "runTemplateFilter": obj.get("runTemplateFilter"),
            "defaultRunTemplateDataset": obj.get("defaultRunTemplateDataset")
        })
        return _obj

