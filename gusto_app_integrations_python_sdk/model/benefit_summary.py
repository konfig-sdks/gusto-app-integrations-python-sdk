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


class BenefitSummary(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            start_date = schemas.StrSchema
            end_date = schemas.StrSchema
            company_benefit_deduction = schemas.StrSchema
            company_benefit_contribution = schemas.StrSchema
        
            @staticmethod
            def employees() -> typing.Type['BenefitSummaryEmployees']:
                return BenefitSummaryEmployees
            __annotations__ = {
                "description": description,
                "start_date": start_date,
                "end_date": end_date,
                "company_benefit_deduction": company_benefit_deduction,
                "company_benefit_contribution": company_benefit_contribution,
                "employees": employees,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_benefit_deduction"]) -> MetaOapg.properties.company_benefit_deduction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_benefit_contribution"]) -> MetaOapg.properties.company_benefit_contribution: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employees"]) -> 'BenefitSummaryEmployees': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "start_date", "end_date", "company_benefit_deduction", "company_benefit_contribution", "employees", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_benefit_deduction"]) -> typing.Union[MetaOapg.properties.company_benefit_deduction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_benefit_contribution"]) -> typing.Union[MetaOapg.properties.company_benefit_contribution, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employees"]) -> typing.Union['BenefitSummaryEmployees', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "start_date", "end_date", "company_benefit_deduction", "company_benefit_contribution", "employees", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, str, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, str, schemas.Unset] = schemas.unset,
        company_benefit_deduction: typing.Union[MetaOapg.properties.company_benefit_deduction, str, schemas.Unset] = schemas.unset,
        company_benefit_contribution: typing.Union[MetaOapg.properties.company_benefit_contribution, str, schemas.Unset] = schemas.unset,
        employees: typing.Union['BenefitSummaryEmployees', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BenefitSummary':
        return super().__new__(
            cls,
            *args,
            description=description,
            start_date=start_date,
            end_date=end_date,
            company_benefit_deduction=company_benefit_deduction,
            company_benefit_contribution=company_benefit_contribution,
            employees=employees,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_app_integrations_python_sdk.model.benefit_summary_employees import BenefitSummaryEmployees
