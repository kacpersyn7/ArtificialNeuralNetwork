#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os.path

sFile = "slownik.txt"
tablica = []
slownik = {}

class neuronkolumna:
	def __init__(self,wartosc,kolumna):
		self.wartosc=wartosc
		self.kolumna=kolumna
	def prin(self):
		print("[",self.wartosc, self.kolumna, "]")

def otworz(plik):
	if os.path.isfile(sFile):
		with open(sFile, "r") as sTxt:
			for i, line in enumerate(sTxt):
				line = line.replace("\n", "")
				t = line.split(" ")
				tablica.append(t)
		return len(tablica)

ileNeuronow = otworz(sFile)
print ("Wpisów w bazie:", ileNeuronow)

def segregowanie(tablica, i):
	return [row[i] for row in tablica]

def wypisywaniekolumn(tablica):
	for i in range(0, len(tablica[0])):
		print ("C",i, ":", segregowanie(tablica,i))
wypisywaniekolumn(tablica)

def szukanie(tablica):
	for i, row in enumerate(tablica):
		t = []
		for j, el in enumerate(row):
			pol = neuronkolumna(el,"C"+str(j));
			t.append(pol);
		slownik["N"+str(i)] = t

szukanie(tablica)

for klucz in slownik:
	print(klucz,":")
	for struktura in slownik[klucz]:
		struktura.prin()
