operation_parameter_map = {
    '/v1/provision-POST': {
        'parameters': [
            {
                'name': 'user'
            },
            {
                'name': 'company'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/custom_fields-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/company_benefits-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'benefit_type'
            },
            {
                'name': 'active'
            },
            {
                'name': 'responsible_for_employer_taxes'
            },
            {
                'name': 'responsible_for_employee_w2'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/benefits-GET': {
        'parameters': [
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/company_benefits-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'enrollment_count'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/company_benefits/{company_benefit_id}-GET': {
        'parameters': [
            {
                'name': 'company_benefit_id'
            },
            {
                'name': 'with_employee_benefits'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/benefits/{benefit_id}/requirements-GET': {
        'parameters': [
            {
                'name': 'benefit_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/company_benefits/{company_benefit_id}/summary-GET': {
        'parameters': [
            {
                'name': 'company_benefit_id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'detailed'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/benefits/{benefit_id}-GET': {
        'parameters': [
            {
                'name': 'benefit_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/company_benefits/{company_benefit_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_benefit_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/company_benefits/{company_benefit_id}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'company_benefit_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'active'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/contractor_payments/{contractor_payment_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'contractor_payment_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/contractor_payments-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'contractor_uuid'
            },
            {
                'name': 'group_by_date'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/contractors-POST': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'wage_type'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'hourly_rate'
            },
            {
                'name': 'self_onboarding'
            },
            {
                'name': 'email'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'middle_initial'
            },
            {
                'name': 'file_new_hire_report'
            },
            {
                'name': 'work_state'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'business_name'
            },
            {
                'name': 'ein'
            },
            {
                'name': 'is_active'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/contractors-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_id}-GET': {
        'parameters': [
            {
                'name': 'contractor_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/contractors/{contractor_id}-PUT': {
        'parameters': [
            {
                'name': 'contractor_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'type'
            },
            {
                'name': 'wage_type'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'hourly_rate'
            },
            {
                'name': 'self_onboarding'
            },
            {
                'name': 'email'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'middle_initial'
            },
            {
                'name': 'file_new_hire_report'
            },
            {
                'name': 'work_state'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'business_name'
            },
            {
                'name': 'ein'
            },
            {
                'name': 'is_active'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/departments/{department_uuid}/add-PUT': {
        'parameters': [
            {
                'name': 'department_uuid'
            },
            {
                'name': 'version'
            },
            {
                'name': 'employees'
            },
            {
                'name': 'contractors'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/departments-POST': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'title'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/departments/{department_uuid}-DELETE': {
        'parameters': [
            {
                'name': 'department_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/departments/{department_uuid}-GET': {
        'parameters': [
            {
                'name': 'department_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_uuid}/departments-GET': {
        'parameters': [
            {
                'name': 'company_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/departments/{department_uuid}/remove-PUT': {
        'parameters': [
            {
                'name': 'department_uuid'
            },
            {
                'name': 'version'
            },
            {
                'name': 'employees'
            },
            {
                'name': 'contractors'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/departments/{department_uuid}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'department_uuid'
            },
            {
                'name': 'title'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/earning_types-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/earning_types/{earning_type_uuid}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'earning_type_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/earning_types-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/earning_types/{earning_type_uuid}-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'earning_type_uuid'
            },
            {
                'name': 'name'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/home_addresses-POST': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'street_1'
            },
            {
                'name': 'street_2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'courtesy_withholding'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/work_addresses-POST': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'location_uuid'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/home_addresses/{home_address_uuid}-DELETE': {
        'parameters': [
            {
                'name': 'home_address_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/work_addresses/{work_address_uuid}-DELETE': {
        'parameters': [
            {
                'name': 'work_address_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/work_addresses/{work_address_uuid}-GET': {
        'parameters': [
            {
                'name': 'work_address_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/home_addresses/{home_address_uuid}-GET': {
        'parameters': [
            {
                'name': 'home_address_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/home_addresses-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/work_addresses-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/home_addresses/{home_address_uuid}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'home_address_uuid'
            },
            {
                'name': 'street_1'
            },
            {
                'name': 'street_2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'courtesy_withholding'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/work_addresses/{work_address_uuid}-PUT': {
        'parameters': [
            {
                'name': 'work_address_uuid'
            },
            {
                'name': 'version'
            },
            {
                'name': 'location_uuid'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/employee_benefits-POST': {
        'parameters': [
            {
                'name': 'company_benefit_uuid'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'active'
            },
            {
                'name': 'employee_deduction'
            },
            {
                'name': 'deduct_as_percentage'
            },
            {
                'name': 'employee_deduction_annual_maximum'
            },
            {
                'name': 'contribution'
            },
            {
                'name': 'elective'
            },
            {
                'name': 'company_contribution_annual_maximum'
            },
            {
                'name': 'limit_option'
            },
            {
                'name': 'catch_up'
            },
            {
                'name': 'coverage_amount'
            },
            {
                'name': 'coverage_salary_multiplier'
            },
            {
                'name': 'deduction_reduces_taxable_income'
            },
            {
                'name': 'company_contribution'
            },
            {
                'name': 'contribute_as_percentage'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/ytd_benefit_amounts_from_different_company-POST': {
        'parameters': [
            {
                'name': 'tax_year'
            },
            {
                'name': 'ytd_employee_deduction_amount'
            },
            {
                'name': 'ytd_company_contribution_amount'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'benefit_type'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/employee_benefits-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employee_benefits/{employee_benefit_id}-GET': {
        'parameters': [
            {
                'name': 'employee_benefit_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employee_benefits/{employee_benefit_id}-DELETE': {
        'parameters': [
            {
                'name': 'employee_benefit_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employee_benefits/{employee_benefit_id}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'employee_benefit_id'
            },
            {
                'name': 'active'
            },
            {
                'name': 'employee_deduction'
            },
            {
                'name': 'deduct_as_percentage'
            },
            {
                'name': 'employee_deduction_annual_maximum'
            },
            {
                'name': 'contribution'
            },
            {
                'name': 'elective'
            },
            {
                'name': 'company_contribution_annual_maximum'
            },
            {
                'name': 'limit_option'
            },
            {
                'name': 'catch_up'
            },
            {
                'name': 'coverage_amount'
            },
            {
                'name': 'deduction_reduces_taxable_income'
            },
            {
                'name': 'coverage_salary_multiplier'
            },
            {
                'name': 'company_contribution'
            },
            {
                'name': 'contribute_as_percentage'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/rehire-POST': {
        'parameters': [
            {
                'name': 'effective_date'
            },
            {
                'name': 'file_new_hire_report'
            },
            {
                'name': 'work_location_uuid'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'employment_status'
            },
            {
                'name': 'two_percent_shareholder'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/terminations-POST': {
        'parameters': [
            {
                'name': 'effective_date'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'run_termination_payroll'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/rehire-DELETE': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/terminations-DELETE': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/employment_history-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/rehire-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/terminations-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/rehire-PUT': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'file_new_hire_report'
            },
            {
                'name': 'work_location_uuid'
            },
            {
                'name': 'employment_status'
            },
            {
                'name': 'two_percent_shareholder'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/terminations/{employee_id}-PUT': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'run_termination_payroll'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/employees-POST': {
        'parameters': [
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'middle_initial'
            },
            {
                'name': 'date_of_birth'
            },
            {
                'name': 'email'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'self_onboarding'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}-DELETE': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/employees-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'terminated'
            },
            {
                'name': 'include'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/custom_fields-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'include'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_uuid}/time_off_activities-GET': {
        'parameters': [
            {
                'name': 'employee_uuid'
            },
            {
                'name': 'time_off_type'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'middle_initial'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'date_of_birth'
            },
            {
                'name': 'email'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'two_percent_shareholder'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/events-GET': {
        'parameters': [
            {
                'name': 'starting_after_uuid'
            },
            {
                'name': 'resource_uuid'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'event_type'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/garnishments-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'court_ordered'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'active'
            },
            {
                'name': 'times'
            },
            {
                'name': 'recurring'
            },
            {
                'name': 'annual_maximum'
            },
            {
                'name': 'pay_period_maximum'
            },
            {
                'name': 'deduct_as_percentage'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/garnishments/{garnishment_id}-GET': {
        'parameters': [
            {
                'name': 'garnishment_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/garnishments-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/garnishments/{garnishment_id}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'garnishment_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'active'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'court_ordered'
            },
            {
                'name': 'times'
            },
            {
                'name': 'recurring'
            },
            {
                'name': 'annual_maximum'
            },
            {
                'name': 'pay_period_maximum'
            },
            {
                'name': 'deduct_as_percentage'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/token_info-GET': {
        'parameters': [
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/oauth/token-POST': {
        'parameters': [
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'refresh_token'
            },
            {
                'name': 'grant_type'
            },
            {
                'name': 'redirect_uri'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/jobs/{job_id}/compensations-POST': {
        'parameters': [
            {
                'name': 'payment_unit'
            },
            {
                'name': 'flsa_status'
            },
            {
                'name': 'job_id'
            },
            {
                'name': 'rate'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'adjust_for_minimum_wage'
            },
            {
                'name': 'minimum_wages'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/jobs-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'hire_date'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'two_percent_shareholder'
            },
            {
                'name': 'state_wc_covered'
            },
            {
                'name': 'state_wc_class_code'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/compensations/{compensation_id}-DELETE': {
        'parameters': [
            {
                'name': 'compensation_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/jobs/{job_id}-DELETE': {
        'parameters': [
            {
                'name': 'job_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/compensations/{compensation_id}-GET': {
        'parameters': [
            {
                'name': 'compensation_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/jobs/{job_id}/compensations-GET': {
        'parameters': [
            {
                'name': 'job_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'include'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/jobs/{job_id}-GET': {
        'parameters': [
            {
                'name': 'job_id'
            },
            {
                'name': 'include'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/employees/{employee_id}/jobs-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'include'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/compensations/{compensation_id}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'compensation_id'
            },
            {
                'name': 'rate'
            },
            {
                'name': 'payment_unit'
            },
            {
                'name': 'flsa_status'
            },
            {
                'name': 'adjust_for_minimum_wage'
            },
            {
                'name': 'minimum_wages'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/jobs/{job_id}-PUT': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'job_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'hire_date'
            },
            {
                'name': 'two_percent_shareholder'
            },
            {
                'name': 'state_wc_covered'
            },
            {
                'name': 'state_wc_class_code'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/locations-POST': {
        'parameters': [
            {
                'name': 'phone_number'
            },
            {
                'name': 'street_1'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'street_2'
            },
            {
                'name': 'country'
            },
            {
                'name': 'mailing_address'
            },
            {
                'name': 'filing_address'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/locations/{location_id}-GET': {
        'parameters': [
            {
                'name': 'location_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/locations/{location_uuid}/minimum_wages-GET': {
        'parameters': [
            {
                'name': 'location_uuid'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/locations-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/locations/{location_id}-PUT': {
        'parameters': [
            {
                'name': 'location_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'phone_number'
            },
            {
                'name': 'street_1'
            },
            {
                'name': 'street_2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'country'
            },
            {
                'name': 'mailing_address'
            },
            {
                'name': 'filing_address'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/pay_schedules/assignments-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/pay_schedules/{pay_schedule_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'pay_schedule_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/pay_schedules-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/pay_periods-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'payroll_types'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/pay_periods/unprocessed_termination_pay_periods-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/payrolls-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'processing_statuses'
            },
            {
                'name': 'payroll_types'
            },
            {
                'name': 'include'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/payrolls/{payroll_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'payroll_id'
            },
            {
                'name': 'include'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/payrolls/{payroll_id}/prepare-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'payroll_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/companies/{company_id}/payrolls/{payroll_id}-PUT': {
        'parameters': [
            {
                'name': 'employee_compensations'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'payroll_id'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/payrolls/{payroll_id}/employees/{employee_id}/calculate_accruing_time_off_hours-POST': {
        'parameters': [
            {
                'name': 'payroll_id'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'regular_hours_worked'
            },
            {
                'name': 'overtime_hours_worked'
            },
            {
                'name': 'double_overtime_hours_worked'
            },
            {
                'name': 'pto_hours_used'
            },
            {
                'name': 'sick_hours_used'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/webhook_subscriptions-POST': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'subscription_types'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/webhook_subscriptions/{webhook_subscription_uuid}-DELETE': {
        'parameters': [
            {
                'name': 'webhook_subscription_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/webhook_subscriptions/{webhook_subscription_uuid}-GET': {
        'parameters': [
            {
                'name': 'webhook_subscription_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/webhook_subscriptions-GET': {
        'parameters': [
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/webhook_subscriptions/{webhook_subscription_uuid}/request_verification_token-GET': {
        'parameters': [
            {
                'name': 'webhook_subscription_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/webhook_subscriptions/{webhook_subscription_uuid}-PUT': {
        'parameters': [
            {
                'name': 'subscription_types'
            },
            {
                'name': 'webhook_subscription_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
    '/v1/webhook_subscriptions/{webhook_subscription_uuid}/verify-PUT': {
        'parameters': [
            {
                'name': 'verification_token'
            },
            {
                'name': 'webhook_subscription_uuid'
            },
            {
                'name': 'X-Gusto-API-Version'
            },
        ]
    },
};