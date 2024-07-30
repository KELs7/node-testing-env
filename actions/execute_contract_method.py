from xian_py.xian import Xian
from xian_py.wallet import Wallet

from config import PRIV_KEY, LOCAL, TESTNET, MAINNET

def execute(contract, method, kwargs ,network="local"):
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

    data = xian.send_tx(
        contract,
        method,
        kwargs
    )

    print(f'sent: {data}')

    time.sleep(3)

    tx = xian.get_tx(data['tx_hash'])
    print(f'tx: {tx}')
