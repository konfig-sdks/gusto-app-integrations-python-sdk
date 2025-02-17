# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_app_integrations_python_sdk.paths.v1_employees_employee_id_employee_benefits.post import CreateBenefitRaw
from gusto_app_integrations_python_sdk.paths.v1_employees_employee_id_ytd_benefit_amounts_from_different_company.post import CreateYtdBenefitAmountsFromDifferentCompanyRaw
from gusto_app_integrations_python_sdk.paths.v1_employees_employee_id_employee_benefits.get import GetAllForEmployeeRaw
from gusto_app_integrations_python_sdk.paths.v1_employee_benefits_employee_benefit_id.get import GetByIdRaw
from gusto_app_integrations_python_sdk.paths.v1_employee_benefits_employee_benefit_id.delete import RemoveBenefitRaw
from gusto_app_integrations_python_sdk.paths.v1_employee_benefits_employee_benefit_id.put import UpdateBenefitRaw


class EmployeeBenefitsApiRaw(
    CreateBenefitRaw,
    CreateYtdBenefitAmountsFromDifferentCompanyRaw,
    GetAllForEmployeeRaw,
    GetByIdRaw,
    RemoveBenefitRaw,
    UpdateBenefitRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
