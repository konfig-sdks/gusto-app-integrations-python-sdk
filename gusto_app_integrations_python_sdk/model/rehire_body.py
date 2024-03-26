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


class RehireBody(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "file_new_hire_report",
            "effective_date",
            "work_location_uuid",
        }
        
        class properties:
            effective_date = schemas.StrSchema
            file_new_hire_report = schemas.BoolSchema
            work_location_uuid = schemas.StrSchema
            
            
            class employment_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "part_time": "PART_TIME",
                        "full_time": "FULL_TIME",
                        "part_time_eligible": "PART_TIME_ELIGIBLE",
                        "variable": "VARIABLE",
                        "seasonal": "SEASONAL",
                        "not_set": "NOT_SET",
                    }
                
                @schemas.classproperty
                def PART_TIME(cls):
                    return cls("part_time")
                
                @schemas.classproperty
                def FULL_TIME(cls):
                    return cls("full_time")
                
                @schemas.classproperty
                def PART_TIME_ELIGIBLE(cls):
                    return cls("part_time_eligible")
                
                @schemas.classproperty
                def VARIABLE(cls):
                    return cls("variable")
                
                @schemas.classproperty
                def SEASONAL(cls):
                    return cls("seasonal")
                
                @schemas.classproperty
                def NOT_SET(cls):
                    return cls("not_set")
            two_percent_shareholder = schemas.BoolSchema
            __annotations__ = {
                "effective_date": effective_date,
                "file_new_hire_report": file_new_hire_report,
                "work_location_uuid": work_location_uuid,
                "employment_status": employment_status,
                "two_percent_shareholder": two_percent_shareholder,
            }
    
    file_new_hire_report: MetaOapg.properties.file_new_hire_report
    effective_date: MetaOapg.properties.effective_date
    work_location_uuid: MetaOapg.properties.work_location_uuid
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effective_date"]) -> MetaOapg.properties.effective_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_new_hire_report"]) -> MetaOapg.properties.file_new_hire_report: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["work_location_uuid"]) -> MetaOapg.properties.work_location_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employment_status"]) -> MetaOapg.properties.employment_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["two_percent_shareholder"]) -> MetaOapg.properties.two_percent_shareholder: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["effective_date", "file_new_hire_report", "work_location_uuid", "employment_status", "two_percent_shareholder", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effective_date"]) -> MetaOapg.properties.effective_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_new_hire_report"]) -> MetaOapg.properties.file_new_hire_report: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["work_location_uuid"]) -> MetaOapg.properties.work_location_uuid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employment_status"]) -> typing.Union[MetaOapg.properties.employment_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["two_percent_shareholder"]) -> typing.Union[MetaOapg.properties.two_percent_shareholder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["effective_date", "file_new_hire_report", "work_location_uuid", "employment_status", "two_percent_shareholder", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        file_new_hire_report: typing.Union[MetaOapg.properties.file_new_hire_report, bool, ],
        effective_date: typing.Union[MetaOapg.properties.effective_date, str, ],
        work_location_uuid: typing.Union[MetaOapg.properties.work_location_uuid, str, ],
        employment_status: typing.Union[MetaOapg.properties.employment_status, str, schemas.Unset] = schemas.unset,
        two_percent_shareholder: typing.Union[MetaOapg.properties.two_percent_shareholder, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RehireBody':
        return super().__new__(
            cls,
            *args,
            file_new_hire_report=file_new_hire_report,
            effective_date=effective_date,
            work_location_uuid=work_location_uuid,
            employment_status=employment_status,
            two_percent_shareholder=two_percent_shareholder,
            _configuration=_configuration,
            **kwargs,
        )
