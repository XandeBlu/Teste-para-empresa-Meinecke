class Loja:
    def __init__(self):
        self._nomelojas = []
        self._cnpjlojas = []

    def get_nomelojas(self):
        return self._nomelojas

    def set_nomelojas(self, nomelojas):
        self._nomelojas = nomelojas

    def get_cnpjlojas(self):
        return self._cnpjlojas

    def set_cnpjlojas(self, cnpjlojas):
        self._cnpjlojas = cnpjlojas

    def cadastrar_loja(self):
        nova_loja = Loja()
        nova_loja.set_nomelojas(self.get_nomelojas() + [input('Digite o nome da loja: ')])
        nova_loja.set_cnpjlojas(self.get_cnpjlojas() + [input('Digite o cnpj da loja: ')])
        return nova_loja

    def ver_lojas(self):
        print('-----------------------------------------')
        print('Lojas')
        print(self._nomelojas)
        print('-----------------------------------------')
        print('Respectivos cnpjs')
        print(self._cnpjlojas)
        print('-----------------------------------------')


class Cliente:
    def __init__(self):
        self._nomeclientes = []
        self._cnpjclientes = []

    def get_nomeclientes(self):
        return self._nomeclientes

    def set_nomeclientes(self, nomeclientes):
        self._nomeclientes = nomeclientes

    def get_cnpjclientes(self):
        return self._cnpjclientes

    def set_cnpjclientes(self, cnpjclientes):
        self._cnpjclientes = cnpjclientes

    def cadastrar_cliente(self):
        novo_cliente = Cliente()
        novo_cliente.set_nomeclientes(self.get_nomeclientes() + [input('Digite o nome do cliente: ')])
        novo_cliente.set_cnpjclientes(self.get_cnpjclientes() + [input('Digite qual o cnpj do cliente: ')])
        return novo_cliente

    def ver_clientes(self):
        print('-----------------------------------------')
        print('Nome dos Clientes')
        print(self._nomeclientes)
        print('-----------------------------------------')
        print('Respectivos Cnpjs')
        print(self._cnpjclientes)
        print('-----------------------------------------')


class Fornecedor:
    def __init__(self):
        self._nomefornecedores = []
        self._cnpjfornecedores = []

    def get_nomefornecedores(self):
        return self._nomefornecedores

    def set_nomefornecedores(self, nomefornecedores):
        self._nomefornecedores = nomefornecedores

    def get_cnpjfornecedores(self):
        return self._cnpjfornecedores

    def set_cnpjfornecedores(self, cnpjfornecedores):
        self._cnpjfornecedores = cnpjfornecedores

    def cadastrar_fornecedor(self):
        novo_fornecedor = Fornecedor()
        novo_fornecedor.set_nomefornecedores(self.get_nomefornecedores() + [input('Digite o nome do fornecedor: ')])
        novo_fornecedor.set_cnpjfornecedores(self.get_cnpjfornecedores() + [input('Digite o cnpj do fornecedor: ')])
        return novo_fornecedor

    def ver_fornecedores(self):
        print('-----------------------------------------')
        print('Nome')
        print(self._nomefornecedores)
        print('-----------------------------------------')
        print('Respectivos Cnpj')
        print(self._cnpjfornecedores)
        print('-----------------------------------------')


class Estoque:
    def __init__(self):
        self._itens = []
        self._precos = []
        self._quantidade = []

    def get_itens(self):
        return self._itens

    def set_itens(self, itens):
        self._itens = itens

    def get_precos(self):
        return self._precos

    def set_precos(self, precos):
        self._precos = precos

    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self, quantidade):
        self._quantidade = quantidade

    def adicionar_ao_estoque(self):
        novo_item = input('Digite qual produto deseja adicionar: ')
        novo_preco = float(input('Digite o preço do produto: '))
        nova_quantidade = int(input('Quantidade do produto: '))
        self.set_itens(self.get_itens() + [novo_item])
        self.set_precos(self.get_precos() + [novo_preco])
        self.set_quantidade(self.get_quantidade() + [nova_quantidade])

    def remover_do_estoque(self):
        item_remover = input('Digite o nome do item que deseja remover: ')
        if item_remover in self.get_itens():
            indice_item = self.get_itens().index(item_remover)
            self.set_itens(self.get_itens()[:indice_item] + self.get_itens()[indice_item + 1:])
            self.set_precos(self.get_precos()[:indice_item] + self.get_precos()[indice_item + 1:])
            self.set_quantidade(self.get_quantidade()[:indice_item] + self.get_quantidade()[indice_item + 1:])
            print(item_remover, ' removido do estoque')
        else:
            print(item_remover, 'não encontrado no estoque')
            print('Certifique-se de ter escrito corretamente o nome do item')

    def ver_estoque(self):
        print('-----------------------------------------')
        print('Item')
        print(self.get_itens())
        print('-----------------------------------------')
        print('Preço')
        print(self.get_precos())
        print('-----------------------------------------')
        print('Quantidade')
        print(self.get_quantidade())
        print('-----------------------------------------')

    def alterar_quantidade(self):
        item_alterar = input('Digite o nome do item que você deseja alterar a quantidade')
        if item_alterar in self.get_itens():
            indice_item = self.get_itens().index(item_alterar)
            nova_quantidade = int(input('Digite a nova quantidade do produto'))
            self.set_quantidade(self.get_quantidade()[:indice_item] + [nova_quantidade] + self.get_quantidade()[indice_item + 1:])
            print('Produto alterado com sucesso!')


# Menu Principal
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

    elif resposta == 1:
        while True:
            print('-----------------------------------------')
            print('1 - Para cadastrar nova loja')
            print('2 - Para ver as lojas cadastradas')
            print('3 - Para voltar ao menu')
            print('-----------------------------------------')
            respostaloja = int(input())

            if respostaloja == 1:
                loja = loja.cadastrar_loja()
                print('-----------------------------------------')
                print('Loja cadastrada com sucesso!')
                print('-----------------------------------------')

            elif respostaloja == 2:
                loja.ver_lojas()

            elif respostaloja == 3:
                break

            else:
                print('Resposta inválida')

    elif resposta == 2:
        while True:
            print('-----------------------------------------')
            print('1 - Para cadastrar novo Cliente')
            print('2 - Para ver os clientes cadastrados')
            print('3 - Para voltar ao menu')
            print('-----------------------------------------')
            respostacliente = int(input())

            if respostacliente == 1:
                cliente = cliente.cadastrar_cliente()
                print('Cliente cadastrado com sucesso!')

            elif respostacliente == 2:
                cliente.ver_clientes()

            elif respostacliente == 3:
                break

            else:
                print('Resposta Inválida')

    elif resposta == 3:
        while True:
            print('-----------------------------------------')
            print('1 - Para cadastrar novo fornecedor')
            print('2 - Para ver os fornecedores cadastrados')
            print('3 - Para voltar ao menu')
            print('-----------------------------------------')
            respostafornecedor = int(input())

            if respostafornecedor == 1:
                fornecedor = fornecedor.cadastrar_fornecedor()
                print('Fornecedor cadastrado com sucesso!')

            elif respostafornecedor == 2:
                fornecedor.ver_fornecedores()

            elif respostafornecedor == 3:
                break

            else:
                print('Resposta Inválida')

    elif resposta == 4:
        while True:
            print('Bem vindo ao estoque!')
            print('-----------------------------------------')
            print('1 - Adicionar itens ao estoque')
            print('2 - Remover itens do estoque')
            print('3 - Alterar quantidade de itens no estoque ')
            print('4 - Ver estoque')
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

            elif respostaestoque == 3:
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
