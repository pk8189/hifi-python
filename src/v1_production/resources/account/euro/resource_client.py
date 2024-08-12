"""File Generated by Sideko (sideko.dev)"""

from v1_production.core import AsyncBaseClient, SyncBaseClient
from v1_production.resources.account.euro.offramp import (
    OfframpClient,
    AsyncOfframpClient,
)


class EuroClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.offramp = OfframpClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncEuroClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.offramp = AsyncOfframpClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
