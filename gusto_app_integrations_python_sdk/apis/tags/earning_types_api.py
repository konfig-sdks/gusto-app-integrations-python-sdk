# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_app_integrations_python_sdk.paths.v1_companies_company_id_earning_types.post import CreateCustomEarningType
from gusto_app_integrations_python_sdk.paths.v1_companies_company_id_earning_types_earning_type_uuid.delete import Deactivate
from gusto_app_integrations_python_sdk.paths.v1_companies_company_id_earning_types.get import GetAll
from gusto_app_integrations_python_sdk.paths.v1_companies_company_id_earning_types_earning_type_uuid.put import UpdateTypeById
from gusto_app_integrations_python_sdk.apis.tags.earning_types_api_raw import EarningTypesApiRaw


class EarningTypesApi(
    CreateCustomEarningType,
    Deactivate,
    GetAll,
    UpdateTypeById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EarningTypesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EarningTypesApiRaw(api_client)
