from web3 import Web3
import json
import requests

infura_url = 'https://mainnet.infura.io/v3/1f136d6e7253493eba27b54cfd0f62c4'
web3 = Web3(Web3.HTTPProvider(infura_url))

req_ethgas_data = requests.get('https://ethgasstation.info/json/ethgasAPI.json')
trans_info = json.loads(req_ethgas_data.content)

print('safeLow', trans_info['safeLow'])
print('average', trans_info['average'])
print('fast', trans_info['fast'])
print('fastest', trans_info['fastest'])
print('Block number:', trans_info['blockNum'])


gas_price = web3.eth.gas_Price
print('Calculated gas price: ', gas_price/10**9)