import os
import re

login_senha = []

def mostrarMenu1():
    print('='*25)
    print('\033[36mBEM VINDO AO SISTEMA DE VALIDAR SENHA\033[m')
    print('='*25)
    print('''
    [1] LOGIN
    [2] CADASTRAR
    ''')

def cadastrar_senha():
    tentativas = 0
    senha_valida = False
    while tentativas < 3 and not senha_valida:
        senha = input("Digite a sua senha: ")
        if (len(senha) < 8 or
            not re.search("[a-z]", senha) or
            not re.search("[A-Z]", senha) or
            not re.search("[0-9]", senha) or
            not re.search("[!@#$%^&*()_+]", senha)):
            print('''A senha deve conter pelo menos 8 caracteres,
            incluindo letras maiúsculas, minúsculas, números e caracteres
            especiais.''')
            tentativas += 1
        else:
            senha_confirmacao = input("Confirme a sua senha: ")
            if senha == senha_confirmacao:
                senha_valida = True
            else:
                print("As senhas não coincidem.")

    if senha_valida:
        print("Senha cadastrada com sucesso!")
        return senha
    else:
        print("Você excedeu o número máximo de tentativas. A senha não foi cadastrada.")
        return None


while True:  # Loop infinito
    mostrarMenu1()
    opc = int(input('Escolha uma opção: '))
    os.system('cls')

    if opc == 1:
        senha = input('DIGITE SUA SENHA: ')
        if senha in login_senha:
            os.system('cls')
            print('\033[32mLOGIN EFETUADO COM SUCESSO!\033[m')
            print('BEM VINDO')
            break
        else:
            print('\033[31mSenha incorreta!\033[m')

    elif opc == 2:
        senha = cadastrar_senha()
        if senha:
            login_senha.append(senha)

    else:
        print('\033[31mOpção inválida!\033[m')

    if opc == 2:
        continue  # Volta ao início do loop para exibir o menu novamente
