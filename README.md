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

Read the [docs](https://github.com/KELs7/node-testing-env/blob/main/docs/api.md) for functions available for use.

## TODO
- [x] Deploy multiple contracts at once
- [] Wrap node endpoints for easy use