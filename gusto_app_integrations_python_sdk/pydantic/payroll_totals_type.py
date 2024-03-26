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


class PayrollTotalsType(BaseModel):
    # The total company debit for the payroll.
    company_debit: typing.Optional[str] = Field(None, alias='company_debit')

    # The total company net pay for the payroll.
    net_pay_debit: typing.Optional[str] = Field(None, alias='net_pay_debit')

    # The total tax debit for the payroll.
    tax_debit: typing.Optional[str] = Field(None, alias='tax_debit')

    # The total reimbursement debit for the payroll.
    reimbursement_debit: typing.Optional[str] = Field(None, alias='reimbursement_debit')

    # The total child support debit for the payroll.
    child_support_debit: typing.Optional[str] = Field(None, alias='child_support_debit')

    # The total reimbursements for the payroll.
    reimbursements: typing.Optional[str] = Field(None, alias='reimbursements')

    # The net pay amount for the payroll.
    net_pay: typing.Optional[str] = Field(None, alias='net_pay')

    # The gross pay amount for the payroll.
    gross_pay: typing.Optional[str] = Field(None, alias='gross_pay')

    # The total employee bonuses amount for the payroll.
    employee_bonuses: typing.Optional[str] = Field(None, alias='employee_bonuses')

    # The total employee commissions amount for the payroll.
    employee_commissions: typing.Optional[str] = Field(None, alias='employee_commissions')

    # The total employee cash tips amount for the payroll.
    employee_cash_tips: typing.Optional[str] = Field(None, alias='employee_cash_tips')

    # The total employee paycheck tips amount for the payroll.
    employee_paycheck_tips: typing.Optional[str] = Field(None, alias='employee_paycheck_tips')

    # The total additional earnings amount for the payroll.
    additional_earnings: typing.Optional[str] = Field(None, alias='additional_earnings')

    # The total owner's draw for the payroll.
    owners_draw: typing.Optional[str] = Field(None, alias='owners_draw')

    # The total check amount for the payroll.
    check_amount: typing.Optional[str] = Field(None, alias='check_amount')

    # The total amount of employer paid taxes for the payroll.
    employer_taxes: typing.Optional[str] = Field(None, alias='employer_taxes')

    # The total amount of employee paid taxes for the payroll.
    employee_taxes: typing.Optional[str] = Field(None, alias='employee_taxes')

    # The total amount of company contributed benefits for the payroll.
    benefits: typing.Optional[str] = Field(None, alias='benefits')

    # The total amount of employee deducted benefits for the payroll.
    employee_benefits_deductions: typing.Optional[str] = Field(None, alias='employee_benefits_deductions')

    # The total amount of payroll taxes deferred for the payroll, such as allowed by the CARES act.
    deferred_payroll_taxes: typing.Optional[str] = Field(None, alias='deferred_payroll_taxes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
