idades = [39,30,20,40]

idades.append(57)

print(idades)

idades.remove(39)

print(idades)

idades.insert(1,99)

print(idades)

idades.extend([19,33])

print(idades)

for elemento in idades:
    print("Idades são: ",elemento)

idades_ano_que_vem = [(idade+1) for idade in idades]

print(idades_ano_que_vem)

lista_de_numeros = [3,4,8,6,2,8,66,3,22,98,100,33]
print(lista_de_numeros)

lista_dobro = [(elemento*2) for elemento in lista_de_numeros]

print(lista_dobro)

def faz_processamento(lista,n):
    print(len(lista))
    lista.append(n)

numeros = [1,2,3,4,5]
faz_processamento(numeros,6)
