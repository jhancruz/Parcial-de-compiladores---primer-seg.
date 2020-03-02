from sys import argv

script, conjunto1, conjunto2 = argv

from sys import argv

script, conjunto1, conjunto2 = argv


con1 = set()
con2 = set()

for caracter in conjunto1:
    if(caracter!="{" and caracter!="}" and caracter!="#"):
        con1.add(caracter)
aux2 = "";
for caracter2 in conjunto2:
    if(caracter2!="{" and caracter2!="}"and caracter2!="#"):
        con2.add(caracter2)



Uni= con1 | con2

print("La union de los conjuntos es: ",Uni,"\n")

dif= con1 - con2

print("La diferencia de los conjuntos es: ",dif,"\n")
