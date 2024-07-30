import time

from xian_py.xian import Xian
from xian_py.wallet import Wallet

from config import PRIV_KEY, LOCAL, TESTNET, MAINNET

def send(amount, to_address, network="local"):
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

    print(f'address: {xian.wallet.public_key}')
    print(f'balance: {xian.get_balance()}')
    data = xian.send(
        amount=amount,
        to_address=to_address
    )
    print(f'sent: {data}')
    print('waiting...')

    time.sleep(3)

    print(f'balance: {xian.get_balance()}')

    data = xian.get_tx(data['tx_hash'])
    print(f'tx result: {data}')
