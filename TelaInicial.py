# Menu inicial
from time import sleep
import cadastro
import os
import sys


def loading():
    # Barra de loading (fake)
    print("\nCarregando Modulo de cadastro:")

    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
                 "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]",
                 "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")
def telaInicialCadastro():
    print(""" ██████╗ █████╗ ██████╗  █████╗ ███████╗████████╗██████╗  ██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗
██║     ███████║██║  ██║███████║███████╗   ██║   ██████╔╝██║   ██║
██║     ██╔══██║██║  ██║██╔══██║╚════██║   ██║   ██╔══██╗██║   ██║
╚██████╗██║  ██║██████╔╝██║  ██║███████║   ██║   ██║  ██║╚██████╔╝
 ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ 
                                                                  """)

def telaInicial():
    print(""" ██████╗ ███████╗███████╗██╗ ██████╗███████╗██████╗     ██████╗ ██╗   ██╗
██╔═══██╗██╔════╝██╔════╝██║██╔════╝██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝
██║   ██║█████╗  █████╗  ██║██║     █████╗  ██████╔╝    ██████╔╝ ╚████╔╝ 
██║   ██║██╔══╝  ██╔══╝  ██║██║     ██╔══╝  ██╔══██╗    ██╔═══╝   ╚██╔╝  
╚██████╔╝██║     ██║     ██║╚██████╗███████╗██║  ██║    ██║        ██║   
 ╚═════╝ ╚═╝     ╚═╝     ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝    ╚═╝        ╚═╝   
                                                                         """)



    print("""\nEste é um projeto que esta em Alpha que consiste em varios modulos que podem 
ser utilizados em escritorios.""")

    print('\nComece selecionando a opção abaixo e veja a magica acontecer:')
    print("""\n(1) Cadastro
(2) Exclusão
(3) Consulta
(4) Sair""")

    opcao = int(input('\nSelecione: '))
    while(opcao != 4):
        if opcao == 1:
            os.system('cls')
            loading()
            os.system('cls')
            telaInicialCadastro()
            cadastro.cadastroFuncionarios()
            break
        else:
            print(f'Opção selecionado esta em desenvolvimento')
            opcao = int(input('Selecione outra opção: '))
    print('\nObrigado por participar do Alpha de nosso programa!!!!')
    encerrar = str(input('\nPrecione ENTER para encerrar o programa'))

if __name__ == '__main__':
    telaInicial()