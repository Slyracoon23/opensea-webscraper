import requests
import json
import sys
import csv

contractAddress = "0x025C6da5BD0e6A5dd1350fda9e3B6a614B205a1F" # ApeToken Contract
topic = sys.argv[1]
# topic = "0x592993b07849bd4ab51c2de371aea3db52156da6f3cd8476b1c585454b254f48" # AlphaClaim event
# topic = "0x60a71155ef46ccb54dcf7272c207d5c8115509a8f30aa6c09b8fc4cbbe3fa486" # BetaClaim event
# topic = "0xe76cdf9bb2f0219ea4bb21f5df9c962806cc82832dc5c7789f0f2ef7b57b1761" # GammaClaim event


YourApiKeyToken = "BAI15JS8BKAH4NVRES148UFTC9RPY7ZFD4"
# Bored Ape

res = requests.get(f'https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey={YourApiKeyToken}')

startBlock = 14403861
blockNumber = int(res.json()["result"],16)

# blockNumber = 14404020

batch_size =  10
tokenIDs_claimed = set()

for i in range(startBlock, blockNumber, batch_size):
    res = requests.get(f'https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock={i}&toBlock={i+batch_size}&address={contractAddress}&topic0={topic}&apikey={YourApiKeyToken}')

    result = res.json()


    for event in result["result"]:
        token_claimed =int(event["topics"][1],16)
        print(f'{sys.argv[3]} tokenID: {token_claimed} claimed')
        tokenIDs_claimed.add(token_claimed)

print(f'Total Claimed: {len(tokenIDs_claimed)}')

total_tokenIds = set(range(0,int(sys.argv[2])))
# total_tokenIds = set(range(0,10000))

claimable = total_tokenIds.difference(tokenIDs_claimed)
print(f'Claimable: {len(claimable)}')


with open(f'{sys.argv[3]}.csv', 'w') as f:
# with open(f'test.csv', 'w') as f:

    writer = csv.writer(f, delimiter='\n')
    
    writer.writerow(claimable)





