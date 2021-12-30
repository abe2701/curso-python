"""
* Criar varíaveis para nome (str), idade (int)
* Altura (float) e peso (float) de uma pessoa
* Criar uma variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Abel'
idade = 24
altura = 1.80
peso = 84.50
ano_atual = 2021
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'OIMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}')