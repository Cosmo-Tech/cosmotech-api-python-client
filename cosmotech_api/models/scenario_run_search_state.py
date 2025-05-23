# coding: utf-8

"""
    Cosmo Tech Platform API

    Cosmo Tech Platform API

    The version of the OpenAPI document: 3.3.4
    Contact: platform@cosmotech.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ScenarioRunSearchState(str, Enum):
    """
    the state to search
    """

    """
    allowed enum values
    """
    FETCHINGDATASETS = 'FetchingDatasets'
    FETCHINGSCENARIOPARAMETERS = 'FetchingScenarioParameters'
    APPLYINGSCENARIOPARAMETERS = 'ApplyingScenarioParameters'
    VALIDATINGSCENARIODATA = 'ValidatingScenarioData'
    SENDINGSCENARIODATATODATAWAREHOUSE = 'SendingScenarioDataToDataWarehouse'
    PRERUN = 'PreRun'
    RUNNING = 'Running'
    POSTRUN = 'PostRun'
    SUCCESS = 'Success'
    FAILED = 'Failed'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ScenarioRunSearchState from a JSON string"""
        return cls(json.loads(json_str))


