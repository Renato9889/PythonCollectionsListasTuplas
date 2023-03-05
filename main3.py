from igualdade import ContaSalario
from heranca_polimorfismo import ContaCorrente
from operator import attrgetter

conta1 = ContaSalario(37)
conta2 = ContaSalario(37)

#print(conta1 == conta2)

#print(conta1 in [conta2])

#print(conta2 in [conta1])

conta1.deposita(100)

#print(conta1 == conta2)

#print(conta1 in [conta2])

#print(conta2 in [conta1])

conta3 = ContaCorrente(37)

#print(conta2==conta3)

#Ordenação Customizada

conta_wanda = ContaSalario(13)
conta_wanda.deposita(6000)

conta_visao = ContaSalario(9)
conta_visao.deposita(6000)

conta_tommy = ContaSalario(24)
conta_tommy.deposita(6000)

contas = [conta_wanda,conta_visao,conta_tommy]

#def extrai_saldo(conta):
 #   return conta._saldo

#for conta in sorted(contas,key=extrai_saldo):
#   print(conta)

#outra forma de ordenação

#for conta in sorted(contas,key=attrgetter("_saldo")):
#    print(conta)

print(conta_wanda>conta_visao)

for conta in sorted(contas,reverse=True):
    print(conta)

print(conta_wanda>=conta_visao)