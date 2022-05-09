from veiculos.controller_veiculo import lerDadosJson as gerarVeiculos
from viagem import controller_viagem
import datetime


def criarViagem():
    listarVeiculos()
    print('\033[1;32m-----------CRIAR VIAGEM---------\033[m')
    dicionarioViagem = controller_viagem.lerDadosJson()
    veiculo = adicionarVeiculo()
    rota = input("Digite o local de destino da viagem: ").lower()
    status = True
    data = criarData()
    idViagem = veiculo['placa']
    dicionarioViagem[idViagem] = {
        "veiculo": veiculo,
        "rota": rota,
        "status": status,
        "data": data,
    }
    controller_viagem.gravarDados(dicionarioViagem)
    print('\033[1;32mViagem cadastrada com sucesso!\033[m')
    print('---' * 15)


def listarVeiculos():
    dicionarioVeiculos = gerarVeiculos()
    print('\n\033[1;32m-----------LISTA DE VEÍCULOS CADASTRADOS---------\033[m')
    if len(dicionarioVeiculos) != 0:
        for veiculo in dicionarioVeiculos.values():
            if veiculo['motorista'] != None:
                print(f'Placa: {veiculo["placa"]}; \n'
                      f'Tipo de veículo: {veiculo["tipo"]}; \n'
                      f'Motorista → CPF: {veiculo["motorista"]["cpf"]}, Nome: {veiculo["motorista"]["nome"]}, Carteira: {veiculo["motorista"]["carteira"]}; \n')
            else:
                print(f'Placa: {veiculo["placa"]}; \n'
                      f'Tipo de veículo: {veiculo["tipo"]}; \n'
                      f'Motorista: {veiculo["motorista"]}\n')
    else:
        print('Nenhum veículo cadastrado!')

def adicionarVeiculo():
    veiculos = gerarVeiculos()
    while True:
        placa = input('Adicione a placa do veículo para está viagem: ')
        placaCadastrada = controller_viagem.checarVeículo(placa)
        if placaCadastrada == True:
            print('\033[1;31mEste veículo já está cadastrado em uma viagem ativa!\033[m')
        else:
            for veiculo in veiculos.values():
                if veiculo['placa'] == placa and veiculo['motorista'] != None:
                    return veiculo
            print('\033[1;31mPlaca não cadastrada ou veículo sem motorista!\033[m') #Só rodará esse print se o placa digitada não estiver cadastrada


def criarData():
    dia = int(input('Digite o dia da viagem: '))
    mes = int(input('Digite o mês da viagem: '))
    ano = int(input('Digite o ano da viagem: '))
    data = datetime.date(ano, mes, dia)
    dataFormatada = data.strftime('%d/%m/%Y')
    return dataFormatada

