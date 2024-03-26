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

from gusto_app_integrations_python_sdk.type.payroll_blockers_error_errors_item_metadata import PayrollBlockersErrorErrorsItemMetadata

class RequiredPayrollBlockersErrorErrorsItem(TypedDict):
    pass

class OptionalPayrollBlockersErrorErrorsItem(TypedDict, total=False):
    # The string \"base\"
    error_key: str

    # The string \"payroll_blocker\"
    category: str

    # Human readable description of the payroll blocker
    message: str

    metadata: PayrollBlockersErrorErrorsItemMetadata

class PayrollBlockersErrorErrorsItem(RequiredPayrollBlockersErrorErrorsItem, OptionalPayrollBlockersErrorErrorsItem):
    pass
