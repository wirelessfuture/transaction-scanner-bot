from typing import List

from entities import Address


class InMemoryDB:
    def __init__(self, last_block: int):
        self.addresslist = []
        self.last_block = last_block

    def get_addresses(self) -> List[Address]:
        return self.addresslist

    def add_address(self, address: Address) -> None:
        if isinstance(address, Address):
            self.addresslist.append(address)

    def remove_address(self, name: str) -> None:
        to_remove = [address for address in self.addresslist if address.name == name][0]
        self.addresslist.remove(to_remove)