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

from gusto_app_integrations_python_sdk.pydantic.departments_add_people_to_department_request_contractors import DepartmentsAddPeopleToDepartmentRequestContractors
from gusto_app_integrations_python_sdk.pydantic.departments_add_people_to_department_request_employees import DepartmentsAddPeopleToDepartmentRequestEmployees

class DepartmentsAddPeopleToDepartmentRequest(BaseModel):
    # The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.
    version: typing.Optional[str] = Field(None, alias='version')

    employees: typing.Optional[DepartmentsAddPeopleToDepartmentRequestEmployees] = Field(None, alias='employees')

    contractors: typing.Optional[DepartmentsAddPeopleToDepartmentRequestContractors] = Field(None, alias='contractors')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
