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


class EmployeeStateTaxInputQuestionFormatOptions(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    For "Select" type questions, the allowed values and display labels.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['EmployeeStateTaxInputQuestionFormatOptionsItem']:
            return EmployeeStateTaxInputQuestionFormatOptionsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['EmployeeStateTaxInputQuestionFormatOptionsItem'], typing.List['EmployeeStateTaxInputQuestionFormatOptionsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EmployeeStateTaxInputQuestionFormatOptions':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'EmployeeStateTaxInputQuestionFormatOptionsItem':
        return super().__getitem__(i)

from gusto_app_integrations_python_sdk.model.employee_state_tax_input_question_format_options_item import EmployeeStateTaxInputQuestionFormatOptionsItem
