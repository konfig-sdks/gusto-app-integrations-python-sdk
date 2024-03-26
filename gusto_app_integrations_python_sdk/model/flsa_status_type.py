# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from gusto_app_integrations_python_sdk import schemas  # noqa: F401


class FlsaStatusType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The FLSA status for this compensation. Salaried ('Exempt') employees are paid a fixed salary every pay period. Salaried with overtime ('Salaried Nonexempt') employees are paid a fixed salary every pay period, and receive overtime pay when applicable. Hourly ('Nonexempt') employees are paid for the hours they work, and receive overtime pay when applicable. Commissioned employees ('Commission Only Exempt') earn wages based only on commission. Commissioned with overtime ('Commission Only Nonexempt') earn wages based on commission, and receive overtime pay when applicable. Owners ('Owner') are employees that own at least twenty percent of the company. 
    """


    class MetaOapg:
        enum_value_to_name = {
            "Exempt": "EXEMPT",
            "Salaried Nonexempt": "SALARIED_NONEXEMPT",
            "Nonexempt": "NONEXEMPT",
            "Owner": "OWNER",
            "Commission Only Exempt": "COMMISSION_ONLY_EXEMPT",
            "Commission Only Nonexempt": "COMMISSION_ONLY_NONEXEMPT",
        }
    
    @schemas.classproperty
    def EXEMPT(cls):
        return cls("Exempt")
    
    @schemas.classproperty
    def SALARIED_NONEXEMPT(cls):
        return cls("Salaried Nonexempt")
    
    @schemas.classproperty
    def NONEXEMPT(cls):
        return cls("Nonexempt")
    
    @schemas.classproperty
    def OWNER(cls):
        return cls("Owner")
    
    @schemas.classproperty
    def COMMISSION_ONLY_EXEMPT(cls):
        return cls("Commission Only Exempt")
    
    @schemas.classproperty
    def COMMISSION_ONLY_NONEXEMPT(cls):
        return cls("Commission Only Nonexempt")
