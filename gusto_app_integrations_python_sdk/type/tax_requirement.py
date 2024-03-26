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

from gusto_app_integrations_python_sdk.type.tax_requirement_applicable_if import TaxRequirementApplicableIf
from gusto_app_integrations_python_sdk.type.tax_requirement_metadata import TaxRequirementMetadata

class RequiredTaxRequirement(TypedDict):
    pass

class OptionalTaxRequirement(TypedDict, total=False):
    # A more detailed customer facing description of the requirement
    description: str

    # An identifier for an individual requirement. Uniqueness is guaranteed within a requirement set.
    key: str

    applicable_if: TaxRequirementApplicableIf

    # A customer facing description of the requirement
    label: str

    # The \"answer\"
    value: str

    metadata: TaxRequirementMetadata

class TaxRequirement(RequiredTaxRequirement, OptionalTaxRequirement):
    pass
