from motorista import menu_motorista
from veiculos import menu_veiculos
from viagem import menu_viagem

def menuPrincipal():
    while True:
        print('\n\033[1;36m-----------MENU PRINCIPAL---------\033[m')
        print('\033[31m[1]\033[m - Menu motoristas')
        print('\033[31m[2]\033[m - Menu veiculos')
        print('\033[31m[3]\033[m - Menu viagens')
        print('\033[31m[4]\033[m - Sair')
        escolha = int(input("Digite uma das opções>>> "))
        if escolha == 1:
            menu_motorista.menuMotorista()
        elif escolha == 2:
            menu_veiculos.menuVeiculo()
        elif escolha == 3:
            menu_viagem.menuViagem()
        elif escolha == 4:
            break
        else:
            print("Opção inválida!")

menuPrincipal()