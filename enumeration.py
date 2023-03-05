idades = [24,56,33,23,24,19,20,30]

idades = list(enumerate(idades))

print(idades)

for indice,idade in idades:
    print(indice,"=>",idade)

usuarios = [
    ("Renato",24,1998),
    ("Paulo",23,1999),
    ("Aline",25,1996)
]

for nome,idade,nascimento in usuarios:
    print(nome)

numeros = [34,55,2,12,76,33,9,23,5,23,88,98,56,44,33,9,3,48,8]

n1 = sorted(numeros)
#n2 = list(reversed(numeros))
n3 = sorted(numeros,reverse=True)

print(n1)
#print(n2)
print(n3)

numeros.sort()

print(numeros)

animais = ["Girafa","Jacare","Cachorro","Galinha","Abelha","Gato"]

print(animais)

animais = sorted(animais)

print(animais)