"""File Generated by Sideko (sideko.dev)"""

from v1_production.core import (
    RequestOptions,
    encode_param,
    to_encodable,
    SyncBaseClient,
    QueryParams,
    default_request_options,
    AsyncBaseClient,
)
from v1_production.types.account.euro.offramp import models, params
import typing


class OfframpClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: typing.Optional[params.PostAccountEuroOfframpBody] = None,
        user_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostAccountEuroOfframpResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["userId"] = encode_param(user_id, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostAccountEuroOfframpBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/account/euro/offramp",
            auth_names=["sec0"],
            query_params=_query,
            json=_json,
            cast_to=models.PostAccountEuroOfframpResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncOfframpClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: typing.Optional[params.PostAccountEuroOfframpBody] = None,
        user_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostAccountEuroOfframpResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["userId"] = encode_param(user_id, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostAccountEuroOfframpBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/account/euro/offramp",
            auth_names=["sec0"],
            query_params=_query,
            json=_json,
            cast_to=models.PostAccountEuroOfframpResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
