
# coding: utf-8

# In[6]:

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
    for i in range(len(hashmap)):
        for key in hashmap[i]:
            #for j in range(len(data[i])):
                cos = neuronkolumna(key,i)
                cos.prin()
                for j in range(len(hashmap[i][key])):
                    hashmap[i][key][j].addConnect(cos)
                #neurons[i].addConnect(cos)
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
        neurons[j].prine()
        
def pobudzNeuron(hashmap,value,kolumna):
        for i in range(len((hashmap[kolumna])[value])):
                  ((hashmap[kolumna])[value])[i].change(1)
class neuronkolumna:
    def __init__(self,wartosc,kolumna):
        self.wartosc=wartosc
        self.kolumna=kolumna
    def prin(self):
        print("[",self.wartosc, self.kolumna, "]")
class Neuron:
    def __init__(self,neuron_id):
        self.neuron_id = neuron_id
        self.power = 0
        self.pointer = None
        self.wartosc = []
    def prin(self):
        print("\tN",self.neuron_id,"moc", self.power)
    def addConnect(self,kolumnaneurona):
        self.wartosc.append(kolumnaneurona)
    def change(self,power):
        self.power = self.power + power
    def connect(self,otherneuron):
        self.pointer = otherneuron
    def prine(self):
        print("N" + str(self.neuron_id) + " moc " + str(self.power))
        for i in range(len(self.wartosc)):
            self.wartosc[i].prin()
krok = 0
listalist = [[1,3,9,7,5],[1,4,6,8,1]]
danewej = [[1,3],[1,6]]
listaslownikow = []
listaneuronow = []

createNetwork(listalist,listaslownikow,listaneuronow)                
wypisz(listaslownikow)
pobudzNeuron(listaslownikow,1,1)
<<<<<<< Updated upstream
pobudzNeuron(listaslownikow,1,0)
=======
>>>>>>> Stashed changes
wypisz(listaslownikow)
print("\tNeurony")
wypiszneurony(listaneuronow)


# In[ ]:



