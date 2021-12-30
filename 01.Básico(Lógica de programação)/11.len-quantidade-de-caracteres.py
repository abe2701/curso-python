usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)
if qtd_caracteres < 6:
    print('O nome do usuário precisa ter no mínimo 6 caracteres.')
else:
    print('Usuário cadastrado com sucesso!  ')