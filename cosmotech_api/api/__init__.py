# flake8: noqa

__all__ = [
    "IAMInfoApi",
    "DatasetApi",
    "MetaApi",
    "OrganizationApi",
    "RunApi",
    "RunnerApi",
    "SolutionApi",
    "WorkspaceApi",
]

import typing as _typing

if _typing.TYPE_CHECKING:
    # import apis into api package
    from cosmotech_api.api.iam_info_api import IAMInfoApi
    from cosmotech_api.api.dataset_api import DatasetApi
    from cosmotech_api.api.meta_api import MetaApi
    from cosmotech_api.api.organization_api import OrganizationApi
    from cosmotech_api.api.run_api import RunApi
    from cosmotech_api.api.runner_api import RunnerApi
    from cosmotech_api.api.solution_api import SolutionApi
    from cosmotech_api.api.workspace_api import WorkspaceApi
    
else:
    from importlib import import_module

    _exports = {
        "IAMInfoApi": ".iam_info_api",
        "DatasetApi": ".dataset_api",
        "MetaApi": ".meta_api",
        "OrganizationApi": ".organization_api",
        "RunApi": ".run_api",
        "RunnerApi": ".runner_api",
        "SolutionApi": ".solution_api",
        "WorkspaceApi": ".workspace_api",
    }

    def __getattr__(name: str) -> object:
        if (module_name := _exports.get(name)) is None:
            raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
        value = getattr(import_module(module_name, __name__), name)
        globals()[name] = value
        return value

    def __dir__() -> list[str]:
        return sorted(globals().keys() | _exports.keys())
