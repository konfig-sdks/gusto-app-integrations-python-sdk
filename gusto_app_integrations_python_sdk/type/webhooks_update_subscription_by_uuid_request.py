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

from gusto_app_integrations_python_sdk.type.webhooks_update_subscription_by_uuid_request_subscription_types import WebhooksUpdateSubscriptionByUuidRequestSubscriptionTypes

class RequiredWebhooksUpdateSubscriptionByUuidRequest(TypedDict):
    subscription_types: WebhooksUpdateSubscriptionByUuidRequestSubscriptionTypes

class OptionalWebhooksUpdateSubscriptionByUuidRequest(TypedDict, total=False):
    pass

class WebhooksUpdateSubscriptionByUuidRequest(RequiredWebhooksUpdateSubscriptionByUuidRequest, OptionalWebhooksUpdateSubscriptionByUuidRequest):
    pass
