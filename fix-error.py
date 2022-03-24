import re
from opensea import query_webpage

fh = open("Bored Ape Kennel Club.csv", "r").read()
output = open("Bored Ape Kennel Club Latest.csv", "w")

for line in re.findall("FAILED: TokenID: .\d", fh):

    tokenID = line.split()[-1]


    result = query_webpage(tokenID)[0]

    output.write(f'{result}\n')


output.close()


# result = re.sub('FAILED: TokenID: .\d', '' ,fh, flags = re.M)
