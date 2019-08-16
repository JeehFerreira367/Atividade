nome = input('Seu nome completo: ')
idade = int(input('Sua idade: '))
saldo = float(input('Seu Saldo: '))

def atm(nome, idade, saldo):

    print('Digite (1) para saque')
    print('Digite (2) para depósito')
    print('Digite (3) para empréstimo')
    print('Digite (4) para visualizar informações')
    print('Digite (Qualquer outro texto ou número) para sair')
    menu = input('Digite aqui: ')

    if menu == '1':
        print('SAQUE')
        valor_saque = float(input('Digite o valor o valor desejado para saque:'))
        if (valor_saque > 1000) or (valor_saque >= float(saldo)):
            print('Saque indiponível, valor indisponível ou acima de R$1000,00')
            atm(nome, idade, saldo)
        else:
            saldo_saque = saldo - valor_saque
            print('SAQUE REALIZADO')
            print('SALDO ATUAL É DE {}'.format(saldo_saque))
            atm(nome, idade, saldo)

    elif menu == '2':
        print('DEPÓSITO')
        valor_deposito = float(input('Digite o valor desejado para deposito'))
        if (valor_deposito > 5000):
            print('Valor maximo para deposito atingido, seu deposito não foi realizado')
            atm(nome, idade, saldo)
        else:
            saldo_deposito = saldo + valor_deposito
            print('DEPOSITO REALIZADO')
            print('SEU SALDO ATUAL É DE {}' .format(saldo_deposito))
            atm(nome, idade, saldo)

    elif menu == '3':
        print ('EMPRESTIMO')
        valor_emprestimo = int(input('Digite o valor desejado para emprestimo'))
        if (valor_emprestimo < 15 * saldo and saldo <2000 and idade<21):
            print('Emprestimo invalido')
            atm(nome, idade, saldo)
        else:
            saldo_emprestimo = saldo + valor_emprestimo
            print('EMPRESTIMO REALIZADO')
            print('SEU SALDO ATUAL É DE {}' .format(saldo_emprestimo))
            atm(nome, idade, saldo)
    elif menu == '4':
        print('INFORMAÇÕES PESSOAIS')
        print('Seu nome é: {}' .format(nome))
        print('Sua idade é:{}' .format(idade))
        print('Seu saldo é de : R${}'.format(saldo))
        atm(nome, idade, saldo)
    else:
        input('Digite qualquer caracter para sair')

if idade != 0:
    atm(nome, idade, saldo)













