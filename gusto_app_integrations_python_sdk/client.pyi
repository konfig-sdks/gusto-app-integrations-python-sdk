# coding: utf-8
"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from gusto_app_integrations_python_sdk.client_custom import ClientCustom
from gusto_app_integrations_python_sdk.configuration import Configuration
from gusto_app_integrations_python_sdk.api_client import ApiClient
from gusto_app_integrations_python_sdk.type_util import copy_signature
from gusto_app_integrations_python_sdk.apis.tags.companies_api import CompaniesApi
from gusto_app_integrations_python_sdk.apis.tags.company_benefits_api import CompanyBenefitsApi
from gusto_app_integrations_python_sdk.apis.tags.contractor_payments_api import ContractorPaymentsApi
from gusto_app_integrations_python_sdk.apis.tags.contractors_api import ContractorsApi
from gusto_app_integrations_python_sdk.apis.tags.departments_api import DepartmentsApi
from gusto_app_integrations_python_sdk.apis.tags.earning_types_api import EarningTypesApi
from gusto_app_integrations_python_sdk.apis.tags.employee_addresses_api import EmployeeAddressesApi
from gusto_app_integrations_python_sdk.apis.tags.employee_benefits_api import EmployeeBenefitsApi
from gusto_app_integrations_python_sdk.apis.tags.employee_employments_api import EmployeeEmploymentsApi
from gusto_app_integrations_python_sdk.apis.tags.employees_api import EmployeesApi
from gusto_app_integrations_python_sdk.apis.tags.events_api import EventsApi
from gusto_app_integrations_python_sdk.apis.tags.garnishments_api import GarnishmentsApi
from gusto_app_integrations_python_sdk.apis.tags.introspection_api import IntrospectionApi
from gusto_app_integrations_python_sdk.apis.tags.jobs_and_compensations_api import JobsAndCompensationsApi
from gusto_app_integrations_python_sdk.apis.tags.locations_api import LocationsApi
from gusto_app_integrations_python_sdk.apis.tags.pay_schedules_api import PaySchedulesApi
from gusto_app_integrations_python_sdk.apis.tags.payrolls_api import PayrollsApi
from gusto_app_integrations_python_sdk.apis.tags.time_off_policies_api import TimeOffPoliciesApi
from gusto_app_integrations_python_sdk.apis.tags.webhooks_api import WebhooksApi



class GustoAppIntegrations(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.companies: CompaniesApi = CompaniesApi(api_client)
        self.company_benefits: CompanyBenefitsApi = CompanyBenefitsApi(api_client)
        self.contractor_payments: ContractorPaymentsApi = ContractorPaymentsApi(api_client)
        self.contractors: ContractorsApi = ContractorsApi(api_client)
        self.departments: DepartmentsApi = DepartmentsApi(api_client)
        self.earning_types: EarningTypesApi = EarningTypesApi(api_client)
        self.employee_addresses: EmployeeAddressesApi = EmployeeAddressesApi(api_client)
        self.employee_benefits: EmployeeBenefitsApi = EmployeeBenefitsApi(api_client)
        self.employee_employments: EmployeeEmploymentsApi = EmployeeEmploymentsApi(api_client)
        self.employees: EmployeesApi = EmployeesApi(api_client)
        self.events: EventsApi = EventsApi(api_client)
        self.garnishments: GarnishmentsApi = GarnishmentsApi(api_client)
        self.introspection: IntrospectionApi = IntrospectionApi(api_client)
        self.jobs_and_compensations: JobsAndCompensationsApi = JobsAndCompensationsApi(api_client)
        self.locations: LocationsApi = LocationsApi(api_client)
        self.pay_schedules: PaySchedulesApi = PaySchedulesApi(api_client)
        self.payrolls: PayrollsApi = PayrollsApi(api_client)
        self.time_off_policies: TimeOffPoliciesApi = TimeOffPoliciesApi(api_client)
        self.webhooks: WebhooksApi = WebhooksApi(api_client)
