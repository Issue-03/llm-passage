"""
Config table model.

Canonical definition for ``embrouter_config``. Re-exported from
``embrouter.proxy._types`` for backwards compatibility.
"""

from embrouter.types.llms.base import EmbRouterPydanticObjectBase


class EmbRouter_Config(EmbRouterPydanticObjectBase):
    param_name: str
    param_value: dict
