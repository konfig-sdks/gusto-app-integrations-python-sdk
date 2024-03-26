# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from gusto_app_integrations_python_sdk.pydantic.unprocessable_entity_error_object_errors import UnprocessableEntityErrorObjectErrors

class UnprocessableEntityErrorObject(BaseModel):
    errors: typing.Optional[UnprocessableEntityErrorObjectErrors] = Field(None, alias='errors')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
