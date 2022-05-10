from veiculos import controller_veiculo as controller


def cadastrarveiculo():
    print('\n\033[1;32m-----------CADASTRAR VEÍCULO---------\033[m')
    placa = cadastrarPlaca()
    tipo = cadastrarTipo()
    motorista = None
    dicionarioVeiculos = controller.lerDadosJson()
    dicionarioVeiculos[placa] = {
        'placa': placa,
        'tipo': tipo,
        'motorista': motorista
    }
    controller.gravarDados(dicionarioVeiculos)
    print('\033[1;32mVeículo cadastrado com sucesso!\033[m')

    print('Deseja cadastar outro veículo? ')
    print('\033[31m[1]\033[m - Sim')
    print('\033[31m[2]\033[m - Não')
    op = int(input())
    if op == 1:
        cadastrarveiculo()


#Função para cadastrar a placa
def cadastrarPlaca():
    while True:
        placa = input('Digite a placa do veículo: ')
        placaCadastrada = controller.checarplaca(placa)
        if placaCadastrada == True:
            print('\033[1;31mEsta placa já está cadastrada!\033[m')
        else:
            return placa



# FUNÇAO QUE CHECA OS VALORES PARA CARRO E MOTO:
def cadastrarTipo():
    op = int(input('O VEICULO É:'
                   '\n [1] - Carro'
                   '\n [2] - Moto'
                   '\n >>> '))
    if op == 1:
        return 'Carro'
    elif op == 2:
        return 'Moto'
    else:
        print('Valor inválido!')
        return cadastrarTipo()