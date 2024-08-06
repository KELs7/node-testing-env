import base64
import json
import subprocess

from config import LOCAL, TESTNET, MAINNET

def query_contracts(network="local", raw=False) -> str | list:
    network_url = LOCAL
    if network == "testnet":
        network_url = TESTNET
    elif network == "mainnet":
        network_url = MAINNET
    query_result = subprocess.check_output(["curl", f'{network_url}/abci_query?path="/contracts"'], text=True)
    if raw:
        print(query_result)
    else:
        dict_query_result = json.loads(query_result)
        value = dict_query_result["result"]["response"]["value"]
        str_value = base64.b64decode(value).decode("utf-8")
        list_value = json.loads(str_value)
        print(list_value)
    
