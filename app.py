
from datetime import datetime
import random

nome_funcionario = input('Informe seu nome: ')
idade_funcionario = int(input('Informe sua idade: '))
data_cadastro = datetime.now()
cartoes = ['R$50,00','R$250,00','R$120,00']
cartao = random.choice(cartoes)
nascimento = datetime.strptime(
    input('Informe sua data de nascimento (dd/mm/aaaa): '), '%d/%m/%Y')

print('Olá, {}! Seu registro foi concluído com sucesso no dia {}.'.format(nome_funcionario, data_cadastro.strftime('%d/%m/%Y')))
print('Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {}.'.format(cartao))