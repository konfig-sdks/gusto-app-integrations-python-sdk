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


class EmployeeFederalTax(BaseModel):
    # The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.
    version: typing.Optional[str] = Field(None, alias='version')

    # It determines which tax return form an individual will use and is an important factor in computing taxable income. One of: - Single - Married - Head of Household - Exempt from withholding - Married, but withhold as Single (does not apply to rev_2020_w4 form)
    filing_status: typing.Optional[str] = Field(None, alias='filing_status')

    # An employee can request an additional amount to be withheld from each paycheck.
    extra_withholding: typing.Optional[str] = Field(None, alias='extra_withholding')

    # If there are only two jobs (i.e., you and your spouse each have a job, or you have two), you can set it to true.
    two_jobs: typing.Optional[bool] = Field(None, alias='two_jobs')

    # A dependent is a person other than the taxpayer or spouse who entitles the taxpayer to claim a dependency exemption.
    dependents_amount: typing.Optional[str] = Field(None, alias='dependents_amount')

    # Other income amount.
    other_income: typing.Optional[str] = Field(None, alias='other_income')

    deductions: typing.Optional[str] = Field(None, alias='deductions')

    # The version of w4 form.
    w4_data_type: typing.Optional[Literal["pre_2020_w4", "rev_2020_w4"]] = Field(None, alias='w4_data_type')

    # *does not apply to rev_2020_w4 form*  An exemption from paying a certain amount of income tax.
    federal_withholding_allowance: typing.Optional[str] = Field(None, alias='federal_withholding_allowance')

    # *does not apply to rev_2020_w4 form*
    additional_withholding: typing.Optional[bool] = Field(None, alias='additional_withholding')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
