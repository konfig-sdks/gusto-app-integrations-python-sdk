<div align="center">

[![Visit Gusto](./header.png)](https://gusto.com)

# Gusto<a id="gusto"></a>

Welcome to Gusto's Embedded Payroll API documentation!


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`gustoappintegrations.companies.create_company`](#gustoappintegrationscompaniescreate_company)
  * [Overview](#overview)
  * [`gustoappintegrations.companies.get_company_info`](#gustoappintegrationscompaniesget_company_info)
  * [`gustoappintegrations.companies.get_custom_fields`](#gustoappintegrationscompaniesget_custom_fields)
  * [`gustoappintegrations.company_benefits.create_company_benefit`](#gustoappintegrationscompany_benefitscreate_company_benefit)
  * [`gustoappintegrations.company_benefits.get_all_supported_benefits`](#gustoappintegrationscompany_benefitsget_all_supported_benefits)
  * [`gustoappintegrations.company_benefits.get_by_company_id`](#gustoappintegrationscompany_benefitsget_by_company_id)
  * [`gustoappintegrations.company_benefits.get_by_id`](#gustoappintegrationscompany_benefitsget_by_id)
  * [`gustoappintegrations.company_benefits.get_fields_requirements_by_id`](#gustoappintegrationscompany_benefitsget_fields_requirements_by_id)
  * [`gustoappintegrations.company_benefits.get_summary_by_id`](#gustoappintegrationscompany_benefitsget_summary_by_id)
  * [`gustoappintegrations.company_benefits.get_supported_benefit_by_id`](#gustoappintegrationscompany_benefitsget_supported_benefit_by_id)
  * [`gustoappintegrations.company_benefits.remove_benefit`](#gustoappintegrationscompany_benefitsremove_benefit)
  * [`gustoappintegrations.company_benefits.update_benefit`](#gustoappintegrationscompany_benefitsupdate_benefit)
  * [`gustoappintegrations.contractor_payments.get_single`](#gustoappintegrationscontractor_paymentsget_single)
  * [`gustoappintegrations.contractor_payments.list_for_company`](#gustoappintegrationscontractor_paymentslist_for_company)
  * [`gustoappintegrations.contractors.create_individual_or_business`](#gustoappintegrationscontractorscreate_individual_or_business)
  * [`gustoappintegrations.contractors.get_all`](#gustoappintegrationscontractorsget_all)
  * [`gustoappintegrations.contractors.get_details`](#gustoappintegrationscontractorsget_details)
  * [`gustoappintegrations.contractors.update_contractor`](#gustoappintegrationscontractorsupdate_contractor)
  * [`gustoappintegrations.departments.add_people_to_department`](#gustoappintegrationsdepartmentsadd_people_to_department)
  * [`gustoappintegrations.departments.create_department`](#gustoappintegrationsdepartmentscreate_department)
  * [`gustoappintegrations.departments.delete_department`](#gustoappintegrationsdepartmentsdelete_department)
  * [`gustoappintegrations.departments.get_by_uuid`](#gustoappintegrationsdepartmentsget_by_uuid)
  * [`gustoappintegrations.departments.list_for_company`](#gustoappintegrationsdepartmentslist_for_company)
  * [`gustoappintegrations.departments.remove_employees`](#gustoappintegrationsdepartmentsremove_employees)
  * [`gustoappintegrations.departments.update_department`](#gustoappintegrationsdepartmentsupdate_department)
  * [`gustoappintegrations.earning_types.create_custom_earning_type`](#gustoappintegrationsearning_typescreate_custom_earning_type)
  * [`gustoappintegrations.earning_types.deactivate`](#gustoappintegrationsearning_typesdeactivate)
  * [`gustoappintegrations.earning_types.get_all`](#gustoappintegrationsearning_typesget_all)
  * [`gustoappintegrations.earning_types.update_type_by_id`](#gustoappintegrationsearning_typesupdate_type_by_id)
  * [`gustoappintegrations.employee_addresses.create_home_address`](#gustoappintegrationsemployee_addressescreate_home_address)
  * [`gustoappintegrations.employee_addresses.create_work_address`](#gustoappintegrationsemployee_addressescreate_work_address)
  * [`gustoappintegrations.employee_addresses.delete_employee_home_address`](#gustoappintegrationsemployee_addressesdelete_employee_home_address)
  * [`gustoappintegrations.employee_addresses.delete_employee_work_address`](#gustoappintegrationsemployee_addressesdelete_employee_work_address)
  * [`gustoappintegrations.employee_addresses.get`](#gustoappintegrationsemployee_addressesget)
  * [`gustoappintegrations.employee_addresses.get_home_address`](#gustoappintegrationsemployee_addressesget_home_address)
  * [`gustoappintegrations.employee_addresses.get_home_addresses`](#gustoappintegrationsemployee_addressesget_home_addresses)
  * [`gustoappintegrations.employee_addresses.get_work_addresses`](#gustoappintegrationsemployee_addressesget_work_addresses)
  * [`gustoappintegrations.employee_addresses.update_home_address`](#gustoappintegrationsemployee_addressesupdate_home_address)
  * [`gustoappintegrations.employee_addresses.update_work_address`](#gustoappintegrationsemployee_addressesupdate_work_address)
  * [`gustoappintegrations.employee_benefits.create_benefit`](#gustoappintegrationsemployee_benefitscreate_benefit)
  * [`gustoappintegrations.employee_benefits.create_ytd_benefit_amounts_from_different_company`](#gustoappintegrationsemployee_benefitscreate_ytd_benefit_amounts_from_different_company)
  * [`gustoappintegrations.employee_benefits.get_all_for_employee`](#gustoappintegrationsemployee_benefitsget_all_for_employee)
  * [`gustoappintegrations.employee_benefits.get_by_id`](#gustoappintegrationsemployee_benefitsget_by_id)
  * [`gustoappintegrations.employee_benefits.remove_benefit`](#gustoappintegrationsemployee_benefitsremove_benefit)
  * [`gustoappintegrations.employee_benefits.update_benefit`](#gustoappintegrationsemployee_benefitsupdate_benefit)
  * [`gustoappintegrations.employee_employments.create_rehire`](#gustoappintegrationsemployee_employmentscreate_rehire)
  * [`gustoappintegrations.employee_employments.create_termination`](#gustoappintegrationsemployee_employmentscreate_termination)
  * [`gustoappintegrations.employee_employments.delete_rehire`](#gustoappintegrationsemployee_employmentsdelete_rehire)
  * [`gustoappintegrations.employee_employments.delete_termination`](#gustoappintegrationsemployee_employmentsdelete_termination)
  * [`gustoappintegrations.employee_employments.get_history`](#gustoappintegrationsemployee_employmentsget_history)
  * [`gustoappintegrations.employee_employments.get_rehire_info`](#gustoappintegrationsemployee_employmentsget_rehire_info)
  * [`gustoappintegrations.employee_employments.list_terminations_for_employee`](#gustoappintegrationsemployee_employmentslist_terminations_for_employee)
  * [`gustoappintegrations.employee_employments.update_rehire`](#gustoappintegrationsemployee_employmentsupdate_rehire)
  * [`gustoappintegrations.employee_employments.update_termination`](#gustoappintegrationsemployee_employmentsupdate_termination)
  * [`gustoappintegrations.employees.create_employee`](#gustoappintegrationsemployeescreate_employee)
  * [`gustoappintegrations.employees.delete_onboarding_employee`](#gustoappintegrationsemployeesdelete_onboarding_employee)
  * [`gustoappintegrations.employees.get_company_employees`](#gustoappintegrationsemployeesget_company_employees)
  * [`gustoappintegrations.employees.get_custom_fields`](#gustoappintegrationsemployeesget_custom_fields)
  * [`gustoappintegrations.employees.get_details`](#gustoappintegrationsemployeesget_details)
  * [`gustoappintegrations.employees.get_time_off_activities`](#gustoappintegrationsemployeesget_time_off_activities)
  * [`gustoappintegrations.employees.update_employee`](#gustoappintegrationsemployeesupdate_employee)
  * [`gustoappintegrations.events.get_all`](#gustoappintegrationseventsget_all)
  * [`gustoappintegrations.garnishments.create_garnishment`](#gustoappintegrationsgarnishmentscreate_garnishment)
  * [`gustoappintegrations.garnishments.get`](#gustoappintegrationsgarnishmentsget)
  * [`gustoappintegrations.garnishments.get_employee_garnishments`](#gustoappintegrationsgarnishmentsget_employee_garnishments)
  * [`gustoappintegrations.garnishments.update`](#gustoappintegrationsgarnishmentsupdate)
  * [`gustoappintegrations.introspection.access_token_info`](#gustoappintegrationsintrospectionaccess_token_info)
  * [`gustoappintegrations.introspection.exchange_refresh_token`](#gustoappintegrationsintrospectionexchange_refresh_token)
  * [`gustoappintegrations.jobs_and_compensations.create_compensation`](#gustoappintegrationsjobs_and_compensationscreate_compensation)
  * [`gustoappintegrations.jobs_and_compensations.create_job`](#gustoappintegrationsjobs_and_compensationscreate_job)
  * [`gustoappintegrations.jobs_and_compensations.delete_compensation`](#gustoappintegrationsjobs_and_compensationsdelete_compensation)
  * [`gustoappintegrations.jobs_and_compensations.delete_specific_job`](#gustoappintegrationsjobs_and_compensationsdelete_specific_job)
  * [`gustoappintegrations.jobs_and_compensations.get_compensation_by_id`](#gustoappintegrationsjobs_and_compensationsget_compensation_by_id)
  * [`gustoappintegrations.jobs_and_compensations.get_compensations_by_job_id`](#gustoappintegrationsjobs_and_compensationsget_compensations_by_job_id)
  * [`gustoappintegrations.jobs_and_compensations.get_details`](#gustoappintegrationsjobs_and_compensationsget_details)
  * [`gustoappintegrations.jobs_and_compensations.get_employee_jobs`](#gustoappintegrationsjobs_and_compensationsget_employee_jobs)
  * [`gustoappintegrations.jobs_and_compensations.update_compensation`](#gustoappintegrationsjobs_and_compensationsupdate_compensation)
  * [`gustoappintegrations.jobs_and_compensations.update_job`](#gustoappintegrationsjobs_and_compensationsupdate_job)
  * [`gustoappintegrations.locations.create_company_location`](#gustoappintegrationslocationscreate_company_location)
  * [`gustoappintegrations.locations.get_details`](#gustoappintegrationslocationsget_details)
  * [`gustoappintegrations.locations.get_minimum_wages`](#gustoappintegrationslocationsget_minimum_wages)
  * [`gustoappintegrations.locations.list_company_locations`](#gustoappintegrationslocationslist_company_locations)
  * [`gustoappintegrations.locations.update_location`](#gustoappintegrationslocationsupdate_location)
  * [`gustoappintegrations.pay_schedules.get_assignments`](#gustoappintegrationspay_schedulesget_assignments)
  * [`gustoappintegrations.pay_schedules.get_details`](#gustoappintegrationspay_schedulesget_details)
  * [`gustoappintegrations.pay_schedules.list`](#gustoappintegrationspay_scheduleslist)
  * [`gustoappintegrations.pay_schedules.list_0`](#gustoappintegrationspay_scheduleslist_0)
  * [`gustoappintegrations.pay_schedules.list_unprocessed_termination_pay_periods`](#gustoappintegrationspay_scheduleslist_unprocessed_termination_pay_periods)
  * [`gustoappintegrations.payrolls.get_all_for_company`](#gustoappintegrationspayrollsget_all_for_company)
  * [`gustoappintegrations.payrolls.get_single_payroll`](#gustoappintegrationspayrollsget_single_payroll)
  * [`gustoappintegrations.payrolls.prepare_for_update`](#gustoappintegrationspayrollsprepare_for_update)
  * [`gustoappintegrations.payrolls.update_by_id`](#gustoappintegrationspayrollsupdate_by_id)
  * [`gustoappintegrations.time_off_policies.calculate_accruing_time_off_hours`](#gustoappintegrationstime_off_policiescalculate_accruing_time_off_hours)
  * [`gustoappintegrations.webhooks.create_subscription`](#gustoappintegrationswebhookscreate_subscription)
  * [`gustoappintegrations.webhooks.delete_subscription_by_uuid`](#gustoappintegrationswebhooksdelete_subscription_by_uuid)
  * [`gustoappintegrations.webhooks.get_subscription_by_uuid`](#gustoappintegrationswebhooksget_subscription_by_uuid)
  * [`gustoappintegrations.webhooks.list_subscriptions`](#gustoappintegrationswebhookslist_subscriptions)
  * [`gustoappintegrations.webhooks.request_verification_token`](#gustoappintegrationswebhooksrequest_verification_token)
  * [`gustoappintegrations.webhooks.update_subscription_by_uuid`](#gustoappintegrationswebhooksupdate_subscription_by_uuid)
  * [`gustoappintegrations.webhooks.verify_subscription_token`](#gustoappintegrationswebhooksverify_subscription_token)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Gusto&serviceName=App%20Integrations&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from gusto_app_integrations_python_sdk import GustoAppIntegrations, ApiException

gustoappintegrations = GustoAppIntegrations(
    api_key_auth="YOUR_API_KEY",
)

try:
    # Create a company
    create_company_response = gustoappintegrations.companies.create_company(
        user={
            "first_name": "first_name_example",
            "last_name": "last_name_example",
            "email": "email_example",
        },
        company={
            "name": "name_example",
        },
        x_gusto_api_version="2024-03-01",
    )
    print(create_company_response)
except ApiException as e:
    print("Exception when calling CompaniesApi.create_company: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from gusto_app_integrations_python_sdk import GustoAppIntegrations, ApiException

gustoappintegrations = GustoAppIntegrations(
    api_key_auth="YOUR_API_KEY",
)


async def main():
    try:
        # Create a company
        create_company_response = await gustoappintegrations.companies.acreate_company(
            user={
                "first_name": "first_name_example",
                "last_name": "last_name_example",
                "email": "email_example",
            },
            company={
                "name": "name_example",
            },
            x_gusto_api_version="2024-03-01",
        )
        print(create_company_response)
    except ApiException as e:
        print("Exception when calling CompaniesApi.create_company: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from gusto_app_integrations_python_sdk import GustoAppIntegrations, ApiException

gustoappintegrations = GustoAppIntegrations(
    api_key_auth="YOUR_API_KEY",
)

try:
    # Create a company
    create_company_response = gustoappintegrations.companies.raw.create_company(
        user={
            "first_name": "first_name_example",
            "last_name": "last_name_example",
            "email": "email_example",
        },
        company={
            "name": "name_example",
        },
        x_gusto_api_version="2024-03-01",
    )
    pprint(create_company_response.body)
    pprint(create_company_response.body["account_claim_url"])
    pprint(create_company_response.headers)
    pprint(create_company_response.status)
    pprint(create_company_response.round_trip_time)
except ApiException as e:
    print("Exception when calling CompaniesApi.create_company: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `gustoappintegrations.companies.create_company`<a id="gustoappintegrationscompaniescreate_company"></a>

### Overview<a id="overview"></a>
The company provisioning API provides a way to create a Gusto company as part of your integration. When you successfully call the API, the API does the following:
* Creates a new company in Gusto.
* Creates a new user in Gusto.
* Makes the new user the primary payroll administrator of the new company.
* Sends a welcome email to the new user.
In the response, you will receive an account claim URL. Redirect the user to this URL to complete their account setup inside of Gusto

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_company_response = gustoappintegrations.companies.create_company(
    user={
        "first_name": "first_name_example",
        "last_name": "last_name_example",
        "email": "email_example",
    },
    company={
        "name": "name_example",
    },
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user: [`CompaniesCreateCompanyRequestUser`](./gusto_app_integrations_python_sdk/type/companies_create_company_request_user.py)<a id="user-companiescreatecompanyrequestusergusto_app_integrations_python_sdktypecompanies_create_company_request_userpy"></a>


##### company: [`CompaniesCreateCompanyRequestCompany`](./gusto_app_integrations_python_sdk/type/companies_create_company_request_company.py)<a id="company-companiescreatecompanyrequestcompanygusto_app_integrations_python_sdktypecompanies_create_company_request_companypy"></a>


##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompaniesCreateCompanyRequest`](./gusto_app_integrations_python_sdk/type/companies_create_company_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesCreateCompanyResponse`](./gusto_app_integrations_python_sdk/pydantic/companies_create_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/provision` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.companies.get_company_info`<a id="gustoappintegrationscompaniesget_company_info"></a>

Get a company.         
The employees:read scope is required to return home_address and non-work locations.         
The company_admin:read scope is required to return primary_payroll_admin.         
The signatories:read scope is required to return primary_signatory.         

scope: `companies:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_info_response = gustoappintegrations.companies.get_company_info(
    company_id="company_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Company`](./gusto_app_integrations_python_sdk/pydantic/company.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.companies.get_custom_fields`<a id="gustoappintegrationscompaniesget_custom_fields"></a>

Returns a list of the custom fields of the company. Useful when you need to know the schema of custom fields for an entire company

scope: `companies:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_fields_response = gustoappintegrations.companies.get_custom_fields(
    company_id="company_id_example",
    page=3.14,
    per=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesGetCustomFieldsResponse`](./gusto_app_integrations_python_sdk/pydantic/companies_get_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/custom_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.company_benefits.create_company_benefit`<a id="gustoappintegrationscompany_benefitscreate_company_benefit"></a>

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

scope: `company_benefits:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_company_benefit_response = (
    gustoappintegrations.company_benefits.create_company_benefit(
        description="string_example",
        company_id="company_id_example",
        benefit_type=3.14,
        active=True,
        responsible_for_employer_taxes=True,
        responsible_for_employee_w2=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

The description of the company benefit.For example, a company may offer multiple benefits with an ID of 1 (for Medical Insurance). The description would show something more specific like “Kaiser Permanente” or “Blue Cross/ Blue Shield”.

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### benefit_type: `Union[int, float]`<a id="benefit_type-unionint-float"></a>

The ID of the benefit to which the company benefit belongs.

##### active: `bool`<a id="active-bool"></a>

Whether this benefit is active for employee participation.

##### responsible_for_employer_taxes: `bool`<a id="responsible_for_employer_taxes-bool"></a>

Whether the employer is subject to pay employer taxes when an employee is on leave. Only applicable to third party sick pay benefits.

##### responsible_for_employee_w2: `bool`<a id="responsible_for_employee_w2-bool"></a>

Whether the employer is subject to file W-2 forms for an employee on leave. Only applicable to third party sick pay benefits.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompanyBenefitsCreateCompanyBenefitRequest`](./gusto_app_integrations_python_sdk/type/company_benefits_create_company_benefit_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompanyBenefit`](./gusto_app_integrations_python_sdk/pydantic/company_benefit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/company_benefits` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.company_benefits.get_all_supported_benefits`<a id="gustoappintegrationscompany_benefitsget_all_supported_benefits"></a>

Returns all benefits supported by Gusto.

The benefit object in Gusto contains high level information about a particular benefit type and its tax considerations. When companies choose to offer a benefit, they are creating a Company Benefit object associated with a particular benefit.

scope: `benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_supported_benefits_response = (
    gustoappintegrations.company_benefits.get_all_supported_benefits(
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyBenefitsGetAllSupportedBenefitsResponse`](./gusto_app_integrations_python_sdk/pydantic/company_benefits_get_all_supported_benefits_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/benefits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.company_benefits.get_by_company_id`<a id="gustoappintegrationscompany_benefitsget_by_company_id"></a>

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

Benefits containing PHI are only visible to applications with the `company_benefits:read:phi` scope.

scope: `company_benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_company_id_response = gustoappintegrations.company_benefits.get_by_company_id(
    company_id="company_id_example",
    enrollment_count=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### enrollment_count: `bool`<a id="enrollment_count-bool"></a>

Whether to return employee enrollment count

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyBenefitsGetByCompanyIdResponse`](./gusto_app_integrations_python_sdk/pydantic/company_benefits_get_by_company_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/company_benefits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.company_benefits.get_by_id`<a id="gustoappintegrationscompany_benefitsget_by_id"></a>

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

When with_employee_benefits parameter with true value is passed, employee_benefits:read scope is required to return employee_benefits.

scope: `company_benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = gustoappintegrations.company_benefits.get_by_id(
    company_benefit_id="company_benefit_id_example",
    with_employee_benefits=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_benefit_id: `str`<a id="company_benefit_id-str"></a>

The UUID of the company benefit

##### with_employee_benefits: `bool`<a id="with_employee_benefits-bool"></a>

Whether to return employee benefits associated with the benefit

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyBenefitWithEmployeeBenefits`](./gusto_app_integrations_python_sdk/pydantic/company_benefit_with_employee_benefits.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company_benefits/{company_benefit_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.company_benefits.get_fields_requirements_by_id`<a id="gustoappintegrationscompany_benefitsget_fields_requirements_by_id"></a>

Returns field requirements for the requested benefit type.

scope: `benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_fields_requirements_by_id_response = (
    gustoappintegrations.company_benefits.get_fields_requirements_by_id(
        benefit_id="benefit_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### benefit_id: `str`<a id="benefit_id-str"></a>

The benefit type in Gusto.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`BenefitTypeRequirements`](./gusto_app_integrations_python_sdk/pydantic/benefit_type_requirements.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/benefits/{benefit_id}/requirements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.company_benefits.get_summary_by_id`<a id="gustoappintegrationscompany_benefitsget_summary_by_id"></a>

Returns summary benefit data for the requested company benefit id.

Benefits containing PHI are only visible to applications with the `company_benefits:read:phi` scope.

scope: `company_benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_summary_by_id_response = gustoappintegrations.company_benefits.get_summary_by_id(
    company_benefit_id="company_benefit_id_example",
    start_date="2022-01-01",
    end_date="2022-12-31",
    detailed=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_benefit_id: `str`<a id="company_benefit_id-str"></a>

The UUID of the company benefit

##### start_date: `str`<a id="start_date-str"></a>

The start date for which to retrieve company benefit summary

##### end_date: `str`<a id="end_date-str"></a>

The end date for which to retrieve company benefit summary

##### detailed: `bool`<a id="detailed-bool"></a>

Display employee payroll item summary

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`BenefitSummary`](./gusto_app_integrations_python_sdk/pydantic/benefit_summary.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company_benefits/{company_benefit_id}/summary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.company_benefits.get_supported_benefit_by_id`<a id="gustoappintegrationscompany_benefitsget_supported_benefit_by_id"></a>

Returns a benefit supported by Gusto.

The benefit object in Gusto contains high level information about a particular benefit type and its tax considerations. When companies choose to offer a benefit, they are creating a Company Benefit object associated with a particular benefit.

scope: `benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_supported_benefit_by_id_response = (
    gustoappintegrations.company_benefits.get_supported_benefit_by_id(
        benefit_id="benefit_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### benefit_id: `str`<a id="benefit_id-str"></a>

The benefit type in Gusto.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`SupportedBenefit`](./gusto_app_integrations_python_sdk/pydantic/supported_benefit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/benefits/{benefit_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.company_benefits.remove_benefit`<a id="gustoappintegrationscompany_benefitsremove_benefit"></a>

The following must be true in order to delete a company benefit
  - There are no employee benefits associated with the company benefit
  - There are no payroll items associated with the company benefit
  - The benefit is not managed by a Partner or by Gusto (type must be 'External')

scope: `company_benefits:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoappintegrations.company_benefits.remove_benefit(
    company_benefit_id="company_benefit_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_benefit_id: `str`<a id="company_benefit_id-str"></a>

The UUID of the company benefit

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company_benefits/{company_benefit_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.company_benefits.update_benefit`<a id="gustoappintegrationscompany_benefitsupdate_benefit"></a>

Company benefits represent the benefits that a company is offering to employees. This ties together a particular supported benefit with the company-specific information for the offering of that benefit.

Note that company benefits can be deactivated only when no employees are enrolled.

scope: `company_benefits:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_benefit_response = gustoappintegrations.company_benefits.update_benefit(
    version="string_example",
    company_benefit_id="company_benefit_id_example",
    description="string_example",
    active=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### company_benefit_id: `str`<a id="company_benefit_id-str"></a>

The UUID of the company benefit

##### description: `str`<a id="description-str"></a>

The description of the company benefit.For example, a company may offer multiple benefits with an ID of 1 (for Medical Insurance). The description would show something more specific like “Kaiser Permanente” or “Blue Cross/ Blue Shield”.

##### active: `bool`<a id="active-bool"></a>

Whether this benefit is active for employee participation. Company benefits may only be deactivated if no employees are actively participating.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompanyBenefitsUpdateBenefitRequest`](./gusto_app_integrations_python_sdk/type/company_benefits_update_benefit_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompanyBenefit`](./gusto_app_integrations_python_sdk/pydantic/company_benefit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company_benefits/{company_benefit_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.contractor_payments.get_single`<a id="gustoappintegrationscontractor_paymentsget_single"></a>

Returns a single contractor payments

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_response = gustoappintegrations.contractor_payments.get_single(
    company_id="company_id_example",
    contractor_payment_id="contractor_payment_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### contractor_payment_id: `str`<a id="contractor_payment_id-str"></a>

The UUID of the contractor payment

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ContractorPayment`](./gusto_app_integrations_python_sdk/pydantic/contractor_payment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/contractor_payments/{contractor_payment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.contractor_payments.list_for_company`<a id="gustoappintegrationscontractor_paymentslist_for_company"></a>

Returns an object containing individual contractor payments, within a given time period, including totals.

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_for_company_response = gustoappintegrations.contractor_payments.list_for_company(
    company_id="company_id_example",
    start_date="2020-01-01",
    end_date="2020-12-31",
    contractor_uuid="string_example",
    group_by_date=True,
    page=3.14,
    per=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### start_date: `str`<a id="start_date-str"></a>

The time period for which to retrieve contractor payments

##### end_date: `str`<a id="end_date-str"></a>

The time period for which to retrieve contractor payments

##### contractor_uuid: `str`<a id="contractor_uuid-str"></a>

The UUID of the contractor. When specified, will load all payments for that contractor.

##### group_by_date: `bool`<a id="group_by_date-bool"></a>

Display contractor payments results group by check date if set to true.

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ContractorPaymentsListForCompanyResponse`](./gusto_app_integrations_python_sdk/pydantic/contractor_payments_list_for_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/contractor_payments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.contractors.create_individual_or_business`<a id="gustoappintegrationscontractorscreate_individual_or_business"></a>

Create an individual or business contractor.

scope: `contractors:manage`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_individual_or_business_response = (
    gustoappintegrations.contractors.create_individual_or_business(
        body=None,
        company_id="company_id_example",
        type="Individual",
        wage_type="Fixed",
        start_date="2020-01-11",
        hourly_rate="40.0",
        self_onboarding=False,
        email="string_example",
        first_name="string_example",
        last_name="string_example",
        middle_initial="string_example",
        file_new_hire_report=False,
        work_state="string_example",
        ssn="048072888",
        business_name="string_example",
        ein="string_example",
        is_active=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### type: `str`<a id="type-str"></a>

The contractor type.

##### wage_type: `str`<a id="wage_type-str"></a>

The contractor’s wage type. 

##### start_date: `str`<a id="start_date-str"></a>

The day when the contractor will start working for the company. 

##### hourly_rate: `str`<a id="hourly_rate-str"></a>

The contractor’s hourly rate. This attribute is required if the wage_type is `Hourly`.

##### self_onboarding: `bool`<a id="self_onboarding-bool"></a>

Whether the contractor or the payroll admin will complete onboarding in Gusto. Self-onboarding is recommended so that contractors receive Gusto accounts. If self_onboarding is true, then email is required.

##### email: `str`<a id="email-str"></a>

The contractor’s email address.

##### first_name: `str`<a id="first_name-str"></a>

The contractor’s first name. This attribute is required for `Individual` contractors and will be ignored for `Business` contractors.

##### last_name: `str`<a id="last_name-str"></a>

The contractor’s last name. This attribute is required for `Individual` contractors and will be ignored for `Business` contractors.

##### middle_initial: `str`<a id="middle_initial-str"></a>

The contractor’s middle initial. This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.

##### file_new_hire_report: `bool`<a id="file_new_hire_report-bool"></a>

The boolean flag indicating whether Gusto will file a new hire report for the contractor. This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.

##### work_state: `Optional[str]`<a id="work_state-optionalstr"></a>

State where the contractor will be conducting the majority of their work for the company. This value is used when generating the new hire report. This attribute is required for `Individual` contractors if `file_new_hire_report` is true and will be ignored for `Business` contractors.

##### ssn: `str`<a id="ssn-str"></a>

This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors. Social security number is needed to file the annual 1099 tax form.

##### business_name: `str`<a id="business_name-str"></a>

The name of the contractor business. This attribute is required for `Business` contractors and will be ignored for `Individual` contractors.

##### ein: `str`<a id="ein-str"></a>

The employer identification number of the contractor business. This attribute is optional for `Business` contractors and will be ignored for `Individual` contractors.

##### is_active: `bool`<a id="is_active-bool"></a>

The status of the contractor.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContractorsCreateIndividualOrBusinessRequest`](./gusto_app_integrations_python_sdk/type/contractors_create_individual_or_business_request.py)
Create an individual or business contractor.

#### 🔄 Return<a id="🔄-return"></a>

[`Contractor`](./gusto_app_integrations_python_sdk/pydantic/contractor.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/contractors` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.contractors.get_all`<a id="gustoappintegrationscontractorsget_all"></a>

Get all contractors, active and inactive, individual and business, for a company.

scope: `contractors:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = gustoappintegrations.contractors.get_all(
    company_id="company_id_example",
    page=3.14,
    per=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`ContractorsGetAllResponse`](./gusto_app_integrations_python_sdk/pydantic/contractors_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/contractors` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.contractors.get_details`<a id="gustoappintegrationscontractorsget_details"></a>

Get a contractor.

scope: `contractors:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = gustoappintegrations.contractors.get_details(
    contractor_id="contractor_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_id: `str`<a id="contractor_id-str"></a>

The UUID of the contractor

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Contractor`](./gusto_app_integrations_python_sdk/pydantic/contractor.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.contractors.update_contractor`<a id="gustoappintegrationscontractorsupdate_contractor"></a>

Update a contractor.

scope: `contractors:write`

> 🚧 Warning
>
> Watch out when changing a contractor's type (when the contractor is finished onboarding). Specifically, changing contractor type can be dangerous since Gusto won’t recognize and file two separate 1099s if they simply change from business to individual

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_contractor_response = gustoappintegrations.contractors.update_contractor(
    body=None,
    contractor_id="contractor_id_example",
    version="string_example",
    type="Individual",
    wage_type="Fixed",
    start_date="2020-01-11",
    hourly_rate="40.0",
    self_onboarding=False,
    email="string_example",
    first_name="string_example",
    last_name="string_example",
    middle_initial="string_example",
    file_new_hire_report=False,
    work_state="string_example",
    ssn="048072888",
    business_name="string_example",
    ein="string_example",
    is_active=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contractor_id: `str`<a id="contractor_id-str"></a>

The UUID of the contractor

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.

##### type: `str`<a id="type-str"></a>

The contractor type.

##### wage_type: `str`<a id="wage_type-str"></a>

The contractor’s wage type. 

##### start_date: `str`<a id="start_date-str"></a>

The day when the contractor will start working for the company. 

##### hourly_rate: `str`<a id="hourly_rate-str"></a>

The contractor’s hourly rate. This attribute is required if the wage_type is `Hourly`.

##### self_onboarding: `bool`<a id="self_onboarding-bool"></a>

Whether the contractor or the payroll admin will complete onboarding in Gusto. Self-onboarding is recommended so that contractors receive Gusto accounts. If self_onboarding is true, then email is required.

##### email: `str`<a id="email-str"></a>

The contractor’s email address.

##### first_name: `str`<a id="first_name-str"></a>

The contractor’s first name. This attribute is required for `Individual` contractors and will be ignored for `Business` contractors.

##### last_name: `str`<a id="last_name-str"></a>

The contractor’s last name. This attribute is required for `Individual` contractors and will be ignored for `Business` contractors.

##### middle_initial: `str`<a id="middle_initial-str"></a>

The contractor’s middle initial. This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.

##### file_new_hire_report: `bool`<a id="file_new_hire_report-bool"></a>

The boolean flag indicating whether Gusto will file a new hire report for the contractor. This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.

##### work_state: `Optional[str]`<a id="work_state-optionalstr"></a>

State where the contractor will be conducting the majority of their work for the company. This value is used when generating the new hire report. This attribute is required for `Individual` contractors if `file_new_hire_report` is true and will be ignored for `Business` contractors.

##### ssn: `str`<a id="ssn-str"></a>

This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors. Social security number is needed to file the annual 1099 tax form.

##### business_name: `str`<a id="business_name-str"></a>

The name of the contractor business. This attribute is required for `Business` contractors and will be ignored for `Individual` contractors.

##### ein: `str`<a id="ein-str"></a>

The employer identification number of the contractor business. This attribute is optional for `Business` contractors and will be ignored for `Individual` contractors.

##### is_active: `bool`<a id="is_active-bool"></a>

The status of the contractor.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContractorsUpdateContractorRequest`](./gusto_app_integrations_python_sdk/type/contractors_update_contractor_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Contractor`](./gusto_app_integrations_python_sdk/pydantic/contractor.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contractors/{contractor_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.departments.add_people_to_department`<a id="gustoappintegrationsdepartmentsadd_people_to_department"></a>

Add employees and contractors to a department

scope: `departments:write`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_people_to_department_response = (
    gustoappintegrations.departments.add_people_to_department(
        department_uuid="department_uuid_example",
        version="string_example",
        employees=[None],
        contractors=[None],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### department_uuid: `str`<a id="department_uuid-str"></a>

The UUID of the department

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### employees: [`DepartmentsAddPeopleToDepartmentRequestEmployees`](./gusto_app_integrations_python_sdk/type/departments_add_people_to_department_request_employees.py)<a id="employees-departmentsaddpeopletodepartmentrequestemployeesgusto_app_integrations_python_sdktypedepartments_add_people_to_department_request_employeespy"></a>

##### contractors: [`DepartmentsAddPeopleToDepartmentRequestContractors`](./gusto_app_integrations_python_sdk/type/departments_add_people_to_department_request_contractors.py)<a id="contractors-departmentsaddpeopletodepartmentrequestcontractorsgusto_app_integrations_python_sdktypedepartments_add_people_to_department_request_contractorspy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DepartmentsAddPeopleToDepartmentRequest`](./gusto_app_integrations_python_sdk/type/departments_add_people_to_department_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Department`](./gusto_app_integrations_python_sdk/pydantic/department.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/departments/{department_uuid}/add` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.departments.create_department`<a id="gustoappintegrationsdepartmentscreate_department"></a>

Create a department

scope: `departments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_department_response = gustoappintegrations.departments.create_department(
    company_uuid="company_uuid_example",
    title="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### title: `str`<a id="title-str"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DepartmentsCreateDepartmentRequest`](./gusto_app_integrations_python_sdk/type/departments_create_department_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Department`](./gusto_app_integrations_python_sdk/pydantic/department.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/departments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.departments.delete_department`<a id="gustoappintegrationsdepartmentsdelete_department"></a>

Delete a department. You cannot delete a department until all employees and contractors have been removed.

scope: `departments:write`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoappintegrations.departments.delete_department(
    department_uuid="department_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### department_uuid: `str`<a id="department_uuid-str"></a>

The UUID of the department

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/departments/{department_uuid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.departments.get_by_uuid`<a id="gustoappintegrationsdepartmentsget_by_uuid"></a>

Get a department given the UUID

scope: `departments:read`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_uuid_response = gustoappintegrations.departments.get_by_uuid(
    department_uuid="department_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### department_uuid: `str`<a id="department_uuid-str"></a>

The UUID of the department

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Department`](./gusto_app_integrations_python_sdk/pydantic/department.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/departments/{department_uuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.departments.list_for_company`<a id="gustoappintegrationsdepartmentslist_for_company"></a>

Get all of the departments for a given company with the employees and contractors assigned to that department.

scope: `departments:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_for_company_response = gustoappintegrations.departments.list_for_company(
    company_uuid="company_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_uuid: `str`<a id="company_uuid-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentsListForCompanyResponse`](./gusto_app_integrations_python_sdk/pydantic/departments_list_for_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_uuid}/departments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.departments.remove_employees`<a id="gustoappintegrationsdepartmentsremove_employees"></a>

Remove employees and contractors from a department

scope: `departments:write`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_employees_response = gustoappintegrations.departments.remove_employees(
    department_uuid="department_uuid_example",
    version="string_example",
    employees=[None],
    contractors=[None],
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### department_uuid: `str`<a id="department_uuid-str"></a>

The UUID of the department

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### employees: [`DepartmentsRemoveEmployeesRequestEmployees`](./gusto_app_integrations_python_sdk/type/departments_remove_employees_request_employees.py)<a id="employees-departmentsremoveemployeesrequestemployeesgusto_app_integrations_python_sdktypedepartments_remove_employees_request_employeespy"></a>

##### contractors: [`DepartmentsRemoveEmployeesRequestContractors`](./gusto_app_integrations_python_sdk/type/departments_remove_employees_request_contractors.py)<a id="contractors-departmentsremoveemployeesrequestcontractorsgusto_app_integrations_python_sdktypedepartments_remove_employees_request_contractorspy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DepartmentsRemoveEmployeesRequest`](./gusto_app_integrations_python_sdk/type/departments_remove_employees_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Department`](./gusto_app_integrations_python_sdk/pydantic/department.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/departments/{department_uuid}/remove` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.departments.update_department`<a id="gustoappintegrationsdepartmentsupdate_department"></a>

Update a department

scope: `departments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_department_response = gustoappintegrations.departments.update_department(
    version="string_example",
    department_uuid="department_uuid_example",
    title="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### department_uuid: `str`<a id="department_uuid-str"></a>

The UUID of the department

##### title: `str`<a id="title-str"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DepartmentsUpdateDepartmentRequest`](./gusto_app_integrations_python_sdk/type/departments_update_department_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Department`](./gusto_app_integrations_python_sdk/pydantic/department.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/departments/{department_uuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.earning_types.create_custom_earning_type`<a id="gustoappintegrationsearning_typescreate_custom_earning_type"></a>

Create a custom earning type.

If an inactive earning type exists with the same name, this will reactivate it instead of creating a new one.

scope: `payrolls:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_custom_earning_type_response = (
    gustoappintegrations.earning_types.create_custom_earning_type(
        name="string_example",
        company_id="company_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the custom earning type.

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EarningTypesCreateCustomEarningTypeRequest`](./gusto_app_integrations_python_sdk/type/earning_types_create_custom_earning_type_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EarningType`](./gusto_app_integrations_python_sdk/pydantic/earning_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/earning_types` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.earning_types.deactivate`<a id="gustoappintegrationsearning_typesdeactivate"></a>

Deactivate an earning type.

scope: `payrolls:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoappintegrations.earning_types.deactivate(
    company_id="company_id_example",
    earning_type_uuid="earning_type_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### earning_type_uuid: `str`<a id="earning_type_uuid-str"></a>

The UUID of the earning type

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/earning_types/{earning_type_uuid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.earning_types.get_all`<a id="gustoappintegrationsearning_typesget_all"></a>

A payroll item in Gusto is associated to an earning type to name the type of earning described by the payroll item.

#### Default Earning Type<a id="default-earning-type"></a>
Certain earning types are special because they have tax considerations. Those earning types are mostly the same for every company depending on its legal structure (LLC, Corporation, etc.)

#### Custom Earning Type<a id="custom-earning-type"></a>
Custom earning types are all the other earning types added specifically for a company.

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = gustoappintegrations.earning_types.get_all(
    company_id="company_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EarningTypesGetAllResponse`](./gusto_app_integrations_python_sdk/pydantic/earning_types_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/earning_types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.earning_types.update_type_by_id`<a id="gustoappintegrationsearning_typesupdate_type_by_id"></a>

Update an earning type.

scope: `payrolls:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_type_by_id_response = gustoappintegrations.earning_types.update_type_by_id(
    company_id="company_id_example",
    earning_type_uuid="earning_type_uuid_example",
    name="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### earning_type_uuid: `str`<a id="earning_type_uuid-str"></a>

The UUID of the earning type

##### name: `str`<a id="name-str"></a>

The name of the custom earning type.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EarningTypesUpdateTypeByIdRequest`](./gusto_app_integrations_python_sdk/type/earning_types_update_type_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EarningType`](./gusto_app_integrations_python_sdk/pydantic/earning_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/earning_types/{earning_type_uuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_addresses.create_home_address`<a id="gustoappintegrationsemployee_addressescreate_home_address"></a>

The home address of an employee is used to determine certain tax information about them. Addresses are geocoded on create and update to ensure validity.

Supports home address effective dating and courtesy withholding.

scope: `employees:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_home_address_response = (
    gustoappintegrations.employee_addresses.create_home_address(
        employee_id="employee_id_example",
        street_1="string_example",
        street_2="string_example",
        city="string_example",
        state="string_example",
        zip="string_example",
        effective_date="1970-01-01",
        courtesy_withholding=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### street_1: `str`<a id="street_1-str"></a>

##### street_2: `Optional[str]`<a id="street_2-optionalstr"></a>

##### city: `str`<a id="city-str"></a>

##### state: `str`<a id="state-str"></a>

##### zip: `str`<a id="zip-str"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### courtesy_withholding: `bool`<a id="courtesy_withholding-bool"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeAddressesCreateHomeAddressRequest`](./gusto_app_integrations_python_sdk/type/employee_addresses_create_home_address_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeAddress`](./gusto_app_integrations_python_sdk/pydantic/employee_address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/home_addresses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_addresses.create_work_address`<a id="gustoappintegrationsemployee_addressescreate_work_address"></a>

The work address of an employee describes when an employee began working at an associated company location.

scope: `employees:manage`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_work_address_response = (
    gustoappintegrations.employee_addresses.create_work_address(
        employee_id="employee_id_example",
        location_uuid="string_example",
        effective_date="1970-01-01",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### location_uuid: `str`<a id="location_uuid-str"></a>

Reference to a company location

##### effective_date: `date`<a id="effective_date-date"></a>

Date the employee began working at the company location

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeAddressesCreateWorkAddressRequest`](./gusto_app_integrations_python_sdk/type/employee_addresses_create_work_address_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeWorkAddress`](./gusto_app_integrations_python_sdk/pydantic/employee_work_address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/work_addresses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_addresses.delete_employee_home_address`<a id="gustoappintegrationsemployee_addressesdelete_employee_home_address"></a>

Used for deleting an employee's home address.  Cannot delete the employee's active home address.

scope: `employees:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoappintegrations.employee_addresses.delete_employee_home_address(
    home_address_uuid="home_address_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### home_address_uuid: `str`<a id="home_address_uuid-str"></a>

The UUID of the home address

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/home_addresses/{home_address_uuid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_addresses.delete_employee_work_address`<a id="gustoappintegrationsemployee_addressesdelete_employee_work_address"></a>

Used for deleting an employee's work address.  Cannot delete the employee's active work address.

scope: `employees:manage`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoappintegrations.employee_addresses.delete_employee_work_address(
    work_address_uuid="work_address_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### work_address_uuid: `str`<a id="work_address_uuid-str"></a>

The UUID of the work address

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/work_addresses/{work_address_uuid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_addresses.get`<a id="gustoappintegrationsemployee_addressesget"></a>

The work address of an employee is used for payroll tax purposes.

scope: `employees:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = gustoappintegrations.employee_addresses.get(
    work_address_uuid="work_address_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### work_address_uuid: `str`<a id="work_address_uuid-str"></a>

The UUID of the work address

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeWorkAddress`](./gusto_app_integrations_python_sdk/pydantic/employee_work_address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/work_addresses/{work_address_uuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_addresses.get_home_address`<a id="gustoappintegrationsemployee_addressesget_home_address"></a>

The home address of an employee is used to determine certain tax information about them. Addresses are geocoded on create and update to ensure validity.

Supports home address effective dating and courtesy withholding.

scope: `employees:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_home_address_response = gustoappintegrations.employee_addresses.get_home_address(
    home_address_uuid="home_address_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### home_address_uuid: `str`<a id="home_address_uuid-str"></a>

The UUID of the home address

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeAddress`](./gusto_app_integrations_python_sdk/pydantic/employee_address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/home_addresses/{home_address_uuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_addresses.get_home_addresses`<a id="gustoappintegrationsemployee_addressesget_home_addresses"></a>

The home address of an employee is used to determine certain tax information about them. Addresses are geocoded on create and update to ensure validity.

Supports home address effective dating and courtesy withholding.

scope: `employees:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_home_addresses_response = (
    gustoappintegrations.employee_addresses.get_home_addresses(
        employee_id="employee_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeAddressesGetHomeAddressesResponse`](./gusto_app_integrations_python_sdk/pydantic/employee_addresses_get_home_addresses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/home_addresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_addresses.get_work_addresses`<a id="gustoappintegrationsemployee_addressesget_work_addresses"></a>

Returns a list of an employee's work addresses. Each address includes its effective date and a boolean
signifying if it is the currently active work address.

scope: `employees:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_addresses_response = (
    gustoappintegrations.employee_addresses.get_work_addresses(
        employee_id="employee_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeAddressesGetWorkAddressesResponse`](./gusto_app_integrations_python_sdk/pydantic/employee_addresses_get_work_addresses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/work_addresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_addresses.update_home_address`<a id="gustoappintegrationsemployee_addressesupdate_home_address"></a>

The home address of an employee is used to determine certain tax information about them. Addresses are geocoded on create and update to ensure validity.

Supports home address effective dating and courtesy withholding.

scope: `employees:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_home_address_response = (
    gustoappintegrations.employee_addresses.update_home_address(
        version="string_example",
        home_address_uuid="home_address_uuid_example",
        street_1="string_example",
        street_2="string_example",
        city="string_example",
        state="string_example",
        zip="string_example",
        effective_date="1970-01-01",
        courtesy_withholding=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### home_address_uuid: `str`<a id="home_address_uuid-str"></a>

The UUID of the home address

##### street_1: `str`<a id="street_1-str"></a>

##### street_2: `Optional[str]`<a id="street_2-optionalstr"></a>

##### city: `str`<a id="city-str"></a>

##### state: `str`<a id="state-str"></a>

##### zip: `str`<a id="zip-str"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### courtesy_withholding: `bool`<a id="courtesy_withholding-bool"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeAddressesUpdateHomeAddressRequest`](./gusto_app_integrations_python_sdk/type/employee_addresses_update_home_address_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeAddress`](./gusto_app_integrations_python_sdk/pydantic/employee_address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/home_addresses/{home_address_uuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_addresses.update_work_address`<a id="gustoappintegrationsemployee_addressesupdate_work_address"></a>

The work address of an employee is used for payroll tax purposes.

scope: `employees:manage`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_work_address_response = (
    gustoappintegrations.employee_addresses.update_work_address(
        work_address_uuid="work_address_uuid_example",
        version="string_example",
        location_uuid="string_example",
        effective_date="1970-01-01",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### work_address_uuid: `str`<a id="work_address_uuid-str"></a>

The UUID of the work address

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### location_uuid: `str`<a id="location_uuid-str"></a>

Reference to a company location

##### effective_date: `date`<a id="effective_date-date"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeAddressesUpdateWorkAddressRequest`](./gusto_app_integrations_python_sdk/type/employee_addresses_update_work_address_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeWorkAddress`](./gusto_app_integrations_python_sdk/pydantic/employee_work_address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/work_addresses/{work_address_uuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_benefits.create_benefit`<a id="gustoappintegrationsemployee_benefitscreate_benefit"></a>

Employee benefits represent an employee enrolled in a particular company benefit. It includes information specific to that employee’s enrollment.

scope: `employee_benefits:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_benefit_response = gustoappintegrations.employee_benefits.create_benefit(
    company_benefit_uuid="string_example",
    employee_id="employee_id_example",
    active=True,
    employee_deduction="0.00",
    deduct_as_percentage=False,
    employee_deduction_annual_maximum="string_example",
    contribution={
        "type": "tiered",
    },
    elective=False,
    company_contribution_annual_maximum="string_example",
    limit_option="string_example",
    catch_up=False,
    coverage_amount="string_example",
    coverage_salary_multiplier="0.00",
    deduction_reduces_taxable_income="unset",
    company_contribution="0.00",
    contribute_as_percentage=False,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_benefit_uuid: `str`<a id="company_benefit_uuid-str"></a>

The UUID of the company benefit.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### active: `bool`<a id="active-bool"></a>

Whether the employee benefit is active.

##### employee_deduction: `str`<a id="employee_deduction-str"></a>

The amount to be deducted, per pay period, from the employee's pay.

##### deduct_as_percentage: `bool`<a id="deduct_as_percentage-bool"></a>

Whether the employee deduction amount should be treated as a percentage to be deducted from each payroll.

##### employee_deduction_annual_maximum: `Optional[str]`<a id="employee_deduction_annual_maximum-optionalstr"></a>

The maximum employee deduction amount per year. A null value signifies no limit.

##### contribution: [`EmployeeBenefitsCreateBenefitRequestContribution`](./gusto_app_integrations_python_sdk/type/employee_benefits_create_benefit_request_contribution.py)<a id="contribution-employeebenefitscreatebenefitrequestcontributiongusto_app_integrations_python_sdktypeemployee_benefits_create_benefit_request_contributionpy"></a>


##### elective: `bool`<a id="elective-bool"></a>

Whether the company contribution is elective (aka \\\"matching\\\"). For `tiered`, `elective_amount`, and `elective_percentage` contribution types this is ignored and assumed to be `true`.

##### company_contribution_annual_maximum: `Optional[str]`<a id="company_contribution_annual_maximum-optionalstr"></a>

The maximum company contribution amount per year. A null value signifies no limit.

##### limit_option: `Optional[str]`<a id="limit_option-optionalstr"></a>

Some benefits require additional information to determine their limit. For example, for an HSA benefit, the limit option should be either \\\"Family\\\" or \\\"Individual\\\". For a Dependent Care FSA benefit, the limit option should be either \\\"Joint Filing or Single\\\" or \\\"Married and Filing Separately\\\".

##### catch_up: `bool`<a id="catch_up-bool"></a>

Whether the employee should use a benefit’s \\\"catch up\\\" rate. Only Roth 401k and 401k benefits use this value for employees over 50.

##### coverage_amount: `Optional[str]`<a id="coverage_amount-optionalstr"></a>

The amount that the employee is insured for. Note: company contribution cannot be present if coverage amount is set.

##### coverage_salary_multiplier: `str`<a id="coverage_salary_multiplier-str"></a>

The coverage amount as a multiple of the employee’s salary. Only applicable for Group Term Life benefits. Note: cannot be set if coverage amount is also set.

##### deduction_reduces_taxable_income: `Optional[str]`<a id="deduction_reduces_taxable_income-optionalstr"></a>

Whether the employee deduction reduces taxable income or not. Only valid for Group Term Life benefits. Note: when the value is not \\\"unset\\\", coverage amount and coverage salary multiplier are ignored.

##### company_contribution: `str`<a id="company_contribution-str"></a>

The amount to be paid, per pay period, by the company.

##### contribute_as_percentage: `bool`<a id="contribute_as_percentage-bool"></a>

Whether the company contribution amount should be treated as a percentage to be deducted from each payroll.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeBenefitsCreateBenefitRequest`](./gusto_app_integrations_python_sdk/type/employee_benefits_create_benefit_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeBenefit`](./gusto_app_integrations_python_sdk/pydantic/employee_benefit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/employee_benefits` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_benefits.create_ytd_benefit_amounts_from_different_company`<a id="gustoappintegrationsemployee_benefitscreate_ytd_benefit_amounts_from_different_company"></a>

Year-to-date benefit amounts from a different company represents the amount of money added to an employee's plan during a current year, made outside of the current contribution when they were employed at a different company.

This endpoint only supports passing outside contributions for 401(k) benefits.

scope: `employee_benefits:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoappintegrations.employee_benefits.create_ytd_benefit_amounts_from_different_company(
    tax_year=2000,
    ytd_employee_deduction_amount="0.00",
    ytd_company_contribution_amount="0.00",
    employee_id="employee_id_example",
    benefit_type=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tax_year: `Union[int, float]`<a id="tax_year-unionint-float"></a>

The tax year for which this amount applies.

##### ytd_employee_deduction_amount: `str`<a id="ytd_employee_deduction_amount-str"></a>

The year-to-date employee deduction made outside the current company.

##### ytd_company_contribution_amount: `str`<a id="ytd_company_contribution_amount-str"></a>

The year-to-date company contribution made outside the current company.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### benefit_type: `Union[int, float]`<a id="benefit_type-unionint-float"></a>

The benefit type supported by Gusto.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeBenefitsCreateYtdBenefitAmountsFromDifferentCompanyRequest`](./gusto_app_integrations_python_sdk/type/employee_benefits_create_ytd_benefit_amounts_from_different_company_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/ytd_benefit_amounts_from_different_company` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_benefits.get_all_for_employee`<a id="gustoappintegrationsemployee_benefitsget_all_for_employee"></a>

Employee benefits represent an employee enrolled in a particular company benefit. It includes information specific to that employee’s enrollment.

Returns an array of all employee benefits for this employee

Benefits containing PHI are only visible to applications with the `employee_benefits:read:phi` scope.

scope: `employee_benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_for_employee_response = (
    gustoappintegrations.employee_benefits.get_all_for_employee(
        employee_id="employee_id_example",
        page=3.14,
        per=3.14,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeBenefitsGetAllForEmployeeResponse`](./gusto_app_integrations_python_sdk/pydantic/employee_benefits_get_all_for_employee_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/employee_benefits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_benefits.get_by_id`<a id="gustoappintegrationsemployee_benefitsget_by_id"></a>

Employee benefits represent an employee enrolled in a particular company benefit. It includes information specific to that employee’s enrollment.

Benefits containing PHI are only visible to applications with the `employee_benefits:read:phi` scope.

scope: `employee_benefits:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = gustoappintegrations.employee_benefits.get_by_id(
    employee_benefit_id="employee_benefit_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_benefit_id: `str`<a id="employee_benefit_id-str"></a>

The UUID of the employee benefit.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeBenefit`](./gusto_app_integrations_python_sdk/pydantic/employee_benefit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employee_benefits/{employee_benefit_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_benefits.remove_benefit`<a id="gustoappintegrationsemployee_benefitsremove_benefit"></a>

Employee benefits represent an employee enrolled in a particular company benefit. It includes information specific to that employee’s enrollment.

scope: `employee_benefits:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoappintegrations.employee_benefits.remove_benefit(
    employee_benefit_id="employee_benefit_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_benefit_id: `str`<a id="employee_benefit_id-str"></a>

The UUID of the employee benefit.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employee_benefits/{employee_benefit_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_benefits.update_benefit`<a id="gustoappintegrationsemployee_benefitsupdate_benefit"></a>

Employee benefits represent an employee enrolled in a particular company benefit. It includes information specific to that employee’s enrollment.

scope: `employee_benefits:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_benefit_response = gustoappintegrations.employee_benefits.update_benefit(
    version="string_example",
    employee_benefit_id="employee_benefit_id_example",
    active=True,
    employee_deduction="0.00",
    deduct_as_percentage=True,
    employee_deduction_annual_maximum="string_example",
    contribution={
        "type": "amount",
    },
    elective=False,
    company_contribution_annual_maximum="string_example",
    limit_option="string_example",
    catch_up=False,
    coverage_amount="string_example",
    deduction_reduces_taxable_income="unset",
    coverage_salary_multiplier="0.00",
    company_contribution="0.00",
    contribute_as_percentage=False,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### employee_benefit_id: `str`<a id="employee_benefit_id-str"></a>

The UUID of the employee benefit.

##### active: `bool`<a id="active-bool"></a>

Whether the employee benefit is active.

##### employee_deduction: `str`<a id="employee_deduction-str"></a>

The amount to be deducted, per pay period, from the employee's pay.

##### deduct_as_percentage: `bool`<a id="deduct_as_percentage-bool"></a>

Whether the employee deduction amount should be treated as a percentage to be deducted from each payroll.

##### employee_deduction_annual_maximum: `Optional[str]`<a id="employee_deduction_annual_maximum-optionalstr"></a>

The maximum employee deduction amount per year. A null value signifies no limit.

##### contribution: [`EmployeeBenefitsUpdateBenefitRequestContribution`](./gusto_app_integrations_python_sdk/type/employee_benefits_update_benefit_request_contribution.py)<a id="contribution-employeebenefitsupdatebenefitrequestcontributiongusto_app_integrations_python_sdktypeemployee_benefits_update_benefit_request_contributionpy"></a>


##### elective: `bool`<a id="elective-bool"></a>

Whether the company contribution is elective (aka \\\"matching\\\"). For `tiered`, `elective_amount`, and `elective_percentage` contribution types this is ignored and assumed to be `true`.

##### company_contribution_annual_maximum: `Optional[str]`<a id="company_contribution_annual_maximum-optionalstr"></a>

The maximum company contribution amount per year. A null value signifies no limit.

##### limit_option: `Optional[str]`<a id="limit_option-optionalstr"></a>

Some benefits require additional information to determine their limit. For example, for an HSA benefit, the limit option should be either \\\"Family\\\" or \\\"Individual\\\". For a Dependent Care FSA benefit, the limit option should be either \\\"Joint Filing or Single\\\" or \\\"Married and Filing Separately\\\".

##### catch_up: `bool`<a id="catch_up-bool"></a>

Whether the employee should use a benefit’s \\\"catch up\\\" rate. Only Roth 401k and 401k benefits use this value for employees over 50.

##### coverage_amount: `Optional[str]`<a id="coverage_amount-optionalstr"></a>

The amount that the employee is insured for. Note: company contribution cannot be present if coverage amount is set.

##### deduction_reduces_taxable_income: `Optional[str]`<a id="deduction_reduces_taxable_income-optionalstr"></a>

Whether the employee deduction reduces taxable income or not. Only valid for Group Term Life benefits. Note: when the value is not \\\"unset\\\", coverage amount and coverage salary multiplier are ignored.

##### coverage_salary_multiplier: `str`<a id="coverage_salary_multiplier-str"></a>

The coverage amount as a multiple of the employee’s salary. Only applicable for Group Term Life benefits. Note: cannot be set if coverage amount is also set.

##### company_contribution: `str`<a id="company_contribution-str"></a>

The amount to be paid, per pay period, by the company.

##### contribute_as_percentage: `bool`<a id="contribute_as_percentage-bool"></a>

Whether the company contribution amount should be treated as a percentage to be deducted from each payroll.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeBenefitsUpdateBenefitRequest`](./gusto_app_integrations_python_sdk/type/employee_benefits_update_benefit_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeBenefit`](./gusto_app_integrations_python_sdk/pydantic/employee_benefit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employee_benefits/{employee_benefit_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_employments.create_rehire`<a id="gustoappintegrationsemployee_employmentscreate_rehire"></a>

Rehire is created whenever an employee is scheduled to return to the company.

scope: `employments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_rehire_response = gustoappintegrations.employee_employments.create_rehire(
    effective_date="string_example",
    file_new_hire_report=True,
    work_location_uuid="string_example",
    employee_id="employee_id_example",
    employment_status="part_time",
    two_percent_shareholder=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `str`<a id="effective_date-str"></a>

The day when the employee returns to work.

##### file_new_hire_report: `bool`<a id="file_new_hire_report-bool"></a>

The boolean flag indicating whether Gusto will file a new hire report for the employee.

##### work_location_uuid: `str`<a id="work_location_uuid-str"></a>

The uuid of the employee's work location.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### employment_status: `str`<a id="employment_status-str"></a>

The employee's employment status. Supplying an invalid option will set the employment_status to *not_set*.

##### two_percent_shareholder: `bool`<a id="two_percent_shareholder-bool"></a>

Whether the employee is a two percent shareholder of the company. This field only applies to companies with an S-Corp entity type.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RehireBody`](./gusto_app_integrations_python_sdk/type/rehire_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Rehire`](./gusto_app_integrations_python_sdk/pydantic/rehire.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/rehire` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_employments.create_termination`<a id="gustoappintegrationsemployee_employmentscreate_termination"></a>

Terminations are created whenever an employee is scheduled to leave the company. The only things required are an effective date (their last day of work) and whether they should receive their wages in a one-off termination payroll or with the rest of the company.

Note that some states require employees to receive their final wages within 24 hours (unless they consent otherwise,) in which case running a one-off payroll may be the only option.

scope: `employments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_termination_response = (
    gustoappintegrations.employee_employments.create_termination(
        effective_date="string_example",
        employee_id="employee_id_example",
        run_termination_payroll=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `str`<a id="effective_date-str"></a>

The employee's last day of work.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### run_termination_payroll: `bool`<a id="run_termination_payroll-bool"></a>

If true, the employee should receive their final wages via an off-cycle payroll. If false, they should receive their final wages on their current pay schedule.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeEmploymentsCreateTerminationRequest`](./gusto_app_integrations_python_sdk/type/employee_employments_create_termination_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Termination`](./gusto_app_integrations_python_sdk/pydantic/termination.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/terminations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_employments.delete_rehire`<a id="gustoappintegrationsemployee_employmentsdelete_rehire"></a>

Delete an employee rehire. An employee rehire cannot be deleted if it's active (past effective date).

scope: `employments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoappintegrations.employee_employments.delete_rehire(
    employee_id="employee_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/rehire` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_employments.delete_termination`<a id="gustoappintegrationsemployee_employmentsdelete_termination"></a>

Delete an employee termination.

scope: `employments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoappintegrations.employee_employments.delete_termination(
    employee_id="employee_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/terminations` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_employments.get_history`<a id="gustoappintegrationsemployee_employmentsget_history"></a>

Retrieve the employment history for a given employee, which includes termination and rehire.

scope: `employments:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_history_response = gustoappintegrations.employee_employments.get_history(
    employee_id="employee_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeEmploymentsGetHistoryResponse`](./gusto_app_integrations_python_sdk/pydantic/employee_employments_get_history_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/employment_history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_employments.get_rehire_info`<a id="gustoappintegrationsemployee_employmentsget_rehire_info"></a>

Retrieve an employee's rehire, which contains information on when the employee returns to work.

scope: `employments:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_rehire_info_response = gustoappintegrations.employee_employments.get_rehire_info(
    employee_id="employee_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Rehire`](./gusto_app_integrations_python_sdk/pydantic/rehire.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/rehire` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_employments.list_terminations_for_employee`<a id="gustoappintegrationsemployee_employmentslist_terminations_for_employee"></a>

Terminations are created whenever an employee is scheduled to leave the company. The only things required are an effective date (their last day of work) and whether they should receive their wages in a one-off termination payroll or with the rest of the company.

Note that some states require employees to receive their final wages within 24 hours (unless they consent otherwise,) in which case running a one-off payroll may be the only option.

scope: `employments:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_terminations_for_employee_response = (
    gustoappintegrations.employee_employments.list_terminations_for_employee(
        employee_id="employee_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeEmploymentsListTerminationsForEmployeeResponse`](./gusto_app_integrations_python_sdk/pydantic/employee_employments_list_terminations_for_employee_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/terminations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_employments.update_rehire`<a id="gustoappintegrationsemployee_employmentsupdate_rehire"></a>

Update an employee's rehire.

scope: `employments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_rehire_response = gustoappintegrations.employee_employments.update_rehire(
    body=None,
    employee_id="employee_id_example",
    version="string_example",
    effective_date="string_example",
    file_new_hire_report=True,
    work_location_uuid="string_example",
    employment_status="part_time",
    two_percent_shareholder=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.

##### effective_date: `str`<a id="effective_date-str"></a>

The day when the employee returns to work.

##### file_new_hire_report: `bool`<a id="file_new_hire_report-bool"></a>

The boolean flag indicating whether Gusto will file a new hire report for the employee.

##### work_location_uuid: `str`<a id="work_location_uuid-str"></a>

The uuid of the employee's work location.

##### employment_status: `str`<a id="employment_status-str"></a>

The employee's employment status. Supplying an invalid option will set the employment_status to *not_set*.

##### two_percent_shareholder: `bool`<a id="two_percent_shareholder-bool"></a>

Whether the employee is a two percent shareholder of the company. This field only applies to companies with an S-Corp entity type.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeEmploymentsUpdateRehireRequest`](./gusto_app_integrations_python_sdk/type/employee_employments_update_rehire_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Rehire`](./gusto_app_integrations_python_sdk/pydantic/rehire.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/rehire` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employee_employments.update_termination`<a id="gustoappintegrationsemployee_employmentsupdate_termination"></a>

Terminations are created whenever an employee is scheduled to leave the company. The only things required are an effective date (their last day of work) and whether they should receive their wages in a one-off termination payroll or with the rest of the company.

Note that some states require employees to receive their final wages within 24 hours (unless they consent otherwise,) in which case running a one-off payroll may be the only option.

scope: `employments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_termination_response = (
    gustoappintegrations.employee_employments.update_termination(
        body=None,
        employee_id="employee_id_example",
        version="string_example",
        effective_date="string_example",
        run_termination_payroll=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.

##### effective_date: `str`<a id="effective_date-str"></a>

The employee's last day of work.

##### run_termination_payroll: `bool`<a id="run_termination_payroll-bool"></a>

If true, the employee should receive their final wages via an off-cycle payroll. If false, they should receive their final wages on their current pay schedule.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeEmploymentsUpdateTerminationRequest`](./gusto_app_integrations_python_sdk/type/employee_employments_update_termination_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Termination`](./gusto_app_integrations_python_sdk/pydantic/termination.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/terminations/{employee_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employees.create_employee`<a id="gustoappintegrationsemployeescreate_employee"></a>

Create an employee.

scope: `employees:manage`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_employee_response = gustoappintegrations.employees.create_employee(
    first_name="string_example",
    last_name="string_example",
    company_id="company_id_example",
    middle_initial="string_example",
    date_of_birth="string_example",
    email="string_example",
    ssn="048072888",
    self_onboarding=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### middle_initial: `str`<a id="middle_initial-str"></a>

##### date_of_birth: `str`<a id="date_of_birth-str"></a>

##### email: `str`<a id="email-str"></a>

##### ssn: `str`<a id="ssn-str"></a>

##### self_onboarding: `bool`<a id="self_onboarding-bool"></a>

If true, employee is expected to self-onboard. If false, payroll admin is expected to enter in the employee's onboarding information

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeesCreateEmployeeRequest`](./gusto_app_integrations_python_sdk/type/employees_create_employee_request.py)
Create an employee.

#### 🔄 Return<a id="🔄-return"></a>

[`Employee`](./gusto_app_integrations_python_sdk/pydantic/employee.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/employees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employees.delete_onboarding_employee`<a id="gustoappintegrationsemployeesdelete_onboarding_employee"></a>

Use this endpoint to delete an employee who is in onboarding. Deleting
an onboarded employee is not allowed. Please check out the Terminations api
if you need to terminate an onboarded employee.

scope: `employees:manage`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoappintegrations.employees.delete_onboarding_employee(
    employee_id="employee_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employees.get_company_employees`<a id="gustoappintegrationsemployeesget_company_employees"></a>

Get all of the employees, onboarding, active and terminated, for a given company.

scope: `employees:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_employees_response = gustoappintegrations.employees.get_company_employees(
    company_id="company_id_example",
    terminated=True,
    include="all_compensations",
    page=3.14,
    per=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### terminated: `bool`<a id="terminated-bool"></a>

Filters employees by the provided boolean

##### include: `str`<a id="include-str"></a>

Include the requested attribute(s) in each employee response, multiple options are comma separated. Available options: - all_compensations: Include all effective dated compensations for each job instead of only the current compensation - custom_fields: Include employees' custom fields

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesGetCompanyEmployeesResponse`](./gusto_app_integrations_python_sdk/pydantic/employees_get_company_employees_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/employees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employees.get_custom_fields`<a id="gustoappintegrationsemployeesget_custom_fields"></a>

Returns a list of the employee's custom fields.

scope: `employees:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_fields_response = gustoappintegrations.employees.get_custom_fields(
    employee_id="employee_id_example",
    page=3.14,
    per=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesGetCustomFieldsResponse`](./gusto_app_integrations_python_sdk/pydantic/employees_get_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/custom_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employees.get_details`<a id="gustoappintegrationsemployeesget_details"></a>

Get an employee.

scope: `employees:read`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = gustoappintegrations.employees.get_details(
    employee_id="employee_id_example",
    include="all_compensations",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### include: `str`<a id="include-str"></a>

Include the requested attribute(s) in each employee response, multiple options are comma separated. Available options: - all_compensations: Include all effective dated compensations for each job instead of only the current compensation - custom_fields: Include employees' custom fields

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Employee`](./gusto_app_integrations_python_sdk/pydantic/employee.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employees.get_time_off_activities`<a id="gustoappintegrationsemployeesget_time_off_activities"></a>

Get employee time off activities.

scope: `employee_time_off_activities:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_time_off_activities_response = (
    gustoappintegrations.employees.get_time_off_activities(
        employee_uuid="employee_uuid_example",
        time_off_type="time_off_type_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_uuid: `str`<a id="employee_uuid-str"></a>

The UUID of the employee

##### time_off_type: `str`<a id="time_off_type-str"></a>

The time off type name you want to query data for. ex: 'sick' or 'vacation'

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffActivity`](./gusto_app_integrations_python_sdk/pydantic/time_off_activity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_uuid}/time_off_activities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.employees.update_employee`<a id="gustoappintegrationsemployeesupdate_employee"></a>

Update an employee.

scope: `employees:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_employee_response = gustoappintegrations.employees.update_employee(
    version="string_example",
    employee_id="employee_id_example",
    first_name="string_example",
    middle_initial="string_example",
    last_name="string_example",
    date_of_birth="string_example",
    email="string_example",
    ssn="048072888",
    two_percent_shareholder=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### first_name: `str`<a id="first_name-str"></a>

##### middle_initial: `str`<a id="middle_initial-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### date_of_birth: `str`<a id="date_of_birth-str"></a>

##### email: `str`<a id="email-str"></a>

##### ssn: `str`<a id="ssn-str"></a>

##### two_percent_shareholder: `bool`<a id="two_percent_shareholder-bool"></a>

Whether the employee is a two percent shareholder of the company. This field only applies to companies with an S-Corp entity type.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeesUpdateEmployeeRequest`](./gusto_app_integrations_python_sdk/type/employees_update_employee_request.py)
Update an employee.

#### 🔄 Return<a id="🔄-return"></a>

[`Employee`](./gusto_app_integrations_python_sdk/pydantic/employee.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.events.get_all`<a id="gustoappintegrationseventsget_all"></a>

Fetch all events, going back up to 30 days, that your partner application has the required scopes for. Note that a partner does NOT have to have verified webhook subscriptions in order to utilize this endpoint.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `events:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = gustoappintegrations.events.get_all(
    starting_after_uuid="string_example",
    resource_uuid="string_example",
    limit="string_example",
    event_type="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### starting_after_uuid: `str`<a id="starting_after_uuid-str"></a>

A cursor for pagination. Returns all events occuring after the specified UUID (exclusive)

##### resource_uuid: `str`<a id="resource_uuid-str"></a>

The UUID of the company. If not specified, will return all events for all companies.

##### limit: `str`<a id="limit-str"></a>

Limits the number of objects returned in a single response, between 1 and 100. The default is 25

##### event_type: `str`<a id="event_type-str"></a>

A string containing the exact event name (e.g. `employee.created`), or use a wildcard match to filter for a group of events (e.g. `employee.*`, `*.created`, `notification.*.created` etc.)

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`EventsGetAllResponse`](./gusto_app_integrations_python_sdk/pydantic/events_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.garnishments.create_garnishment`<a id="gustoappintegrationsgarnishmentscreate_garnishment"></a>

Garnishments, or employee deductions, are fixed amounts or percentages deducted from an employee’s pay. They can be deducted a specific number of times or on a recurring basis. Garnishments can also have maximum deductions on a yearly or per-pay-period bases. Common uses for garnishments are court-ordered payments for child support or back taxes. Some companies provide loans to their employees that are repaid via garnishments.

scope: `garnishments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_garnishment_response = gustoappintegrations.garnishments.create_garnishment(
    description="string_example",
    amount="string_example",
    court_ordered=True,
    employee_id="employee_id_example",
    active=True,
    times=1,
    recurring=False,
    annual_maximum="string_example",
    pay_period_maximum="string_example",
    deduct_as_percentage=False,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

The description of the garnishment.

##### amount: `float`<a id="amount-float"></a>

The amount of the garnishment. Either a percentage or a fixed dollar amount. Represented as a float, e.g. \\\"8.00\\\".

##### court_ordered: `bool`<a id="court_ordered-bool"></a>

Whether the garnishment is court ordered.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### active: `bool`<a id="active-bool"></a>

Whether or not this garnishment is currently active.

##### times: `Optional[int]`<a id="times-optionalint"></a>

The number of times to apply the garnishment. Ignored if recurring is true.

##### recurring: `bool`<a id="recurring-bool"></a>

Whether the garnishment should recur indefinitely.

##### annual_maximum: `Optional[float]`<a id="annual_maximum-optionalfloat"></a>

The maximum deduction per annum. A null value indicates no maximum. Represented as a float, e.g. \\\"200.00\\\".

##### pay_period_maximum: `Optional[float]`<a id="pay_period_maximum-optionalfloat"></a>

The maximum deduction per pay period. A null value indicates no maximum. Represented as a float, e.g. \\\"16.00\\\".

##### deduct_as_percentage: `bool`<a id="deduct_as_percentage-bool"></a>

Whether the amount should be treated as a percentage to be deducted per pay period.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GarnishmentsCreateGarnishmentRequest`](./gusto_app_integrations_python_sdk/type/garnishments_create_garnishment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Garnishment`](./gusto_app_integrations_python_sdk/pydantic/garnishment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/garnishments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.garnishments.get`<a id="gustoappintegrationsgarnishmentsget"></a>

Garnishments, or employee deductions, are fixed amounts or percentages deducted from an employee’s pay. They can be deducted a specific number of times or on a recurring basis. Garnishments can also have maximum deductions on a yearly or per-pay-period bases. Common uses for garnishments are court-ordered payments for child support or back taxes. Some companies provide loans to their employees that are repaid via garnishments.

scope: `garnishments:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = gustoappintegrations.garnishments.get(
    garnishment_id="garnishment_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### garnishment_id: `str`<a id="garnishment_id-str"></a>

The UUID of the garnishment

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Garnishment`](./gusto_app_integrations_python_sdk/pydantic/garnishment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/garnishments/{garnishment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.garnishments.get_employee_garnishments`<a id="gustoappintegrationsgarnishmentsget_employee_garnishments"></a>

Garnishments, or employee deductions, are fixed amounts or percentages deducted from an employee’s pay. They can be deducted a specific number of times or on a recurring basis. Garnishments can also have maximum deductions on a yearly or per-pay-period bases. Common uses for garnishments are court-ordered payments for child support or back taxes. Some companies provide loans to their employees that are repaid via garnishments.

scope: `garnishments:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_garnishments_response = (
    gustoappintegrations.garnishments.get_employee_garnishments(
        employee_id="employee_id_example",
        page=3.14,
        per=3.14,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`GarnishmentsGetEmployeeGarnishmentsResponse`](./gusto_app_integrations_python_sdk/pydantic/garnishments_get_employee_garnishments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/garnishments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.garnishments.update`<a id="gustoappintegrationsgarnishmentsupdate"></a>

Garnishments, or employee deductions, are fixed amounts or percentages deducted from an employee’s pay. They can be deducted a specific number of times or on a recurring basis. Garnishments can also have maximum deductions on a yearly or per-pay-period bases. Common uses for garnishments are court-ordered payments for child support or back taxes. Some companies provide loans to their employees that are repaid via garnishments.

scope: `garnishments:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = gustoappintegrations.garnishments.update(
    version="string_example",
    garnishment_id="garnishment_id_example",
    description="string_example",
    active=True,
    amount="string_example",
    court_ordered=True,
    times=1,
    recurring=False,
    annual_maximum="string_example",
    pay_period_maximum="string_example",
    deduct_as_percentage=False,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### garnishment_id: `str`<a id="garnishment_id-str"></a>

The UUID of the garnishment

##### description: `str`<a id="description-str"></a>

The description of the garnishment.

##### active: `bool`<a id="active-bool"></a>

Whether or not this garnishment is currently active.

##### amount: `float`<a id="amount-float"></a>

The amount of the garnishment. Either a percentage or a fixed dollar amount. Represented as a float, e.g. \\\"8.00\\\".

##### court_ordered: `bool`<a id="court_ordered-bool"></a>

Whether the garnishment is court ordered.

##### times: `Optional[int]`<a id="times-optionalint"></a>

The number of times to apply the garnishment. Ignored if recurring is true.

##### recurring: `bool`<a id="recurring-bool"></a>

Whether the garnishment should recur indefinitely.

##### annual_maximum: `Optional[float]`<a id="annual_maximum-optionalfloat"></a>

The maximum deduction per annum. A null value indicates no maximum. Represented as a float, e.g. \\\"200.00\\\".

##### pay_period_maximum: `Optional[float]`<a id="pay_period_maximum-optionalfloat"></a>

The maximum deduction per pay period. A null value indicates no maximum. Represented as a float, e.g. \\\"16.00\\\".

##### deduct_as_percentage: `bool`<a id="deduct_as_percentage-bool"></a>

Whether the amount should be treated as a percentage to be deducted per pay period.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GarnishmentsUpdateRequest`](./gusto_app_integrations_python_sdk/type/garnishments_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Garnishment`](./gusto_app_integrations_python_sdk/pydantic/garnishment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/garnishments/{garnishment_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.introspection.access_token_info`<a id="gustoappintegrationsintrospectionaccess_token_info"></a>

Returns scope and resource information associated with the current access token.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
access_token_info_response = gustoappintegrations.introspection.access_token_info(
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`IntrospectionAccessTokenInfoResponse`](./gusto_app_integrations_python_sdk/pydantic/introspection_access_token_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/token_info` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.introspection.exchange_refresh_token`<a id="gustoappintegrationsintrospectionexchange_refresh_token"></a>

Exchange a refresh token for a new access token.

The previous `refresh_token` will be revoked on the first usage of the new `access_token`.

The `expires_in` value is provided in seconds from when the `access_token` was generated.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
exchange_refresh_token_response = (
    gustoappintegrations.introspection.exchange_refresh_token(
        client_id="string_example",
        client_secret="string_example",
        refresh_token="string_example",
        grant_type="string_example",
        redirect_uri="string_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_id: `str`<a id="client_id-str"></a>

Your client id

##### client_secret: `str`<a id="client_secret-str"></a>

Your client secret

##### refresh_token: `str`<a id="refresh_token-str"></a>

The `refresh_token` being exchanged for an access token code

##### grant_type: `str`<a id="grant_type-str"></a>

this should be the literal string 'refresh_token'

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

The redirect URI you set up via the Developer Portal

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IntrospectionExchangeRefreshTokenRequest`](./gusto_app_integrations_python_sdk/type/introspection_exchange_refresh_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Authentication`](./gusto_app_integrations_python_sdk/pydantic/authentication.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.jobs_and_compensations.create_compensation`<a id="gustoappintegrationsjobs_and_compensationscreate_compensation"></a>

Compensations contain information on how much is paid out for a job. Jobs may have many compensations, but only one that is active. The current compensation is the one with the most recent `effective_date`.

scope: `jobs:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_compensation_response = (
    gustoappintegrations.jobs_and_compensations.create_compensation(
        payment_unit="Hour",
        flsa_status="Nonexempt",
        job_id="job_id_example",
        rate="string_example",
        effective_date="string_example",
        adjust_for_minimum_wage=True,
        minimum_wages=[{}],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_unit: `str`<a id="payment_unit-str"></a>

The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'.

##### flsa_status: [`FlsaStatusType`](./gusto_app_integrations_python_sdk/type/flsa_status_type.py)<a id="flsa_status-flsastatustypegusto_app_integrations_python_sdktypeflsa_status_typepy"></a>

##### job_id: `str`<a id="job_id-str"></a>

The UUID of the job

##### rate: `str`<a id="rate-str"></a>

The dollar amount paid per payment unit.

##### effective_date: `str`<a id="effective_date-str"></a>

The date when the compensation takes effect.

##### adjust_for_minimum_wage: `bool`<a id="adjust_for_minimum_wage-bool"></a>

Determines whether the compensation should be adjusted for minimum wage. Only applies to Nonexempt employees.

##### minimum_wages: [`JobsAndCompensationsCreateCompensationRequestMinimumWages`](./gusto_app_integrations_python_sdk/type/jobs_and_compensations_create_compensation_request_minimum_wages.py)<a id="minimum_wages-jobsandcompensationscreatecompensationrequestminimumwagesgusto_app_integrations_python_sdktypejobs_and_compensations_create_compensation_request_minimum_wagespy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobsAndCompensationsCreateCompensationRequest`](./gusto_app_integrations_python_sdk/type/jobs_and_compensations_create_compensation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Compensation`](./gusto_app_integrations_python_sdk/pydantic/compensation.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/jobs/{job_id}/compensations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.jobs_and_compensations.create_job`<a id="gustoappintegrationsjobs_and_compensationscreate_job"></a>

Create a job.

scope: `jobs:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_job_response = gustoappintegrations.jobs_and_compensations.create_job(
    title="string_example",
    hire_date="string_example",
    employee_id="employee_id_example",
    two_percent_shareholder=True,
    state_wc_covered=True,
    state_wc_class_code="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

The job title

##### hire_date: `str`<a id="hire_date-str"></a>

The date when the employee was hired or rehired for the job.

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### two_percent_shareholder: `bool`<a id="two_percent_shareholder-bool"></a>

Whether the employee owns at least 2% of the company.

##### state_wc_covered: `bool`<a id="state_wc_covered-bool"></a>

Whether this job is eligible for workers' compensation coverage in the state of Washington (WA).

##### state_wc_class_code: `str`<a id="state_wc_class_code-str"></a>

The risk class code for workers' compensation in Washington state. Please visit [Washington state's Risk Class page](https://www.lni.wa.gov/insurance/rates-risk-classes/risk-classes-for-workers-compensation/risk-class-lookup#/) to learn more.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobsAndCompensationsCreateJobRequest`](./gusto_app_integrations_python_sdk/type/jobs_and_compensations_create_job_request.py)
Create a job.

#### 🔄 Return<a id="🔄-return"></a>

[`Job`](./gusto_app_integrations_python_sdk/pydantic/job.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/jobs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.jobs_and_compensations.delete_compensation`<a id="gustoappintegrationsjobs_and_compensationsdelete_compensation"></a>

Compensations contain information on how much is paid out for a job. Jobs may have many compensations, but only one that is active. The current compensation is the one with the most recent `effective_date`. This endpoint deletes a compensation for a job that hasn't been processed on payroll.

scope: `jobs:write`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoappintegrations.jobs_and_compensations.delete_compensation(
    compensation_id="compensation_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### compensation_id: `str`<a id="compensation_id-str"></a>

The UUID of the compensation

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/compensations/{compensation_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.jobs_and_compensations.delete_specific_job`<a id="gustoappintegrationsjobs_and_compensationsdelete_specific_job"></a>

Deletes a specific job that an employee holds.

scope: `jobs:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoappintegrations.jobs_and_compensations.delete_specific_job(
    job_id="job_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

The UUID of the job

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/jobs/{job_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.jobs_and_compensations.get_compensation_by_id`<a id="gustoappintegrationsjobs_and_compensationsget_compensation_by_id"></a>

Compensations contain information on how much is paid out for a job. Jobs may have many compensations, but only one that is active. The current compensation is the one with the most recent `effective_date`.

scope: `jobs:read`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_compensation_by_id_response = (
    gustoappintegrations.jobs_and_compensations.get_compensation_by_id(
        compensation_id="compensation_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### compensation_id: `str`<a id="compensation_id-str"></a>

The UUID of the compensation

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Compensation`](./gusto_app_integrations_python_sdk/pydantic/compensation.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/compensations/{compensation_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.jobs_and_compensations.get_compensations_by_job_id`<a id="gustoappintegrationsjobs_and_compensationsget_compensations_by_job_id"></a>

Compensations contain information on how much is paid out for a job. Jobs may have many compensations, but only one that is active. The current compensation is the one with the most recent `effective_date`. By default the API returns only the current compensation - see the `include` query parameter for retrieving all compensations.

Note: Currently the API does not support creating multiple compensations per job - creating a compensation with the same `job_uuid` as another will fail with a relevant error.

Use `flsa_status` to determine if an employee is eligible for overtime.

scope: `jobs:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_compensations_by_job_id_response = (
    gustoappintegrations.jobs_and_compensations.get_compensations_by_job_id(
        job_id="job_id_example",
        page=3.14,
        per=3.14,
        include="all_compensations",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

The UUID of the job

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### include: `str`<a id="include-str"></a>

Available options: - all_compensations: Include all effective dated compensations for each job instead of only the current compensation

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`JobsAndCompensationsGetCompensationsByJobIdResponse`](./gusto_app_integrations_python_sdk/pydantic/jobs_and_compensations_get_compensations_by_job_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/jobs/{job_id}/compensations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.jobs_and_compensations.get_details`<a id="gustoappintegrationsjobs_and_compensationsget_details"></a>

Get a job.

scope: `jobs:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = gustoappintegrations.jobs_and_compensations.get_details(
    job_id="job_id_example",
    include="all_compensations",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

The UUID of the job

##### include: `str`<a id="include-str"></a>

Available options: - all_compensations: Include all effective dated compensations for the job instead of only the current compensation

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Job`](./gusto_app_integrations_python_sdk/pydantic/job.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/jobs/{job_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.jobs_and_compensations.get_employee_jobs`<a id="gustoappintegrationsjobs_and_compensationsget_employee_jobs"></a>

Get all of the jobs that an employee holds.

scope: `jobs:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_jobs_response = (
    gustoappintegrations.jobs_and_compensations.get_employee_jobs(
        employee_id="employee_id_example",
        page=3.14,
        per=3.14,
        include="all_compensations",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### include: `str`<a id="include-str"></a>

Available options: - all_compensations: Include all effective dated compensations for each job instead of only the current compensation

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`JobsAndCompensationsGetEmployeeJobsResponse`](./gusto_app_integrations_python_sdk/pydantic/jobs_and_compensations_get_employee_jobs_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employee_id}/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.jobs_and_compensations.update_compensation`<a id="gustoappintegrationsjobs_and_compensationsupdate_compensation"></a>

Compensations contain information on how much is paid out for a job. Jobs may have many compensations, but only one that is active. The current compensation is the one with the most recent `effective_date`.

scope: `jobs:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_compensation_response = (
    gustoappintegrations.jobs_and_compensations.update_compensation(
        version="string_example",
        compensation_id="compensation_id_example",
        rate="string_example",
        payment_unit="Hour",
        flsa_status="Nonexempt",
        adjust_for_minimum_wage=True,
        minimum_wages=[{}],
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### compensation_id: `str`<a id="compensation_id-str"></a>

The UUID of the compensation

##### rate: `str`<a id="rate-str"></a>

The dollar amount paid per payment unit.

##### payment_unit: `str`<a id="payment_unit-str"></a>

The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'.

##### flsa_status: [`FlsaStatusType`](./gusto_app_integrations_python_sdk/type/flsa_status_type.py)<a id="flsa_status-flsastatustypegusto_app_integrations_python_sdktypeflsa_status_typepy"></a>

##### adjust_for_minimum_wage: `bool`<a id="adjust_for_minimum_wage-bool"></a>

Determines whether the compensation should be adjusted for minimum wage. Only applies to Nonexempt employees.

##### minimum_wages: [`JobsAndCompensationsUpdateCompensationRequestMinimumWages`](./gusto_app_integrations_python_sdk/type/jobs_and_compensations_update_compensation_request_minimum_wages.py)<a id="minimum_wages-jobsandcompensationsupdatecompensationrequestminimumwagesgusto_app_integrations_python_sdktypejobs_and_compensations_update_compensation_request_minimum_wagespy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobsAndCompensationsUpdateCompensationRequest`](./gusto_app_integrations_python_sdk/type/jobs_and_compensations_update_compensation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Compensation`](./gusto_app_integrations_python_sdk/pydantic/compensation.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/compensations/{compensation_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.jobs_and_compensations.update_job`<a id="gustoappintegrationsjobs_and_compensationsupdate_job"></a>

Update a job.

scope: `jobs:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_job_response = gustoappintegrations.jobs_and_compensations.update_job(
    version="string_example",
    job_id="job_id_example",
    title="string_example",
    hire_date="string_example",
    two_percent_shareholder=True,
    state_wc_covered=True,
    state_wc_class_code="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.

##### job_id: `str`<a id="job_id-str"></a>

The UUID of the job

##### title: `str`<a id="title-str"></a>

The job title

##### hire_date: `str`<a id="hire_date-str"></a>

The date when the employee was hired or rehired for the job.

##### two_percent_shareholder: `bool`<a id="two_percent_shareholder-bool"></a>

Whether the employee owns at least 2% of the company.

##### state_wc_covered: `bool`<a id="state_wc_covered-bool"></a>

Whether this job is eligible for workers' compensation coverage in the state of Washington (WA).

##### state_wc_class_code: `str`<a id="state_wc_class_code-str"></a>

The risk class code for workers' compensation in Washington state. Please visit [Washington state's Risk Class page](https://www.lni.wa.gov/insurance/rates-risk-classes/risk-classes-for-workers-compensation/risk-class-lookup#/) to learn more.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobsAndCompensationsUpdateJobRequest`](./gusto_app_integrations_python_sdk/type/jobs_and_compensations_update_job_request.py)
Update a job.

#### 🔄 Return<a id="🔄-return"></a>

[`Job`](./gusto_app_integrations_python_sdk/pydantic/job.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/jobs/{job_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.locations.create_company_location`<a id="gustoappintegrationslocationscreate_company_location"></a>

Company locations represent all addresses associated with a company. These can be filing addresses, mailing addresses, and/or work locations; one address may serve multiple, or all, purposes.

Since all company locations are subsets of locations, retrieving or updating an individual record should be done via the locations endpoints.

scope: `companies.write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_company_location_response = (
    gustoappintegrations.locations.create_company_location(
        phone_number="0480728880",
        street_1="string_example",
        city="string_example",
        state="string_example",
        zip="string_example",
        company_id="company_id_example",
        street_2="string_example",
        country="USA",
        mailing_address=True,
        filing_address=True,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### phone_number: `str`<a id="phone_number-str"></a>

##### street_1: `str`<a id="street_1-str"></a>

##### city: `str`<a id="city-str"></a>

##### state: `str`<a id="state-str"></a>

##### zip: `str`<a id="zip-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### street_2: `Optional[str]`<a id="street_2-optionalstr"></a>

##### country: `str`<a id="country-str"></a>

##### mailing_address: `bool`<a id="mailing_address-bool"></a>

Specify if this location is the company's mailing address.

##### filing_address: `bool`<a id="filing_address-bool"></a>

Specify if this location is the company's filing address.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LocationsCreateCompanyLocationRequest`](./gusto_app_integrations_python_sdk/type/locations_create_company_location_request.py)
Create a company location.

#### 🔄 Return<a id="🔄-return"></a>

[`Location`](./gusto_app_integrations_python_sdk/pydantic/location.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/locations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.locations.get_details`<a id="gustoappintegrationslocationsget_details"></a>

Get a location.

scope: `companies:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = gustoappintegrations.locations.get_details(
    location_id="location_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### location_id: `str`<a id="location_id-str"></a>

The UUID of the location

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Location`](./gusto_app_integrations_python_sdk/pydantic/location.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/locations/{location_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.locations.get_minimum_wages`<a id="gustoappintegrationslocationsget_minimum_wages"></a>

Get minimum wages for a location

scope: `companies:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_minimum_wages_response = gustoappintegrations.locations.get_minimum_wages(
    location_uuid="location_uuid_example",
    effective_date="2020-01-31",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### location_uuid: `str`<a id="location_uuid-str"></a>

The UUID of the location

##### effective_date: `str`<a id="effective_date-str"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`LocationsGetMinimumWagesResponse`](./gusto_app_integrations_python_sdk/pydantic/locations_get_minimum_wages_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/locations/{location_uuid}/minimum_wages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.locations.list_company_locations`<a id="gustoappintegrationslocationslist_company_locations"></a>

Company locations represent all addresses associated with a company. These can be filing addresses, mailing addresses, and/or work locations; one address may serve multiple, or all, purposes.

Since all company locations are subsets of locations, retrieving or updating an individual record should be done via the locations endpoints.

scope: `companies:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_company_locations_response = gustoappintegrations.locations.list_company_locations(
    company_id="company_id_example",
    page=3.14,
    per=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`LocationsListCompanyLocationsResponse`](./gusto_app_integrations_python_sdk/pydantic/locations_list_company_locations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/locations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.locations.update_location`<a id="gustoappintegrationslocationsupdate_location"></a>

Update a location.

scope: `companies.write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_location_response = gustoappintegrations.locations.update_location(
    body=None,
    location_id="location_id_example",
    version="string_example",
    phone_number="0480728880",
    street_1="string_example",
    street_2="string_example",
    city="string_example",
    state="string_example",
    zip="string_example",
    country="string_example",
    mailing_address=True,
    filing_address=True,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### location_id: `str`<a id="location_id-str"></a>

The UUID of the location

##### version: `str`<a id="version-str"></a>

The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.

##### phone_number: `str`<a id="phone_number-str"></a>

##### street_1: `str`<a id="street_1-str"></a>

##### street_2: `Optional[str]`<a id="street_2-optionalstr"></a>

##### city: `str`<a id="city-str"></a>

##### state: `str`<a id="state-str"></a>

##### zip: `str`<a id="zip-str"></a>

##### country: `str`<a id="country-str"></a>

##### mailing_address: `bool`<a id="mailing_address-bool"></a>

For a company location, specify if this location is the company's mailing address. A company has a single mailing address, so this designation will override any previous selection.

##### filing_address: `bool`<a id="filing_address-bool"></a>

For a company location, specify if this location is the company's filing address. A company has a single filing address, so this designation will override any previous selection.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LocationsUpdateLocationRequest`](./gusto_app_integrations_python_sdk/type/locations_update_location_request.py)
Update a location

#### 🔄 Return<a id="🔄-return"></a>

[`Location`](./gusto_app_integrations_python_sdk/pydantic/location.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/locations/{location_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.pay_schedules.get_assignments`<a id="gustoappintegrationspay_schedulesget_assignments"></a>

This endpoint returns the current pay schedule assignment for a company, with pay schedule and employee/department mappings depending on the pay schedule type.

scope: `pay_schedules:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_assignments_response = gustoappintegrations.pay_schedules.get_assignments(
    company_id="company_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PayScheduleAssignment`](./gusto_app_integrations_python_sdk/pydantic/pay_schedule_assignment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/pay_schedules/assignments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.pay_schedules.get_details`<a id="gustoappintegrationspay_schedulesget_details"></a>

The pay schedule object in Gusto captures the details of when employees work and when they should be paid. A company can have multiple pay schedules.

scope: `pay_schedules:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = gustoappintegrations.pay_schedules.get_details(
    company_id="company_id_example",
    pay_schedule_id="pay_schedule_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### pay_schedule_id: `str`<a id="pay_schedule_id-str"></a>

The UUID of the pay schedule

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PaySchedule`](./gusto_app_integrations_python_sdk/pydantic/pay_schedule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/pay_schedules/{pay_schedule_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.pay_schedules.list`<a id="gustoappintegrationspay_scheduleslist"></a>

The pay schedule object in Gusto captures the details of when employees work and when they should be paid. A company can have multiple pay schedules.

scope: `pay_schedules:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = gustoappintegrations.pay_schedules.list(
    company_id="company_id_example",
    page=3.14,
    per=3.14,
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.

##### per: `Union[int, float]`<a id="per-unionint-float"></a>

Number of objects per page. For majority of endpoints will default to 25

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PaySchedulesListResponse`](./gusto_app_integrations_python_sdk/pydantic/pay_schedules_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/pay_schedules` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.pay_schedules.list_0`<a id="gustoappintegrationspay_scheduleslist_0"></a>

Pay periods are the foundation of payroll. Compensation, time & attendance, taxes, and expense reports all rely on when they happened. To begin submitting information for a given payroll, we need to agree on the time period.

By default, this endpoint returns pay periods starting from 6 months ago to the date today.  Use the `start_date` and `end_date` parameters to change the scope of the response.  End dates can be up to 3 months in the future and there is no limit on start dates.

Starting in version '2023-04-01', the eligible_employees attribute was removed from the response.  The eligible employees for a payroll are determined by the employee_compensations returned from the payrolls#prepare endpoint.

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_0_response = gustoappintegrations.pay_schedules.list_0(
    company_id="company_id_example",
    start_date="2020-01-01",
    end_date="2020-01-31",
    payroll_types="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### start_date: `str`<a id="start_date-str"></a>

##### end_date: `str`<a id="end_date-str"></a>

##### payroll_types: `str`<a id="payroll_types-str"></a>

regular and/or transition. Multiple options are comma separated. The default is regular pay periods if nothing is passed in.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PaySchedulesList200Response`](./gusto_app_integrations_python_sdk/pydantic/pay_schedules_list200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/pay_periods` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.pay_schedules.list_unprocessed_termination_pay_periods`<a id="gustoappintegrationspay_scheduleslist_unprocessed_termination_pay_periods"></a>

When a payroll admin terminates an employee and selects "Dismissal Payroll" as the employee's final payroll, their last pay period will appear on the list.

This endpoint returns the unprocessed pay periods for past and future terminated employees in a given company.

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_unprocessed_termination_pay_periods_response = (
    gustoappintegrations.pay_schedules.list_unprocessed_termination_pay_periods(
        company_id="company_id_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PaySchedulesListUnprocessedTerminationPayPeriodsResponse`](./gusto_app_integrations_python_sdk/pydantic/pay_schedules_list_unprocessed_termination_pay_periods_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/pay_periods/unprocessed_termination_pay_periods` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.payrolls.get_all_for_company`<a id="gustoappintegrationspayrollsget_all_for_company"></a>

Returns a list of payrolls for a company. You can change the payrolls returned by updating the processing_status, payroll_types, start_date, & end_date params.

By default, will return processed, regular payrolls for the past 6 months.

Notes:
* Dollar amounts are returned as string representations of numeric decimals, are represented to the cent.
* end_date can be at most 3 months in the future and start_date and end_date can't be more than 1 year apart.

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_for_company_response = gustoappintegrations.payrolls.get_all_for_company(
    company_id="company_id_example",
    processing_statuses="unprocessed",
    payroll_types="regular",
    include="totals",
    start_date="string_example",
    end_date="string_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### processing_statuses: `str`<a id="processing_statuses-str"></a>

Whether to include processed and/or unprocessed payrolls in the response, defaults to processed, for multiple attributes comma separate the values, i.e. `?processing_statuses=processed,unprocessed`

##### payroll_types: `str`<a id="payroll_types-str"></a>

Whether to include regular and/or off_cycle payrolls in the response, defaults to regular, for multiple attributes comma separate the values, i.e. `?payroll_types=regular,off_cycle`

##### include: `str`<a id="include-str"></a>

Include the requested attribute in the response. In v2023-04-01 totals are no longer included by default. For multiple attributes comma separate the values, i.e. `?include=totals,payroll_status_meta`

##### start_date: `str`<a id="start_date-str"></a>

Return payrolls whose pay period is after the start date

##### end_date: `str`<a id="end_date-str"></a>

Return payrolls whose pay period is before the end date

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PayrollsGetAllForCompanyResponse`](./gusto_app_integrations_python_sdk/pydantic/payrolls_get_all_for_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/payrolls` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.payrolls.get_single_payroll`<a id="gustoappintegrationspayrollsget_single_payroll"></a>

Returns a payroll. If payroll is calculated or processed, will return employee_compensations and totals.

Notes:
* Hour and dollar amounts are returned as string representations of numeric decimals.
* Hours are represented to the thousands place; dollar amounts are represented to the cent.
* Every eligible compensation is returned for each employee. If no data has yet be inserted for a given field, it defaults to “0.00” (for fixed amounts) or “0.000” (for hours ).
* When include parameter with benefits value is passed, employee_benefits:read scope is required to return benefits
  * Benefits containing PHI are only visible with the `employee_benefits:read:phi` scope

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_payroll_response = gustoappintegrations.payrolls.get_single_payroll(
    company_id="company_id_example",
    payroll_id="payroll_id_example",
    include="benefits",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### payroll_id: `str`<a id="payroll_id-str"></a>

The UUID of the payroll

##### include: `str`<a id="include-str"></a>

Include the requested attribute in the response, for multiple attributes comma separate the values, i.e. `?include=benefits,deductions,taxes`

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`Payroll`](./gusto_app_integrations_python_sdk/pydantic/payroll.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/payrolls/{payroll_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.payrolls.prepare_for_update`<a id="gustoappintegrationspayrollsprepare_for_update"></a>

This endpoint will build the payroll and get it ready for making updates. This includes adding/removing eligible employees from the Payroll and updating the check_date, payroll_deadline, and payroll_status_meta dates & times.

Notes:
 * Will null out calculated_at & totals if a payroll has already been calculated.
 * Will return the version param used for updating the payroll

scope: `payrolls:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
prepare_for_update_response = gustoappintegrations.payrolls.prepare_for_update(
    company_id="company_id_example",
    payroll_id="payroll_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### payroll_id: `str`<a id="payroll_id-str"></a>

The UUID of the payroll

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`PayrollPrepared`](./gusto_app_integrations_python_sdk/pydantic/payroll_prepared.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/payrolls/{payroll_id}/prepare` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.payrolls.update_by_id`<a id="gustoappintegrationspayrollsupdate_by_id"></a>

This endpoint allows you to update information for one or more employees for a specific **unprocessed** payroll.  You can think of the **unprocessed**
payroll object as a template of fields that you can update.  You cannot modify the structure of the payroll object through this endpoint, only values
of the fields included in the payroll.  If you do not include specific employee compensations or fixed/hourly compensations in your request body, they
will not be removed from the payroll.

scope: `payrolls:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = gustoappintegrations.payrolls.update_by_id(
    employee_compensations=[
        {
            "payment_method": "Direct Deposit",
        }
    ],
    company_id="company_id_example",
    payroll_id="payroll_id_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_compensations: [`PayrollsUpdateByIdRequestEmployeeCompensations`](./gusto_app_integrations_python_sdk/type/payrolls_update_by_id_request_employee_compensations.py)<a id="employee_compensations-payrollsupdatebyidrequestemployeecompensationsgusto_app_integrations_python_sdktypepayrolls_update_by_id_request_employee_compensationspy"></a>

##### company_id: `str`<a id="company_id-str"></a>

The UUID of the company

##### payroll_id: `str`<a id="payroll_id-str"></a>

The UUID of the payroll

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayrollsUpdateByIdRequest`](./gusto_app_integrations_python_sdk/type/payrolls_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayrollPrepared`](./gusto_app_integrations_python_sdk/pydantic/payroll_prepared.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}/payrolls/{payroll_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.time_off_policies.calculate_accruing_time_off_hours`<a id="gustoappintegrationstime_off_policiescalculate_accruing_time_off_hours"></a>

Returns a list of accruing time off for each time off policy associated with the employee.

Factors affecting the accrued hours:
  * the time off policy accrual method (whether they get pay per hour worked, per hour paid, with / without overtime, accumulate time off based on pay period / calendar year / anniversary)
  * how many hours of work during this pay period
  * how many hours of PTO / sick hours taken during this pay period (for per hour paid policies only)
  * company pay schedule frequency (for per pay period)

If none of the parameters is passed in, the accrued time off hour will be 0.

scope: `payrolls:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
calculate_accruing_time_off_hours_response = (
    gustoappintegrations.time_off_policies.calculate_accruing_time_off_hours(
        payroll_id="payroll_id_example",
        employee_id="employee_id_example",
        regular_hours_worked=3.14,
        overtime_hours_worked=3.14,
        double_overtime_hours_worked=3.14,
        pto_hours_used=3.14,
        sick_hours_used=3.14,
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payroll_id: `str`<a id="payroll_id-str"></a>

The UUID of the payroll

##### employee_id: `str`<a id="employee_id-str"></a>

The UUID of the employee

##### regular_hours_worked: `Union[int, float]`<a id="regular_hours_worked-unionint-float"></a>

regular hours worked in this pay period

##### overtime_hours_worked: `Union[int, float]`<a id="overtime_hours_worked-unionint-float"></a>

overtime hours worked in this pay period

##### double_overtime_hours_worked: `Union[int, float]`<a id="double_overtime_hours_worked-unionint-float"></a>

double overtime hours worked in this pay period

##### pto_hours_used: `Union[int, float]`<a id="pto_hours_used-unionint-float"></a>

paid time off hours used in this pay period

##### sick_hours_used: `Union[int, float]`<a id="sick_hours_used-unionint-float"></a>

sick hours used in this pay period

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffPoliciesCalculateAccruingTimeOffHoursRequest`](./gusto_app_integrations_python_sdk/type/time_off_policies_calculate_accruing_time_off_hours_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffPoliciesCalculateAccruingTimeOffHoursResponse`](./gusto_app_integrations_python_sdk/pydantic/time_off_policies_calculate_accruing_time_off_hours_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payrolls/{payroll_id}/employees/{employee_id}/calculate_accruing_time_off_hours` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.webhooks.create_subscription`<a id="gustoappintegrationswebhookscreate_subscription"></a>

Create a webhook subscription to receive events of the specified subscription_types whenever there is a state change.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `webhook_subscriptions:write`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_subscription_response = gustoappintegrations.webhooks.create_subscription(
    url="string_example",
    subscription_types=["string_example"],
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

##### subscription_types: [`WebhooksCreateSubscriptionRequestSubscriptionTypes`](./gusto_app_integrations_python_sdk/type/webhooks_create_subscription_request_subscription_types.py)<a id="subscription_types-webhookscreatesubscriptionrequestsubscriptiontypesgusto_app_integrations_python_sdktypewebhooks_create_subscription_request_subscription_typespy"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksCreateSubscriptionRequest`](./gusto_app_integrations_python_sdk/type/webhooks_create_subscription_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhookSubscription`](./gusto_app_integrations_python_sdk/pydantic/webhook_subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook_subscriptions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.webhooks.delete_subscription_by_uuid`<a id="gustoappintegrationswebhooksdelete_subscription_by_uuid"></a>

Deletes the Webhook Subscription associated with the provided UUID.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `webhook_subscriptions:write`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoappintegrations.webhooks.delete_subscription_by_uuid(
    webhook_subscription_uuid="webhook_subscription_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_subscription_uuid: `str`<a id="webhook_subscription_uuid-str"></a>

The webhook subscription UUID.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook_subscriptions/{webhook_subscription_uuid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.webhooks.get_subscription_by_uuid`<a id="gustoappintegrationswebhooksget_subscription_by_uuid"></a>

Returns the Webhook Subscription associated with the provided UUID.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `webhook_subscriptions:read`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_subscription_by_uuid_response = (
    gustoappintegrations.webhooks.get_subscription_by_uuid(
        webhook_subscription_uuid="webhook_subscription_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_subscription_uuid: `str`<a id="webhook_subscription_uuid-str"></a>

The webhook subscription UUID.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookSubscription`](./gusto_app_integrations_python_sdk/pydantic/webhook_subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook_subscriptions/{webhook_subscription_uuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.webhooks.list_subscriptions`<a id="gustoappintegrationswebhookslist_subscriptions"></a>

Returns all webhook subscriptions associated with the provided Partner API token.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `webhook_subscriptions:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_subscriptions_response = gustoappintegrations.webhooks.list_subscriptions(
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksListSubscriptionsResponse`](./gusto_app_integrations_python_sdk/pydantic/webhooks_list_subscriptions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook_subscriptions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.webhooks.request_verification_token`<a id="gustoappintegrationswebhooksrequest_verification_token"></a>

Request that the webhook subscription `verification_token` be POSTed to the Subscription URL.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `webhook_subscriptions:read`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gustoappintegrations.webhooks.request_verification_token(
    webhook_subscription_uuid="webhook_subscription_uuid_example",
    x_gusto_api_version="2024-03-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_subscription_uuid: `str`<a id="webhook_subscription_uuid-str"></a>

The webhook subscription UUID.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook_subscriptions/{webhook_subscription_uuid}/request_verification_token` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.webhooks.update_subscription_by_uuid`<a id="gustoappintegrationswebhooksupdate_subscription_by_uuid"></a>

Updates the Webhook Subscription associated with the provided UUID.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `webhook_subscriptions:write`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_subscription_by_uuid_response = (
    gustoappintegrations.webhooks.update_subscription_by_uuid(
        subscription_types=["string_example"],
        webhook_subscription_uuid="webhook_subscription_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscription_types: [`WebhooksUpdateSubscriptionByUuidRequestSubscriptionTypes`](./gusto_app_integrations_python_sdk/type/webhooks_update_subscription_by_uuid_request_subscription_types.py)<a id="subscription_types-webhooksupdatesubscriptionbyuuidrequestsubscriptiontypesgusto_app_integrations_python_sdktypewebhooks_update_subscription_by_uuid_request_subscription_typespy"></a>

##### webhook_subscription_uuid: `str`<a id="webhook_subscription_uuid-str"></a>

The webhook subscription UUID.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksUpdateSubscriptionByUuidRequest`](./gusto_app_integrations_python_sdk/type/webhooks_update_subscription_by_uuid_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhookSubscription`](./gusto_app_integrations_python_sdk/pydantic/webhook_subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook_subscriptions/{webhook_subscription_uuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gustoappintegrations.webhooks.verify_subscription_token`<a id="gustoappintegrationswebhooksverify_subscription_token"></a>

When a webhook subscription is created, a `verification_token` is POSTed to the registered webhook subscription URL. This `verify` endpoint needs to be called with `verification_token` before webhook events can be sent to the registered webhook URL.

Use the /v1/webhook_subscriptions/{webhook_subscription_uuid}/request_verification_token API to resend the `verification_token` to the Subscriber.

> 📘 Token Authentication
>
> This endpoint uses the [organization level api token and the Token scheme with HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/authentication#api-token-authentication).

scope: `webhook_subscriptions:write`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_subscription_token_response = (
    gustoappintegrations.webhooks.verify_subscription_token(
        verification_token="string_example",
        webhook_subscription_uuid="webhook_subscription_uuid_example",
        x_gusto_api_version="2024-03-01",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### verification_token: `str`<a id="verification_token-str"></a>

The token POSTed to the Subscription URL.

##### webhook_subscription_uuid: `str`<a id="webhook_subscription_uuid-str"></a>

The webhook subscription UUID.

##### x_gusto_api_version: `str`<a id="x_gusto_api_version-str"></a>

Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksVerifySubscriptionTokenRequest`](./gusto_app_integrations_python_sdk/type/webhooks_verify_subscription_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhookSubscription`](./gusto_app_integrations_python_sdk/pydantic/webhook_subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook_subscriptions/{webhook_subscription_uuid}/verify` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
