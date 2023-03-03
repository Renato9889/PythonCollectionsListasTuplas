from heranca_polimorfismo import ContaCorrente
from heranca_polimorfismo import ContaPoupanca
import numpy as np

conta_paulo = ContaCorrente(24)
conta_paulo.depositar(1200)
conta_paulo.passa_o_mes()
print(conta_paulo)

conta_renato = ContaPoupanca(22)
conta_renato.depositar(1200)
conta_renato.passa_o_mes()
print(conta_renato)

contas = [conta_paulo,conta_renato]

for conta in contas:
    conta.passa_o_mes()
    print(conta)

numeros = np.array([1,3,2,4,5])

numeros = numeros*3

print(numeros)