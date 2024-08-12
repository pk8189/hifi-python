"""File Generated by Sideko (sideko.dev)"""

from v1_production.core import SyncBaseClient, AsyncBaseClient
from v1_production.resources.transfer.conversion_rate import (
    ConversionRateClient,
    AsyncConversionRateClient,
)
from v1_production.resources.transfer.crypto_to_crypto import (
    CryptoToCryptoClient,
    AsyncCryptoToCryptoClient,
)
from v1_production.resources.transfer.crypto_to_fiat import (
    AsyncCryptoToFiatClient,
    CryptoToFiatClient,
)
from v1_production.resources.transfer.fiat_to_crypto import (
    FiatToCryptoClient,
    AsyncFiatToCryptoClient,
)


class TransferClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.conversion_rate = ConversionRateClient(base_client=self._base_client)
        self.crypto_to_crypto = CryptoToCryptoClient(base_client=self._base_client)
        self.crypto_to_fiat = CryptoToFiatClient(base_client=self._base_client)
        self.fiat_to_crypto = FiatToCryptoClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncTransferClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.conversion_rate = AsyncConversionRateClient(base_client=self._base_client)
        self.crypto_to_crypto = AsyncCryptoToCryptoClient(base_client=self._base_client)
        self.crypto_to_fiat = AsyncCryptoToFiatClient(base_client=self._base_client)
        self.fiat_to_crypto = AsyncFiatToCryptoClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
