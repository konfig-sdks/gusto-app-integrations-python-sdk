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


class ContractorPaymentReceipt(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            contractor_payment_uuid = schemas.StrSchema
            company_uuid = schemas.StrSchema
            name_of_sender = schemas.StrSchema
            name_of_recipient = schemas.StrSchema
            debit_date = schemas.DateSchema
            license = schemas.StrSchema
            license_uri = schemas.StrSchema
            right_to_refund = schemas.StrSchema
            liability_of_licensee = schemas.StrSchema
        
            @staticmethod
            def totals() -> typing.Type['ContractorPaymentReceiptTotals']:
                return ContractorPaymentReceiptTotals
        
            @staticmethod
            def contractor_payments() -> typing.Type['ContractorPaymentReceiptContractorPayments']:
                return ContractorPaymentReceiptContractorPayments
        
            @staticmethod
            def licensee() -> typing.Type['ContractorPaymentReceiptLicensee']:
                return ContractorPaymentReceiptLicensee
            __annotations__ = {
                "contractor_payment_uuid": contractor_payment_uuid,
                "company_uuid": company_uuid,
                "name_of_sender": name_of_sender,
                "name_of_recipient": name_of_recipient,
                "debit_date": debit_date,
                "license": license,
                "license_uri": license_uri,
                "right_to_refund": right_to_refund,
                "liability_of_licensee": liability_of_licensee,
                "totals": totals,
                "contractor_payments": contractor_payments,
                "licensee": licensee,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractor_payment_uuid"]) -> MetaOapg.properties.contractor_payment_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_uuid"]) -> MetaOapg.properties.company_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name_of_sender"]) -> MetaOapg.properties.name_of_sender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name_of_recipient"]) -> MetaOapg.properties.name_of_recipient: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["debit_date"]) -> MetaOapg.properties.debit_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["license"]) -> MetaOapg.properties.license: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["license_uri"]) -> MetaOapg.properties.license_uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["right_to_refund"]) -> MetaOapg.properties.right_to_refund: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["liability_of_licensee"]) -> MetaOapg.properties.liability_of_licensee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totals"]) -> 'ContractorPaymentReceiptTotals': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractor_payments"]) -> 'ContractorPaymentReceiptContractorPayments': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["licensee"]) -> 'ContractorPaymentReceiptLicensee': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["contractor_payment_uuid", "company_uuid", "name_of_sender", "name_of_recipient", "debit_date", "license", "license_uri", "right_to_refund", "liability_of_licensee", "totals", "contractor_payments", "licensee", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractor_payment_uuid"]) -> typing.Union[MetaOapg.properties.contractor_payment_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_uuid"]) -> typing.Union[MetaOapg.properties.company_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name_of_sender"]) -> typing.Union[MetaOapg.properties.name_of_sender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name_of_recipient"]) -> typing.Union[MetaOapg.properties.name_of_recipient, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["debit_date"]) -> typing.Union[MetaOapg.properties.debit_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["license"]) -> typing.Union[MetaOapg.properties.license, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["license_uri"]) -> typing.Union[MetaOapg.properties.license_uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["right_to_refund"]) -> typing.Union[MetaOapg.properties.right_to_refund, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["liability_of_licensee"]) -> typing.Union[MetaOapg.properties.liability_of_licensee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totals"]) -> typing.Union['ContractorPaymentReceiptTotals', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractor_payments"]) -> typing.Union['ContractorPaymentReceiptContractorPayments', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["licensee"]) -> typing.Union['ContractorPaymentReceiptLicensee', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contractor_payment_uuid", "company_uuid", "name_of_sender", "name_of_recipient", "debit_date", "license", "license_uri", "right_to_refund", "liability_of_licensee", "totals", "contractor_payments", "licensee", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        contractor_payment_uuid: typing.Union[MetaOapg.properties.contractor_payment_uuid, str, schemas.Unset] = schemas.unset,
        company_uuid: typing.Union[MetaOapg.properties.company_uuid, str, schemas.Unset] = schemas.unset,
        name_of_sender: typing.Union[MetaOapg.properties.name_of_sender, str, schemas.Unset] = schemas.unset,
        name_of_recipient: typing.Union[MetaOapg.properties.name_of_recipient, str, schemas.Unset] = schemas.unset,
        debit_date: typing.Union[MetaOapg.properties.debit_date, str, date, schemas.Unset] = schemas.unset,
        license: typing.Union[MetaOapg.properties.license, str, schemas.Unset] = schemas.unset,
        license_uri: typing.Union[MetaOapg.properties.license_uri, str, schemas.Unset] = schemas.unset,
        right_to_refund: typing.Union[MetaOapg.properties.right_to_refund, str, schemas.Unset] = schemas.unset,
        liability_of_licensee: typing.Union[MetaOapg.properties.liability_of_licensee, str, schemas.Unset] = schemas.unset,
        totals: typing.Union['ContractorPaymentReceiptTotals', schemas.Unset] = schemas.unset,
        contractor_payments: typing.Union['ContractorPaymentReceiptContractorPayments', schemas.Unset] = schemas.unset,
        licensee: typing.Union['ContractorPaymentReceiptLicensee', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContractorPaymentReceipt':
        return super().__new__(
            cls,
            *args,
            contractor_payment_uuid=contractor_payment_uuid,
            company_uuid=company_uuid,
            name_of_sender=name_of_sender,
            name_of_recipient=name_of_recipient,
            debit_date=debit_date,
            license=license,
            license_uri=license_uri,
            right_to_refund=right_to_refund,
            liability_of_licensee=liability_of_licensee,
            totals=totals,
            contractor_payments=contractor_payments,
            licensee=licensee,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_app_integrations_python_sdk.model.contractor_payment_receipt_contractor_payments import ContractorPaymentReceiptContractorPayments
from gusto_app_integrations_python_sdk.model.contractor_payment_receipt_licensee import ContractorPaymentReceiptLicensee
from gusto_app_integrations_python_sdk.model.contractor_payment_receipt_totals import ContractorPaymentReceiptTotals
