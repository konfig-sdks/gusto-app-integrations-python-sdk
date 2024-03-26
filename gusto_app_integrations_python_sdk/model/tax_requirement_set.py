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


class TaxRequirementSet(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            state = schemas.StrSchema
            key = schemas.StrSchema
            label = schemas.StrSchema
        
            @staticmethod
            def effective_from() -> typing.Type['TaxRequirementEffectiveFrom']:
                return TaxRequirementEffectiveFrom
            
            
            class requirements(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TaxRequirement']:
                        return TaxRequirement
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TaxRequirement'], typing.List['TaxRequirement']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'requirements':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TaxRequirement':
                    return super().__getitem__(i)
            __annotations__ = {
                "state": state,
                "key": key,
                "label": label,
                "effective_from": effective_from,
                "requirements": requirements,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effective_from"]) -> 'TaxRequirementEffectiveFrom': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requirements"]) -> MetaOapg.properties.requirements: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["state", "key", "label", "effective_from", "requirements", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effective_from"]) -> typing.Union['TaxRequirementEffectiveFrom', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requirements"]) -> typing.Union[MetaOapg.properties.requirements, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["state", "key", "label", "effective_from", "requirements", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        effective_from: typing.Union['TaxRequirementEffectiveFrom', schemas.Unset] = schemas.unset,
        requirements: typing.Union[MetaOapg.properties.requirements, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TaxRequirementSet':
        return super().__new__(
            cls,
            *args,
            state=state,
            key=key,
            label=label,
            effective_from=effective_from,
            requirements=requirements,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_app_integrations_python_sdk.model.tax_requirement import TaxRequirement
from gusto_app_integrations_python_sdk.model.tax_requirement_effective_from import TaxRequirementEffectiveFrom
