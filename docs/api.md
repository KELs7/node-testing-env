# API

## approve
approve a contract
```
parameters:
    inputs:
        contract: string
        amount: number
    defaults:
        network = "local"      #other options: "testnet" | "mainnet"

returns:
    string
```

## deploy
deploy a single contract
```
parameters:
    inputs:
        contract_name: string 
    defaults:
        network="local"     #other options: "testnet" | "mainnet"

returns:
    string
```

## deploy_contracts
deploy multiple contracts once
```
parameters:
    inputs:
        folder: string 
    defaults:
        network="local"     #other options: "testnet" | "mainnet"
returns:
    string
```

## execute
call a contract method
```
parameters:
    inputs:
        contract_name: string 
        method: string
        kwargs: dictionary
    defaults:
        network="local"     #other options: "testnet" | "mainnet"
returns:
    string
```

## send
send Xian to an address
```
parameters:
    inputs:
        contract_name: string 
        amount: number
        to_address: string
    defaults:
        network="local"     #other options: "testnet" | "mainnet"

returns:
    string
```

## query_contracts
fetch deployed contracts on Xian
```
parameters:
    defaults:
        network = "local"       #other options: "testnet" | "mainnet"
        raw = False     #returns decoded value

returns:
    list | string
```
## query_state
fetch key-value states of a contract from a Xian node
```
parameters:
    inputs:
        contract: string
        storage_name: string
    defaults:
        limit = 1       #returns one item
        offset = 0      #start from a certain point from last known state
        network = "local"       #other options: "testnet" | "mainnet"
        raw = False     #returns decoded value

returns:
    list | string
```