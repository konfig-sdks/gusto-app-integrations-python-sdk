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


class InvoiceDataActiveCompaniesItem(BaseModel):
    # unique identifier for the company associated with the invoice data
    company_uuid: typing.Optional[str] = Field(None, alias='company_uuid')

    # The number of active employees the company was or will be invoiced for that invoice period. Active employees are calculated as the count of onboarded employees hired before the end of the invoice period and not terminated before the start of the invoice period.
    active_employees: typing.Optional[int] = Field(None, alias='active_employees')

    # The number of active contractors the company was or will be invoiced for that invoice period. Active contractors are calculated as any contractor with an active contractor payment during the invoice period.
    active_contractors: typing.Optional[int] = Field(None, alias='active_contractors')

    # The first invoice period for the company. This will either be the invoice period of the first invoice-able event (first payroll or contractor payment) or the date they migrated to embedded, whichever is later.
    initial_invoice_period: typing.Optional[str] = Field(None, alias='initial_invoice_period')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
