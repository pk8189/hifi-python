"""File Generated by Sideko (sideko.dev)"""

from v1_production.core import (
    to_encodable,
    default_request_options,
    encode_param,
    SyncBaseClient,
    AsyncBaseClient,
    RequestOptions,
    QueryParams,
)
from v1_production.types.account.usd.onramp.plaid import models, params
import typing


class PlaidClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: typing.Optional[params.PostAccountUsdOnrampPlaidBody] = None,
        user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostAccountUsdOnrampPlaidResponse:
        """
        HIFI and Plaid have partnered to enable you to use your existing Plaid integration to connect bank accounts and leverage HIFI's transfer automation capabilities.  To get started, follow the below guide from Plaid's API docs. Completing the process will result in the creation of a processor_token.  Sending the processor_token to this endpoint will create an Account for a User within the HIFI platform. You can then easily use the resulting account id as the source of a onramp transaction. https://plaid.com/docs/api/processors/
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if user_id is not None:
            _query["userId"] = encode_param(user_id, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostAccountUsdOnrampPlaidBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/account/usd/onramp/plaid",
            auth_names=["sec0"],
            query_params=_query,
            json=_json,
            cast_to=models.PostAccountUsdOnrampPlaidResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncPlaidClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: typing.Optional[params.PostAccountUsdOnrampPlaidBody] = None,
        user_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostAccountUsdOnrampPlaidResponse:
        """
        HIFI and Plaid have partnered to enable you to use your existing Plaid integration to connect bank accounts and leverage HIFI's transfer automation capabilities.  To get started, follow the below guide from Plaid's API docs. Completing the process will result in the creation of a processor_token.  Sending the processor_token to this endpoint will create an Account for a User within the HIFI platform. You can then easily use the resulting account id as the source of a onramp transaction. https://plaid.com/docs/api/processors/
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if user_id is not None:
            _query["userId"] = encode_param(user_id, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostAccountUsdOnrampPlaidBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/account/usd/onramp/plaid",
            auth_names=["sec0"],
            query_params=_query,
            json=_json,
            cast_to=models.PostAccountUsdOnrampPlaidResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
