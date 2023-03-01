from objetos_proprios import ContaCorrente

conta_renato = ContaCorrente(15)
conta_renato.depositar(400)

conta_paulo = ContaCorrente(19)
conta_paulo.depositar(2000)

contas = [conta_renato,conta_paulo]

for conta in contas:
    print(conta)


