# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_app_integrations_python_sdk.paths.v1_webhook_subscriptions.post import CreateSubscription
from gusto_app_integrations_python_sdk.paths.v1_webhook_subscriptions_webhook_subscription_uuid.delete import DeleteSubscriptionByUuid
from gusto_app_integrations_python_sdk.paths.v1_webhook_subscriptions_webhook_subscription_uuid.get import GetSubscriptionByUuid
from gusto_app_integrations_python_sdk.paths.v1_webhook_subscriptions.get import ListSubscriptions
from gusto_app_integrations_python_sdk.paths.v1_webhook_subscriptions_webhook_subscription_uuid_request_verification_token.get import RequestVerificationToken
from gusto_app_integrations_python_sdk.paths.v1_webhook_subscriptions_webhook_subscription_uuid.put import UpdateSubscriptionByUuid
from gusto_app_integrations_python_sdk.paths.v1_webhook_subscriptions_webhook_subscription_uuid_verify.put import VerifySubscriptionToken
from gusto_app_integrations_python_sdk.apis.tags.webhooks_api_raw import WebhooksApiRaw


class WebhooksApi(
    CreateSubscription,
    DeleteSubscriptionByUuid,
    GetSubscriptionByUuid,
    ListSubscriptions,
    RequestVerificationToken,
    UpdateSubscriptionByUuid,
    VerifySubscriptionToken,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: WebhooksApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = WebhooksApiRaw(api_client)
