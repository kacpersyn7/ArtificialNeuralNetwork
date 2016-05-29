
# coding: utf-8

# In[73]:

#! /usr/bin/env python

import os.path

sFile = "slownik.txt"
tablica = []
slownik = {}
neurons = []
class neuronkolumna:
    def __init__(self,wartosc,kolumna):
        self.wartosc=wartosc
        self.kolumna=kolumna
    def prin(self):
        print("[",self.wartosc, self.kolumna, "]")
class Neuron:
    def __init__(self,id):
        self.wartosc = []
        self.id = id
    def addConnect(self,kolumnaneurona):
        self.wartosc.append(kolumnaneurona)
    def prine(self):
        print(self.id)
        for i in range(len(self.wartosc)):
            self.wartosc[i].prin()
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
print(tablica)

def segregowanie(tablica, i):
	return [row[i] for row in tablica]

def wypisywaniekolumn(tablica):
	for i in range(0, len(tablica[0])): #Dla każdej kolumny
		neurWkol = {} #Słownik wartość -> połączenie
		wartosci = segregowanie(tablica,i)
		for wartosc in wartosci: #Dla każdej wartości
			neurWkol[wartosc] = [] #Dodaj pustą tablicę połączeń
		slownik["C"+str(i)] = neurWkol #Dodaj do słownika
wypisywaniekolumn(tablica)

def szukanie(tablica):
	for i, row in enumerate(tablica): #Dla każdego rzędu
		t = [] #Stwórz tablicę połączeń
		for j, el in enumerate(row): #Dla każdego elementu
			pol = neuronkolumna(el,"C"+str(j)); #Dodaj połączenie z wartością
			t.append(pol);
			slownik["C"+str(j)][el].append("N"+str(i)) #Tej wartości dodaj połączenie z tym neuronem
#		if i<len(tablica)-1:
#			t.append(neuronkolumna("N"+str(i+1),"N"))
		slownik["N"+str(i)] = t

szukanie(tablica)


wypisane = [];
def wypsygnalu(typ, neuron):
	wypisane.append(neuron)
	if(typ is "n"):
		print(neuron)
		for pol in slownik[neuron]:
			if(pol not in wypisane):
				wypsygnalu("k", pol)
	elif(typ is "k"):
		neuron.prin()
		for pol in slownik[neuron.kolumna][neuron.wartosc]:
			if(pol not in wypisane):
				wypsygnalu("n", pol)

def wyppolaczen():
	x=input("wpisz wartość z kolumny c0 ")
	y=input("wpisz warość z kolumny c1 ")
	odl={}
	odl_y={}
	for el in slownik["C0"]:
		if(abs(int(el)-int(x)) not in odl):
			odl[abs(int(el)-int(x))] = []
		odl[abs(int(el)-int(x))].append(neuronkolumna(el,"C0"))
	for el in slownik["C1"]:
		if(abs(int(el)-int(x)) not in odl):
			odl[abs(int(el)-int(x))] = []
		odl[abs(int(el)-int(y))].append(neuronkolumna(el,"C1"))

	for o in odl:
		print(o,":")
		for el in odl[o]:
			el.prin()
			print("  ->", slownik[el.kolumna][el.wartosc])

#	print(odl_y)

#	for el in odl_x:
#		for pol in odl_x[el]:
#			print(pol)
#			for a in slownik[pol]:
#				a.prin()

wyppolaczen()



for i in range(0, len(tablica[0])):
	print("C"+str(i)+":")
	for key in sorted(slownik["C"+str(i)]):
		print(key+" :", slownik["C"+str(i)][key])
for i in range(0, len(tablica)):
    print("N"+str(i)+":")
    neurons.append(Neuron("N"+str(i)))
    for el in slownik["N"+str(i)]:
        neurons[i].addConnect(el)
        el.prin()
        
#x=1
#y=2
#i=0
#n1 = Neuron(1)
#for el in (slownik["N"+str(1)]):
#        n1.addConnect(el)
#print("")
#for i in range(len(neurons)):
#    neurons[i].prine()
#

#slownik["N1"][0].prin()


# In[ ]:



