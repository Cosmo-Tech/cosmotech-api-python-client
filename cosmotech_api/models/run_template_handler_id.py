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
import json
from enum import Enum
from typing_extensions import Self


class RunTemplateHandlerId(str, Enum):
    """
    the Run Template step handler identifier
    """

    """
    allowed enum values
    """
    PARAMETERS_HANDLER = 'parameters_handler'
    VALIDATOR = 'validator'
    PRERUN = 'prerun'
    ENGINE = 'engine'
    POSTRUN = 'postrun'
    SCENARIODATA_TRANSFORM = 'scenariodata_transform'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RunTemplateHandlerId from a JSON string"""
        return cls(json.loads(json_str))

