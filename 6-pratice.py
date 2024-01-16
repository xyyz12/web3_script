from web3 import Web3
from env import *


# Your Infura Project ID
INFURA_SECRET_KEY = ENV.INFURA_SECRET_KEY.value

I = "http://127.0.0.1:xxxx"
# get w3 endpoint by network name
def get_w3_by_network(network='mainnet'):
    infura_url = f'https://{network}.infura.io/v3/{INFURA_SECRET_KEY}' # 接入 Infura 节点
    w3 = Web3(Web3.HTTPProvider(infura_url, request_kwargs={"proxies":{'https' : I, 'http' : I }}))
    return w3


def refuel_eth(w3, from_address, private_key, contract_address, amount_in_ether, chainId, destinationChainId):

    from_address = Web3.toChecksumAddress(from_address)
    contract_address = Web3.toChecksumAddress(contract_address)

    ABI = ''

    amount_in_wei = w3.toWei(amount_in_ether, 'ether')
    nonce = w3.eth.getTransactionCount(from_address)

    params = {   
        'chainId': chainId,
        'gas': 250000,
        'nonce': nonce,
        'from': from_address,
        'value': amount_in_wei,
        # 'gasPrice': w3.toWei('5', 'gwei'),
        'maxFeePerGas': w3.toWei(5, 'gwei'),
        'maxPriorityFeePerGas': w3.toWei(5, 'gwei'),
    }


    contract = w3.eth.contract(address=contract_address, abi=ABI)
    
    try:
        raw_txn = contract.functions.depositNativeToken(destinationChainId, from_address).buildTransaction(params)
        
        signed_txn = w3.eth.account.sign_transaction(raw_txn, private_key=private_key)
        txn = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return {'status': 'succeed', 'txn_hash': w3.toHex(txn), 'task': 'arb Bridge ETH'}
    except Exception as e:
        return {'status': 'failed', 'error': e, 'task': 'arb Bridge ETH'}



def main():

    w3 = get_w3_by_network(network='mainnet')

    from_address = ENV.From_Address.value
    private_key = ENV.Private_Key.value

    contract_address = '0xb584D4bE1A5470CA1a8778E9B86c81e165204599'

    amount_in_ether = 0.0018
   
    chainId = 1 #主网
    destinationChainId = 42161 #arb链
    
    result = refuel_eth(w3, from_address, private_key, contract_address, amount_in_ether, chainId, destinationChainId)
    print(result)


if __name__ == "__main__":
    main()