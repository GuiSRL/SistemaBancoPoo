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