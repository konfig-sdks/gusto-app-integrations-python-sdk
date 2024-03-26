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


class EmployeesCreateEmployeeRequest(BaseModel):
    first_name: str = Field(alias='first_name')

    last_name: str = Field(alias='last_name')

    middle_initial: typing.Optional[str] = Field(None, alias='middle_initial')

    date_of_birth: typing.Optional[str] = Field(None, alias='date_of_birth')

    email: typing.Optional[str] = Field(None, alias='email')

    ssn: typing.Optional[str] = Field(None, alias='ssn')

    # If true, employee is expected to self-onboard. If false, payroll admin is expected to enter in the employee's onboarding information
    self_onboarding: typing.Optional[bool] = Field(None, alias='self_onboarding')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
