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

from gusto_app_integrations_python_sdk.type.tax_requirement import TaxRequirement
from gusto_app_integrations_python_sdk.type.tax_requirement_effective_from import TaxRequirementEffectiveFrom

class RequiredTaxRequirementSet(TypedDict):
    pass

class OptionalTaxRequirementSet(TypedDict, total=False):
    # One of the two-letter state abbreviations for the fifty United States and the District of Columbia (DC)
    state: str

    # An identifier for a set of requirements. A list of requirement sets can contain multiple sets with the same `key` and different `effective_from` values.
    key: str

    # Customer facing label for the requirement set, e.g. \"Registrations\"
    label: str

    effective_from: TaxRequirementEffectiveFrom

    requirements: typing.List[TaxRequirement]

class TaxRequirementSet(RequiredTaxRequirementSet, OptionalTaxRequirementSet):
    pass
