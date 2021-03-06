import json
from veiculos.controller_veiculo import lerDadosJson as pegarVeiculos
from datetime import datetime


def lerDadosJson():
    with open('viagem/bdViagens.json', 'r+') as arqjson:
        dicionarioViagem = json.load(arqjson)
    return dicionarioViagem


def gravarDados(dicionario):
    with open('viagem/bdViagens.json', 'w') as arqJson:
        json.dump(dicionario, arqJson, indent=4)


def checarVeículo(placa):
    dicionarioViagem = lerDadosJson()
    for viagem in dicionarioViagem.values():
        if viagem['veiculo']['placa'] == placa and viagem['status'] != False:
            return True
    return False


def separarVeiculosViajando():
    dicionarioVeiculos = pegarVeiculos()
    dicionarioViagens = lerDadosJson()
    veiculosViajando = {}
    for viagem in dicionarioViagens.values():
        for veiculo in dicionarioVeiculos.values():
            if viagem['veiculo'] == veiculo and viagem['status'] == True:
                veiculosViajando[veiculo['placa']] = veiculo
    return veiculosViajando


def separarVeiculosDisponiveis():
    veiculos = pegarVeiculos()
    viagens = lerDadosJson()
    veiculosDisponiveis = {}
    for veiculo in veiculos.values():
        contador = 0
        for viagem in viagens.values():
            if viagem['veiculo'] != veiculo or (viagem['veiculo'] == veiculo and viagem['status'] == False):
                contador += 1
                if contador == len(viagens):
                    veiculosDisponiveis[veiculo['placa']] = veiculo
                    contador = 0
    return veiculosDisponiveis


def finalizarViagem(placa):
    dicionarioViagens = lerDadosJson()
    for viagem in dicionarioViagens.values():
        if viagem['veiculo']['placa'] == placa and viagem['status'] == True:
            viagem['status'] = False
            dicionarioViagens[viagem['id']] = viagem
            gravarDados(dicionarioViagens)
            return True
    return False


def viagensAtivas():
    dicionarioViagens = lerDadosJson()
    viagensAtivas = {}
    for viagem in dicionarioViagens.values():
        if viagem['status'] == True:
            viagensAtivas[viagem['id']] = viagem
    return viagensAtivas


def viagensEntrePeriodo(data1, data2):
    dicionarioViagens = lerDadosJson()
    viagensEntrePeriodo = {}
    for viagem in dicionarioViagens.values():
        dataViagem = datetime.strptime(viagem["data"], '%d/%m/%Y').date()
        if dataViagem > data1 and dataViagem < data2:
            viagensEntrePeriodo[viagem['id']] = viagem
    return viagensEntrePeriodo
