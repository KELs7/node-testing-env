# you can import only what you need
from actions import (
    approve, # noqa: F401
    deploy, # noqa: F401
    deploy_contracts, # noqa: F401 
    execute, # noqa: F401
    query_contracts, # noqa: F401
    query_state, # noqa: F401
    send # noqa: F401
)

# This is where to run scripts
# Uncomment this to run locally
#deploy('con_my_token')

# 5fa1b314468832fb9d391e8af756140e85325a565d8b411ae2f2001d37c30ef4
# send(100, "5fa1b314468832fb9d391e8af756140e85325a565d8b411ae2f2001d37c30ef4")

#deploy_contracts("pixel_frames", network="testnet")
# query_state("stamp_cost", "S", network="testnet", raw=True)
query_contracts(network="testnet", raw=True)
