"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informa que não é um número inteiro.
"""
num1 = input('Digite um número inteiro: ')
if num1.isnumeric():
    num2 = int(num1)
    if (num2 % 2 == 0):
        print(f'O número {num2} é par.')
    else:
        print(f'O número {num2} é impar.')
else:
    print(f'Número {num1} não é inteiro.')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropirada.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input('Digite somente a hora atual sem os minutos: ')
converter_horario=int(horario)
if converter_horario < 0 or converter_horario > 23:
    print('Horário inválido!')
elif converter_horario <= 11:
    print('Bom dia!')
elif converter_horario <= 17:
    print('Boa tarde!')
else:
    print('Boa noite!')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; Maior que 6 letras escreva "Seu nome é muito grande" 
"""
nome = input('Digite seu primeiro nome: ')
if len(nome) <= 4:
    print('Seu nome é curto.')
elif len(nome) <=6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')