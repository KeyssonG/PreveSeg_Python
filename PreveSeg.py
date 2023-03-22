# Variaveis
login = 'keysson@'
senha = int(123456)
job = 1, 2, 3

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

print(40*'-') 


job = int(input('Escolha uma das opções abaixo: [1]Cartões [2]Contas [3]Transações: ' ))

if job == 1:
    print('Cartão de final 1048.')
    print('Ativado em 02/03/2019.')
    print('tentativa de transação no valor de R$4.000 reais no PICPAY, negado por saldo insuficiente.')

elif job == 2:
    print('Conta criada no dia 01/03/2017.')
    print('Recebe mensalmente R$1200.00.')
    print('Tem uma média de gasto de R$800.00.')
    print('No dia 22/03/2023 as 02h00 tentou fazer um saque de R$5000.00.')
elif job == 3:
    print('Saldo da conta R$20.000')
    print('A conta possui um histórico de TEDs com valor máximo de R$2.000.')
    print('No dia 22/03/2023 as 00h30 tentou fazer um pix para PF no valor de R$50.000.')
    print('As transações foram negadas devido o valor ser alto.')
    print('Foram um total de 18 tentativas alertadas.')    