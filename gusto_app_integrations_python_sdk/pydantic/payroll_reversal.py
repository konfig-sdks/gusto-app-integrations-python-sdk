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

from gusto_app_integrations_python_sdk.pydantic.payroll_reversal_reversed_employee_uuids import PayrollReversalReversedEmployeeUuids

class PayrollReversal(BaseModel):
    # The UUID for the payroll run being reversed.
    reversed_payroll_uuid: typing.Optional[str] = Field(None, alias='reversed_payroll_uuid')

    # The UUID of the payroll where the reversal was applied.
    reversal_payroll_uuid: typing.Optional[str] = Field(None, alias='reversal_payroll_uuid')

    # A reason provided by the admin who created the reversal.
    reason: typing.Optional[str] = Field(None, alias='reason')

    # Timestamp of when the reversal was approved.
    approved_at: typing.Optional[typing.Optional[str]] = Field(None, alias='approved_at')

    # Category chosen by the admin who requested the reversal.
    category: typing.Optional[typing.List[int]] = Field(None, alias='category')

    reversed_employee_uuids: typing.Optional[PayrollReversalReversedEmployeeUuids] = Field(None, alias='reversed_employee_uuids')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
