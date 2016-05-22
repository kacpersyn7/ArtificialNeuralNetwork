
# coding: utf-8

# In[68]:

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
def wypisz(hashmap):
    for j in range(len(hashmap)):
        print("Kolumna nr -",j,"-")
        for key in hashmap[j]:
            print(key, end="")
            print(":", end="")
            for i in range(len((hashmap[j])[key])):
                  ((hashmap[j])[key])[i].prin()
def wypiszneurony(neurons):
    for j in range(len(neurons)):
        neurons[j].prin()
def pobudzNeuron(hashmap,value,kolumna):
        for i in range(len((hashmap[kolumna])[value])):
                  ((hashmap[kolumna])[value])[i].change(1)
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
print("\tNeurony")
wypiszneurony(listaneuronow)

