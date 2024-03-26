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

from gusto_app_integrations_python_sdk.pydantic.compensation import Compensation

class Job(BaseModel):
    # The title for the job.
    title: typing.Optional[typing.Optional[str]] = Field(None, alias='title')

    # The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.
    version: typing.Optional[str] = Field(None, alias='version')

    # The UUID of the job.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    # The UUID of the employee to which the job belongs.
    employee_uuid: typing.Optional[str] = Field(None, alias='employee_uuid')

    # The date when the employee was hired or rehired for the job.
    hire_date: typing.Optional[str] = Field(None, alias='hire_date')

    # Whether this is the employee's primary job. The value will be set to true unless an existing job exists for the employee.
    primary: typing.Optional[bool] = Field(None, alias='primary')

    # The current compensation rate of the job.
    rate: typing.Optional[str] = Field(None, alias='rate')

    # The payment unit of the current compensation for the job.
    payment_unit: typing.Optional[str] = Field(None, alias='payment_unit')

    # The UUID of the current compensation of the job.
    current_compensation_uuid: typing.Optional[str] = Field(None, alias='current_compensation_uuid')

    # Whether the employee owns at least 2% of the company.
    two_percent_shareholder: typing.Optional[bool] = Field(None, alias='two_percent_shareholder')

    # Whether this job is eligible for workers' compensation coverage in the state of Washington (WA).
    state_wc_covered: typing.Optional[bool] = Field(None, alias='state_wc_covered')

    # The risk class code for workers' compensation in Washington state. Please visit [Washington state's Risk Class page](https://www.lni.wa.gov/insurance/rates-risk-classes/risk-classes-for-workers-compensation/risk-class-lookup#/) to learn more.
    state_wc_class_code: typing.Optional[str] = Field(None, alias='state_wc_class_code')

    compensations: typing.Optional[typing.List[Compensation]] = Field(None, alias='compensations')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
