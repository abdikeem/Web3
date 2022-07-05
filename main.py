import json
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/e9f149bc1a424e689eefdd70d379e11c"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())
