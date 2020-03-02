from sys import argv

script, conjunto1, conjunto2 = argv

from sys import argv

script, conjunto1, conjunto2 = argv



aux1 = "";
for caracter in conjunto1:
    if(caracter!="{" and caracter!="}" and caracter!="," and caracter!="#"):
        aux1 = aux1 + caracter
aux2 = "";
for caracter2 in conjunto2:
    if(caracter2!="{" and caracter2!="}" and caracter2!="," and caracter2!="#"):
        aux2 = aux2 + caracter2



Uni= aux1 | aux2

print("La union de los conjuntos es: ",Uni,"\n")

dif= aux1 - aux2

print("La diferencia de los conjuntos es: ",dif,"\n")
