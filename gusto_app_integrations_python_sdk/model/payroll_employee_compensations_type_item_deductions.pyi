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


class PayrollEmployeeCompensationsTypeItemDeductions(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    An array of employee deductions for the pay period. Deductions are only included for processed payroll when the include parameter is present.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['PayrollEmployeeCompensationsTypeItemDeductionsItem']:
            return PayrollEmployeeCompensationsTypeItemDeductionsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['PayrollEmployeeCompensationsTypeItemDeductionsItem'], typing.List['PayrollEmployeeCompensationsTypeItemDeductionsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PayrollEmployeeCompensationsTypeItemDeductions':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'PayrollEmployeeCompensationsTypeItemDeductionsItem':
        return super().__getitem__(i)

from gusto_app_integrations_python_sdk.model.payroll_employee_compensations_type_item_deductions_item import PayrollEmployeeCompensationsTypeItemDeductionsItem
