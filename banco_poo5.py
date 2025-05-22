import json

class ContaBancaria:
    """
    Representa uma conta bancária com saldo e histórico de transações
    """
    # Método construtor que defini os atributos dos objetos a serem criados (instanciados)
    def __init__(self, numero_conta, saldo_inicial=0, extrato_inicial=None):
        self.saldo = saldo_inicial
        self.numero_conta = numero_conta
        self.extrato = extrato_inicial if extrato_inicial is not None else []

def salvar_dados(conta, filename="banco_dados.json"):
   """ Salva o saldo e o extrato de uma conta em um arquivo JSON. """
   dados = {
       "numero_conta": conta.numero_conta,  # Incluir o número da conta para recriar o objeto
       "saldo": conta.saldo,
       "extrato": conta.extrato
   }
   with open(filename, "w") as f:  # Abre o arquivo "banco_dados.json" em modo de escrita ("w")
       json.dump(dados, f, indent=4)  # Salva o saldo e o extrato no arquivo usando json.dump()
       print(f"Dados da conta '{conta.numero_conta}' salvos com sucesso!")
def carregar_dados(filename="banco_dados.json"):
   """ Carrega o saldo e o extrato de uma conta a partir de um arquivo JSON. """
   try:
       # Tentar abrir um arquivo chamado "banco_dados.json" em modo de leitura ("r").
       with open(filename, "r") as f:
           dados = json.load(f)  # Se o arquivo existir, carregar o saldo e o extrato de lá.
           # Retorna uma instância de ContaBancaria com os dados carregados
           return ContaBancaria(dados["numero_conta"], dados["saldo"], dados["extrato"])
   except FileNotFoundError:
       # Se o arquivo não existir (FileNotFoundError), definir o saldo inicial e o extrato como uma lista vazia.
       print("Arquivo de dados não encontrado. Criando nova conta com número padrão '00000-0'.")
       return ContaBancaria("00000-0")

if __name__ == "__main__":
    minha_conta = carregar_dados()  # Chamar carregar_dados() para obter uma instância de ContaBancaria.
 
    # Exemplo de como você poderia ter uma segunda conta (para transferência)
    outra_conta = carregar_dados(filename="banco_secundario.json")
    if outra_conta.numero_conta == "0000-0":  # Se for uma conta recém-criada (não carregada de arquivo)
        outra_conta.numero_conta = "3212-9"  # Atribui um número real para demonstração
 
    while True:  # Manter o loop while True que exibe o menu de opções.
        print("\nOlá! Bem-vindo ao seu banco virtual.")
        print("1 - Consultar Saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Exibir Extrato")
        print("5 - Transferir")
        print("6 - Sair")
 
        opcao_str = input("Digite a opção desejada: ")
        try:
            opcao = int(opcao_str)
            if not (1 <= opcao <= 6):  # Validar a opção escolhida
                print("Opção inválida. Por favor, digite um número entre 1 e 6.")
                continue  # Continua o loop para pedir a opção novamente
        except ValueError:
            print("Opção inválida. Por favor, digite um número inteiro.")
            continue
 
        if opcao == 1:
            minha_conta.consultar_saldo()
        elif opcao == 2:
            valor = input("Digite o valor a depositar: R$ ")
            minha_conta.depositar(valor)
        elif opcao == 3:
            valor = input("Digite o valor a sacar: R$ ")
            minha_conta.sacar(valor)
        elif opcao == 4:
            minha_conta.exibir_extrato()
        elif opcao == 5:
            print(f"Realizando transferência da conta {minha_conta.numero_conta} para {outra_conta.numero_conta}")
            valor_transferencia = input("Digite o valor a ser transferido: R$ ")
            minha_conta.transferir(outra_conta, valor_transferencia)
        elif opcao == 6:
            salvar_dados(minha_conta)  # Salvar os dados da conta principal antes de sair.
            salvar_dados(outra_conta, filename="banco_secundario.json")  # Salvar a segunda conta também
            print("Obrigado por utilizar nosso banco virtual!")
            break