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

from gusto_app_integrations_python_sdk.type.benefit_type_requirements_employee_deduction_choices import BenefitTypeRequirementsEmployeeDeductionChoices
from gusto_app_integrations_python_sdk.type.benefit_type_requirements_employee_deduction_default_value import BenefitTypeRequirementsEmployeeDeductionDefaultValue

class RequiredBenefitTypeRequirementsEmployeeDeduction(TypedDict):
    pass

class OptionalBenefitTypeRequirementsEmployeeDeduction(TypedDict, total=False):
    required: bool

    editable: bool

    default_value: BenefitTypeRequirementsEmployeeDeductionDefaultValue

    choices: BenefitTypeRequirementsEmployeeDeductionChoices

class BenefitTypeRequirementsEmployeeDeduction(RequiredBenefitTypeRequirementsEmployeeDeduction, OptionalBenefitTypeRequirementsEmployeeDeduction):
    pass
