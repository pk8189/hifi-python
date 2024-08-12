"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class GetAccountResponseRail(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    payment_rail: typing.Optional[str] = pydantic.Field(
        alias="paymentRail", default=None
    )
    rail_type: typing.Optional[str] = pydantic.Field(alias="railType", default=None)


class GetAccountResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_id: typing.Optional[str] = pydantic.Field(alias="accountId", default=None)
    account_number: typing.Optional[str] = pydantic.Field(
        alias="accountNumber", default=None
    )
    account_type: typing.Optional[str] = pydantic.Field(
        alias="accountType", default=None
    )
    bank_name: typing.Optional[str] = pydantic.Field(alias="bankName", default=None)
    created_at: typing.Optional[str] = pydantic.Field(alias="createdAt", default=None)
    rail: typing.Optional[GetAccountResponseRail] = pydantic.Field(
        alias="rail", default=None
    )
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routingNumber", default=None
    )
    user_id: typing.Optional[str] = pydantic.Field(alias="userId", default=None)
