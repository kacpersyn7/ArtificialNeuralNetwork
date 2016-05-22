ileNeuronow = otworz(sFile)
 print ("Wpisów w bazie:", ileNeuronow)
+print(tablica)
 
 def segregowanie(tablica, i):
 	return [row[i] for row in tablica]
 
 def wypisywaniekolumn(tablica):
-	for i in range(0, len(tablica[0])):
-		print ("C",i, ":", segregowanie(tablica,i))
+	for i in range(0, len(tablica[0])): #Dla każdej kolumny
+		neurWkol = {} #Słownik wartość -> połączenie
+		wartosci = segregowanie(tablica,i)
+		for wartosc in wartosci: #Dla każdej wartości
+			neurWkol[wartosc] = [] #Dodaj pustą tablicę połączeń
+		slownik["C"+str(i)] = neurWkol #Dodaj do słownika
 wypisywaniekolumn(tablica)
 
 def szukanie(tablica):
-	for i, row in enumerate(tablica):
-		t = []
-		for j, el in enumerate(row):
-			pol = neuronkolumna(el,"C"+str(j));
+	for i, row in enumerate(tablica): #Dla każdego rzędu
+		t = [] #Stwórz tablicę połączeń
+		for j, el in enumerate(row): #Dla każdego elementu
+			pol = neuronkolumna(el,"C"+str(j)); #Dodaj połączenie z wartością
 			t.append(pol);
+			slownik["C"+str(j)][el].append("N"+str(i)) #Tej wartości dodaj połączenie z tym neuronem
+		if i<len(tablica)-1:
+			t.append(neuronkolumna("N"+str(i+1),"N"))
 		slownik["N"+str(i)] = t
 
 szukanie(tablica)
 
-for klucz in slownik:
-	print(klucz,":")
-	for struktura in slownik[klucz]:
-		struktura.prin()
+#for klucz in slownik:
+#	print(klucz,":")
+#	for struktura in slownik[klucz]:
+#		if(type(struktura) == neuronkolumna):
+#			struktura.prin()
+
+for i in range(0, len(tablica[0])):
+	print("C"+str(i)+":")
+	for key in sorted(slownik["C"+str(i)]):
+		print(key+" :", slownik["C"+str(i)][key])
+for i in range(0, len(tablica)):
+	print("N"+str(i)+":")
+	for el in slownik["N"+str(i)]:
+		el.prin()
+
