from tkinter import E
from web3 import web3, EthereumTesterProvider
w3 = web3(EthereumTesterProvider())

w3.isConnected()
