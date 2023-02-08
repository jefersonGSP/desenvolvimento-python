'''lista=[]
lista=list()
lista=[26,'abacate',3.142,False]
lista_de_listas=[10,[1,2,3,]]'''

lista=[26,'abacate',3.142,False]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-1])#ultimo da lista

lista=[10,50,30,45,35,60,6]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])

for elemento in lista:
    print(lista)

print('Comprimento da lista: ',len(lista))

for i in range(len(lista)):
    print(i)

#METODOS DE LISTAS 

lista=[1,3,12,8,2]

#append

print('antes do append: ',lista)

lista.append(3)

print('depois do append: ',lista)

#insert

lista.insert(2,10)

print('depois do insert: ',lista)

#EXTEND

lista2=[1,2,3]

lista.extend(lista2)

print('depois do extend: ',lista)

#pop

lista.pop()

print('lista após o pop: ',lista)

lista.pop(0)

print('lista após o pop: ',lista)

#remove

lista.remove(3)

print('depois do remove',lista)

#count

print('quantidade de 2 na lista: ',lista.count(2))

#index 

print('indice do elemento 12 na lista: ',lista.index(12))

#sort
 
lista.sort()#reverse=True       reverte
 
print(lista)

#FUNÇÕES PARA LISTA

#LEN

print(len(lista))

#SUM

print(sum(lista))

#MAX

print('maior elemento da lista: ',max(lista))

#MIN

print('menor elemento da lista: ',min(lista))
