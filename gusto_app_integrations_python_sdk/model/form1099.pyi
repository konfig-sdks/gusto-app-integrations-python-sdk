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


class Form1099(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            description = schemas.StrSchema
            uuid = schemas.StrSchema
            name = schemas.StrSchema
            draft = schemas.BoolSchema
            
            
            class year(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'year':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class quarter(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'quarter':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            requires_signing = schemas.BoolSchema
            contractor_uuid = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "description": description,
                "uuid": uuid,
                "name": name,
                "draft": draft,
                "year": year,
                "quarter": quarter,
                "requires_signing": requires_signing,
                "contractor_uuid": contractor_uuid,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["draft"]) -> MetaOapg.properties.draft: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["year"]) -> MetaOapg.properties.year: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quarter"]) -> MetaOapg.properties.quarter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requires_signing"]) -> MetaOapg.properties.requires_signing: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractor_uuid"]) -> MetaOapg.properties.contractor_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "description", "uuid", "name", "draft", "year", "quarter", "requires_signing", "contractor_uuid", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["draft"]) -> typing.Union[MetaOapg.properties.draft, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["year"]) -> typing.Union[MetaOapg.properties.year, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quarter"]) -> typing.Union[MetaOapg.properties.quarter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requires_signing"]) -> typing.Union[MetaOapg.properties.requires_signing, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractor_uuid"]) -> typing.Union[MetaOapg.properties.contractor_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "description", "uuid", "name", "draft", "year", "quarter", "requires_signing", "contractor_uuid", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        draft: typing.Union[MetaOapg.properties.draft, bool, schemas.Unset] = schemas.unset,
        year: typing.Union[MetaOapg.properties.year, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        quarter: typing.Union[MetaOapg.properties.quarter, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        requires_signing: typing.Union[MetaOapg.properties.requires_signing, bool, schemas.Unset] = schemas.unset,
        contractor_uuid: typing.Union[MetaOapg.properties.contractor_uuid, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Form1099':
        return super().__new__(
            cls,
            *args,
            title=title,
            description=description,
            uuid=uuid,
            name=name,
            draft=draft,
            year=year,
            quarter=quarter,
            requires_signing=requires_signing,
            contractor_uuid=contractor_uuid,
            _configuration=_configuration,
            **kwargs,
        )
