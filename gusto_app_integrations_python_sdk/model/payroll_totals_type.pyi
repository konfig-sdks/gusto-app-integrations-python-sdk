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


class PayrollTotalsType(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The subtotals for the payroll.
    """


    class MetaOapg:
        
        class properties:
            company_debit = schemas.StrSchema
            
            
            class net_pay_debit(
                schemas.StrSchema
            ):
                pass
            tax_debit = schemas.StrSchema
            reimbursement_debit = schemas.StrSchema
            child_support_debit = schemas.StrSchema
            reimbursements = schemas.StrSchema
            net_pay = schemas.StrSchema
            gross_pay = schemas.StrSchema
            employee_bonuses = schemas.StrSchema
            employee_commissions = schemas.StrSchema
            employee_cash_tips = schemas.StrSchema
            employee_paycheck_tips = schemas.StrSchema
            additional_earnings = schemas.StrSchema
            owners_draw = schemas.StrSchema
            check_amount = schemas.StrSchema
            employer_taxes = schemas.StrSchema
            employee_taxes = schemas.StrSchema
            benefits = schemas.StrSchema
            employee_benefits_deductions = schemas.StrSchema
            deferred_payroll_taxes = schemas.StrSchema
            __annotations__ = {
                "company_debit": company_debit,
                "net_pay_debit": net_pay_debit,
                "tax_debit": tax_debit,
                "reimbursement_debit": reimbursement_debit,
                "child_support_debit": child_support_debit,
                "reimbursements": reimbursements,
                "net_pay": net_pay,
                "gross_pay": gross_pay,
                "employee_bonuses": employee_bonuses,
                "employee_commissions": employee_commissions,
                "employee_cash_tips": employee_cash_tips,
                "employee_paycheck_tips": employee_paycheck_tips,
                "additional_earnings": additional_earnings,
                "owners_draw": owners_draw,
                "check_amount": check_amount,
                "employer_taxes": employer_taxes,
                "employee_taxes": employee_taxes,
                "benefits": benefits,
                "employee_benefits_deductions": employee_benefits_deductions,
                "deferred_payroll_taxes": deferred_payroll_taxes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_debit"]) -> MetaOapg.properties.company_debit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["net_pay_debit"]) -> MetaOapg.properties.net_pay_debit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tax_debit"]) -> MetaOapg.properties.tax_debit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reimbursement_debit"]) -> MetaOapg.properties.reimbursement_debit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["child_support_debit"]) -> MetaOapg.properties.child_support_debit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reimbursements"]) -> MetaOapg.properties.reimbursements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["net_pay"]) -> MetaOapg.properties.net_pay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gross_pay"]) -> MetaOapg.properties.gross_pay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_bonuses"]) -> MetaOapg.properties.employee_bonuses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_commissions"]) -> MetaOapg.properties.employee_commissions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_cash_tips"]) -> MetaOapg.properties.employee_cash_tips: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_paycheck_tips"]) -> MetaOapg.properties.employee_paycheck_tips: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additional_earnings"]) -> MetaOapg.properties.additional_earnings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owners_draw"]) -> MetaOapg.properties.owners_draw: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["check_amount"]) -> MetaOapg.properties.check_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employer_taxes"]) -> MetaOapg.properties.employer_taxes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_taxes"]) -> MetaOapg.properties.employee_taxes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["benefits"]) -> MetaOapg.properties.benefits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_benefits_deductions"]) -> MetaOapg.properties.employee_benefits_deductions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deferred_payroll_taxes"]) -> MetaOapg.properties.deferred_payroll_taxes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["company_debit", "net_pay_debit", "tax_debit", "reimbursement_debit", "child_support_debit", "reimbursements", "net_pay", "gross_pay", "employee_bonuses", "employee_commissions", "employee_cash_tips", "employee_paycheck_tips", "additional_earnings", "owners_draw", "check_amount", "employer_taxes", "employee_taxes", "benefits", "employee_benefits_deductions", "deferred_payroll_taxes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_debit"]) -> typing.Union[MetaOapg.properties.company_debit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["net_pay_debit"]) -> typing.Union[MetaOapg.properties.net_pay_debit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tax_debit"]) -> typing.Union[MetaOapg.properties.tax_debit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reimbursement_debit"]) -> typing.Union[MetaOapg.properties.reimbursement_debit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["child_support_debit"]) -> typing.Union[MetaOapg.properties.child_support_debit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reimbursements"]) -> typing.Union[MetaOapg.properties.reimbursements, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["net_pay"]) -> typing.Union[MetaOapg.properties.net_pay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gross_pay"]) -> typing.Union[MetaOapg.properties.gross_pay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_bonuses"]) -> typing.Union[MetaOapg.properties.employee_bonuses, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_commissions"]) -> typing.Union[MetaOapg.properties.employee_commissions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_cash_tips"]) -> typing.Union[MetaOapg.properties.employee_cash_tips, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_paycheck_tips"]) -> typing.Union[MetaOapg.properties.employee_paycheck_tips, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additional_earnings"]) -> typing.Union[MetaOapg.properties.additional_earnings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owners_draw"]) -> typing.Union[MetaOapg.properties.owners_draw, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["check_amount"]) -> typing.Union[MetaOapg.properties.check_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employer_taxes"]) -> typing.Union[MetaOapg.properties.employer_taxes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_taxes"]) -> typing.Union[MetaOapg.properties.employee_taxes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["benefits"]) -> typing.Union[MetaOapg.properties.benefits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_benefits_deductions"]) -> typing.Union[MetaOapg.properties.employee_benefits_deductions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deferred_payroll_taxes"]) -> typing.Union[MetaOapg.properties.deferred_payroll_taxes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["company_debit", "net_pay_debit", "tax_debit", "reimbursement_debit", "child_support_debit", "reimbursements", "net_pay", "gross_pay", "employee_bonuses", "employee_commissions", "employee_cash_tips", "employee_paycheck_tips", "additional_earnings", "owners_draw", "check_amount", "employer_taxes", "employee_taxes", "benefits", "employee_benefits_deductions", "deferred_payroll_taxes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        company_debit: typing.Union[MetaOapg.properties.company_debit, str, schemas.Unset] = schemas.unset,
        net_pay_debit: typing.Union[MetaOapg.properties.net_pay_debit, str, schemas.Unset] = schemas.unset,
        tax_debit: typing.Union[MetaOapg.properties.tax_debit, str, schemas.Unset] = schemas.unset,
        reimbursement_debit: typing.Union[MetaOapg.properties.reimbursement_debit, str, schemas.Unset] = schemas.unset,
        child_support_debit: typing.Union[MetaOapg.properties.child_support_debit, str, schemas.Unset] = schemas.unset,
        reimbursements: typing.Union[MetaOapg.properties.reimbursements, str, schemas.Unset] = schemas.unset,
        net_pay: typing.Union[MetaOapg.properties.net_pay, str, schemas.Unset] = schemas.unset,
        gross_pay: typing.Union[MetaOapg.properties.gross_pay, str, schemas.Unset] = schemas.unset,
        employee_bonuses: typing.Union[MetaOapg.properties.employee_bonuses, str, schemas.Unset] = schemas.unset,
        employee_commissions: typing.Union[MetaOapg.properties.employee_commissions, str, schemas.Unset] = schemas.unset,
        employee_cash_tips: typing.Union[MetaOapg.properties.employee_cash_tips, str, schemas.Unset] = schemas.unset,
        employee_paycheck_tips: typing.Union[MetaOapg.properties.employee_paycheck_tips, str, schemas.Unset] = schemas.unset,
        additional_earnings: typing.Union[MetaOapg.properties.additional_earnings, str, schemas.Unset] = schemas.unset,
        owners_draw: typing.Union[MetaOapg.properties.owners_draw, str, schemas.Unset] = schemas.unset,
        check_amount: typing.Union[MetaOapg.properties.check_amount, str, schemas.Unset] = schemas.unset,
        employer_taxes: typing.Union[MetaOapg.properties.employer_taxes, str, schemas.Unset] = schemas.unset,
        employee_taxes: typing.Union[MetaOapg.properties.employee_taxes, str, schemas.Unset] = schemas.unset,
        benefits: typing.Union[MetaOapg.properties.benefits, str, schemas.Unset] = schemas.unset,
        employee_benefits_deductions: typing.Union[MetaOapg.properties.employee_benefits_deductions, str, schemas.Unset] = schemas.unset,
        deferred_payroll_taxes: typing.Union[MetaOapg.properties.deferred_payroll_taxes, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayrollTotalsType':
        return super().__new__(
            cls,
            *args,
            company_debit=company_debit,
            net_pay_debit=net_pay_debit,
            tax_debit=tax_debit,
            reimbursement_debit=reimbursement_debit,
            child_support_debit=child_support_debit,
            reimbursements=reimbursements,
            net_pay=net_pay,
            gross_pay=gross_pay,
            employee_bonuses=employee_bonuses,
            employee_commissions=employee_commissions,
            employee_cash_tips=employee_cash_tips,
            employee_paycheck_tips=employee_paycheck_tips,
            additional_earnings=additional_earnings,
            owners_draw=owners_draw,
            check_amount=check_amount,
            employer_taxes=employer_taxes,
            employee_taxes=employee_taxes,
            benefits=benefits,
            employee_benefits_deductions=employee_benefits_deductions,
            deferred_payroll_taxes=deferred_payroll_taxes,
            _configuration=_configuration,
            **kwargs,
        )
