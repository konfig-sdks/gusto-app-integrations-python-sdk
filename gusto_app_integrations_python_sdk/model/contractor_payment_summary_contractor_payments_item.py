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


class ContractorPaymentSummaryContractorPaymentsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            contractor_uuid = schemas.NumberSchema
            reimbursement_total = schemas.StrSchema
            wage_total = schemas.StrSchema
            
            
            class payments(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = False
                    
                    @staticmethod
                    def items() -> typing.Type['ContractorPayment']:
                        return ContractorPayment
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ContractorPayment'], typing.List['ContractorPayment']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'payments':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ContractorPayment':
                    return super().__getitem__(i)
            __annotations__ = {
                "contractor_uuid": contractor_uuid,
                "reimbursement_total": reimbursement_total,
                "wage_total": wage_total,
                "payments": payments,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractor_uuid"]) -> MetaOapg.properties.contractor_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reimbursement_total"]) -> MetaOapg.properties.reimbursement_total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wage_total"]) -> MetaOapg.properties.wage_total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payments"]) -> MetaOapg.properties.payments: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["contractor_uuid", "reimbursement_total", "wage_total", "payments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractor_uuid"]) -> typing.Union[MetaOapg.properties.contractor_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reimbursement_total"]) -> typing.Union[MetaOapg.properties.reimbursement_total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wage_total"]) -> typing.Union[MetaOapg.properties.wage_total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payments"]) -> typing.Union[MetaOapg.properties.payments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contractor_uuid", "reimbursement_total", "wage_total", "payments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        contractor_uuid: typing.Union[MetaOapg.properties.contractor_uuid, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        reimbursement_total: typing.Union[MetaOapg.properties.reimbursement_total, str, schemas.Unset] = schemas.unset,
        wage_total: typing.Union[MetaOapg.properties.wage_total, str, schemas.Unset] = schemas.unset,
        payments: typing.Union[MetaOapg.properties.payments, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContractorPaymentSummaryContractorPaymentsItem':
        return super().__new__(
            cls,
            *args,
            contractor_uuid=contractor_uuid,
            reimbursement_total=reimbursement_total,
            wage_total=wage_total,
            payments=payments,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_app_integrations_python_sdk.model.contractor_payment import ContractorPayment
