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


class ExternalPayrollBasic(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The representation of an external payroll with minimal information.
    """


    class MetaOapg:
        
        class properties:
            uuid = schemas.StrSchema
            company_uuid = schemas.StrSchema
            check_date = schemas.StrSchema
            payment_period_start_date = schemas.StrSchema
            payment_period_end_date = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def UNPROCESSED(cls):
                    return cls("unprocessed")
                
                @schemas.classproperty
                def PROCESSED(cls):
                    return cls("processed")
            __annotations__ = {
                "uuid": uuid,
                "company_uuid": company_uuid,
                "check_date": check_date,
                "payment_period_start_date": payment_period_start_date,
                "payment_period_end_date": payment_period_end_date,
                "status": status,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_uuid"]) -> MetaOapg.properties.company_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["check_date"]) -> MetaOapg.properties.check_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_period_start_date"]) -> MetaOapg.properties.payment_period_start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_period_end_date"]) -> MetaOapg.properties.payment_period_end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["uuid", "company_uuid", "check_date", "payment_period_start_date", "payment_period_end_date", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_uuid"]) -> typing.Union[MetaOapg.properties.company_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["check_date"]) -> typing.Union[MetaOapg.properties.check_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_period_start_date"]) -> typing.Union[MetaOapg.properties.payment_period_start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_period_end_date"]) -> typing.Union[MetaOapg.properties.payment_period_end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uuid", "company_uuid", "check_date", "payment_period_start_date", "payment_period_end_date", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        company_uuid: typing.Union[MetaOapg.properties.company_uuid, str, schemas.Unset] = schemas.unset,
        check_date: typing.Union[MetaOapg.properties.check_date, str, schemas.Unset] = schemas.unset,
        payment_period_start_date: typing.Union[MetaOapg.properties.payment_period_start_date, str, schemas.Unset] = schemas.unset,
        payment_period_end_date: typing.Union[MetaOapg.properties.payment_period_end_date, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExternalPayrollBasic':
        return super().__new__(
            cls,
            *args,
            uuid=uuid,
            company_uuid=company_uuid,
            check_date=check_date,
            payment_period_start_date=payment_period_start_date,
            payment_period_end_date=payment_period_end_date,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )
