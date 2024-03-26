# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from gusto_app_integrations_python_sdk.pydantic.companies_create_company_request_company_addresses import CompaniesCreateCompanyRequestCompanyAddresses
from gusto_app_integrations_python_sdk.pydantic.companies_create_company_request_company_states import CompaniesCreateCompanyRequestCompanyStates

class CompaniesCreateCompanyRequestCompany(BaseModel):
    # The legal name of the company.
    name: str = Field(alias='name')

    # The name of the company.
    trade_name: typing.Optional[str] = Field(None, alias='trade_name')

    # The employer identification number (EIN) of the company.
    ein: typing.Optional[str] = Field(None, alias='ein')

    states: typing.Optional[CompaniesCreateCompanyRequestCompanyStates] = Field(None, alias='states')

    # The number of employees in the company.
    number_employees: typing.Optional[typing.Union[int, float]] = Field(None, alias='number_employees')

    addresses: typing.Optional[CompaniesCreateCompanyRequestCompanyAddresses] = Field(None, alias='addresses')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
