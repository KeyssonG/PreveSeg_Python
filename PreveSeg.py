# Variaveis
login = 'keysson@'
senha = int(123456)

# Tela de login do usuário

login = input('Digite o seu login de acesso: ')
senha = int(input('Digite a sua senha: '))

if login == login and senha == senha:
    print('Login efetuado com sucesso!')
else:
    print('Senha incorreta, digite novamente!')

print(40*'-')

setor = int(input('Qual setor deseja acessar? Prevenção [1] RH [2] Financeiro [3]:'))

if setor == 1:
    print('Seja bem vindo ao setor de Prevenção!')

else:
    print('Você não escolheu nenhum setor, tente novamente')