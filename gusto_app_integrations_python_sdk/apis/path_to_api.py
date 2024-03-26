import typing_extensions

from gusto_app_integrations_python_sdk.paths import PathValues
from gusto_app_integrations_python_sdk.apis.paths.v1_token_info import V1TokenInfo
from gusto_app_integrations_python_sdk.apis.paths.oauth_token import OauthToken
from gusto_app_integrations_python_sdk.apis.paths.v1_provision import V1Provision
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id import V1CompaniesCompanyId
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_custom_fields import V1CompaniesCompanyIdCustomFields
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_locations import V1CompaniesCompanyIdLocations
from gusto_app_integrations_python_sdk.apis.paths.v1_locations_location_id import V1LocationsLocationId
from gusto_app_integrations_python_sdk.apis.paths.v1_locations_location_uuid_minimum_wages import V1LocationsLocationUuidMinimumWages
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_pay_schedules import V1CompaniesCompanyIdPaySchedules
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_pay_schedules_pay_schedule_id import V1CompaniesCompanyIdPaySchedulesPayScheduleId
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_pay_periods import V1CompaniesCompanyIdPayPeriods
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_pay_periods_unprocessed_termination_pay_periods import V1CompaniesCompanyIdPayPeriodsUnprocessedTerminationPayPeriods
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_pay_schedules_assignments import V1CompaniesCompanyIdPaySchedulesAssignments
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_employees import V1CompaniesCompanyIdEmployees
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_uuid_departments import V1CompaniesCompanyUuidDepartments
from gusto_app_integrations_python_sdk.apis.paths.v1_departments_department_uuid import V1DepartmentsDepartmentUuid
from gusto_app_integrations_python_sdk.apis.paths.v1_departments_department_uuid_add import V1DepartmentsDepartmentUuidAdd
from gusto_app_integrations_python_sdk.apis.paths.v1_departments_department_uuid_remove import V1DepartmentsDepartmentUuidRemove
from gusto_app_integrations_python_sdk.apis.paths.v1_employees_employee_id import V1EmployeesEmployeeId
from gusto_app_integrations_python_sdk.apis.paths.v1_employees_employee_id_terminations import V1EmployeesEmployeeIdTerminations
from gusto_app_integrations_python_sdk.apis.paths.v1_terminations_employee_id import V1TerminationsEmployeeId
from gusto_app_integrations_python_sdk.apis.paths.v1_employees_employee_id_rehire import V1EmployeesEmployeeIdRehire
from gusto_app_integrations_python_sdk.apis.paths.v1_employees_employee_id_employment_history import V1EmployeesEmployeeIdEmploymentHistory
from gusto_app_integrations_python_sdk.apis.paths.v1_employees_employee_id_home_addresses import V1EmployeesEmployeeIdHomeAddresses
from gusto_app_integrations_python_sdk.apis.paths.v1_home_addresses_home_address_uuid import V1HomeAddressesHomeAddressUuid
from gusto_app_integrations_python_sdk.apis.paths.v1_employees_employee_id_work_addresses import V1EmployeesEmployeeIdWorkAddresses
from gusto_app_integrations_python_sdk.apis.paths.v1_work_addresses_work_address_uuid import V1WorkAddressesWorkAddressUuid
from gusto_app_integrations_python_sdk.apis.paths.v1_employees_employee_id_custom_fields import V1EmployeesEmployeeIdCustomFields
from gusto_app_integrations_python_sdk.apis.paths.v1_employees_employee_id_jobs import V1EmployeesEmployeeIdJobs
from gusto_app_integrations_python_sdk.apis.paths.v1_employees_employee_uuid_time_off_activities import V1EmployeesEmployeeUuidTimeOffActivities
from gusto_app_integrations_python_sdk.apis.paths.v1_jobs_job_id import V1JobsJobId
from gusto_app_integrations_python_sdk.apis.paths.v1_jobs_job_id_compensations import V1JobsJobIdCompensations
from gusto_app_integrations_python_sdk.apis.paths.v1_compensations_compensation_id import V1CompensationsCompensationId
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_earning_types import V1CompaniesCompanyIdEarningTypes
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_earning_types_earning_type_uuid import V1CompaniesCompanyIdEarningTypesEarningTypeUuid
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_contractors import V1CompaniesCompanyIdContractors
from gusto_app_integrations_python_sdk.apis.paths.v1_contractors_contractor_id import V1ContractorsContractorId
from gusto_app_integrations_python_sdk.apis.paths.v1_webhook_subscriptions import V1WebhookSubscriptions
from gusto_app_integrations_python_sdk.apis.paths.v1_webhook_subscriptions_webhook_subscription_uuid import V1WebhookSubscriptionsWebhookSubscriptionUuid
from gusto_app_integrations_python_sdk.apis.paths.v1_webhook_subscriptions_webhook_subscription_uuid_verify import V1WebhookSubscriptionsWebhookSubscriptionUuidVerify
from gusto_app_integrations_python_sdk.apis.paths.v1_webhook_subscriptions_webhook_subscription_uuid_request_verification_token import V1WebhookSubscriptionsWebhookSubscriptionUuidRequestVerificationToken
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_payrolls import V1CompaniesCompanyIdPayrolls
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_payrolls_payroll_id import V1CompaniesCompanyIdPayrollsPayrollId
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_payrolls_payroll_id_prepare import V1CompaniesCompanyIdPayrollsPayrollIdPrepare
from gusto_app_integrations_python_sdk.apis.paths.v1_payrolls_payroll_id_employees_employee_id_calculate_accruing_time_off_hours import V1PayrollsPayrollIdEmployeesEmployeeIdCalculateAccruingTimeOffHours
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_contractor_payments import V1CompaniesCompanyIdContractorPayments
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_contractor_payments_contractor_payment_id import V1CompaniesCompanyIdContractorPaymentsContractorPaymentId
from gusto_app_integrations_python_sdk.apis.paths.v1_companies_company_id_company_benefits import V1CompaniesCompanyIdCompanyBenefits
from gusto_app_integrations_python_sdk.apis.paths.v1_company_benefits_company_benefit_id import V1CompanyBenefitsCompanyBenefitId
from gusto_app_integrations_python_sdk.apis.paths.v1_benefits import V1Benefits
from gusto_app_integrations_python_sdk.apis.paths.v1_benefits_benefit_id import V1BenefitsBenefitId
from gusto_app_integrations_python_sdk.apis.paths.v1_company_benefits_company_benefit_id_summary import V1CompanyBenefitsCompanyBenefitIdSummary
from gusto_app_integrations_python_sdk.apis.paths.v1_benefits_benefit_id_requirements import V1BenefitsBenefitIdRequirements
from gusto_app_integrations_python_sdk.apis.paths.v1_employees_employee_id_employee_benefits import V1EmployeesEmployeeIdEmployeeBenefits
from gusto_app_integrations_python_sdk.apis.paths.v1_employee_benefits_employee_benefit_id import V1EmployeeBenefitsEmployeeBenefitId
from gusto_app_integrations_python_sdk.apis.paths.v1_employees_employee_id_ytd_benefit_amounts_from_different_company import V1EmployeesEmployeeIdYtdBenefitAmountsFromDifferentCompany
from gusto_app_integrations_python_sdk.apis.paths.v1_employees_employee_id_garnishments import V1EmployeesEmployeeIdGarnishments
from gusto_app_integrations_python_sdk.apis.paths.v1_garnishments_garnishment_id import V1GarnishmentsGarnishmentId
from gusto_app_integrations_python_sdk.apis.paths.v1_events import V1Events

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_TOKEN_INFO: V1TokenInfo,
        PathValues.OAUTH_TOKEN: OauthToken,
        PathValues.V1_PROVISION: V1Provision,
        PathValues.V1_COMPANIES_COMPANY_ID: V1CompaniesCompanyId,
        PathValues.V1_COMPANIES_COMPANY_ID_CUSTOM_FIELDS: V1CompaniesCompanyIdCustomFields,
        PathValues.V1_COMPANIES_COMPANY_ID_LOCATIONS: V1CompaniesCompanyIdLocations,
        PathValues.V1_LOCATIONS_LOCATION_ID: V1LocationsLocationId,
        PathValues.V1_LOCATIONS_LOCATION_UUID_MINIMUM_WAGES: V1LocationsLocationUuidMinimumWages,
        PathValues.V1_COMPANIES_COMPANY_ID_PAY_SCHEDULES: V1CompaniesCompanyIdPaySchedules,
        PathValues.V1_COMPANIES_COMPANY_ID_PAY_SCHEDULES_PAY_SCHEDULE_ID: V1CompaniesCompanyIdPaySchedulesPayScheduleId,
        PathValues.V1_COMPANIES_COMPANY_ID_PAY_PERIODS: V1CompaniesCompanyIdPayPeriods,
        PathValues.V1_COMPANIES_COMPANY_ID_PAY_PERIODS_UNPROCESSED_TERMINATION_PAY_PERIODS: V1CompaniesCompanyIdPayPeriodsUnprocessedTerminationPayPeriods,
        PathValues.V1_COMPANIES_COMPANY_ID_PAY_SCHEDULES_ASSIGNMENTS: V1CompaniesCompanyIdPaySchedulesAssignments,
        PathValues.V1_COMPANIES_COMPANY_ID_EMPLOYEES: V1CompaniesCompanyIdEmployees,
        PathValues.V1_COMPANIES_COMPANY_UUID_DEPARTMENTS: V1CompaniesCompanyUuidDepartments,
        PathValues.V1_DEPARTMENTS_DEPARTMENT_UUID: V1DepartmentsDepartmentUuid,
        PathValues.V1_DEPARTMENTS_DEPARTMENT_UUID_ADD: V1DepartmentsDepartmentUuidAdd,
        PathValues.V1_DEPARTMENTS_DEPARTMENT_UUID_REMOVE: V1DepartmentsDepartmentUuidRemove,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID: V1EmployeesEmployeeId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_TERMINATIONS: V1EmployeesEmployeeIdTerminations,
        PathValues.V1_TERMINATIONS_EMPLOYEE_ID: V1TerminationsEmployeeId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_REHIRE: V1EmployeesEmployeeIdRehire,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_EMPLOYMENT_HISTORY: V1EmployeesEmployeeIdEmploymentHistory,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_HOME_ADDRESSES: V1EmployeesEmployeeIdHomeAddresses,
        PathValues.V1_HOME_ADDRESSES_HOME_ADDRESS_UUID: V1HomeAddressesHomeAddressUuid,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_WORK_ADDRESSES: V1EmployeesEmployeeIdWorkAddresses,
        PathValues.V1_WORK_ADDRESSES_WORK_ADDRESS_UUID: V1WorkAddressesWorkAddressUuid,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_CUSTOM_FIELDS: V1EmployeesEmployeeIdCustomFields,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_JOBS: V1EmployeesEmployeeIdJobs,
        PathValues.V1_EMPLOYEES_EMPLOYEE_UUID_TIME_OFF_ACTIVITIES: V1EmployeesEmployeeUuidTimeOffActivities,
        PathValues.V1_JOBS_JOB_ID: V1JobsJobId,
        PathValues.V1_JOBS_JOB_ID_COMPENSATIONS: V1JobsJobIdCompensations,
        PathValues.V1_COMPENSATIONS_COMPENSATION_ID: V1CompensationsCompensationId,
        PathValues.V1_COMPANIES_COMPANY_ID_EARNING_TYPES: V1CompaniesCompanyIdEarningTypes,
        PathValues.V1_COMPANIES_COMPANY_ID_EARNING_TYPES_EARNING_TYPE_UUID: V1CompaniesCompanyIdEarningTypesEarningTypeUuid,
        PathValues.V1_COMPANIES_COMPANY_ID_CONTRACTORS: V1CompaniesCompanyIdContractors,
        PathValues.V1_CONTRACTORS_CONTRACTOR_ID: V1ContractorsContractorId,
        PathValues.V1_WEBHOOK_SUBSCRIPTIONS: V1WebhookSubscriptions,
        PathValues.V1_WEBHOOK_SUBSCRIPTIONS_WEBHOOK_SUBSCRIPTION_UUID: V1WebhookSubscriptionsWebhookSubscriptionUuid,
        PathValues.V1_WEBHOOK_SUBSCRIPTIONS_WEBHOOK_SUBSCRIPTION_UUID_VERIFY: V1WebhookSubscriptionsWebhookSubscriptionUuidVerify,
        PathValues.V1_WEBHOOK_SUBSCRIPTIONS_WEBHOOK_SUBSCRIPTION_UUID_REQUEST_VERIFICATION_TOKEN: V1WebhookSubscriptionsWebhookSubscriptionUuidRequestVerificationToken,
        PathValues.V1_COMPANIES_COMPANY_ID_PAYROLLS: V1CompaniesCompanyIdPayrolls,
        PathValues.V1_COMPANIES_COMPANY_ID_PAYROLLS_PAYROLL_ID: V1CompaniesCompanyIdPayrollsPayrollId,
        PathValues.V1_COMPANIES_COMPANY_ID_PAYROLLS_PAYROLL_ID_PREPARE: V1CompaniesCompanyIdPayrollsPayrollIdPrepare,
        PathValues.V1_PAYROLLS_PAYROLL_ID_EMPLOYEES_EMPLOYEE_ID_CALCULATE_ACCRUING_TIME_OFF_HOURS: V1PayrollsPayrollIdEmployeesEmployeeIdCalculateAccruingTimeOffHours,
        PathValues.V1_COMPANIES_COMPANY_ID_CONTRACTOR_PAYMENTS: V1CompaniesCompanyIdContractorPayments,
        PathValues.V1_COMPANIES_COMPANY_ID_CONTRACTOR_PAYMENTS_CONTRACTOR_PAYMENT_ID: V1CompaniesCompanyIdContractorPaymentsContractorPaymentId,
        PathValues.V1_COMPANIES_COMPANY_ID_COMPANY_BENEFITS: V1CompaniesCompanyIdCompanyBenefits,
        PathValues.V1_COMPANY_BENEFITS_COMPANY_BENEFIT_ID: V1CompanyBenefitsCompanyBenefitId,
        PathValues.V1_BENEFITS: V1Benefits,
        PathValues.V1_BENEFITS_BENEFIT_ID: V1BenefitsBenefitId,
        PathValues.V1_COMPANY_BENEFITS_COMPANY_BENEFIT_ID_SUMMARY: V1CompanyBenefitsCompanyBenefitIdSummary,
        PathValues.V1_BENEFITS_BENEFIT_ID_REQUIREMENTS: V1BenefitsBenefitIdRequirements,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_EMPLOYEE_BENEFITS: V1EmployeesEmployeeIdEmployeeBenefits,
        PathValues.V1_EMPLOYEE_BENEFITS_EMPLOYEE_BENEFIT_ID: V1EmployeeBenefitsEmployeeBenefitId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_YTD_BENEFIT_AMOUNTS_FROM_DIFFERENT_COMPANY: V1EmployeesEmployeeIdYtdBenefitAmountsFromDifferentCompany,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_GARNISHMENTS: V1EmployeesEmployeeIdGarnishments,
        PathValues.V1_GARNISHMENTS_GARNISHMENT_ID: V1GarnishmentsGarnishmentId,
        PathValues.V1_EVENTS: V1Events,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_TOKEN_INFO: V1TokenInfo,
        PathValues.OAUTH_TOKEN: OauthToken,
        PathValues.V1_PROVISION: V1Provision,
        PathValues.V1_COMPANIES_COMPANY_ID: V1CompaniesCompanyId,
        PathValues.V1_COMPANIES_COMPANY_ID_CUSTOM_FIELDS: V1CompaniesCompanyIdCustomFields,
        PathValues.V1_COMPANIES_COMPANY_ID_LOCATIONS: V1CompaniesCompanyIdLocations,
        PathValues.V1_LOCATIONS_LOCATION_ID: V1LocationsLocationId,
        PathValues.V1_LOCATIONS_LOCATION_UUID_MINIMUM_WAGES: V1LocationsLocationUuidMinimumWages,
        PathValues.V1_COMPANIES_COMPANY_ID_PAY_SCHEDULES: V1CompaniesCompanyIdPaySchedules,
        PathValues.V1_COMPANIES_COMPANY_ID_PAY_SCHEDULES_PAY_SCHEDULE_ID: V1CompaniesCompanyIdPaySchedulesPayScheduleId,
        PathValues.V1_COMPANIES_COMPANY_ID_PAY_PERIODS: V1CompaniesCompanyIdPayPeriods,
        PathValues.V1_COMPANIES_COMPANY_ID_PAY_PERIODS_UNPROCESSED_TERMINATION_PAY_PERIODS: V1CompaniesCompanyIdPayPeriodsUnprocessedTerminationPayPeriods,
        PathValues.V1_COMPANIES_COMPANY_ID_PAY_SCHEDULES_ASSIGNMENTS: V1CompaniesCompanyIdPaySchedulesAssignments,
        PathValues.V1_COMPANIES_COMPANY_ID_EMPLOYEES: V1CompaniesCompanyIdEmployees,
        PathValues.V1_COMPANIES_COMPANY_UUID_DEPARTMENTS: V1CompaniesCompanyUuidDepartments,
        PathValues.V1_DEPARTMENTS_DEPARTMENT_UUID: V1DepartmentsDepartmentUuid,
        PathValues.V1_DEPARTMENTS_DEPARTMENT_UUID_ADD: V1DepartmentsDepartmentUuidAdd,
        PathValues.V1_DEPARTMENTS_DEPARTMENT_UUID_REMOVE: V1DepartmentsDepartmentUuidRemove,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID: V1EmployeesEmployeeId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_TERMINATIONS: V1EmployeesEmployeeIdTerminations,
        PathValues.V1_TERMINATIONS_EMPLOYEE_ID: V1TerminationsEmployeeId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_REHIRE: V1EmployeesEmployeeIdRehire,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_EMPLOYMENT_HISTORY: V1EmployeesEmployeeIdEmploymentHistory,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_HOME_ADDRESSES: V1EmployeesEmployeeIdHomeAddresses,
        PathValues.V1_HOME_ADDRESSES_HOME_ADDRESS_UUID: V1HomeAddressesHomeAddressUuid,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_WORK_ADDRESSES: V1EmployeesEmployeeIdWorkAddresses,
        PathValues.V1_WORK_ADDRESSES_WORK_ADDRESS_UUID: V1WorkAddressesWorkAddressUuid,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_CUSTOM_FIELDS: V1EmployeesEmployeeIdCustomFields,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_JOBS: V1EmployeesEmployeeIdJobs,
        PathValues.V1_EMPLOYEES_EMPLOYEE_UUID_TIME_OFF_ACTIVITIES: V1EmployeesEmployeeUuidTimeOffActivities,
        PathValues.V1_JOBS_JOB_ID: V1JobsJobId,
        PathValues.V1_JOBS_JOB_ID_COMPENSATIONS: V1JobsJobIdCompensations,
        PathValues.V1_COMPENSATIONS_COMPENSATION_ID: V1CompensationsCompensationId,
        PathValues.V1_COMPANIES_COMPANY_ID_EARNING_TYPES: V1CompaniesCompanyIdEarningTypes,
        PathValues.V1_COMPANIES_COMPANY_ID_EARNING_TYPES_EARNING_TYPE_UUID: V1CompaniesCompanyIdEarningTypesEarningTypeUuid,
        PathValues.V1_COMPANIES_COMPANY_ID_CONTRACTORS: V1CompaniesCompanyIdContractors,
        PathValues.V1_CONTRACTORS_CONTRACTOR_ID: V1ContractorsContractorId,
        PathValues.V1_WEBHOOK_SUBSCRIPTIONS: V1WebhookSubscriptions,
        PathValues.V1_WEBHOOK_SUBSCRIPTIONS_WEBHOOK_SUBSCRIPTION_UUID: V1WebhookSubscriptionsWebhookSubscriptionUuid,
        PathValues.V1_WEBHOOK_SUBSCRIPTIONS_WEBHOOK_SUBSCRIPTION_UUID_VERIFY: V1WebhookSubscriptionsWebhookSubscriptionUuidVerify,
        PathValues.V1_WEBHOOK_SUBSCRIPTIONS_WEBHOOK_SUBSCRIPTION_UUID_REQUEST_VERIFICATION_TOKEN: V1WebhookSubscriptionsWebhookSubscriptionUuidRequestVerificationToken,
        PathValues.V1_COMPANIES_COMPANY_ID_PAYROLLS: V1CompaniesCompanyIdPayrolls,
        PathValues.V1_COMPANIES_COMPANY_ID_PAYROLLS_PAYROLL_ID: V1CompaniesCompanyIdPayrollsPayrollId,
        PathValues.V1_COMPANIES_COMPANY_ID_PAYROLLS_PAYROLL_ID_PREPARE: V1CompaniesCompanyIdPayrollsPayrollIdPrepare,
        PathValues.V1_PAYROLLS_PAYROLL_ID_EMPLOYEES_EMPLOYEE_ID_CALCULATE_ACCRUING_TIME_OFF_HOURS: V1PayrollsPayrollIdEmployeesEmployeeIdCalculateAccruingTimeOffHours,
        PathValues.V1_COMPANIES_COMPANY_ID_CONTRACTOR_PAYMENTS: V1CompaniesCompanyIdContractorPayments,
        PathValues.V1_COMPANIES_COMPANY_ID_CONTRACTOR_PAYMENTS_CONTRACTOR_PAYMENT_ID: V1CompaniesCompanyIdContractorPaymentsContractorPaymentId,
        PathValues.V1_COMPANIES_COMPANY_ID_COMPANY_BENEFITS: V1CompaniesCompanyIdCompanyBenefits,
        PathValues.V1_COMPANY_BENEFITS_COMPANY_BENEFIT_ID: V1CompanyBenefitsCompanyBenefitId,
        PathValues.V1_BENEFITS: V1Benefits,
        PathValues.V1_BENEFITS_BENEFIT_ID: V1BenefitsBenefitId,
        PathValues.V1_COMPANY_BENEFITS_COMPANY_BENEFIT_ID_SUMMARY: V1CompanyBenefitsCompanyBenefitIdSummary,
        PathValues.V1_BENEFITS_BENEFIT_ID_REQUIREMENTS: V1BenefitsBenefitIdRequirements,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_EMPLOYEE_BENEFITS: V1EmployeesEmployeeIdEmployeeBenefits,
        PathValues.V1_EMPLOYEE_BENEFITS_EMPLOYEE_BENEFIT_ID: V1EmployeeBenefitsEmployeeBenefitId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_YTD_BENEFIT_AMOUNTS_FROM_DIFFERENT_COMPANY: V1EmployeesEmployeeIdYtdBenefitAmountsFromDifferentCompany,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_GARNISHMENTS: V1EmployeesEmployeeIdGarnishments,
        PathValues.V1_GARNISHMENTS_GARNISHMENT_ID: V1GarnishmentsGarnishmentId,
        PathValues.V1_EVENTS: V1Events,
    }
)
