# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:57:33 2023

@author: Tim
"""

import time 
import requests

#Retrieve first 100 compounds from pubchem
url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/'
url_input = 'compound/cid/'
cids = []

for i in range(1,101):
    cids.append(i)
    
url_output = '/property/CanonicalSMILES/txt'
f = open('trial_mols.sdf', 'w')
for cid in range(len(cids)):
    req_list = [url, url_input, str(cids[cid]), url_output]
    req = ''.join(req_list)
    res = requests.get(req)
    f.write(res.text)
    time.sleep(0.2)
   
f.close()
