from igualdade import ContaSalario
from heranca_polimorfismo import ContaCorrente

conta1 = ContaSalario(37)
conta2 = ContaSalario(37)

print(conta1 == conta2)

print(conta1 in [conta2])

print(conta2 in [conta1])

conta1.deposita(100)

print(conta1 == conta2)

print(conta1 in [conta2])

print(conta2 in [conta1])

conta3 = ContaCorrente(37)

print(conta2==conta3)