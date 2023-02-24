# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:57:33 2023

@author: Tim
"""

import time 
import requests
from rdkit import Chem
from rdkit.Chem.rdmolfiles import SDWriter

url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/'
url_input = 'compound/cid/'
cids = []

for i in range(1,101):
    cids.append(i)
    
mol_list = []
url_output = '/property/CanonicalSMILES/txt'
for cid in range(len(cids)):
    req_list = [url, url_input, str(cids[cid]), url_output]
    req = ''.join(req_list)
    res = requests.get(req)
    res = res.text
    mol = Chem.MolFromSmiles(res)
    mol_list.append(mol)
    time.sleep(0.2)
   
with SDWriter('trial_mols.sdf') as w:
    for mol in mol_list:
        w.write(mol)

        
