class ContaCorrente:
    def __init__(self,codigo):
        self.codigo = codigo
        self.saldo = 0
    def depositar(self,valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo,self.saldo)

