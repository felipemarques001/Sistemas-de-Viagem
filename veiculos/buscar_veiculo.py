from veiculos import controller_veiculo as controller

def buscarVeiculo():
    print('\033[1;36m-----------BUSCAR VEÍCULO PELA PLACA---------\033[m')
    dicionarioVeiculos = controller.lerDadosJson()
    if len(dicionarioVeiculos) != 0:
        placa = input("Digite a placa do veículo: ")
        veiculoEncontrado = controller.buscarVeiculo(dicionarioVeiculos, placa)
        if len(veiculoEncontrado) != 0:
            print('\033[32m-----------DADOS DO VEÍCULO---------\033[m')
            print(f'Placa: {veiculoEncontrado.get("placa")}\n'
                  f'Tipo de veículo: {veiculoEncontrado.get("tipo")}')
            if veiculoEncontrado['motorista'] != None:
                  print(f'Motorista → CPF: {veiculoEncontrado["motorista"]["cpf"]}, nome: {veiculoEncontrado["motorista"]["nome"]}, carteira: {veiculoEncontrado["motorista"]["carteira"]}\n')
            else:
                print(f'Motorista → {veiculoEncontrado["motorista"]}')
            return veiculoEncontrado #Estamos usando essa função quando vamos adicionar ou remover o motorista ao veículo
        else:
            print('\033[31mVeículo não encontrado!\033[m')
            return veiculoEncontrado  # Estamos usando essa função quando vamos adicionar ou remover o motorista ao veículo
    else:
        print('\033[31mSem veículos cadastrados!\033[m')