from motorista import controller, cadastrar_motorista


def listarTodosMotoristas():
    print('\n\033[1;32m-----------LISTA DE MOTORISTAS---------\033[m')
    dicionarioMotoristas = controller.gerarDicionarioMotoristas()
    if len(dicionarioMotoristas) != 0:
        for motorista in dicionarioMotoristas.values():
            print(f'CPF: {motorista.get("cpf")}\n'
                  f'Nome: {motorista.get("nome")}\n'
                  f'Tipo de habilitação: {motorista.get("carteira")}')
            print('')
    else:
        print('\033[31mSem motoristas cadastrados!\033[m')


def listarMotoristaPorCarteira():
    print('\n\033[1;32m-----------LISTAR MOTORISTAS POR TIPO DE CARTEIRA---------\033[m')
    dicionarioMotoristas = controller.gerarDicionarioMotoristas()
    if len(dicionarioMotoristas) != 0:
        print('Selecione o tipo da habilitação')
        carteira = cadastrar_motorista.selecionarCarteira()
        contador = 0
        print(f'\033[1;33m-----------LISTA DE MOTORISTAS COM CARTEIRA {carteira}---------\033[m')
        for motorista in dicionarioMotoristas.values():
            if motorista['carteira'] == carteira:
                print(f'CPF: {motorista.get("cpf")}\n'
                      f'Nome: {motorista.get("nome")}\n'
                      f'Tipo de habilitação: {motorista.get("carteira")}')
                print('')
                contador += 1
        if contador == 0:
            print('\033[31mNenhum motorista encontrado com este tipo de carteira!\033[m')
    else:
        print('\033[31mSem motoristas cadastrados!\033[m')

