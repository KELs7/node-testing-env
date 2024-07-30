from xian_py.xian import Xian
from xian_py.wallet import Wallet

from config import PRIV_KEY, LOCAL, TESTNET, MAINNET

def approve(contract, amount=10000000000 ,network="local"):
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

    approved = xian.get_approved_amount(contract)
    print(f'approved: {approved}')
    
    approve = xian.approve(contract, amount=amount)
    print(f'approve: {approve}')
    print('waiting...')
    
    time.sleep(3)
    
    approved = xian.get_approved_amount(contract)
    print(f'approved: {approved}')
    
    tx = xian.get_tx(approve['tx_hash'])
    print(f'tx: {tx}')
