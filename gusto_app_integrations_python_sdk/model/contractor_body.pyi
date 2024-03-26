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


class ContractorBody(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INDIVIDUAL(cls):
                    return cls("Individual")
                
                @schemas.classproperty
                def BUSINESS(cls):
                    return cls("Business")
            
            
            class wage_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FIXED(cls):
                    return cls("Fixed")
                
                @schemas.classproperty
                def HOURLY(cls):
                    return cls("Hourly")
            start_date = schemas.StrSchema
            hourly_rate = schemas.StrSchema
            self_onboarding = schemas.BoolSchema
            email = schemas.StrSchema
            first_name = schemas.StrSchema
            last_name = schemas.StrSchema
            middle_initial = schemas.StrSchema
            file_new_hire_report = schemas.BoolSchema
            
            
            class work_state(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'work_state':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ssn(
                schemas.StrSchema
            ):
                pass
            business_name = schemas.StrSchema
            ein = schemas.StrSchema
            is_active = schemas.BoolSchema
            __annotations__ = {
                "type": type,
                "wage_type": wage_type,
                "start_date": start_date,
                "hourly_rate": hourly_rate,
                "self_onboarding": self_onboarding,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "middle_initial": middle_initial,
                "file_new_hire_report": file_new_hire_report,
                "work_state": work_state,
                "ssn": ssn,
                "business_name": business_name,
                "ein": ein,
                "is_active": is_active,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wage_type"]) -> MetaOapg.properties.wage_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hourly_rate"]) -> MetaOapg.properties.hourly_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self_onboarding"]) -> MetaOapg.properties.self_onboarding: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["middle_initial"]) -> MetaOapg.properties.middle_initial: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_new_hire_report"]) -> MetaOapg.properties.file_new_hire_report: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["work_state"]) -> MetaOapg.properties.work_state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssn"]) -> MetaOapg.properties.ssn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["business_name"]) -> MetaOapg.properties.business_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ein"]) -> MetaOapg.properties.ein: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "wage_type", "start_date", "hourly_rate", "self_onboarding", "email", "first_name", "last_name", "middle_initial", "file_new_hire_report", "work_state", "ssn", "business_name", "ein", "is_active", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wage_type"]) -> typing.Union[MetaOapg.properties.wage_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hourly_rate"]) -> typing.Union[MetaOapg.properties.hourly_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self_onboarding"]) -> typing.Union[MetaOapg.properties.self_onboarding, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> typing.Union[MetaOapg.properties.first_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> typing.Union[MetaOapg.properties.last_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["middle_initial"]) -> typing.Union[MetaOapg.properties.middle_initial, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_new_hire_report"]) -> typing.Union[MetaOapg.properties.file_new_hire_report, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["work_state"]) -> typing.Union[MetaOapg.properties.work_state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssn"]) -> typing.Union[MetaOapg.properties.ssn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["business_name"]) -> typing.Union[MetaOapg.properties.business_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ein"]) -> typing.Union[MetaOapg.properties.ein, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_active"]) -> typing.Union[MetaOapg.properties.is_active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "wage_type", "start_date", "hourly_rate", "self_onboarding", "email", "first_name", "last_name", "middle_initial", "file_new_hire_report", "work_state", "ssn", "business_name", "ein", "is_active", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        wage_type: typing.Union[MetaOapg.properties.wage_type, str, schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, str, schemas.Unset] = schemas.unset,
        hourly_rate: typing.Union[MetaOapg.properties.hourly_rate, str, schemas.Unset] = schemas.unset,
        self_onboarding: typing.Union[MetaOapg.properties.self_onboarding, bool, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        first_name: typing.Union[MetaOapg.properties.first_name, str, schemas.Unset] = schemas.unset,
        last_name: typing.Union[MetaOapg.properties.last_name, str, schemas.Unset] = schemas.unset,
        middle_initial: typing.Union[MetaOapg.properties.middle_initial, str, schemas.Unset] = schemas.unset,
        file_new_hire_report: typing.Union[MetaOapg.properties.file_new_hire_report, bool, schemas.Unset] = schemas.unset,
        work_state: typing.Union[MetaOapg.properties.work_state, None, str, schemas.Unset] = schemas.unset,
        ssn: typing.Union[MetaOapg.properties.ssn, str, schemas.Unset] = schemas.unset,
        business_name: typing.Union[MetaOapg.properties.business_name, str, schemas.Unset] = schemas.unset,
        ein: typing.Union[MetaOapg.properties.ein, str, schemas.Unset] = schemas.unset,
        is_active: typing.Union[MetaOapg.properties.is_active, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContractorBody':
        return super().__new__(
            cls,
            *args,
            type=type,
            wage_type=wage_type,
            start_date=start_date,
            hourly_rate=hourly_rate,
            self_onboarding=self_onboarding,
            email=email,
            first_name=first_name,
            last_name=last_name,
            middle_initial=middle_initial,
            file_new_hire_report=file_new_hire_report,
            work_state=work_state,
            ssn=ssn,
            business_name=business_name,
            ein=ein,
            is_active=is_active,
            _configuration=_configuration,
            **kwargs,
        )
