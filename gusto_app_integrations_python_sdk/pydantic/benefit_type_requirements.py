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

from gusto_app_integrations_python_sdk.pydantic.benefit_type_requirements_catch_up import BenefitTypeRequirementsCatchUp
from gusto_app_integrations_python_sdk.pydantic.benefit_type_requirements_company_contribution_annual_maximum import BenefitTypeRequirementsCompanyContributionAnnualMaximum
from gusto_app_integrations_python_sdk.pydantic.benefit_type_requirements_contribution import BenefitTypeRequirementsContribution
from gusto_app_integrations_python_sdk.pydantic.benefit_type_requirements_coverage_amount import BenefitTypeRequirementsCoverageAmount
from gusto_app_integrations_python_sdk.pydantic.benefit_type_requirements_coverage_salary_multiplier import BenefitTypeRequirementsCoverageSalaryMultiplier
from gusto_app_integrations_python_sdk.pydantic.benefit_type_requirements_deduct_as_percentage import BenefitTypeRequirementsDeductAsPercentage
from gusto_app_integrations_python_sdk.pydantic.benefit_type_requirements_employee_deduction import BenefitTypeRequirementsEmployeeDeduction
from gusto_app_integrations_python_sdk.pydantic.benefit_type_requirements_limit_option import BenefitTypeRequirementsLimitOption

class BenefitTypeRequirements(BaseModel):
    employee_deduction: typing.Optional[BenefitTypeRequirementsEmployeeDeduction] = Field(None, alias='employee_deduction')

    contribution: typing.Optional[BenefitTypeRequirementsContribution] = Field(None, alias='contribution')

    deduct_as_percentage: typing.Optional[BenefitTypeRequirementsDeductAsPercentage] = Field(None, alias='deduct_as_percentage')

    catch_up: typing.Optional[BenefitTypeRequirementsCatchUp] = Field(None, alias='catch_up')

    limit_option: typing.Optional[BenefitTypeRequirementsLimitOption] = Field(None, alias='limit_option')

    company_contribution_annual_maximum: typing.Optional[BenefitTypeRequirementsCompanyContributionAnnualMaximum] = Field(None, alias='company_contribution_annual_maximum')

    coverage_salary_multiplier: typing.Optional[BenefitTypeRequirementsCoverageSalaryMultiplier] = Field(None, alias='coverage_salary_multiplier')

    coverage_amount: typing.Optional[BenefitTypeRequirementsCoverageAmount] = Field(None, alias='coverage_amount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
