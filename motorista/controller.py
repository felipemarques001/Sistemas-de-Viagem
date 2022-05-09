import json


def gerarDicionarioMotoristas():
    with open('motorista/banco_motoristas.json', 'r+') as arqJson:
        dicionarioMotoristas = json.load(arqJson)
    return dicionarioMotoristas


def salvarDicionarioJson(dicionario):
    with open('motorista/banco_motoristas.json', 'w') as arqJson:
        json.dump(dicionario, arqJson, indent=3)


def verificarCPF(cpf):
    dicionarioMotoristas = gerarDicionarioMotoristas()
    for motorista in dicionarioMotoristas.values():
        if motorista.get('cpf') == cpf:
            return True
    return False


def removerMotoristaPorCpf(cpf, dicionarioMotoristas):
    igual = verificarCPF(cpf)
    if igual == True:
        del dicionarioMotoristas[str(cpf)]
        salvarDicionarioJson(dicionarioMotoristas)
        print('Motorista excluído com sucesso!')
    else:
        print('\033[31mNenhum motorista com este CPF encontrado!\033[m')


def removerTodosOsMotoristas(dicionarioMotoristas):
    dicionarioMotoristas.clear()
    salvarDicionarioJson(dicionarioMotoristas)
    print('Motoristas excluídos com sucesso!')


def buscarMotoristaPorCpf(dicionario, cpf):
    motoristaEncontrado = {}
    for motorista in dicionario.values():
        if motorista['cpf'] == cpf:
            motoristaEncontrado = motorista
    return motoristaEncontrado