import json


def lerDadosJson():
    with open('veiculos/banco_veiculos.json', 'r+') as arqjson:
        dicionarioVeiculos = json.load(arqjson)
    return dicionarioVeiculos


def gravarDados(dicionario):
    with open('veiculos/banco_veiculos.json', 'w') as arqJson:
        json.dump(dicionario, arqJson, indent=3)


# CHECAR SE A PLACA EXISTE:
def checarplaca(placa):
    dicionarioVeiculos = lerDadosJson()
    for veiculo in dicionarioVeiculos.values():
        if veiculo.get('placa') == placa:
            return True
    return False


def buscarVeiculo(dicionario, placa):
    veiculoEncontrado = {}
    for veiculo in dicionario.values():
        if veiculo.get('placa') == placa:
            veiculoEncontrado = veiculo
    return veiculoEncontrado