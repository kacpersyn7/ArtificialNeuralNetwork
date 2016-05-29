
# coding: utf-8

# In[7]:

import matplotlib.pyplot as plt
import pandas as pd
import os 
tablica = []
slownik = {}
name = input("Podaj nazwe pliku ")
while (error != 0) and (name != 'q')
def open(name):
    length = 0
    if os.path.exists(name) and name[-4:] == ".csv" :
        data = pd.read_csv(name)
        print("wczytano")
        print (data)
        length = len(tablica)
    else:
        print("Blad wczytywania")
    return length
        #name = input("Podaj nazwe pliku ")
#data = pd.read_csv(name)
#print (data)

