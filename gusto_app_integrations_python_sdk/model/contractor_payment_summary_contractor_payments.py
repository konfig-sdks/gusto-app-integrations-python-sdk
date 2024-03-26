# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from gusto_app_integrations_python_sdk import schemas  # noqa: F401


class ContractorPaymentSummaryContractorPayments(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    The individual contractor payments, within a given time period, grouped by contractor.
    """


    class MetaOapg:
        unique_items = False
        
        @staticmethod
        def items() -> typing.Type['ContractorPaymentSummaryContractorPaymentsItem']:
            return ContractorPaymentSummaryContractorPaymentsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ContractorPaymentSummaryContractorPaymentsItem'], typing.List['ContractorPaymentSummaryContractorPaymentsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ContractorPaymentSummaryContractorPayments':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ContractorPaymentSummaryContractorPaymentsItem':
        return super().__getitem__(i)

from gusto_app_integrations_python_sdk.model.contractor_payment_summary_contractor_payments_item import ContractorPaymentSummaryContractorPaymentsItem
