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


class PayrollsUpdateByIdRequestEmployeeCompensationsItemPaidTimeOffItem(BaseModel):
    # The name of the PTO. This also serves as the unique, immutable identifier for the PTO. Must pass in name or policy_uuid but not both.
    name: typing.Optional[str] = Field(None, alias='name')

    # The hours of this PTO taken during the pay period.
    hours: typing.Optional[str] = Field(None, alias='hours')

    # The uuid of the PTO policy. Must pass in name or policy_uuid but not both.
    policy_uuid: typing.Optional[str] = Field(None, alias='policy_uuid')

    # The outstanding hours paid upon termination. This field is only applicable for termination payrolls.
    final_payout_unused_hours_input: typing.Optional[str] = Field(None, alias='final_payout_unused_hours_input')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
