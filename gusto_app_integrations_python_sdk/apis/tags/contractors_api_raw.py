# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_app_integrations_python_sdk.paths.v1_companies_company_id_contractors.post import CreateIndividualOrBusinessRaw
from gusto_app_integrations_python_sdk.paths.v1_companies_company_id_contractors.get import GetAllRaw
from gusto_app_integrations_python_sdk.paths.v1_contractors_contractor_id.get import GetDetailsRaw
from gusto_app_integrations_python_sdk.paths.v1_contractors_contractor_id.put import UpdateContractorRaw


class ContractorsApiRaw(
    CreateIndividualOrBusinessRaw,
    GetAllRaw,
    GetDetailsRaw,
    UpdateContractorRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
