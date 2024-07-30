import os

from xian_py.xian import Xian
from xian_py.wallet import Wallet

from config import PRIV_KEY, LOCAL, TESTNET, MAINNET

def deploy(contract_name, network="local"):
    xian = Xian(
        LOCAL,
        wallet=Wallet(PRIV_KEY)
    )
    if network == "testnet": 
        xian =  Xian(
            TESTNET,
            wallet=Wallet(PRIV_KEY)
        )
    elif network == "mainnet":
        xian =  Xian(
            MAINNET,
            wallet=Wallet(PRIV_KEY)
        )

    with open(f'contracts/{contract_name}.py') as f: # ensure the contract name is the same as the file name
        code = f.read()    
        submit = xian.submit_contract(contract_name, code)

        print(f'success: {submit["success"]}')
        print(f'tx_hash: {submit["tx_hash"]}')
        print(f'message: {submit["message"]}')
