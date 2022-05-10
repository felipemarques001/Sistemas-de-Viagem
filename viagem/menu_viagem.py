import viagem.listar_viagem
import viagem.add_viagem
import viagem.finalizar_viagem
import viagem.mostrar_veiculos


def menuViagem():
    while True:
        print('\n\033[1;36m-----------MENU VIAGEM---------\033[m')
        print('\033[1;31m[1]\033[m - Criar Viagem')
        print('\033[1;31m[2]\033[m - Finalizar Viagem por placa')
        print('\033[1;31m[3]\033[m - Listar viagens Ativas')
        print('\033[1;31m[4]\033[m - Listar veiculos que estão em Viagem')
        print('\033[1;31m[5]\033[m - Listar veiculos que estão disponíveis para Viagem')
        print('\033[1;31m[6]\033[m - Listar todas as viagens')
        print('\033[1;31m[7]\033[m - Listar todas as viagens por período')
        print('\033[1;31m[8]\033[m - Sair do menu viagem')
        print('-' * 35)
        escolha = int(input("DIGITE UMA DAS OPÇÕES>>> "))
        if escolha == 1:
            viagem.add_viagem.criarViagem()
        elif escolha == 2:
            viagem.finalizar_viagem.finalizarViagem()
        elif escolha == 3:
            viagem.listar_viagem.listarViagensAtivas()
        elif escolha == 4:
            viagem.mostrar_veiculos.mostrarVeiculosViajando()
        elif escolha == 5:
            viagem.mostrar_veiculos.mostrarVeiculosDisponiveis()
        elif escolha == 6:
            viagem.listar_viagem.listarTodasViagens()
        elif escolha == 7:
            viagem.listar_viagem.listarViagemPorPeriodo()
        elif escolha == 8:
            break
        else:
            print("\033[31mOpção inválida!\033[m")
