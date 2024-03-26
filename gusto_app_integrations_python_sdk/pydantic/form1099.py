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


class Form1099(BaseModel):
    # The title of the form
    title: typing.Optional[str] = Field(None, alias='title')

    # The description of the form
    description: typing.Optional[str] = Field(None, alias='description')

    # The UUID of the form
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    # The type identifier of the form
    name: typing.Optional[str] = Field(None, alias='name')

    # If the form is in a draft state. E.g. End of year tax forms may be provided in a draft state prior to being finalized.
    draft: typing.Optional[bool] = Field(None, alias='draft')

    # The year of this form. For some forms, e.g. tax forms, this is the year which the form represents. A 1099 for January - December 2022 would be delivered in January 2023 and have a year value of 2022. This value is nullable and will not be present on all forms.
    year: typing.Optional[typing.Optional[int]] = Field(None, alias='year')

    # The quarter of this form. This value is currently always null since it is not present on any contractor forms.
    quarter: typing.Optional[typing.Optional[int]] = Field(None, alias='quarter')

    # A boolean flag that indicates whether the form needs signing or not. Note that this value will change after the form is signed.
    requires_signing: typing.Optional[bool] = Field(None, alias='requires_signing')

    # The contractor UUID
    contractor_uuid: typing.Optional[str] = Field(None, alias='contractor_uuid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
