import veiculos.listar_veiculos
import veiculos.remover_veiculo
import veiculos.operacoes_motorista
import veiculos.add_veiculo
import veiculos.buscar_veiculo


def menuVeiculo():
    while True:
        print('\n\033[1;36m-----------MENU VEÍCULO---------\033[m')
        print('\033[1;31m[1]\033[m - Cadastrar Veiculo')
        print('\033[1;31m[2]\033[m - Buscar Veiculo por placa')
        print('\033[1;31m[3]\033[m - Adicionar motorista ao veiculo')
        print('\033[1;31m[4]\033[m - Remover motorista do veiculo')
        print('\033[1;31m[5]\033[m - Listar veiculos com motoristas')
        print('\033[1;31m[6]\033[m - Listar veiculos sem motoristas')
        print('\033[1;31m[7]\033[m - Remover veiculo')
        print('\033[1;31m[8]\033[m - Sair do menu veículo')
        print('-'*35)
        escolha = int(input("DIGITE UMA DAS OPÇÕES>>> "))
        if escolha == 1:
            veiculos.add_veiculo.cadastrarveiculo()
        elif escolha == 2:
            veiculos.buscar_veiculo.buscarVeiculo()
        elif escolha == 3:
            veiculos.operacoes_motorista.listarMotoristas()
        elif escolha == 4:
            veiculos.operacoes_motorista.removerMotorista()
        elif escolha == 5:
            veiculos.listar_veiculos.listarVeiculosComMotoristas()
        elif escolha == 6:
            veiculos.listar_veiculos.listarVeiculosSemMotoristas()
        elif escolha == 7:
            veiculos.remover_veiculo.removerVeiculo()
        elif escolha == 8:
            break
        else:
            print("\033[31mOpção inválida!\033[m")
