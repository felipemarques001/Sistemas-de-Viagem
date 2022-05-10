from veiculos import controller_veiculo

#Usarei esta função quando for remover um motorista do veículo
def listarVeiculosComMotoristas():
    print('\n\033[1;32m-----------LISTAS DE VEÍCULOS COM MOTORISTAS---------\033[m')
    dicionarioVeiculos = controller_veiculo.lerDadosJson()
    contador = 0
    for veiculo in dicionarioVeiculos.values():
        if veiculo['motorista'] != None:
            contador += 1
            print(f'Placa: {veiculo["placa"]}; \n'
                  f'Tipo de veículo: {veiculo["tipo"]}; \n'
                  f'Motorista → CPF: {veiculo["motorista"]["cpf"]}, Nome: {veiculo["motorista"]["nome"]}, Carteira: {veiculo["motorista"]["carteira"]}; \n')
    if contador == 0:
        print('\033[1;31mNenhum veículo com motorista cadastrado!\033[m')
def listarVeiculosSemMotoristas():
    print('\n\033[1;32m-----------LISTAS DE VEÍCULOS SEM MOTORISTAS---------\033[m')
    dicionarioVeiculos = controller_veiculo.lerDadosJson()
    contador = 0
    for veiculo in dicionarioVeiculos.values():
        if veiculo['motorista'] == None:
            contador += 1
            print(f'Placa: {veiculo["placa"]}; \n'
                  f'Tipo de veículo: {veiculo["tipo"]}; \n')
    if contador == 0:
        print('\033[1;31mNenhum veículo sem motorista cadastrado!\033[m')