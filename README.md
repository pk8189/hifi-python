
# v1 production Python SDK

## Overview


## Initilization
Initialize either the synchronous or asynchronous client to authenticate

### Synchronous Client
```python
from v1_production import Client
from os import getenv

Client(api_key=getenv("API_KEY"))
```

### Asynchronous Client
```python
from v1_production import AsyncClient
from os import getenv

AsyncClient(api_key=getenv("API_KEY"))
```


### Get Account
> Returns a bank account that was added with HIFI's /account endpoints.

```python
client.account.list(account_id="string")
```

---

### Get All Accounts
> Returns all bank accounts that was added with HIFI's /account endpoints under specified rail.

```python
client.account.all.list(
    created_after="string",
    created_before="string",
    currency="usd",
    limit="string",
    payment_rail="ach",
    rail_type="onramp",
    user_id="string",
)
```

---

### Get Deposit Bank Account Information
> Get the virtual account information for stable coin deposit. The response will also include the micro deposit information requested by institution.

```python
client.account.on_ramp_rail.virtual_account.list(
    destination_chain="POLYGON_MAINNET",
    destination_currency="usdc",
    rail="US_ACH_WIRE",
    user_id="string",
    created_after="string",
    created_before="string",
    limit="string",
)
```

---

### Ping HIFI Servers
> 

```python
client.ping.list()
```

---

### Stablecoin-to-Fiat Conversion Rate
> Retrieve conversion rate between stablecoin and fiat currency

```python
client.transfer.conversion_rate.crypto_to_fiat.list(
    from_currency="usdc", to_currency="usd"
)
```

---

### Get a Stablecoin-to-Stablecoin Transfer Record
> Get the transfer history of a specific crypto to crypto transfer

```python
client.transfer.crypto_to_crypto.list(id="string")
```

---

### Get All Stablecoin-to-Stablecoin Transfer Records
> Get all the transfer history of a user as a sender or all transfer records of your organization

```python
client.transfer.crypto_to_crypto.all.list(
    created_after="string", created_before="string", limit="string", user_id="string"
)
```

---

### Get a Stablecoin-to-Fiat Transfer Record
> Get the transfer history of a specific stablecoin to fiat transfer

```python
client.transfer.crypto_to_fiat.list(id="string")
```

---

### Get All Stablecoin-to-Fiat Transfer Records
> Get all the transfer history of a user or your organization

```python
client.transfer.crypto_to_fiat.all.list(
    created_after="string", created_before="string", limit="string", user_id="string"
)
```

---

### Get a Fiat-to-Stablecoin Transfer Record
> Get the transfer history of a specific fiat to stablecoin transfer

```python
client.transfer.fiat_to_crypto.list(id="string")
```

---

### Get All Fiat-to-Stablecoin Transfer Records
> Get all the transfer history of a user or your organization

```python
client.transfer.fiat_to_crypto.all.list(
    created_after="string", created_before="string", limit="string", user_id="string"
)
```

---

### Get User
> 

```python
client.user.list(user_id="string")
```

---

### Get All Users
> Get all the users created under your organization

```python
client.user.all.list(
    created_after="string",
    created_before="string",
    limit="string",
    user_type="individual",
)
```

---

### Activate Fiat to Stablecoin Conversion
> Enable ACH to stablecoin converstion for users. This is a billable event.

```python
client.account.activate_on_ramp_rail.create(
    user_id="string",
    data={
        "destination_chain": "POLYGON_MAINNET",
        "destination_currency": "usdc",
        "rail": "US_ACH_WIRE",
    },
)
```

---

### Add a Bank Account to Receiver for BRL Offramp
> 

```python
client.account.brl.offramp.create(
    data={
        "bank_country": "string",
        "currency": "BRL",
        "name": "string",
        "pix_key": "string",
        "receiver_id": "string",
        "user_id": "string",
    }
)
```

---

### Add a Receiver for BRL Offramp
> 

```python
client.account.brl.receiver.create(
    data={
        "address_line_1": "string",
        "address_line_2": "string",
        "city": "string",
        "country": "string",
        "date_of_birth": "string",
        "email_field": "string",
        "first_name": "string",
        "image_url": "string",
        "last_name": "string",
        "postal_code": "string",
        "state_province_region": "string",
        "tax_id": "string",
        "type": "individual",
        "user_id": "string",
    }
)
```

