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


class JobsAndCompensationsUpdateJobRequest(BaseModel):
    # The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.
    version: str = Field(alias='version')

    # The job title
    title: typing.Optional[str] = Field(None, alias='title')

    # The date when the employee was hired or rehired for the job.
    hire_date: typing.Optional[str] = Field(None, alias='hire_date')

    # Whether the employee owns at least 2% of the company.
    two_percent_shareholder: typing.Optional[bool] = Field(None, alias='two_percent_shareholder')

    # Whether this job is eligible for workers' compensation coverage in the state of Washington (WA).
    state_wc_covered: typing.Optional[bool] = Field(None, alias='state_wc_covered')

    # The risk class code for workers' compensation in Washington state. Please visit [Washington state's Risk Class page](https://www.lni.wa.gov/insurance/rates-risk-classes/risk-classes-for-workers-compensation/risk-class-lookup#/) to learn more.
    state_wc_class_code: typing.Optional[str] = Field(None, alias='state_wc_class_code')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
