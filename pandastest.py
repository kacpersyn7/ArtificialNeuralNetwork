# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
df = pd.DataFrame({'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]}); df
print (df)
dictionary = {'pierwsza': df.AAA,'druga': df.BBB, 'trzecia': df.CCC}
print (dictionary['druga'])
table = [df.AAA, df.BBB, df.CCC]
print("przechodzenie po zwyklej tablicy")
for i in table:
    print(i)
print("przechodzenie po slowniku - tablicy asocjacyjnej")
for i, j in dictionary.items():
    print(i,j)
    
    