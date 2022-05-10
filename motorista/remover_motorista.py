from motorista import controller


def menuRemoverMotorista():
    dicionarioMotoristas = controller.gerarDicionarioMotoristas()
    print('\n\033[1;32m-----------APAGAR MOTORISTAS---------\033[m')
    if len(dicionarioMotoristas) != 0:
        while True:
            print('\033[31m[1]\033[m - Remover motorista por CPF')
            print('\033[31m[2]\033[m - Remover todos os motoristas')
            print('\033[31m[3]\033[m - Voltar para o menu motorista')
            opcao = int(input())
            if opcao == 1:
                cpf = int(input("Digite o CPF do motorista (sem sinais): "))
                controller.removerMotoristaPorCpf(cpf, dicionarioMotoristas)
                break
            elif opcao == 2:
                controller.removerTodosOsMotoristas(dicionarioMotoristas)
                break
            elif opcao == 3:
                break
            else:
                print('Opção inválida!')
    else:
        print('\033[31mSem motoristas cadastrados!\033[m')







