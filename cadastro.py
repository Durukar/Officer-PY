from time import sleep
import sys
import os
import TelaInicial


def loading():
    # Barra de loading (fake)


    print("\nFuncionario sendo cadastrado")

    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
                 "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]",
                 "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")

def cadastroFuncionarios():
    # Caminho onde sera salva a ficha de cadastro
    fichaCadastralTXT = './ficha.txt'

    # Encerrar o cadastro
    encerrarCadastro = False

    # Laço de cadastro
    with open(fichaCadastralTXT, 'a') as fichaTXT:
        while (not encerrarCadastro):
            # Ficha de cadastro
            try:
                nome = str(input('Digite o nome completo do(a) funcionario(a): ')).title().strip()
                idade = int(input('Digite a idade do(a) funcionario(a): '))
            except:
                print('Para nome use somente letras e para idade utilize somente numeros INTEIROS!!!!!!')
                continue
            loading()

            print('Funcionario(a) cadastrado(a)')
            # Salvar em TXT
            print(f'{nome:<3} , {idade:<15}', file=fichaTXT)

            sleep(2)

            continuar = int(input("""Deseja realizar um novo cadastro?
(1) Sim
(2) Não
Selecione: """))
            if continuar != 1:
                break

    encerrar = input('\nPrecione ENTER para encerrar o modulo')


if (__name__ == '__main__'):
    cadastroFuncionarios()
