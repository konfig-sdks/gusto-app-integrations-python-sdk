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


class CompaniesCreateCompanyRequestCompany(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            trade_name = schemas.StrSchema
            ein = schemas.StrSchema
        
            @staticmethod
            def states() -> typing.Type['CompaniesCreateCompanyRequestCompanyStates']:
                return CompaniesCreateCompanyRequestCompanyStates
            number_employees = schemas.NumberSchema
        
            @staticmethod
            def addresses() -> typing.Type['CompaniesCreateCompanyRequestCompanyAddresses']:
                return CompaniesCreateCompanyRequestCompanyAddresses
            __annotations__ = {
                "name": name,
                "trade_name": trade_name,
                "ein": ein,
                "states": states,
                "number_employees": number_employees,
                "addresses": addresses,
            }
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trade_name"]) -> MetaOapg.properties.trade_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ein"]) -> MetaOapg.properties.ein: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["states"]) -> 'CompaniesCreateCompanyRequestCompanyStates': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number_employees"]) -> MetaOapg.properties.number_employees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addresses"]) -> 'CompaniesCreateCompanyRequestCompanyAddresses': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "trade_name", "ein", "states", "number_employees", "addresses", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trade_name"]) -> typing.Union[MetaOapg.properties.trade_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ein"]) -> typing.Union[MetaOapg.properties.ein, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["states"]) -> typing.Union['CompaniesCreateCompanyRequestCompanyStates', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number_employees"]) -> typing.Union[MetaOapg.properties.number_employees, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addresses"]) -> typing.Union['CompaniesCreateCompanyRequestCompanyAddresses', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "trade_name", "ein", "states", "number_employees", "addresses", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        trade_name: typing.Union[MetaOapg.properties.trade_name, str, schemas.Unset] = schemas.unset,
        ein: typing.Union[MetaOapg.properties.ein, str, schemas.Unset] = schemas.unset,
        states: typing.Union['CompaniesCreateCompanyRequestCompanyStates', schemas.Unset] = schemas.unset,
        number_employees: typing.Union[MetaOapg.properties.number_employees, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        addresses: typing.Union['CompaniesCreateCompanyRequestCompanyAddresses', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompaniesCreateCompanyRequestCompany':
        return super().__new__(
            cls,
            *args,
            name=name,
            trade_name=trade_name,
            ein=ein,
            states=states,
            number_employees=number_employees,
            addresses=addresses,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_app_integrations_python_sdk.model.companies_create_company_request_company_addresses import CompaniesCreateCompanyRequestCompanyAddresses
from gusto_app_integrations_python_sdk.model.companies_create_company_request_company_states import CompaniesCreateCompanyRequestCompanyStates
