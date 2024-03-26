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

from gusto_app_integrations_python_sdk.type.tax_requirement_metadata_options import TaxRequirementMetadataOptions
from gusto_app_integrations_python_sdk.type.tax_requirement_metadata_validation import TaxRequirementMetadataValidation

class RequiredTaxRequirementMetadata(TypedDict):
    # Describes the type of requirement - each type may have additional metadata properties to describe possible values, formats, etc.  - `text`: free-text input, no additional requirements - `currency`: a value representing a dollar amount, e.g. `374.55` representing `$374.55` - `radio`: choose one of options provided, see `options` - `select`: choose one of options provided, see `options` - `percent`: A decimal value representing a percentage, e.g. `0.034` representing `3.4%` - `account_number`: An account number for a tax agency, more information provided by `mask` and `prefix` - `tax_rate`: A decimal value representing a tax rate, e.g. `0.034` representing a tax rate of `3.4%`, see `validation` for additional validation guidance - `workers_compensation_rate`: A decimal value representing a percentage, see `risk_class_code`, `risk_class_description`, and `rate_type` 
    type: str

class OptionalTaxRequirementMetadata(TypedDict, total=False):
    options: TaxRequirementMetadataOptions

    # [for `workers_compensation_rate`] The industry risk class code for the rate being requested
    risk_class_code: str

    # [for `workers_compensation_rate`] A description of the industry risk class for the rate being requested
    risk_class_description: str

    # [for `workers_compensation_rate`] The type of rate being collected. Either:  - `percent`: A percentage formatted as a decimal, e.g. `0.01` for 1%  - `currency_per_hour`: A dollar amount per hour, e.g. `3.24` for $3.24/hr 
    rate_type: str

    # [for `account_number`] A pattern describing the format of the account number  The mask is a sequence of characters representing the requirements of the actual account number. Each character in the mask represents a single character in the account number as follows: - `#`: a digit (`\\d`) - `@`: a upper or lower case letter (`[a-zA-Z]`) - `^`: an uppercase letter (`[A-Z]`) - `%`: a digit or uppercase letter (`[0-9A-Z]`) - any other character represents the literal character  Examples: - mask: `WHT-######` represents `WHT-` followed by 5 digits, e.g. `WHT-33421` - mask: `%####-^^` supports values of `75544-AB` and `Z7654-HK` 
    mask: str

    # [for `account_number`] A value that precedes the value to be collected - useful for display, but should not be submitted as part of the value. E.g. some tax agencies use an account number that is a company's federal ein plus two digits. In that case the mask would be `##` and the prefix `XXXXX1234`.
    prefix: str

    validation: TaxRequirementMetadataValidation

class TaxRequirementMetadata(RequiredTaxRequirementMetadata, OptionalTaxRequirementMetadata):
    pass
