'''''
#“Criar um projeto de movimentação de estoque de produtos de limpeza de uma loja, para isso,
# será necessário cadastrar a loja, os clientes, os fornecedores e o controle de estoque
# (entrada e saída de produtos)”

Regras:
•	Linguagem de programação: A que tiver mais afinidade, desde que seja Orientada a objeto (POO)
•	Não é necessário utilizar banco de dados
•	Criar classes com setters e getters
'''
#----------------------------------------------------------------
class Loja:
    def __init__(self, nomeloja,cnpjloja):
        self.nomeloja = nomeloja
        self.cnpj = cnpjloja

    def cadastrar_loja(self):
        self.nomeloja = input('Digite o nome da loja: ')
        self.cnpjloja = input('Digite o cnpj da loja: ')

#------------------------------------------------------------------
class Cliente:
    def __init__(self, nomecliente,cnpjcliente):
        self.nomecliente = nomecliente
        self.cnpjcliente = cnpjcliente

    def cadastrarcliente(self):
        self.nomecliente = input('Digite o nome do cliente: ')
        self.cnpjcliente = input('Digite qual o cnpj do cliente: ')
#-------------------------------------------------------------------
class Fornecedor:
    def __init__(self, nomefornecedor, cnpjfornecedor):
        self.nomefornecedor = nomefornecedor
        self.cnpjfornecedor = cnpjfornecedor

    def cadastrarfornecedor(self):
        self.nomefornecedor = input('Digite o nome do fornecedor: ')
        self.cnpjfornecedor = input('Digite o cnpj do fornecedor: ')
#--------------------------------------------------------------------
class Estoque:
    def __init__(self):
        self.itens = []
        self.precos = []
        self.quantidade = []

    def adicionar_ao_estoque(self):
        item = input('Digite qual produto deseja adicionar: ')
        preco = float(input('Digite o preço do produto: '))
        quantidade = int(input('Quantidade do produto: '))
        self.itens.append(item)
        self.precos.append(preco)
        self.quantidade.append(quantidade)

    def remover_do_estoque(self):
        item_remover = input('Digite o nome do item que deseja remover: ')
        if item_remover in self.itens:
            indice_item = self.itens.index(item_remover)
            del self.itens[indice_item]
            del self.precos[indice_item]
            print(f"{item_remover} removido do estoque.")
        else:
            print(f"{item_remover} não encontrado no estoque. ")
            print('Certifique-se de ter escrito corretamente o nome do item')

    def ver_estoque(self):
        print('Item')
        print(self.itens)
        print('Preço')
        print(self.precos)
        print('Quantidade')
        print(self.quantidade)

#--------------------------------------------------------------------
estoque = Estoque()
while True:

    print('Bem-Vindo ao Sistema!')
    print('')
    print('Digite 1 para cadastrar loja')
    print('Digite 2 para cadastrar clientes')
    print('Digite 3 para cadastrar fornecedores')
    print('Digite 4 para acessar o estoque')
    print('Digite 0 para encerrar o programa')
    resposta = int(input())

    if resposta == 0:
        print('Encerrando o programa!')
        break

    elif resposta == 1:
        nova_loja = Loja(nomeloja="", cnpjloja="")
        nova_loja.cadastrar_loja()
        print('Loja cadastrada com sucesso!')

    elif resposta == 2 :
        novo_cliente = Cliente(nomecliente="", cnpjcliente="")
        novo_cliente.cadastrarcliente()
        print('Cliente cadastrado com sucesso!')

    elif resposta == 3:
        novo_fornecedor = Fornecedor(nomefornecedor="", cnpjfornecedor="")
        novo_fornecedor.cadastrarfornecedor()
        print('Fornedor cadastrado com sucesso!')

    elif resposta == 4:
        print('Bem vindo ao estoque!')
        print('1-Adicionar itens ao estoque')
        print('2-Remover itens do estoque')
        print('3-Ver estoque ')
        print('0 - Voltar ao menu')
        respostaestoque = int(input())


        if respostaestoque == 1:
            estoque.adicionar_ao_estoque()

        elif respostaestoque == 2:
            estoque.remover_do_estoque()

        elif  respostaestoque == 3:
            estoque.ver_estoque()

        elif respostaestoque == 0:
            print('De volta ao menu!')
            break
        else:
            print('Resposta inválida!')
