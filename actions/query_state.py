import base64
import json
import subprocess

from config import LOCAL, TESTNET, MAINNET


def query_state(contract, storage_name, limit=0, offset=0,network="local", raw=False) -> str | list:
    network_url = LOCAL
    if network == "testnet":
        network_url = TESTNET
    elif network == "mainnet":
        network_url = MAINNET
    query_result = subprocess.check_output(
        [
            "curl",
            f"{network_url}/abci_query?path=%22/state/{contract}.{storage_name}/limit={limit}/offset={offset}%22",
        ],
        text=True,
    )
    if raw:
        print(query_result)
    else:
        dict_query_result = json.loads(query_result)
        value = dict_query_result["result"]["response"]["value"]
        str_value = base64.b64decode(value).decode("utf-8")
        list_value = json.loads(str_value)
        print(list_value)
