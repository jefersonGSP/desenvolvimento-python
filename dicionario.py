dicionario={}
dicionario=dict()

dicionario={'nome':'Walisson','idade':26,'altura':1.77}

print(dicionario)
print(dicionario['idade'])


dicionario['programador']=True

print(dicionario)

dicionario['altura']=2

print(dicionario)
#
for chave in dicionario:
    print(chave,dicionario[chave])
    

#
print('peso' in  dicionario)
print('altura' in  dicionario)
