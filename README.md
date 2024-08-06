# node-testing-environment
An easy way to run testing scripts for xian nodes

## Features
- [x] Send Xian coins to an address
- [x] Send a contract transaction
- [x] Approve XSC001 contract to spend tokens
- [x] Deploy contract to network(local node, testnet, mainnet)

## Requirement
* Install Python 3.11.8
* Install xian-py
```
pip install xian-py
```

## Usage
Clone this repo and start writing your scripts in `main.py`
```
git clone https://github.com/KELs7/node-testing-env.git
```
Run with `python3 main.py` or `python main.py`

Change default values in `config.py` as you need

### Contract deployment
To submit a single contract, put the contract file in the `contracts` folder and make sure the name of your contract file is passed to the deploy function `ie deploy(contract_file_name)`. To submit a number of contracts, create a folder within the `contracts` folder and pass the folder name to the deploy contracts function `ie deploy_contracts(folder)`

## TODO
- [x] Deploy multiple contracts at once
- [] Wrap node endpoints for easy use