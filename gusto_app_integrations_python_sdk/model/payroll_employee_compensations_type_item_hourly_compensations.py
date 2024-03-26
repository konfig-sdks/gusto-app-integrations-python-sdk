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


class PayrollEmployeeCompensationsTypeItemHourlyCompensations(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    An array of hourly compensations for the employee. Hourly compensations include regular, overtime, and double overtime hours. If this payroll has been processed, only hourly compensations with a value greater than 0.00 are returned. For an unprocessed payroll, all active hourly compensations are returned.
    """


    class MetaOapg:
        unique_items = False
        
        @staticmethod
        def items() -> typing.Type['PayrollEmployeeCompensationsTypeItemHourlyCompensationsItem']:
            return PayrollEmployeeCompensationsTypeItemHourlyCompensationsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['PayrollEmployeeCompensationsTypeItemHourlyCompensationsItem'], typing.List['PayrollEmployeeCompensationsTypeItemHourlyCompensationsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PayrollEmployeeCompensationsTypeItemHourlyCompensations':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'PayrollEmployeeCompensationsTypeItemHourlyCompensationsItem':
        return super().__getitem__(i)

from gusto_app_integrations_python_sdk.model.payroll_employee_compensations_type_item_hourly_compensations_item import PayrollEmployeeCompensationsTypeItemHourlyCompensationsItem
