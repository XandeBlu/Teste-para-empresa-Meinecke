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
    def __init__(self):
        self.nomelojas = []
        self.cnpjlojas = []

    def cadastrar_loja(self):
        self.nomeloja = input('Digite o nome da loja: ')
        self.cnpjloja = input('Digite o cnpj da loja: ')
        self.nomelojas.append(self.nomeloja)
        self.cnpjlojas.append(self.cnpjloja)

    def ver_lojas(self):
        print('-----------------------------------------')
        print('Lojas')
        print(self.nomelojas)
        print('-----------------------------------------')
        print('Respectivos cnpjs')
        print(self.cnpjlojas)
        print('-----------------------------------------')


#------------------------------------------------------------------
class Cliente:
    def __init__(self):
        self.nomeclientes = []
        self.cnpjclientes = []

    def cadastrar_cliente(self):
        self.nomecliente = input('Digite o nome do cliente: ')
        self.cnpjcliente = input('Digite qual o cnpj do cliente: ')
        self.nomeclientes.append(self.nomecliente)
        self.cnpjclientes.append(self.cnpjcliente)

    def ver_clientes(self):
        print('-----------------------------------------')
        print('Nome dos Clientes')
        print(self.nomeclientes)
        print('-----------------------------------------')
        print('Respectivos Cnpjs')
        print(self.cnpjclientes)
        print('-----------------------------------------')
#-------------------------------------------------------------------
class Fornecedor:
    def __init__(self):
        self.nomefornecedores = []
        self.cnpjfornecedores = []

    def cadastrar_fornecedor(self):
        self.nomefornecedor = input('Digite o nome do fornecedor: ')
        self.cnpjfornecedor = input('Digite o cnpj do fornecedor: ')
        self.nomefornecedores.append(self.nomefornecedor)
        self.cnpjfornecedores.append(self.cnpjfornecedor)

    def ver_fornecedores(self):
        print('-----------------------------------------')
        print('Nome')
        print(self.nomefornecedores)
        print('-----------------------------------------')
        print('Respectivos Cnpj')
        print(self.cnpjfornecedores)
        print('-----------------------------------------')
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
            del self.quantidade[indice_item]
            print(item_remover, ' removido do estoque')
        else:
            print(item_remover, 'não encontrado no estoque')
            print('Certifique-se de ter escrito corretamente o nome do item')

    def ver_estoque(self):
        print('-----------------------------------------')
        print('Item')
        print(self.itens)
        print('-----------------------------------------')
        print('Preço')
        print(self.precos)
        print('-----------------------------------------')
        print('Quantidade')
        print(self.quantidade)
        print('-----------------------------------------')

    def alterar_quantidade(self):
        item_alterar = input('Digite o nome do item que você deseja alterar a quantidade')
        if item_alterar in self.itens:
            indice_item = self.itens.index(item_alterar)
            nova_quantidade = int(input('Digite a nova quantidade do produto'))
            self.quantidade[indice_item] = nova_quantidade


#--------------------------------------------------------------------
#Menu Principal
estoque = Estoque()
loja = Loja()
cliente = Cliente()
fornecedor = Fornecedor()
while True:

    print('Bem-Vindo ao Sistema!')
    print('')
    print('1 - Acessar área das loja')
    print('2 - Acessar área dos clientes')
    print('3 - Acessar área dos fornecedores')
    print('4 - Acessar o estoque')
    print('0 - Encerrar o programa')
    print('-----------------------------------------')
    resposta = int(input())

    if resposta == 0:
        print('Encerrando o programa!')
        break
#--------------------------------------------------------
# Área da loja

    elif resposta == 1:
        while True:
            print('-----------------------------------------')
            print('1 - Para cadastrar nova loja')
            print('2 - Para ver as lojas cadastradas')
            print('3 - Para voltar ao menu')
            print('-----------------------------------------')
            respostaloja = int(input())

            if respostaloja == 1:
                loja.cadastrar_loja()
                print('-----------------------------------------')
                print('Loja cadastrada com sucesso!')
                print('-----------------------------------------')

            elif respostaloja == 2:
                loja.ver_lojas()

            elif respostaloja == 3:
                break

            else:
                print('Resposta inválida')
#------------------------------------------------------------
#Área do Cliente
    elif resposta == 2 :

        while True:
            print('-----------------------------------------')
            print('1 - Para cadastrar novo Cliente')
            print('2 - Para ver os clientes cadastrados')
            print('3 - Para voltar ao menu')
            print('-----------------------------------------')
            respostacliente = int(input())

            if respostacliente == 1 :
                cliente.cadastrar_cliente()
                print('Cliente cadastrado com sucesso!')

            elif respostacliente == 2:
                cliente.ver_clientes()

            elif respostacliente == 3:
                break

            else:
                print('Resposta Inválida')


#--------------------------------------------------------------
#Área dos Fornecedores

    elif resposta == 3:
        while True:
            print('-----------------------------------------')
            print('1 - Para cadastrar novo fornecedor')
            print('2 - Para ver os fornecedores cadastrados')
            print('3 - Para voltar ao menu')
            print('-----------------------------------------')
            respostafornecedor = int(input())

            if respostafornecedor == 1:
                fornecedor.cadastrar_fornecedor()
                print('Fornecedor cadastrado com sucesso!')

            elif respostafornecedor == 2:
                fornecedor.ver_fornecedores()

            elif respostafornecedor == 3:
                break

            else:
                print('Resposta Inválida')

#------------------------------------------------------------------------
#Área do Estoque
    elif resposta == 4:
        while True:
        print('Bem vindo ao estoque!')
        print('-----------------------------------------')
        print('1-Adicionar itens ao estoque')
        print('2-Remover itens do estoque')
        print('3-Alterar quantidade de itens no estoque ')
        print('4 - ver estoque')
        print('0 - Voltar ao menu')
        print('-----------------------------------------')
        respostaestoque = int(input())

        if respostaestoque == 1:
            estoque.adicionar_ao_estoque()
            print('Produto adicionado com sucesso!')
            print('-----------------------------------------')

        elif respostaestoque == 2:
            estoque.remover_do_estoque()
            print('Produto removido com sucesso!')
            print('-----------------------------------------')

        elif respostaestoque==3:
            estoque.alterar_quantidade()
            print('Produto alterado com sucesso!')
            print('-----------------------------------------')

        elif respostaestoque == 4:
            estoque.ver_estoque()

        elif respostaestoque == 0:
            print('De volta ao menu!')
            break
        else:
            print('Resposta inválida!')
    else:
        print('Resposta inválida')
