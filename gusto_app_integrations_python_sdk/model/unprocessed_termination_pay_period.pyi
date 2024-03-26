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


class UnprocessedTerminationPayPeriod(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The representation of an unprocessed termination pay period.
    """


    class MetaOapg:
        
        class properties:
            start_date = schemas.StrSchema
            end_date = schemas.StrSchema
            check_date = schemas.StrSchema
            debit_date = schemas.StrSchema
            employee_name = schemas.StrSchema
            employee_uuid = schemas.StrSchema
            pay_schedule_uuid = schemas.StrSchema
            __annotations__ = {
                "start_date": start_date,
                "end_date": end_date,
                "check_date": check_date,
                "debit_date": debit_date,
                "employee_name": employee_name,
                "employee_uuid": employee_uuid,
                "pay_schedule_uuid": pay_schedule_uuid,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["check_date"]) -> MetaOapg.properties.check_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["debit_date"]) -> MetaOapg.properties.debit_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_name"]) -> MetaOapg.properties.employee_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_uuid"]) -> MetaOapg.properties.employee_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pay_schedule_uuid"]) -> MetaOapg.properties.pay_schedule_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["start_date", "end_date", "check_date", "debit_date", "employee_name", "employee_uuid", "pay_schedule_uuid", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["check_date"]) -> typing.Union[MetaOapg.properties.check_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["debit_date"]) -> typing.Union[MetaOapg.properties.debit_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_name"]) -> typing.Union[MetaOapg.properties.employee_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_uuid"]) -> typing.Union[MetaOapg.properties.employee_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pay_schedule_uuid"]) -> typing.Union[MetaOapg.properties.pay_schedule_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["start_date", "end_date", "check_date", "debit_date", "employee_name", "employee_uuid", "pay_schedule_uuid", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        start_date: typing.Union[MetaOapg.properties.start_date, str, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, str, schemas.Unset] = schemas.unset,
        check_date: typing.Union[MetaOapg.properties.check_date, str, schemas.Unset] = schemas.unset,
        debit_date: typing.Union[MetaOapg.properties.debit_date, str, schemas.Unset] = schemas.unset,
        employee_name: typing.Union[MetaOapg.properties.employee_name, str, schemas.Unset] = schemas.unset,
        employee_uuid: typing.Union[MetaOapg.properties.employee_uuid, str, schemas.Unset] = schemas.unset,
        pay_schedule_uuid: typing.Union[MetaOapg.properties.pay_schedule_uuid, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UnprocessedTerminationPayPeriod':
        return super().__new__(
            cls,
            *args,
            start_date=start_date,
            end_date=end_date,
            check_date=check_date,
            debit_date=debit_date,
            employee_name=employee_name,
            employee_uuid=employee_uuid,
            pay_schedule_uuid=pay_schedule_uuid,
            _configuration=_configuration,
            **kwargs,
        )
