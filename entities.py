from dataclasses import dataclass


@dataclass
class Address:
    name: str
    address: float

@dataclass
class Transaction:
    txhash: string
    block_height: int
    timestamp: int
    nonce: int
    from_address: string
    to_address: string
    value: int
    gas_price: int
    tx_input: string
    position_in_block: int
    is_error: bool