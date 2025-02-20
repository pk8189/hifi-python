"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class PutUserBusinessResponseRampsEuroSepaOffRampActionNeeded(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    actions: typing.Optional[typing.Any] = pydantic.Field(alias="actions", default=None)
    fields_to_resubmit: typing.Optional[typing.Any] = pydantic.Field(
        alias="fieldsToResubmit", default=None
    )


class PutUserBusinessResponseRampsEuroSepaOnRampActionNeeded(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    actions: typing.Optional[typing.Any] = pydantic.Field(alias="actions", default=None)
    fields_to_resubmit: typing.Optional[typing.Any] = pydantic.Field(
        alias="fieldsToResubmit", default=None
    )


class PutUserBusinessResponseRampsUsdAchOffRampActionNeeded(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    actions: typing.Optional[typing.Any] = pydantic.Field(alias="actions", default=None)
    fields_to_resubmit: typing.Optional[typing.Any] = pydantic.Field(
        alias="fieldsToResubmit", default=None
    )


class PutUserBusinessResponseRampsUsdAchOnRampAchPullActionNeeded(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    actions: typing.Optional[typing.Any] = pydantic.Field(alias="actions", default=None)
    fields_to_resubmit: typing.Optional[typing.Any] = pydantic.Field(
        alias="fieldsToResubmit", default=None
    )


class PutUserBusinessResponseRampsUsdAchOnRampActionNeeded(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    actions: typing.Optional[typing.Any] = pydantic.Field(alias="actions", default=None)
    fields_to_resubmit: typing.Optional[typing.Any] = pydantic.Field(
        alias="fieldsToResubmit", default=None
    )


class PutUserBusinessResponseUser(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)


class PutUserBusinessResponseUserKycActionNeeded(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    actions: typing.Optional[typing.Any] = pydantic.Field(alias="actions", default=None)
    fields_to_resubmit: typing.Optional[typing.Any] = pydantic.Field(
        alias="fieldsToResubmit", default=None
    )


class PutUserBusinessResponseWalletActionNeeded(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    actions: typing.Optional[typing.Any] = pydantic.Field(alias="actions", default=None)
    fields_to_resubmit: typing.Optional[typing.Any] = pydantic.Field(
        alias="fieldsToResubmit", default=None
    )


class PutUserBusinessResponseWalletWalletAddressEthereumMainnet(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)


class PutUserBusinessResponseWalletWalletAddressOptimismMainnet(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)


class PutUserBusinessResponseWalletWalletAddressPolygonMainnet(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)


class PutUserBusinessResponseRampsEuroSepaOffRamp(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    action_needed: typing.Optional[
        PutUserBusinessResponseRampsEuroSepaOffRampActionNeeded
    ] = pydantic.Field(alias="actionNeeded", default=None)
    message: typing.Optional[str] = pydantic.Field(alias="message", default=None)
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)


class PutUserBusinessResponseRampsEuroSepaOnRamp(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    action_needed: typing.Optional[
        PutUserBusinessResponseRampsEuroSepaOnRampActionNeeded
    ] = pydantic.Field(alias="actionNeeded", default=None)
    message: typing.Optional[str] = pydantic.Field(alias="message", default=None)
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)


class PutUserBusinessResponseRampsUsdAchOffRamp(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    action_needed: typing.Optional[
        PutUserBusinessResponseRampsUsdAchOffRampActionNeeded
    ] = pydantic.Field(alias="actionNeeded", default=None)
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)


class PutUserBusinessResponseRampsUsdAchOnRampAchPull(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ach_pull_status: typing.Optional[str] = pydantic.Field(
        alias="achPullStatus", default=None
    )
    action_needed: typing.Optional[
        PutUserBusinessResponseRampsUsdAchOnRampAchPullActionNeeded
    ] = pydantic.Field(alias="actionNeeded", default=None)


class PutUserBusinessResponseUserKyc(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    action_needed: typing.Optional[PutUserBusinessResponseUserKycActionNeeded] = (
        pydantic.Field(alias="actionNeeded", default=None)
    )
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)


class PutUserBusinessResponseWalletWalletAddress(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ethereum_mainnet: typing.Optional[
        PutUserBusinessResponseWalletWalletAddressEthereumMainnet
    ] = pydantic.Field(alias="ETHEREUM_MAINNET", default=None)
    optimism_mainnet: typing.Optional[
        PutUserBusinessResponseWalletWalletAddressOptimismMainnet
    ] = pydantic.Field(alias="OPTIMISM_MAINNET", default=None)
    polygon_mainnet: typing.Optional[
        PutUserBusinessResponseWalletWalletAddressPolygonMainnet
    ] = pydantic.Field(alias="POLYGON_MAINNET", default=None)


class PutUserBusinessResponseRampsEuroSepa(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    off_ramp: typing.Optional[PutUserBusinessResponseRampsEuroSepaOffRamp] = (
        pydantic.Field(alias="offRamp", default=None)
    )
    on_ramp: typing.Optional[PutUserBusinessResponseRampsEuroSepaOnRamp] = (
        pydantic.Field(alias="onRamp", default=None)
    )


class PutUserBusinessResponseRampsUsdAchOnRamp(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ach_pull: typing.Optional[PutUserBusinessResponseRampsUsdAchOnRampAchPull] = (
        pydantic.Field(alias="achPull", default=None)
    )
    action_needed: typing.Optional[
        PutUserBusinessResponseRampsUsdAchOnRampActionNeeded
    ] = pydantic.Field(alias="actionNeeded", default=None)
    message: typing.Optional[str] = pydantic.Field(alias="message", default=None)
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)


class PutUserBusinessResponseWallet(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    action_needed: typing.Optional[PutUserBusinessResponseWalletActionNeeded] = (
        pydantic.Field(alias="actionNeeded", default=None)
    )
    wallet_address: typing.Optional[PutUserBusinessResponseWalletWalletAddress] = (
        pydantic.Field(alias="walletAddress", default=None)
    )
    wallet_message: typing.Optional[str] = pydantic.Field(
        alias="walletMessage", default=None
    )
    wallet_status: typing.Optional[str] = pydantic.Field(
        alias="walletStatus", default=None
    )


class PutUserBusinessResponseRampsUsdAch(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    off_ramp: typing.Optional[PutUserBusinessResponseRampsUsdAchOffRamp] = (
        pydantic.Field(alias="offRamp", default=None)
    )
    on_ramp: typing.Optional[PutUserBusinessResponseRampsUsdAchOnRamp] = pydantic.Field(
        alias="onRamp", default=None
    )


class PutUserBusinessResponseRamps(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    euro_sepa: typing.Optional[PutUserBusinessResponseRampsEuroSepa] = pydantic.Field(
        alias="euroSepa", default=None
    )
    usd_ach: typing.Optional[PutUserBusinessResponseRampsUsdAch] = pydantic.Field(
        alias="usdAch", default=None
    )


class PutUserBusinessResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ramps: typing.Optional[PutUserBusinessResponseRamps] = pydantic.Field(
        alias="ramps", default=None
    )
    user: typing.Optional[PutUserBusinessResponseUser] = pydantic.Field(
        alias="user", default=None
    )
    user_kyc: typing.Optional[PutUserBusinessResponseUserKyc] = pydantic.Field(
        alias="user_kyc", default=None
    )
    wallet: typing.Optional[PutUserBusinessResponseWallet] = pydantic.Field(
        alias="wallet", default=None
    )
