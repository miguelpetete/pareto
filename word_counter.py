from operator import itemgetter
import sys
import re

file = open("sherlock.txt", "r")

text = file.read()

list = re.split(r'\W+',text)

list.remove('')

#inicializacion diccionario
def dicc(lista):
    diccionario = {}
    for word in lista: 
        word = word.lower()
        diccionario[word] = 0
    return diccionario

dic_ejemplo = dicc(list)

#print(dic_ejemplo)

#contador ocurrencias palabras
def cont(lista, diccionario):
    for word in lista: 
        diccionario[word] = diccionario[word] + 1
    return diccionario

dic_ejemplo = cont(list,dic_ejemplo)

#print(dic_ejemplo)

#aparicion de una palabra
def apar(palabra):
    return dic_ejemplo[palabra]
    
#print(apar("aaa"))

def contador(dicc):
    cont = 0
    for word in dicc:
        cont+=1
    return cont

def total(dicc):
    cont=0
    for word in dicc:
        cont+=dicc[word]
    return cont

c = contador(dic_ejemplo)
print("Number of diferent words:")
print(c)

c2 = total(dic_ejemplo)
print("Number of words in total:")
print(c2) 

#Diccionario ordenado por ocurrencias:
def sorter(dicc):
    sort = sorted(dicc.items(), key=lambda x: x[1], reverse=True)
    return sort


ordenado = sorter(dic_ejemplo)

def num_palabras():
    cont = 0
    aux = 0
    ochenta = c2*0.8
    for word in ordenado:
        cont+=1
        aux += word[1]
        if aux > ochenta:
            break
    return cont


print("Num palabras necesarias: ")
print(num_palabras())