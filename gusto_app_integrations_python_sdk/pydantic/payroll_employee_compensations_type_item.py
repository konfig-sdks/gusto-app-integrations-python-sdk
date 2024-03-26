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

from gusto_app_integrations_python_sdk.pydantic.payroll_employee_compensations_type_item_benefits import PayrollEmployeeCompensationsTypeItemBenefits
from gusto_app_integrations_python_sdk.pydantic.payroll_employee_compensations_type_item_deductions import PayrollEmployeeCompensationsTypeItemDeductions
from gusto_app_integrations_python_sdk.pydantic.payroll_employee_compensations_type_item_fixed_compensations import PayrollEmployeeCompensationsTypeItemFixedCompensations
from gusto_app_integrations_python_sdk.pydantic.payroll_employee_compensations_type_item_hourly_compensations import PayrollEmployeeCompensationsTypeItemHourlyCompensations
from gusto_app_integrations_python_sdk.pydantic.payroll_employee_compensations_type_item_paid_time_off import PayrollEmployeeCompensationsTypeItemPaidTimeOff
from gusto_app_integrations_python_sdk.pydantic.payroll_employee_compensations_type_item_taxes import PayrollEmployeeCompensationsTypeItemTaxes

class PayrollEmployeeCompensationsTypeItem(BaseModel):
    # The current version of this employee compensation. This field is only available for prepared payrolls. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.
    version: typing.Optional[str] = Field(None, alias='version')

    # The UUID of the employee.
    employee_uuid: typing.Optional[str] = Field(None, alias='employee_uuid')

    # This employee will be excluded from payroll calculation and will not be paid for the payroll. Cancelling a payroll would reset all employees' excluded back to false.
    excluded: typing.Optional[bool] = Field(None, alias='excluded')

    # The employee's gross pay, equal to regular wages + cash tips + payroll tips + any other additional earnings, excluding imputed income. This value is only available for processed payrolls.
    gross_pay: typing.Optional[typing.Optional[str]] = Field(None, alias='gross_pay')

    # The employee's net pay, equal to gross_pay - employee taxes - employee deductions or garnishments - cash tips. This value is only available for processed payrolls.
    net_pay: typing.Optional[typing.Optional[str]] = Field(None, alias='net_pay')

    # The employee's check amount, equal to net_pay + reimbursements. This value is only available for processed payrolls.
    check_amount: typing.Optional[typing.Optional[str]] = Field(None, alias='check_amount')

    # The employee's compensation payment method.
    payment_method: typing.Optional[Literal["Check", "Direct Deposit"]] = Field(None, alias='payment_method')

    # Custom text that will be printed as a personal note to the employee on a paystub.
    memo: typing.Optional[typing.Optional[str]] = Field(None, alias='memo')

    fixed_compensations: typing.Optional[PayrollEmployeeCompensationsTypeItemFixedCompensations] = Field(None, alias='fixed_compensations')

    hourly_compensations: typing.Optional[PayrollEmployeeCompensationsTypeItemHourlyCompensations] = Field(None, alias='hourly_compensations')

    paid_time_off: typing.Optional[PayrollEmployeeCompensationsTypeItemPaidTimeOff] = Field(None, alias='paid_time_off')

    benefits: typing.Optional[PayrollEmployeeCompensationsTypeItemBenefits] = Field(None, alias='benefits')

    deductions: typing.Optional[PayrollEmployeeCompensationsTypeItemDeductions] = Field(None, alias='deductions')

    taxes: typing.Optional[PayrollEmployeeCompensationsTypeItemTaxes] = Field(None, alias='taxes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
