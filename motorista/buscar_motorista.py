from motorista import controller


def buscarMotorista():  # Esta função também é usada quando vamos editar o motorista
    print('\033[1;36m-----------BUSCAR MOTORISTA POR CPF---------\033[m')
    dicionarioMotoristas = controller.gerarDicionarioMotoristas();
    if len(dicionarioMotoristas) != 0:
        cpf = int(input("Digite o CPF do motorista: "))
        motoristaEncontrado = controller.buscarMotoristaPorCpf(dicionarioMotoristas, cpf)

        if len(motoristaEncontrado) != 0:
            print('\033[32m-----------DADOS DO MOTORISTA---------\033[m')
            print(f'CPF: {motoristaEncontrado.get("cpf")}\n'
                  f'Nome: {motoristaEncontrado.get("nome")}\n'
                  f'Tipo de habilitação: {motoristaEncontrado.get("carteira")}')
            return motoristaEncontrado  # Este return está sendo usado no arquivo editar_nome_motorista
        else:
            print('\033[31mMotorista não encontrado!\033[m')
            return motoristaEncontrado  # Este return será usado para evitar um bug no arquivo editar_nome_motorista
    else:
        print('\033[31mSem motoristas cadastrados!\033[m')
