import datetime

class ContaBancaria:
    """
    Representa uma conta bancária com saldo e histórico de transações
    """
    # Método construtor que defini os atributos dos objetos a serem criados (instanciados)
    def __init__(self, numero_conta, saldo_inicial=0, extrato_inicial=None):
        self.saldo = saldo_inicial
        self.numero_conta = numero_conta
        self.extrato = extrato_inicial if extrato_inicial is not None else []

    def consultar_saldo(self):
        """Exibir o saldo atual da conta"""
        print(f"Saldo atual da conta: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        """Realiza um depósito na conta"""
        try:
            valor_deposito = float(valor)
            if (valor_deposito <= 0):
                print("Valor de depósito inválido. Digite um número positivo.")
                return
            self.saldo += valor_deposito # Atualiza o saldo (somando o valor do depósito)
            # Registra a transação no extrato
            agora = datetime.datetime.now()
            self.extrato.append({
                "data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"),
                "tipo": "Depósito",
                "valor": valor_deposito
            })
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
            print(f"Seu novo saldo é: R$ {self.saldo:.2f}")
        except ValueError:
            print("Valor de depósito inválido. Por favor, digite um número.")

    def sacar(self, valor):
        """ Realiza uma operação de saque na conta, verificando o saldo."""
        try:
            valor_saque = float(valor)
            if (valor_saque <= 0):
                print("Valor de depósito inválido. Digite um número positivo.")
                return
            if (valor_saque <= self.saldo): # Verifica se o saldo é suficiente
                self.saldo -= valor_saque # Atualiza o saldo
                # Registra a transação no extrato
                agora = datetime.datetime.now()
                self.extrato.append({
                 "data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"),
                "tipo": "Saque",
                "valor": valor_saque   
                })
                print(f"Saque de: R$ {valor_saque:.2f} realizado com sucesso!")
                print(f"Seu saldo atual é: R$ {self.saldo:.2f}")
            else:
                print("Saldo insuficiente para realizar o saque.")

        except ValueError:
            print("Valor de depósito inválido. Por favor, digite um número.")

# Exemplo de uso da classe (para testar os métodos)
if __name__ == "__main__":
    # Criando uma conta bancária de exemplo
    minha_conta = ContaBancaria(numero_conta="98765-4", saldo_inicial=500.0)
    print(f"Conta {minha_conta.numero_conta} criada com saldo: R$ {minha_conta.saldo:.2f}")

    print("\n--- Testando operações ---")
    minha_conta.consultar_saldo()
    minha_conta.depositar(200)
    minha_conta.consultar_saldo()
    minha_conta.sacar(150)
    minha_conta.consultar_saldo()
    minha_conta.sacar(700)
    minha_conta.consultar_saldo()
    minha_conta.depositar("abc")
    minha_conta.sacar("xyz")