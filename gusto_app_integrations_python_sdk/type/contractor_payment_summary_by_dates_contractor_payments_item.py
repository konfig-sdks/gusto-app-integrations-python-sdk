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

from gusto_app_integrations_python_sdk.type.contractor_payment import ContractorPayment

class RequiredContractorPaymentSummaryByDatesContractorPaymentsItem(TypedDict):
    pass

class OptionalContractorPaymentSummaryByDatesContractorPaymentsItem(TypedDict, total=False):
    # The UUID of the contractor.
    contractor_uuid: str

    # The payment check date.
    check_date: str

    # The total reimbursements for the contractor within a given time period.
    reimbursement_total: str

    # The total wages for the contractor within a given time period.
    wage_total: str

    # The contractor’s payments within a given time period. 
    payments: typing.List[ContractorPayment]

class ContractorPaymentSummaryByDatesContractorPaymentsItem(RequiredContractorPaymentSummaryByDatesContractorPaymentsItem, OptionalContractorPaymentSummaryByDatesContractorPaymentsItem):
    pass
