"""File Generated by Sideko (sideko.dev)"""

from v1_production.core import (
    default_request_options,
    SyncBaseClient,
    to_encodable,
    RequestOptions,
    AsyncBaseClient,
)
from v1_production.types.user.create_business import models, params
import typing


class CreateBusinessClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: typing.Optional[params.PostUserCreateBusinessBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostUserCreateBusinessResponse:
        """
        This endpoint handles user creation in an asynchronous manner. Polling the GET /user endpoint after creating the user is highly recommended. Note that adding "#business" at the end of the url is optional.
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostUserCreateBusinessBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/user/create#business",
            auth_names=["sec0"],
            json=_json,
            cast_to=models.PostUserCreateBusinessResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncCreateBusinessClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: typing.Optional[params.PostUserCreateBusinessBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostUserCreateBusinessResponse:
        """
        This endpoint handles user creation in an asynchronous manner. Polling the GET /user endpoint after creating the user is highly recommended. Note that adding "#business" at the end of the url is optional.
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostUserCreateBusinessBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/user/create#business",
            auth_names=["sec0"],
            json=_json,
            cast_to=models.PostUserCreateBusinessResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
