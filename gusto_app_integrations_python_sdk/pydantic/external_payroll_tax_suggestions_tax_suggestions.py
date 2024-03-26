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


class ExternalPayrollTaxSuggestionsTaxSuggestions(BaseModel):
    # The ID of the tax.
    tax_id: typing.Optional[int] = Field(None, alias='tax_id')

    # Calculated tax amount.
    amount: typing.Optional[str] = Field(None, alias='amount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
