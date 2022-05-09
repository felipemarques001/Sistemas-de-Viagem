from veiculos import controller_veiculo

def removerVeiculo():
    print('\033[1;36m-----------REMOVER VEÍCULO---------\033[m')
    dicionarioVeiculos = controller_veiculo.lerDadosJson()
    if len(dicionarioVeiculos) != 0:
        placa = input("Digite a placa do veículo a ser removido: ")
        veiculoEncontrado = controller_veiculo.buscarVeiculo(dicionarioVeiculos, placa)
        if len(veiculoEncontrado) != 0:
            del dicionarioVeiculos[placa]
            controller_veiculo.gravarDados(dicionarioVeiculos)
            print('Veículo removido com sucesso!')
        else:
           print('\033[31mVeículo não encontrado!\033[m')
    else:
        print('\033[31mSem veículos cadastrados!\033[m')