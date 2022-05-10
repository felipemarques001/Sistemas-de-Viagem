import motorista.cadastrar_motorista
import motorista.remover_motorista
import motorista.listar_motoristas
import motorista.editar_nome_motorista
import motorista.buscar_motorista


def menuMotorista():
    while True:
        print('')
        print('\033[1;34m-----------MENU MOTORISTAS---------\033[m')
        print('\033[31m[1]\033[m - Cadastrar motorista')
        print('\033[31m[2]\033[m - Buscar motorista por cpf')
        print('\033[31m[3]\033[m - Editar nome do motorista')
        print('\033[31m[4]\033[m - Remover motorista')
        print('\033[31m[5]\033[m - Listar todos os motorista por tipo da carteira')
        print('\033[31m[6]\033[m - Listar todos os motorista')
        print('\033[31m[7]\033[m - Sair do menu motorista')
        print()
        escolha = int(input("Digite uma das opções>>>"))

        if escolha == 1:
            motorista.cadastrar_motorista.cadastrarMotorista()
        elif escolha == 2:
            motorista.buscar_motorista.buscarMotorista()
        elif escolha == 3:
            motorista.editar_nome_motorista.editarNomeMotorista()
        elif escolha == 4:
            motorista.remover_motorista.menuRemoverMotorista()
        elif escolha == 5:
            motorista.listar_motoristas.listarMotoristaPorCarteira()
        elif escolha == 6:
            motorista.listar_motoristas.listarTodosMotoristas()
        elif escolha == 7:
            break
        else:
            print('\033[Opção inválida!\033[m')
