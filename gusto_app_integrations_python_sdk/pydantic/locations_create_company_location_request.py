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


class LocationsCreateCompanyLocationRequest(BaseModel):
    phone_number: str = Field(alias='phone_number')

    street_1: str = Field(alias='street_1')

    city: str = Field(alias='city')

    state: str = Field(alias='state')

    zip: str = Field(alias='zip')

    street_2: typing.Optional[typing.Optional[str]] = Field(None, alias='street_2')

    country: typing.Optional[str] = Field(None, alias='country')

    # Specify if this location is the company's mailing address.
    mailing_address: typing.Optional[bool] = Field(None, alias='mailing_address')

    # Specify if this location is the company's filing address.
    filing_address: typing.Optional[bool] = Field(None, alias='filing_address')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
