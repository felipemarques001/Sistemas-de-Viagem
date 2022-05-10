from motorista import buscar_motorista
from motorista import controller

def editarNomeMotorista():
    print('\n\033[1;33m↓ ↓ ↓ ↓ ↓ ↓ ↓ EDITAR MOTORISTA ↓ ↓ ↓ ↓ ↓ ↓ ↓\033[m')
    motorista = buscar_motorista.buscarMotorista() or {}
    if len(motorista) != 0:
        novoNome = input("Digite o novo nome do motorista: ")
        motorista['nome'] = novoNome
        salvarMotoristaAtualizado(motorista.get('cpf'), motorista)


def salvarMotoristaAtualizado(cpf, motorista):
    dicionarioMotoristas = controller.gerarDicionarioMotoristas()
    dicionarioMotoristas[str(cpf)] = motorista
    controller.salvarDicionarioJson(dicionarioMotoristas)
    print('\033[1;32mNome do motorista atualizado com sucesso!\033[m')

