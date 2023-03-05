from collections import defaultdict
from collections import Counter
usuarios_data_science = [13,24,21,67,45]
usuarios_machine_learnigh = [15,23,45,13,38]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learnigh)
print(assistiram)
assistiram = set(assistiram)
print(assistiram)

for i in assistiram:
    print(i)

usuarios_data_science = {13,24,21,67,45}
usuarios_machine_learnigh = {15,23,45,13,38}

assistiram2 = usuarios_machine_learnigh | usuarios_data_science

print(assistiram2)

assistiram3 = usuarios_machine_learnigh & usuarios_data_science

print(assistiram3)

assistiram4 = usuarios_machine_learnigh - usuarios_data_science

print(assistiram4)

assistiram5 = usuarios_machine_learnigh ^ usuarios_data_science

print(assistiram5)

usuarios = {1,3,6,9,8,5}
print(len(usuarios))
usuarios.add(4)
print(len(usuarios))
usuarios.add(9)
print(len(usuarios))
print(usuarios)
usuarios = frozenset(usuarios)
#usuarios.add(7)
print(usuarios)

meu_texto = "Bem vindo meu nome e Renato adoro nomes e sou Renato e cientista da computacao e busco me aperfeicoar cada vez mais em computaçao e nomes e nomes"
meu_texto1 = meu_texto.split()
print(meu_texto1)
meu_texto1 = set(meu_texto1)
print(meu_texto1)

#Dicionario(Mapa etc)

aparicoes = {
    "Renato" : 2,
    "nome" : 1,
    "nomes" : 3,
    "e" : 6
}
print("Tem", aparicoes.get("Renato"), "Renato")

print(aparicoes)

aparicoes["Paulo"] = 3

print(aparicoes)

del aparicoes["nome"]

print(aparicoes)

print("Paulo" in aparicoes)

for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, "=",valor)

lista = ["palavra {}".format(chave) for chave in aparicoes.keys()]
print(lista)

meu_texto = meu_texto.lower()

print(meu_texto)

vezes_aparece = defaultdict(int)
for palavra in meu_texto.split():
    vezes_aparece[palavra] += 1

print(vezes_aparece)

class Conta:
    def __init__(self):
        print("Criando uma conta")

contas = defaultdict(Conta)
contas[15]
contas[17]

#Counter

aparicoes = Counter()

for palavra in meu_texto.split():
    aparicoes[palavra] +=1

print(aparicoes)

aparicoes = Counter(meu_texto.split())

print(aparicoes)

