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

from gusto_app_integrations_python_sdk.pydantic.employee_benefits_create_benefit_request_contribution import EmployeeBenefitsCreateBenefitRequestContribution

class EmployeeBenefitsCreateBenefitRequest(BaseModel):
    # The UUID of the company benefit.
    company_benefit_uuid: str = Field(alias='company_benefit_uuid')

    # Whether the employee benefit is active.
    active: typing.Optional[bool] = Field(None, alias='active')

    # The amount to be deducted, per pay period, from the employee's pay.
    employee_deduction: typing.Optional[str] = Field(None, alias='employee_deduction')

    # Whether the employee deduction amount should be treated as a percentage to be deducted from each payroll.
    deduct_as_percentage: typing.Optional[bool] = Field(None, alias='deduct_as_percentage')

    # The maximum employee deduction amount per year. A null value signifies no limit.
    employee_deduction_annual_maximum: typing.Optional[typing.Optional[str]] = Field(None, alias='employee_deduction_annual_maximum')

    contribution: typing.Optional[EmployeeBenefitsCreateBenefitRequestContribution] = Field(None, alias='contribution')

    # Whether the company contribution is elective (aka \"matching\"). For `tiered`, `elective_amount`, and `elective_percentage` contribution types this is ignored and assumed to be `true`.
    elective: typing.Optional[bool] = Field(None, alias='elective')

    # The maximum company contribution amount per year. A null value signifies no limit.
    company_contribution_annual_maximum: typing.Optional[typing.Optional[str]] = Field(None, alias='company_contribution_annual_maximum')

    # Some benefits require additional information to determine their limit. For example, for an HSA benefit, the limit option should be either \"Family\" or \"Individual\". For a Dependent Care FSA benefit, the limit option should be either \"Joint Filing or Single\" or \"Married and Filing Separately\".
    limit_option: typing.Optional[typing.Optional[str]] = Field(None, alias='limit_option')

    # Whether the employee should use a benefit’s \"catch up\" rate. Only Roth 401k and 401k benefits use this value for employees over 50.
    catch_up: typing.Optional[bool] = Field(None, alias='catch_up')

    # The amount that the employee is insured for. Note: company contribution cannot be present if coverage amount is set.
    coverage_amount: typing.Optional[typing.Optional[str]] = Field(None, alias='coverage_amount')

    # The coverage amount as a multiple of the employee’s salary. Only applicable for Group Term Life benefits. Note: cannot be set if coverage amount is also set.
    coverage_salary_multiplier: typing.Optional[str] = Field(None, alias='coverage_salary_multiplier')

    # Whether the employee deduction reduces taxable income or not. Only valid for Group Term Life benefits. Note: when the value is not \"unset\", coverage amount and coverage salary multiplier are ignored.
    deduction_reduces_taxable_income: typing.Optional[Literal["unset", "reduces_taxable_income", "does_not_reduce_taxable_income", None]] = Field(None, alias='deduction_reduces_taxable_income')

    # WARNING: This property is deprecated
    # The amount to be paid, per pay period, by the company.
    company_contribution: typing.Optional[str] = Field(None, alias='company_contribution')

    # WARNING: This property is deprecated
    # Whether the company contribution amount should be treated as a percentage to be deducted from each payroll.
    contribute_as_percentage: typing.Optional[bool] = Field(None, alias='contribute_as_percentage')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
