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


class CompanyBenefitsGetByCompanyIdResponse(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['CompanyBenefit']:
            return CompanyBenefit

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['CompanyBenefit'], typing.List['CompanyBenefit']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CompanyBenefitsGetByCompanyIdResponse':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'CompanyBenefit':
        return super().__getitem__(i)

from gusto_app_integrations_python_sdk.model.company_benefit import CompanyBenefit
