import typing_extensions

from gusto_app_integrations_python_sdk.apis.tags import TagValues
from gusto_app_integrations_python_sdk.apis.tags.employee_addresses_api import EmployeeAddressesApi
from gusto_app_integrations_python_sdk.apis.tags.jobs_and_compensations_api import JobsAndCompensationsApi
from gusto_app_integrations_python_sdk.apis.tags.employee_employments_api import EmployeeEmploymentsApi
from gusto_app_integrations_python_sdk.apis.tags.company_benefits_api import CompanyBenefitsApi
from gusto_app_integrations_python_sdk.apis.tags.employees_api import EmployeesApi
from gusto_app_integrations_python_sdk.apis.tags.departments_api import DepartmentsApi
from gusto_app_integrations_python_sdk.apis.tags.webhooks_api import WebhooksApi
from gusto_app_integrations_python_sdk.apis.tags.employee_benefits_api import EmployeeBenefitsApi
from gusto_app_integrations_python_sdk.apis.tags.locations_api import LocationsApi
from gusto_app_integrations_python_sdk.apis.tags.pay_schedules_api import PaySchedulesApi
from gusto_app_integrations_python_sdk.apis.tags.earning_types_api import EarningTypesApi
from gusto_app_integrations_python_sdk.apis.tags.contractors_api import ContractorsApi
from gusto_app_integrations_python_sdk.apis.tags.payrolls_api import PayrollsApi
from gusto_app_integrations_python_sdk.apis.tags.garnishments_api import GarnishmentsApi
from gusto_app_integrations_python_sdk.apis.tags.companies_api import CompaniesApi
from gusto_app_integrations_python_sdk.apis.tags.introspection_api import IntrospectionApi
from gusto_app_integrations_python_sdk.apis.tags.contractor_payments_api import ContractorPaymentsApi
from gusto_app_integrations_python_sdk.apis.tags.time_off_policies_api import TimeOffPoliciesApi
from gusto_app_integrations_python_sdk.apis.tags.events_api import EventsApi
from gusto_app_integrations_python_sdk.apis.tags.flows_api import FlowsApi
from gusto_app_integrations_python_sdk.apis.tags.bank_accounts_api import BankAccountsApi
from gusto_app_integrations_python_sdk.apis.tags.payment_configs_api import PaymentConfigsApi
from gusto_app_integrations_python_sdk.apis.tags.employee_tax_setup_api import EmployeeTaxSetupApi
from gusto_app_integrations_python_sdk.apis.tags.employee_payment_method_api import EmployeePaymentMethodApi
from gusto_app_integrations_python_sdk.apis.tags.contractor_payment_method_api import ContractorPaymentMethodApi
from gusto_app_integrations_python_sdk.apis.tags.company_forms_api import CompanyFormsApi
from gusto_app_integrations_python_sdk.apis.tags.employee_forms_api import EmployeeFormsApi
from gusto_app_integrations_python_sdk.apis.tags.federal_tax_details_api import FederalTaxDetailsApi
from gusto_app_integrations_python_sdk.apis.tags.industry_selection_api import IndustrySelectionApi
from gusto_app_integrations_python_sdk.apis.tags.signatories_api import SignatoriesApi
from gusto_app_integrations_python_sdk.apis.tags.external_payrolls_api import ExternalPayrollsApi
from gusto_app_integrations_python_sdk.apis.tags.tax_requirements_api import TaxRequirementsApi
from gusto_app_integrations_python_sdk.apis.tags.contractor_forms_api import ContractorFormsApi
from gusto_app_integrations_python_sdk.apis.tags.holiday_pay_policies_api import HolidayPayPoliciesApi
from gusto_app_integrations_python_sdk.apis.tags.generated_documents_api import GeneratedDocumentsApi
from gusto_app_integrations_python_sdk.apis.tags.notifications_api import NotificationsApi
from gusto_app_integrations_python_sdk.apis.tags.invoices_api import InvoicesApi
from gusto_app_integrations_python_sdk.apis.tags.recovery_cases_api import RecoveryCasesApi
from gusto_app_integrations_python_sdk.apis.tags.ach_transactions_api import ACHTransactionsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EMPLOYEE_ADDRESSES: EmployeeAddressesApi,
        TagValues.JOBS_AND_COMPENSATIONS: JobsAndCompensationsApi,
        TagValues.EMPLOYEE_EMPLOYMENTS: EmployeeEmploymentsApi,
        TagValues.COMPANY_BENEFITS: CompanyBenefitsApi,
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.EMPLOYEE_BENEFITS: EmployeeBenefitsApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.PAY_SCHEDULES: PaySchedulesApi,
        TagValues.EARNING_TYPES: EarningTypesApi,
        TagValues.CONTRACTORS: ContractorsApi,
        TagValues.PAYROLLS: PayrollsApi,
        TagValues.GARNISHMENTS: GarnishmentsApi,
        TagValues.COMPANIES: CompaniesApi,
        TagValues.INTROSPECTION: IntrospectionApi,
        TagValues.CONTRACTOR_PAYMENTS: ContractorPaymentsApi,
        TagValues.TIME_OFF_POLICIES: TimeOffPoliciesApi,
        TagValues.EVENTS: EventsApi,
        TagValues.FLOWS: FlowsApi,
        TagValues.BANK_ACCOUNTS: BankAccountsApi,
        TagValues.PAYMENT_CONFIGS: PaymentConfigsApi,
        TagValues.EMPLOYEE_TAX_SETUP: EmployeeTaxSetupApi,
        TagValues.EMPLOYEE_PAYMENT_METHOD: EmployeePaymentMethodApi,
        TagValues.CONTRACTOR_PAYMENT_METHOD: ContractorPaymentMethodApi,
        TagValues.COMPANY_FORMS: CompanyFormsApi,
        TagValues.EMPLOYEE_FORMS: EmployeeFormsApi,
        TagValues.FEDERAL_TAX_DETAILS: FederalTaxDetailsApi,
        TagValues.INDUSTRY_SELECTION: IndustrySelectionApi,
        TagValues.SIGNATORIES: SignatoriesApi,
        TagValues.EXTERNAL_PAYROLLS: ExternalPayrollsApi,
        TagValues.TAX_REQUIREMENTS: TaxRequirementsApi,
        TagValues.CONTRACTOR_FORMS: ContractorFormsApi,
        TagValues.HOLIDAY_PAY_POLICIES: HolidayPayPoliciesApi,
        TagValues.GENERATED_DOCUMENTS: GeneratedDocumentsApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.INVOICES: InvoicesApi,
        TagValues.RECOVERY_CASES: RecoveryCasesApi,
        TagValues.ACH_TRANSACTIONS: ACHTransactionsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EMPLOYEE_ADDRESSES: EmployeeAddressesApi,
        TagValues.JOBS_AND_COMPENSATIONS: JobsAndCompensationsApi,
        TagValues.EMPLOYEE_EMPLOYMENTS: EmployeeEmploymentsApi,
        TagValues.COMPANY_BENEFITS: CompanyBenefitsApi,
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.EMPLOYEE_BENEFITS: EmployeeBenefitsApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.PAY_SCHEDULES: PaySchedulesApi,
        TagValues.EARNING_TYPES: EarningTypesApi,
        TagValues.CONTRACTORS: ContractorsApi,
        TagValues.PAYROLLS: PayrollsApi,
        TagValues.GARNISHMENTS: GarnishmentsApi,
        TagValues.COMPANIES: CompaniesApi,
        TagValues.INTROSPECTION: IntrospectionApi,
        TagValues.CONTRACTOR_PAYMENTS: ContractorPaymentsApi,
        TagValues.TIME_OFF_POLICIES: TimeOffPoliciesApi,
        TagValues.EVENTS: EventsApi,
        TagValues.FLOWS: FlowsApi,
        TagValues.BANK_ACCOUNTS: BankAccountsApi,
        TagValues.PAYMENT_CONFIGS: PaymentConfigsApi,
        TagValues.EMPLOYEE_TAX_SETUP: EmployeeTaxSetupApi,
        TagValues.EMPLOYEE_PAYMENT_METHOD: EmployeePaymentMethodApi,
        TagValues.CONTRACTOR_PAYMENT_METHOD: ContractorPaymentMethodApi,
        TagValues.COMPANY_FORMS: CompanyFormsApi,
        TagValues.EMPLOYEE_FORMS: EmployeeFormsApi,
        TagValues.FEDERAL_TAX_DETAILS: FederalTaxDetailsApi,
        TagValues.INDUSTRY_SELECTION: IndustrySelectionApi,
        TagValues.SIGNATORIES: SignatoriesApi,
        TagValues.EXTERNAL_PAYROLLS: ExternalPayrollsApi,
        TagValues.TAX_REQUIREMENTS: TaxRequirementsApi,
        TagValues.CONTRACTOR_FORMS: ContractorFormsApi,
        TagValues.HOLIDAY_PAY_POLICIES: HolidayPayPoliciesApi,
        TagValues.GENERATED_DOCUMENTS: GeneratedDocumentsApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.INVOICES: InvoicesApi,
        TagValues.RECOVERY_CASES: RecoveryCasesApi,
        TagValues.ACH_TRANSACTIONS: ACHTransactionsApi,
    }
)