---

### Add a SEPA Destination Bank Account for EURO Offramp
> 

```python
client.account.euro.offramp.create(
    user_id="string",
    data={
        "account_owner_name": "string",
        "account_owner_type": "individual",
        "bank_name": "string",
        "business_identifier_code": "string",
        "business_name": "string",
        "currency": "eur",
        "first_name": "string",
        "iban_account_number": "string",
        "iban_country_code": "string",
        "last_name": "string",
    },
)
```

---

### Add a ACH Destination Bank Account for USD Offramp
> 

```python
client.account.usd.offramp.create(
    user_id="string",
    data={
        "account_number": "string",
        "account_owner_name": "string",
        "account_owner_type": "individual",
        "bank_name": "string",
        "city": "string",
        "country": "string",
        "currency": "usd",
        "postal_code": "string",
        "routing_number": "string",
        "state": "string",
        "street_line1": "string",
        "street_line2": "string",
    },
)
```

---

### Add a Wire Destination Bank Account for USD Offramp
> 

```python
client.account.usd.offramp.wire.create(
    user_id="string",
    data={
        "account_number": "string",
        "account_owner_type": "individual",
        "bank_identifier_code": "string",
        "bank_name": "string",
        "business_name": "string",
        "city": "string",
        "country": "string",
        "currency": "usd",
        "first_name": "string",
        "iban": "string",
        "last_name": "string",
        "legal_full_name": "string",
        "middle_name": "string",
        "postal_code": "string",
        "state": "string",
        "street_line1": "string",
        "street_line2": "string",
    },
)
```

---

### Add a Plaid Bank Account for USD Onramp
> HIFI and Plaid have partnered to enable you to use your existing Plaid integration to connect bank accounts and leverage HIFI's transfer automation capabilities.  To get started, follow the below guide from Plaid's API docs. Completing the process will result in the creation of a processor_token.  Sending the processor_token to this endpoint will create an Account for a User within the HIFI platform. You can then easily use the resulting account id as the source of a onramp transaction. https://plaid.com/docs/api/processors/

```python
client.account.usd.onramp.plaid.create(
    user_id="string",
    data={
        "account_type": "CHECKING",
        "bank_name": "string",
        "plaid_processor_token": "string",
    },
)
```

---

### Generate Terms of Service Link
> The Terms of Service page must be displayed to the end user. This page can be whitelabeled upon request.

```python
client.tos_link.create(
    data={
        "idempotency_key": "string",
        "redirect_url": "string",
        "template_id": "string",
    }
)
```

---

### Transfer Stablecoin to Stablecoin
> Transfer stablecoins between users or wallet addresses

```python
client.transfer.crypto_to_crypto.create(
    data={
        "amount": 123.45,
        "chain": "POLYGON_MAINNET",
        "currency": "usdc",
        "recipient_address": "string",
        "recipient_user_id": "string",
        "request_id": "string",
        "sender_user_id": "string",
    }
)
```

---

### Transfer Stablecoin to Fiat
> Liquidate stablecoin into fiat currency and send to a destination bank account

```python
client.transfer.crypto_to_fiat.create(
    data={
        "amount": 123.45,
        "chain": "POLYGON_MAINNET",
        "description": "string",
        "destination_account_id": "string",
        "destination_currency": "usd",
        "destination_user_id": "string",
        "payment_rail": "ach",
        "purpose_of_payment": "payment_for_goods",
        "request_id": "string",
        "source_currency": "usdc",
        "source_user_id": "string",
    }
)
```

---

### Transfer Fiat to Stablecoin
> Move fiat funds in a bank account into stablecoin on the blockchain

```python
client.transfer.fiat_to_crypto.create(
    data={
        "amount": 123.45,
        "chain": "POLYGON_MAINNET",
        "destination_currency": "usdc",
        "destination_user_id": "string",
        "is_instant": True,
        "request_id": "string",
        "source_account_id": "string",
        "source_currency": "usd",
        "source_user_id": "string",
    }
)
```

---

### Create User (Individual)
> This endpoint handles user creation in an asynchronous manner. Polling the GET /user endpoint after creating the user is highly recommended. Note that adding "#individual" at the end of the url is optional.

