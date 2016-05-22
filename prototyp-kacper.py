
# coding: utf-8

# In[63]:

def createNetwork(data,hashmap,neurons):
    for i in range(len(data)):
        hashmap.append({})
    for i in range(len(data)):
        for j in range(len(data[i])):
            (hashmap[i])[data[i][j]] = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if(i == 0):
                neurons.append(Neuron(j))
            (hashmap[i])[data[i][j]].append(neurons[j])
def wypisz(slowniki):
    for j in range(len(slowniki)):
        print("Kolumna nr -",j,"-")
        for klucz in slowniki[j]:
            print(klucz, end="")
            print(":", end="")
            for i in range(len((slowniki[j])[klucz])):
                  ((slowniki[j])[klucz])[i].prin()
def wypiszneurony(neurony):
    for j in range(len(neurony)):
        neurony[j].prin()
def pobudzNeuron(slowniki,wartosc,kolumna):
        for i in range(len((slowniki[kolumna])[wartosc])):
                  ((slowniki[kolumna])[wartosc])[i].change(1)
class Neuron:
    def __init__(self,neuron_id):
        self.neuron_id = neuron_id
        self.power = 0
        self.pointer = None
    def prin(self):
        print("\tN",self.neuron_id,"moc", self.power)
    def change(self,power):
        self.power = power
    def connect(self,otherneuron):
        self.pointer = otherneuron
listalist = [[1,3,9,7,5],[1,4,6,8,1]]
danewej = [[1,3],[1,6]]
listaslownikow = []
listaneuronow = []

createNetwork(listalist,listaslownikow,listaneuronow)                
wypisz(listaslownikow)
pobudzneuron(listaslownikow,1,1)
wypisz(listaslownikow)
wypiszneurony(listaneuronow)

