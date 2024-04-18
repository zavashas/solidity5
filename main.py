from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address


w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract = w3.eth.contract(address=contract_address, abi=abi)


print(f"Баланс первого аккаунта: {w3.eth.get_balance('0x49dEBFF101bd9Ce9770df6ed2B9e2A60a61dDC08')}")
print(f"Баланс второго аккаунта: {w3.eth.get_balance('0x7e8CCCe7DDe14dEf327888D6B04c488533913722')}")
print(f"Баланс третьего аккаунта: {w3.eth.get_balance('0x1976A592aBAFe62Eb98ec3b5789b2F71F6C5D30d')}")
print(f"Баланс четвертого аккаунта: {w3.eth.get_balance('0xb029B40BC7858659C2Dc18afB1B0e4Bb028f4916')}")
print(f"Баланс пятого аккаунта: {w3.eth.get_balance('0xE5Cc65694a84c167c86223455Fdf8Cba4a10C0A5')}")