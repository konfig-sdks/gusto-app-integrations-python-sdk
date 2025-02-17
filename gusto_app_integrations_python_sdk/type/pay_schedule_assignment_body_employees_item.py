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


class RequiredPayScheduleAssignmentBodyEmployeesItem(TypedDict):
    pass

class OptionalPayScheduleAssignmentBodyEmployeesItem(TypedDict, total=False):
    # Employee UUID
    employee_uuid: str

    # Pay schedule UUID
    pay_schedule_uuid: str

class PayScheduleAssignmentBodyEmployeesItem(RequiredPayScheduleAssignmentBodyEmployeesItem, OptionalPayScheduleAssignmentBodyEmployeesItem):
    pass
