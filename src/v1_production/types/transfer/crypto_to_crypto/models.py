"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class GetTransferCryptoToCryptoResponseTransferDetailsRecipient(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    business_name: typing.Optional[typing.Any] = pydantic.Field(
        alias="business_name", default=None
    )
    compliance_email: typing.Optional[str] = pydantic.Field(
        alias="compliance_email", default=None
    )
    legal_first_name: typing.Optional[str] = pydantic.Field(
        alias="legal_first_name", default=None
    )
    legal_last_name: typing.Optional[str] = pydantic.Field(
        alias="legal_last_name", default=None
    )


class GetTransferCryptoToCryptoResponseTransferDetailsSender(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    business_name: typing.Optional[typing.Any] = pydantic.Field(
        alias="business_name", default=None
    )
    compliance_email: typing.Optional[str] = pydantic.Field(
        alias="compliance_email", default=None
    )
    legal_first_name: typing.Optional[str] = pydantic.Field(
        alias="legal_first_name", default=None
    )
    legal_last_name: typing.Optional[str] = pydantic.Field(
        alias="legal_last_name", default=None
    )


class PostTransferCryptoToCryptoResponseTransferDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: typing.Optional[float] = pydantic.Field(alias="amount", default=None)
    chain: typing.Optional[str] = pydantic.Field(alias="chain", default=None)
    contract_address: typing.Optional[str] = pydantic.Field(
        alias="contractAddress", default=None
    )
    created_at: typing.Optional[str] = pydantic.Field(alias="createdAt", default=None)
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    failed_reason: typing.Optional[str] = pydantic.Field(
        alias="failedReason", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    recipient_address: typing.Optional[str] = pydantic.Field(
        alias="recipientAddress", default=None
    )
    recipient_user_id: typing.Optional[str] = pydantic.Field(
        alias="recipientUserId", default=None
    )
    request_id: typing.Optional[str] = pydantic.Field(alias="requestId", default=None)
    sender_user_id: typing.Optional[str] = pydantic.Field(
        alias="senderUserId", default=None
    )
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)
    transaction_hash: typing.Optional[str] = pydantic.Field(
        alias="transactionHash", default=None
    )


class GetTransferCryptoToCryptoResponseTransferDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    chain: typing.Optional[str] = pydantic.Field(alias="chain", default=None)
    contract_address: typing.Optional[str] = pydantic.Field(
        alias="contractAddress", default=None
    )
    created_at: typing.Optional[str] = pydantic.Field(alias="createdAt", default=None)
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    recipient: typing.Optional[
        GetTransferCryptoToCryptoResponseTransferDetailsRecipient
    ] = pydantic.Field(alias="recipient", default=None)
    recipient_address: typing.Optional[str] = pydantic.Field(
        alias="recipientAddress", default=None
    )
    recipient_user_id: typing.Optional[str] = pydantic.Field(
        alias="recipientUserId", default=None
    )
    request_id: typing.Optional[str] = pydantic.Field(alias="requestId", default=None)
    sender: typing.Optional[GetTransferCryptoToCryptoResponseTransferDetailsSender] = (
        pydantic.Field(alias="sender", default=None)
    )
    sender_user_id: typing.Optional[str] = pydantic.Field(
        alias="senderUserId", default=None
    )
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)
    transaction_hash: typing.Optional[str] = pydantic.Field(
        alias="transactionHash", default=None
    )
    updated_at: typing.Optional[str] = pydantic.Field(alias="updatedAt", default=None)


class PostTransferCryptoToCryptoResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    transfer_details: typing.Optional[
        PostTransferCryptoToCryptoResponseTransferDetails
    ] = pydantic.Field(alias="transferDetails", default=None)
    transfer_type: typing.Optional[str] = pydantic.Field(
        alias="transferType", default=None
    )


class GetTransferCryptoToCryptoResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    transfer_details: typing.Optional[
        GetTransferCryptoToCryptoResponseTransferDetails
    ] = pydantic.Field(alias="transferDetails", default=None)
    transfer_type: typing.Optional[str] = pydantic.Field(
        alias="transferType", default=None
    )
