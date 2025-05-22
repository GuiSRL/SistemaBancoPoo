class ContaBancaria:
    """
    Representa uma conta bancária com saldo e histórico de transações
    """
    # Método construtor que defini os atributos dos objetos a serem criados (instanciados)
    def __init__(self, numero_conta, saldo_inicial=0, extrato_inicial=None):
        self.saldo = saldo_inicial
        self.numero_conta = numero_conta
        self.extrato = extrato_inicial if extrato_inicial is not None else []
     
     # Exemplo de como você poderia usar a classe
     # Criando uma nova conta bancária
minha_conta = ContaBancaria(numero_conta="12345-X", saldo_inicial=1000.0)
print(f"Conta criada com sucesso! Número da conta: {minha_conta.numero_conta}, Saldo inicial: R$ {minha_conta.saldo:.2f}")

# Criando uma nova bancária para demonstrar a independência
conta_joao = ContaBancaria(numero_conta="98765-X")
print(f"Conta criada com sucesso! Número da conta: {conta_joao.numero_conta}, Saldo inicial: R$ {conta_joao:.2f}")
# O extrato é uma lista vazia no início
print(f"Extrato inicial da conta {minha_conta.numero_conta}: {minha_conta.extrato}")
