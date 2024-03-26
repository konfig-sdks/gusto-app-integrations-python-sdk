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


class CompanyBenefitsCreateCompanyBenefitRequest(BaseModel):
    # The description of the company benefit.For example, a company may offer multiple benefits with an ID of 1 (for Medical Insurance). The description would show something more specific like “Kaiser Permanente” or “Blue Cross/ Blue Shield”.
    description: str = Field(alias='description')

    # The ID of the benefit to which the company benefit belongs.
    benefit_type: typing.Optional[typing.Union[int, float]] = Field(None, alias='benefit_type')

    # Whether this benefit is active for employee participation.
    active: typing.Optional[bool] = Field(None, alias='active')

    # Whether the employer is subject to pay employer taxes when an employee is on leave. Only applicable to third party sick pay benefits.
    responsible_for_employer_taxes: typing.Optional[bool] = Field(None, alias='responsible_for_employer_taxes')

    # Whether the employer is subject to file W-2 forms for an employee on leave. Only applicable to third party sick pay benefits.
    responsible_for_employee_w2: typing.Optional[bool] = Field(None, alias='responsible_for_employee_w2')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
