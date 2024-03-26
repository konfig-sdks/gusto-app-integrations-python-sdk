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

from gusto_app_integrations_python_sdk.type.off_cycle_reason_type import OffCycleReasonType
from gusto_app_integrations_python_sdk.type.payroll_employee_compensations_type import PayrollEmployeeCompensationsType
from gusto_app_integrations_python_sdk.type.payroll_fixed_compensation_types_type import PayrollFixedCompensationTypesType
from gusto_app_integrations_python_sdk.type.payroll_pay_period_type import PayrollPayPeriodType
from gusto_app_integrations_python_sdk.type.payroll_payment_speed_changed_type import PayrollPaymentSpeedChangedType
from gusto_app_integrations_python_sdk.type.payroll_payroll_status_meta_type import PayrollPayrollStatusMetaType
from gusto_app_integrations_python_sdk.type.payroll_withholding_pay_period_type import PayrollWithholdingPayPeriodType

class RequiredPayrollPrepared(TypedDict):
    pass

class OptionalPayrollPrepared(TypedDict, total=False):
    # A timestamp that is the deadline for the payroll to be run in order for employees to be paid on time.
    payroll_deadline: datetime

    # The date on which employees will be paid for the payroll.
    check_date: str

    # Whether or not the payroll has been successfully processed. Note that processed payrolls cannot be updated. Additionally, a payroll is not guaranteed to be processed just because the payroll deadline has passed. Late payrolls are not uncommon. Conversely, users may choose to run payroll before the payroll deadline.
    processed: bool

    # The date at which the payroll was processed. Null if the payroll isn't processed yet.
    processed_date: str

    # A timestamp of the last valid payroll calculation. Null is there isn't a valid calculation.
    calculated_at: str

    # The UUID of the payroll.
    payroll_uuid: str

    # The UUID of the company for the payroll.
    company_uuid: str

    # Indicates whether the payroll is an off-cycle payroll
    off_cycle: bool

    off_cycle_reason: typing.Optional[OffCycleReasonType]

    # Indicates whether the payroll is an external payroll
    external: bool

    # Indicates whether the payroll is the final payroll for a terminated employee. Only included for off-cycle payrolls.
    final_termination_payroll: bool

    withholding_pay_period: PayrollWithholdingPayPeriodType

    # Block regular deductions and contributions for this payroll.  Only included for off-cycle payrolls.
    skip_regular_deductions: bool

    # Enable taxes to be withheld at the IRS's required rate of 22% for federal income taxes. State income taxes will be taxed at the state's supplemental tax rate. Otherwise, we'll sum the entirety of the employee's wages and withhold taxes on the entire amount at the rate for regular wages. Only included for off-cycle payrolls.
    fixed_withholding_rate: bool

    pay_period: PayrollPayPeriodType

    payroll_status_meta: PayrollPayrollStatusMetaType

    employee_compensations: PayrollEmployeeCompensationsType

    payment_speed_changed: PayrollPaymentSpeedChangedType

    # Datetime for when the resource was created.
    created_at: datetime

    fixed_compensation_types: PayrollFixedCompensationTypesType

class PayrollPrepared(RequiredPayrollPrepared, OptionalPayrollPrepared):
    pass
