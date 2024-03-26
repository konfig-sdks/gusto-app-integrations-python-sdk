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


class RequiredContractorBankAccount(TypedDict):
    pass

class OptionalContractorBankAccount(TypedDict, total=False):
    # UUID of the bank account
    uuid: str

    # UUID of the employee
    contractor_uuid: str

    # Bank account type
    account_type: str

    # Name for the bank account
    name: str

    # The bank account's routing number
    routing_number: str

    # Masked bank account number
    hidden_account_number: str

class ContractorBankAccount(RequiredContractorBankAccount, OptionalContractorBankAccount):
    pass
