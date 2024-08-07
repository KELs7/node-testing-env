import os
import time

from xian_py.xian import Xian
from xian_py.wallet import Wallet

from config import PRIV_KEY, LOCAL, TESTNET, MAINNET, TESTNET_CHAIN_ID, MAINNET_CHAIN_ID

contracts_folder = "contracts"

def deploy(contract_name, network="local"):
    xian = None
    
    if network == "testnet": 
        xian =  Xian(
            TESTNET,
            chain_id=TESTNET_CHAIN_ID,
            wallet=Wallet(PRIV_KEY)
        )
    elif network == "mainnet":
        xian =  Xian(
            MAINNET,
            chain_id=MAINNET_CHAIN_ID,
            wallet=Wallet(PRIV_KEY)
        )
    else:
        xian = Xian(
            LOCAL,
            wallet=Wallet(PRIV_KEY)
        )

    with open(f'{contracts_folder}/{contract_name}.py') as f: # ensure the contract name is the same as the file name
        code = f.read()    
        submit = xian.submit_contract(contract_name, code)

        print(f'success: {submit["success"]}')
        print(f'tx_hash: {submit["tx_hash"]}')
        print(f'message: {submit["message"]}')

def deploy_contracts(folder, network="local"):
    xian = None

    if network == "testnet": 
        xian =  Xian(
            TESTNET,
            chain_id=TESTNET_CHAIN_ID,
            wallet=Wallet(PRIV_KEY)
        )
    elif network == "mainnet":
        xian =  Xian(
            MAINNET,
            chain_id=MAINNET_CHAIN_ID,
            wallet=Wallet(PRIV_KEY)
        )
    else:
        xian = Xian(
            LOCAL,
            wallet=Wallet(PRIV_KEY)
        )

    for root, dirs, files in os.walk(f'{contracts_folder}/{folder}'):
        for file in files:
            contract_name = file[:-3]

            with open(f'{contracts_folder}/{folder}/{contract_name}.py') as f:
                code = f.read()    
                submit = xian.submit_contract(contract_name, code)

                print(f'success: {submit["success"]}')
                print(f'tx_hash: {submit["tx_hash"]}')
                print(f'message: {submit["message"]}')

            time.sleep(3)
