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


class CompaniesCreateCompanyRequestCompanyAddressesItem(BaseModel):
    street_1: typing.Optional[str] = Field(None, alias='street_1')

    street_2: typing.Optional[typing.Optional[str]] = Field(None, alias='street_2')

    city: typing.Optional[str] = Field(None, alias='city')

    zip: typing.Optional[str] = Field(None, alias='zip')

    state: typing.Optional[str] = Field(None, alias='state')

    phone: typing.Optional[str] = Field(None, alias='phone')

    # Whether or not this is a primary address for the company. If set to true, the address will be used as the mailing and filing address for the company and will be added as a work location. If set to false or not included, the address will only be added as a work location for the company. If multiple addresses are included, only one should be marked as primary.
    is_primary: typing.Optional[str] = Field(None, alias='is_primary')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
