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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cosmotech_api.models.container_resource_sizing import ContainerResourceSizing
from typing import Optional, Set
from typing_extensions import Self

class RunContainer(BaseModel):
    """
    a Run container description
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="the container Id")
    name: StrictStr = Field(description="the container name")
    labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="the metadata labels")
    env_vars: Optional[Dict[str, StrictStr]] = Field(default=None, description="environment variable map", alias="envVars")
    image: StrictStr = Field(description="the container image URI")
    entrypoint: Optional[StrictStr] = Field(default=None, description="the container entry point")
    run_args: Optional[List[StrictStr]] = Field(default=None, description="the list of run arguments for the container", alias="runArgs")
    dependencies: Optional[List[StrictStr]] = Field(default=None, description="the list of dependencies container name to run this container")
    solution_container: Optional[StrictBool] = Field(default=None, description="whether or not this container is a Cosmo Tech solution container", alias="solutionContainer")
    node_label: Optional[StrictStr] = Field(default=None, description="the node label request", alias="nodeLabel")
    run_sizing: Optional[ContainerResourceSizing] = Field(default=None, alias="runSizing")
    __properties: ClassVar[List[str]] = ["id", "name", "labels", "envVars", "image", "entrypoint", "runArgs", "dependencies", "solutionContainer", "nodeLabel", "runSizing"]

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
        """Create an instance of RunContainer from a JSON string"""
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
            "id",
            "solution_container",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of run_sizing
        if self.run_sizing:
            _dict['runSizing'] = self.run_sizing.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RunContainer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "labels": obj.get("labels"),
            "envVars": obj.get("envVars"),
            "image": obj.get("image"),
            "entrypoint": obj.get("entrypoint"),
            "runArgs": obj.get("runArgs"),
            "dependencies": obj.get("dependencies"),
            "solutionContainer": obj.get("solutionContainer"),
            "nodeLabel": obj.get("nodeLabel"),
            "runSizing": ContainerResourceSizing.from_dict(obj["runSizing"]) if obj.get("runSizing") is not None else None
        })
        return _obj


