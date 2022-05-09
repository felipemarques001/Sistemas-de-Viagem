from viagem import controller_viagem
import datetime

def listarTodasViagens():
    print('\033[1;32m\n-----------LISTA DE VIAGENS---------\033[m')
    dicionarioViagens = controller_viagem.lerDadosJson()
    if len(dicionarioViagens) != 0:
        for viagem in dicionarioViagens.values():
            print(f'Veículo → placa: {viagem["veiculo"]["placa"]}, tipo: {viagem["veiculo"]["tipo"]}\n'
                  f'Motorista → CPF: {viagem["veiculo"]["motorista"]["cpf"]}, nome: {viagem["veiculo"]["motorista"]["nome"]}, carteira: {viagem["veiculo"]["motorista"]["carteira"]}\n'
                  f'Rota → {viagem["rota"]}\n'
                  f'Status → {viagem["status"]}\n'
                  f'Data → {viagem["data"]}\n')
    else:
        print('\033[1;31mNenhuma viagem cadastrada!\033[m')

def listarViagensAtivas():
    print('\033[1;32m\n-----------LISTA DE VIAGENS ATIVAS---------\033[m')
    viagensAtivas = controller_viagem.viagensAtivas()
    if len(viagensAtivas) != 0:
        for viagem in viagensAtivas.values():
            print(f'Veículo → placa: {viagem["veiculo"]["placa"]}, tipo: {viagem["veiculo"]["tipo"]}\n'
                  f'Motorista → CPF: {viagem["veiculo"]["motorista"]["cpf"]}, nome: {viagem["veiculo"]["motorista"]["nome"]}, carteira: {viagem["veiculo"]["motorista"]["carteira"]}\n'
                  f'Rota → {viagem["rota"]}\n'
                  f'Status → {viagem["status"]}\n'
                  f'Data → {viagem["data"]}\n')
    else:
        print('\033[1;31mNenhuma viagem cadastrada!\033[m')


def listarViagemPorPeriodo():
    if len(controller_viagem.viagensAtivas()) != 0:
        print('\033[1;32m\n-----------LISTA DE VIAGENS EM UM PERÍODO---------\033[m')
        print('\n--------Digite a primeira data--------')
        data1 = criarData()
        print('\n--------Digite a segunda data--------')
        data2 = criarData()
        viagens = controller_viagem.viagensEntrePeriodo(data1, data2)
        if len(viagens) != 0:
            print(f'\n--------Lista de viagens entre {data1.strftime("%d/%m/%Y")} a {data2.strftime("%d/%m/%Y")}--------')
            for viagem in viagens.values():
                print(f'Veículo → placa: {viagem["veiculo"]["placa"]}, tipo: {viagem["veiculo"]["tipo"]}\n'
                      f'Motorista → CPF: {viagem["veiculo"]["motorista"]["cpf"]}, nome: {viagem["veiculo"]["motorista"]["nome"]}, carteira: {viagem["veiculo"]["motorista"]["carteira"]}\n'
                      f'Rota → {viagem["rota"]}\n'
                      f'Status → {viagem["status"]}\n'
                      f'Data → {viagem["data"]}\n')
        else:
            print('\033[1;31mNenhuma viagem entre este período cadastrada!\033[m')
    else:
        print('\033[1;31mNenhuma viagem cadastrada!\033[m')

def criarData():
    dia = int(input('Digite o dia da viagem: '))
    mes = int(input('Digite o mês da viagem: '))
    ano = int(input('Digite o ano da viagem: '))
    data = datetime.date(ano, mes, dia)
    return data