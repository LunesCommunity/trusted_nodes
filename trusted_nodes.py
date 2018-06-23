#!/usr/bin/python
import LunesLIB as pw
import requests
import math
import json
import re
import urllib2
import io

node = 'http://api.lunes.in'
#nblocks = pw.height()
nblocks = 1440
total_balance = 0
total_fees = 0
generators = []
unique_generators = []
last = requests.get(node + '/blocks/height').json()['height']
data = {}  
path_out=""
data['node'] = []  
def get_address(url):
    try:
        response = requests.get(url)

        # Consider any status other than 2xx an error
        if not response.status_code // 100 == 2:
            return "Error: Unexpected response {}".format(response)

        TXT_Data = response.text
        return TXT_Data
    except requests.exceptions.RequestException as e:
        # A serious problem happened, like an SSLError or InvalidURL
        return "Error: {}".format(e)

for n in range(0, int(math.ceil(nblocks / 100.0))):
    for block in requests.get('%s/blocks/seq/%d/%d' % (node, last - nblocks + n * 100, min(last, last - nblocks + (n + 1) * 100 - 1))).json():
        generators.append((str(block['generator']), float(block['fee']) / 100000000))
for generator in set([x[0] for x in generators]):
    fees = sum(g[1] for g in filter(lambda x: x[0] == generator, generators))
    count = sum(1 for g in filter(lambda x: x[0] == generator, generators))
    total_fees += fees
    generator_balance = float(requests.get(node + '/consensus/generatingbalance/' + generator).json()['balance']) / 100000000
    unique_generators.append((generator, generator_balance, count, fees))
    total_balance += generator_balance
for i, generator in enumerate(sorted(unique_generators, key=lambda x: -x[1])):
   char_list = ['\[', ',', '\]', '\"', "\'"]
   alias = json.dumps( requests.get (node + '/addresses/alias/by-address/' + generator[0]).json())
   limpo = re.sub("|".join(char_list), "", str(alias.split(':')) )
   if limpo.strip():
      domain = limpo.split()[2]
      URL =  'https://' + limpo.split()[2] + '/address.txt'
#      print "Fetching URL '{}'".format(URL), get_address(URL)
      node_address = get_address(URL)
      if node_address == str(generator[0]):
         data['node'].append({'domain': domain, 'address': str(generator[0]), 'balance': str(generator[1]), 'share': str(generator[1] / total_balance * 100), 'blocks': str(generator[2]), 'fees': str(generator[3])})

with open(path_out + '/trust.json', 'w') as outfile:  
    json.dump(data, outfile)
