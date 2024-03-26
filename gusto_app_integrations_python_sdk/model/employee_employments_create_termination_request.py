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


class EmployeeEmploymentsCreateTerminationRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "effective_date",
        }
        
        class properties:
            effective_date = schemas.StrSchema
            run_termination_payroll = schemas.BoolSchema
            __annotations__ = {
                "effective_date": effective_date,
                "run_termination_payroll": run_termination_payroll,
            }
    
    effective_date: MetaOapg.properties.effective_date
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effective_date"]) -> MetaOapg.properties.effective_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["run_termination_payroll"]) -> MetaOapg.properties.run_termination_payroll: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["effective_date", "run_termination_payroll", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effective_date"]) -> MetaOapg.properties.effective_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["run_termination_payroll"]) -> typing.Union[MetaOapg.properties.run_termination_payroll, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["effective_date", "run_termination_payroll", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        effective_date: typing.Union[MetaOapg.properties.effective_date, str, ],
        run_termination_payroll: typing.Union[MetaOapg.properties.run_termination_payroll, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeEmploymentsCreateTerminationRequest':
        return super().__new__(
            cls,
            *args,
            effective_date=effective_date,
            run_termination_payroll=run_termination_payroll,
            _configuration=_configuration,
            **kwargs,
        )