```python
client.user.create.create(
    data={
        "address_line1": "string",
        "address_line2": "string",
        "city": "string",
        "compliance_email": "string",
        "compliance_phone": "string",
        "country": "string",
        "date_of_birth": "string",
        "gov_id_back": "string",
        "gov_id_country": "string",
        "gov_id_front": "string",
        "ip_address": "string",
        "legal_first_name": "string",
        "legal_last_name": "string",
        "postal_code": "string",
        "proof_of_residency": "string",
        "signed_agreement_id": "string",
        "state_province_region": "string",
        "tax_identification_number": "string",
        "user_type": "individual",
    }
)
```

---

### Create User (Business)
> This endpoint handles user creation in an asynchronous manner. Polling the GET /user endpoint after creating the user is highly recommended. Note that adding "#business" at the end of the url is optional.

```python
client.user.create_business.create(
    data={
        "address_line1": "string",
        "address_line2": "string",
        "business_description": "string",
        "business_name": "string",
        "business_type": "cooperative",
        "city": "string",
        "compliance_email": "string",
        "compliance_screening_explanation": "string",
        "country": "string",
        "formation_doc": "string",
        "ip_address": "string",
        "is_dao": True,
        "postal_code": "string",
        "proof_of_ownership": "string",
        "proof_of_residency": "string",
        "signed_agreement_id": "string",
        "source_of_funds": "string",
        "state_province_region": "string",
        "tax_identification_number": "string",
        "transmits_customer_funds": True,
        "ultimate_beneficial_owners": [
            {
                "address_line1": "string",
                "address_line2": "string",
                "city": "string",
                "compliance_email": "string",
                "compliance_phone": "string",
                "country": "string",
                "date_of_birth": "string",
                "gov_id_back": "string",
                "gov_id_country": "string",
                "gov_id_front": "string",
                "legal_first_name": "string",
                "legal_last_name": "string",
                "postal_code": "string",
                "proof_of_residency": "string",
                "state_province_region": "string",
                "tax_identification_number": "string",
            }
        ],
        "user_type": "business",
        "website": "string",
    }
)
```

---

### Update User (Individual)
> Use this endpoint to update a User. Submit only the properties you wish to update. For example, if the actions array from the Create User response indicates the ID was blurry, you could use this endpoint to submit a new govIdFront.

```python
client.user.put(
    user_id="string",
    data={
        "address_line1": "string",
        "address_line2": "string",
        "city": "string",
        "compliance_email": "string",
        "compliance_phone": "string",
        "country": "string",
        "date_of_birth": "string",
        "gov_id_back": "string",
        "gov_id_country": "string",
        "gov_id_front": "string",
        "ip_address": "string",
        "legal_first_name": "string",
        "legal_last_name": "string",
        "postal_code": "string",
        "proof_of_residency": "string",
        "signed_agreement_id": "string",
        "state_province_region": "string",
        "tax_identification_number": "string",
    },
)
```

---

### Update User (Business)
> Use this endpoint to update a User. Submit only the properties you wish to update. For example, if the actions array from the Create User response indicates the ID was blurry, you could use this endpoint to submit a new govIdFront.

```python
client.user_business.put(
    user_id="string",
    data={
        "address_line1": "string",
        "address_line2": "string",
        "business_description": "string",
        "business_name": "string",
        "business_type": "cooperative",
        "city": "string",
        "compliance_email": "string",
        "compliance_screening_explanation": "string",
        "country": "string",
        "formation_doc": "string",
        "ip_address": "string",
        "is_dao": True,
        "postal_code": "string",
        "proof_of_ownership": "string",
        "proof_of_residency": "string",
        "signed_agreement_id": "string",
        "source_of_funds": "string",
        "state_province_region": "string",
        "tax_identification_number": "string",
        "transmits_customer_funds": True,
        "ultimate_beneficial_owners": [
            {
                "address_line1": "string",
                "address_line2": "string",
                "city": "string",
                "compliance_email": "string",
                "compliance_phone": "string",
                "country": "string",
                "date_of_birth": "string",
                "gov_id_back": "string",
                "gov_id_country": "string",
                "gov_id_front": "string",
                "legal_first_name": "string",
                "legal_last_name": "string",
                "postal_code": "string",
                "proof_of_residency": "string",
                "state_province_region": "string",
                "tax_identification_number": "string",
            }
        ],
        "website": "string",
    },
)
```


