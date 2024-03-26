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


class PayrollPaymentSpeedChangedType(BaseModel):
    # Original check date when fast ach applies.
    original_check_date: typing.Optional[str] = Field(None, alias='original_check_date')

    # Current check date.
    current_check_date: typing.Optional[str] = Field(None, alias='current_check_date')

    # Original debit date when fast ach applies.
    original_debit_date: typing.Optional[typing.Union[int, float]] = Field(None, alias='original_debit_date')

    # Current debit date.
    current_debit_date: typing.Optional[str] = Field(None, alias='current_debit_date')

    # The reason why the payroll is moved to four day.
    reason: typing.Optional[str] = Field(None, alias='reason')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
