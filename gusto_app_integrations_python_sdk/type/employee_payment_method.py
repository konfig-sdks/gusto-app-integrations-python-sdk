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

from gusto_app_integrations_python_sdk.type.payment_method_bank_account import PaymentMethodBankAccount

class RequiredEmployeePaymentMethod(TypedDict):
    pass

class OptionalEmployeePaymentMethod(TypedDict, total=False):
    # The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.
    version: str

    # The payment method type. If type is Check, then split_by and splits do not need to be populated. If type is Direct Deposit, split_by and splits are required.
    type: str

    # Describes how the payment will be split. If split_by is Percentage, then the split amounts must add up to exactly 100. If split_by is Amount, then the last split amount must be nil to capture the remainder.
    split_by: typing.Optional[str]

    splits: typing.Optional[typing.List[PaymentMethodBankAccount]]

class EmployeePaymentMethod(RequiredEmployeePaymentMethod, OptionalEmployeePaymentMethod):
    pass
