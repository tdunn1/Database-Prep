# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 20:06:21 2023

@author: Tim
"""

from rdkit import Chem
import pandas as pd
from rdkit.Chem import DetectChemistryProblems, rdMolDescriptors

smis = []
info = open('trial_mols.sdf', 'rb')
with Chem.ForwardSDMolSupplier(info) as fsuppl:
    for mol in fsuppl:
        if mol is None or len(DetectChemistryProblems(mol)) != 0 :continue
        smis.append(Chem.MolToSmiles(mol))

df = pd.DataFrame(data = smis, columns = ['Smiles'])

for i in df.index:
    mol = Chem.MolFromSmiles(df.loc[i,'Smiles'])
    df.loc[i,'Rot Bonds'] = rdMolDescriptors.CalcNumRotatableBonds(mol)
    df.loc[i, 'TPSA'] = rdMolDescriptors.CalcTPSA(mol) 
    df.loc[i, 'Num AroHetCycles'] = rdMolDescriptors.CalcNumAromaticHeterocycles(mol)
    

        
