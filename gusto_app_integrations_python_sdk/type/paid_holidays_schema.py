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


class RequiredPaidHolidaysSchema(TypedDict):
    pass

class OptionalPaidHolidaysSchema(TypedDict, total=False):
    # the holiday's identifier
    holiday_key: str

    # the holiday's official name
    holiday_name: str

    # the holiday's start date (YYYY-MM-DD)
    start_date: str

    # the holiday's end date (YYYY-MM-DD)
    end_date: str

class PaidHolidaysSchema(RequiredPaidHolidaysSchema, OptionalPaidHolidaysSchema):
    pass
