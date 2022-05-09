from veiculos import buscar_veiculo
from veiculos import controller_veiculo
from motorista.controller import gerarDicionarioMotoristas


def listarMotoristas():
    veiculo = buscar_veiculo.buscarVeiculo()
    dicionarioMotoristas = gerarDicionarioMotoristas()
    dicionarioVeiculos = controller_veiculo.lerDadosJson()
    dicionarioMotoristasCapazes = {}
    if len(dicionarioVeiculos) != 0:
        if veiculo['motorista'] == None:
            #Listar motoristas capazes de conduzir o veículo
            print('\n\033[1;36m-----------LISTA DE MOTORISTAS CAPAZES DE CONDUZIR ESTE VEÍCULO---------\033[m')
            if veiculo.get('tipo') == 'Carro':
                for motorista in dicionarioMotoristas.values():
                    if motorista.get('carteira') == 'B' or motorista.get('carteira') == 'AB':
                        print(f'CPF: {motorista["cpf"]}, Nome: {motorista["nome"]}, Habilitação: {motorista["carteira"]}')
                        dicionarioMotoristasCapazes[str(motorista.get('cpf'))] = motorista

            else:
                for motorista in dicionarioMotoristas.values():
                    print(motorista)
                    dicionarioMotoristasCapazes[str(motorista.get('cpf'))] = motorista

            resposta = adicionarMotorista(veiculo, dicionarioMotoristasCapazes)
            if resposta == True:
                print('\033[1;32mMotorista adicionado com sucesso!\033[m')
            else:
                print('\033[1;31mO CPF inserido não existe ou pertence a um motorista incapaz de conduzir o veículo!\033[m')
        else:
            print('\033[1;31mEste veículo já possuí motorista!\033[m')


def adicionarMotorista(veiculo, motoristas):
    print()
    cpf = int(input('Digite o cpf do motorista a ser adicionado: '))
    for motorista in motoristas.values():
        if motorista['cpf'] == cpf:
            veiculo['motorista'] = motorista
            dicionarioVeiculos = controller_veiculo.lerDadosJson()
            dicionarioVeiculos[veiculo.get('placa')] = veiculo
            controller_veiculo.gravarDados(dicionarioVeiculos)
            return True
    return False


def removerMotorista():
    print('\033[1;36m-----------REMOVER MOTORISTA DO VEÍCULO---------\033[m')
    dicionarioVeiculos = controller_veiculo.lerDadosJson()
    if len(dicionarioVeiculos) != 0:
        placa = input("Digite a placa do veículo: ")
        veiculoEncontrado = controller_veiculo.buscarVeiculo(dicionarioVeiculos, placa)
        if len(veiculoEncontrado) != 0:
            if veiculoEncontrado['motorista'] != None:
                veiculoEncontrado['motorista'] = None
                dicionarioVeiculos[veiculoEncontrado.get('placa')] = veiculoEncontrado
                controller_veiculo.gravarDados(dicionarioVeiculos)
                print('Motorista removido com sucesso!')
            else:
                print('\033[1;31mEste veículo não possuí motorista!\033[m')
        else:
            print('\033[1;31mVeículo não encontrado!\033[m')
    else:
        print('\033[31mSem veículos cadastrados!\033[m')

