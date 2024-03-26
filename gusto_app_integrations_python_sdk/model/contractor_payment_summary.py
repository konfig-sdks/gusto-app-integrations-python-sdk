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


class ContractorPaymentSummary(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The representation of the summary of contractor payments for a given company in a given time period.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def total() -> typing.Type['ContractorPaymentSummaryTotal']:
                return ContractorPaymentSummaryTotal
        
            @staticmethod
            def contractor_payments() -> typing.Type['ContractorPaymentSummaryContractorPayments']:
                return ContractorPaymentSummaryContractorPayments
            __annotations__ = {
                "total": total,
                "contractor_payments": contractor_payments,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> 'ContractorPaymentSummaryTotal': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractor_payments"]) -> 'ContractorPaymentSummaryContractorPayments': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total", "contractor_payments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> typing.Union['ContractorPaymentSummaryTotal', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractor_payments"]) -> typing.Union['ContractorPaymentSummaryContractorPayments', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total", "contractor_payments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        total: typing.Union['ContractorPaymentSummaryTotal', schemas.Unset] = schemas.unset,
        contractor_payments: typing.Union['ContractorPaymentSummaryContractorPayments', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContractorPaymentSummary':
        return super().__new__(
            cls,
            *args,
            total=total,
            contractor_payments=contractor_payments,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_app_integrations_python_sdk.model.contractor_payment_summary_contractor_payments import ContractorPaymentSummaryContractorPayments
from gusto_app_integrations_python_sdk.model.contractor_payment_summary_total import ContractorPaymentSummaryTotal
