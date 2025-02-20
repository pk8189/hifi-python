"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostAccountUsdOfframpWireBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    account_number: typing_extensions.Required[str]
    account_owner_type: typing_extensions.Required[
        typing_extensions.Literal["individual", "business"]
    ]
    bank_identifier_code: typing_extensions.NotRequired[str]
    bank_name: typing_extensions.Required[str]
    business_name: typing_extensions.Required[str]
    city: typing_extensions.Required[str]
    country: typing_extensions.Required[str]
    currency: typing_extensions.Required[typing_extensions.Literal["usd"]]
    first_name: typing_extensions.NotRequired[str]
    iban: typing_extensions.NotRequired[str]
    last_name: typing_extensions.NotRequired[str]
    legal_full_name: typing_extensions.NotRequired[str]
    middle_name: typing_extensions.NotRequired[str]
    postal_code: typing_extensions.Required[str]
    state: typing_extensions.Required[str]
    street_line1: typing_extensions.Required[str]
    street_line2: typing_extensions.NotRequired[str]


class _SerializerPostAccountUsdOfframpWireBody(pydantic.BaseModel):
    """
    Serializer for PostAccountUsdOfframpWireBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_number: str = pydantic.Field(alias="accountNumber")
    account_owner_type: typing_extensions.Literal["individual", "business"] = (
        pydantic.Field(alias="accountOwnerType")
    )
    bank_identifier_code: typing.Optional[str] = pydantic.Field(
        alias="bankIdentifierCode", default=None
    )
    bank_name: str = pydantic.Field(alias="bankName")
    business_name: str = pydantic.Field(alias="businessName")
    city: str = pydantic.Field(alias="city")
    country: str = pydantic.Field(alias="country")
    currency: typing_extensions.Literal["usd"] = pydantic.Field(alias="currency")
    first_name: typing.Optional[str] = pydantic.Field(alias="firstName", default=None)
    iban: typing.Optional[str] = pydantic.Field(alias="iban", default=None)
    last_name: typing.Optional[str] = pydantic.Field(alias="lastName", default=None)
    legal_full_name: typing.Optional[str] = pydantic.Field(
        alias="legalFullName", default=None
    )
    middle_name: typing.Optional[str] = pydantic.Field(alias="middleName", default=None)
    postal_code: str = pydantic.Field(alias="postalCode")
    state: str = pydantic.Field(alias="state")
    street_line1: str = pydantic.Field(alias="streetLine1")
    street_line2: typing.Optional[str] = pydantic.Field(
        alias="streetLine2", default=None
    )
