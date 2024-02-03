'''''
#“Criar um projeto de movimentação de estoque de produtos de limpeza de uma loja, para isso,
# será necessário cadastrar a loja, os clientes, os fornecedores e o controle de estoque
# (entrada e saída de produtos)”

Regras:
•	Linguagem de programação: A que tiver mais afinidade, desde que seja Orientada a objeto (POO)
•	Não é necessário utilizar banco de dados
•	Criar classes com setters e getters
'''
class Loja:
    def __init__(self, nomeloja):
        self.nomeloja = nomeloja

    def cadastrar_loja(self):
        self.nomeloja = input('Digite o nome da loja: ')

print('Bem-Vindo ao Sistema!')
print('Digite 1 para cadastrar loja')
print('Digite 2 para cadastrar clientes')
print('Digite 3 para cadastrar fornecedores')
print('Digite 4 para acessar o estoque')
resposta = int(input())

if resposta == 1:
    nova_loja = Loja(nomeloja="")
    nova_loja.cadastrar_loja()
    print('Loja cadastrada com sucesso!')
else:
    print('Opção inválida')
