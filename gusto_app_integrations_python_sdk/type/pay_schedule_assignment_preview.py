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

from gusto_app_integrations_python_sdk.type.pay_schedule_assignment_employee_change import PayScheduleAssignmentEmployeeChange

class RequiredPayScheduleAssignmentPreview(TypedDict):
    pass

class OptionalPayScheduleAssignmentPreview(TypedDict, total=False):
    # The pay schedule assignment type.
    type: str

    # A list of pay schedule changes including pay period and transition pay period.
    employee_changes: typing.List[PayScheduleAssignmentEmployeeChange]

class PayScheduleAssignmentPreview(RequiredPayScheduleAssignmentPreview, OptionalPayScheduleAssignmentPreview):
    pass
