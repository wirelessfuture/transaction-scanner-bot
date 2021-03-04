from dataclasses import dataclass


@dataclass
class Address:
    name: str
    address: float

@dataclass
class Transaction:
    txhash: str
    block_height: int
    timestamp: int
    nonce: int
    from_address: str
    to_address: str
    value: int
    gas_price: int
    gas_used: int
    tx_input: str
    position_in_block: int
    is_error: bool