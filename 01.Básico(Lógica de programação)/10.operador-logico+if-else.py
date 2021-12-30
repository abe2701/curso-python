usuario = input('Nome do usuário:')
senha = input('Senha do usuário: ')
usuario_db = 'Abel'
senha_db = 'Hoje'
if usuario == usuario_db and senha == senha_db:
    print('Sucesso!!!')
else:
    print('Acesso negado!!!')