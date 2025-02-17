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

from gusto_app_integrations_python_sdk.type.introspection_access_token_info_response_resource import IntrospectionAccessTokenInfoResponseResource

class RequiredIntrospectionAccessTokenInfoResponse(TypedDict):
    pass

class OptionalIntrospectionAccessTokenInfoResponse(TypedDict, total=False):
    # Space delimited string of accessible scopes.
    scope: str

    resource: IntrospectionAccessTokenInfoResponseResource

class IntrospectionAccessTokenInfoResponse(RequiredIntrospectionAccessTokenInfoResponse, OptionalIntrospectionAccessTokenInfoResponse):
    pass
