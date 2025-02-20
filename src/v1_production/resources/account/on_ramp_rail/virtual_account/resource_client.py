"""File Generated by Sideko (sideko.dev)"""

from v1_production.core import (
    default_request_options,
    RequestOptions,
    QueryParams,
    SyncBaseClient,
    AsyncBaseClient,
    encode_param,
)
import typing_extensions
import typing
from v1_production.types.account.on_ramp_rail.virtual_account import models


class VirtualAccountClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        destination_chain: typing_extensions.Literal[
            "POLYGON_MAINNET", "ETHEREUM_MAINNET", "OPTIMISM_MAINNET", "BASE_MAINNET"
        ],
        destination_currency: typing_extensions.Literal["usdc", "usdt"],
        rail: typing_extensions.Literal["US_ACH_WIRE"],
        user_id: str,
        created_after: typing.Optional[str] = None,
        created_before: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetAccountOnRampRailVirtualAccountResponse:
        """
        Get the virtual account information for stable coin deposit. The response will also include the micro deposit information requested by institution.
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["destinationChain"] = encode_param(destination_chain, False)
        _query["destinationCurrency"] = encode_param(destination_currency, False)
        _query["rail"] = encode_param(rail, False)
        _query["userId"] = encode_param(user_id, False)
        if created_after is not None:
            _query["createdAfter"] = encode_param(created_after, False)
        if created_before is not None:
            _query["createdBefore"] = encode_param(created_before, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path="/account/onRampRail/virtualAccount",
            auth_names=["sec0"],
            query_params=_query,
            cast_to=models.GetAccountOnRampRailVirtualAccountResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncVirtualAccountClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        destination_chain: typing_extensions.Literal[
            "POLYGON_MAINNET", "ETHEREUM_MAINNET", "OPTIMISM_MAINNET", "BASE_MAINNET"
        ],
        destination_currency: typing_extensions.Literal["usdc", "usdt"],
        rail: typing_extensions.Literal["US_ACH_WIRE"],
        user_id: str,
        created_after: typing.Optional[str] = None,
        created_before: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetAccountOnRampRailVirtualAccountResponse:
        """
        Get the virtual account information for stable coin deposit. The response will also include the micro deposit information requested by institution.
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["destinationChain"] = encode_param(destination_chain, False)
        _query["destinationCurrency"] = encode_param(destination_currency, False)
        _query["rail"] = encode_param(rail, False)
        _query["userId"] = encode_param(user_id, False)
        if created_after is not None:
            _query["createdAfter"] = encode_param(created_after, False)
        if created_before is not None:
            _query["createdBefore"] = encode_param(created_before, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path="/account/onRampRail/virtualAccount",
            auth_names=["sec0"],
            query_params=_query,
            cast_to=models.GetAccountOnRampRailVirtualAccountResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
