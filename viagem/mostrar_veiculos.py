from viagem import controller_viagem


def mostrarVeiculosViajando():
    print('\033[1;32m\n-----------VEÍCULOS VIAJANDO---------\033[m')
    veiculosViajando = controller_viagem.separarVeiculosViajando()
    if len(veiculosViajando) != 0:
        for veiculo in veiculosViajando.values():
            print(f'Veículo → placa: {veiculo["placa"]}, tipo: {veiculo["tipo"]}\n'
                f'Motorista → CPF: {veiculo["motorista"]["cpf"]}, nome: {veiculo["motorista"]["nome"]}, carteira: {veiculo["motorista"]["carteira"]}\n')
    else:
        print('\033[1;31mNenhum veículo em viagem!\033[m')


def mostrarVeiculosDisponiveis():
    print('\033[1;32m\n-----------VEÍCULOS DISPONÍVEIS PARA VIAGEM---------\033[m')
    veiculosDisponiveis = controller_viagem.separarVeiculosDisponiveis()
    if len(veiculosDisponiveis) != 0:
        for veiculo in veiculosDisponiveis.values():
            if veiculo['motorista'] != None:
                print(f'Veículo → placa: {veiculo["placa"]}, tipo: {veiculo["tipo"]}\n'
                    f'Motorista → CPF: {veiculo["motorista"]["cpf"]}, nome: {veiculo["motorista"]["nome"]}, carteira: {veiculo["motorista"]["carteira"]}\n')
    else:
        print('\033[1;31mNenhum veículo disponível!\033[m')