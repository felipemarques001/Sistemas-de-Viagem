from motorista import controller


def cadastrarMotorista():
    dicionarioMotoristas = controller.gerarDicionarioMotoristas()
    print('\n\033[1;32m-----------CADASTRAR MOTORISTAS---------\033[m')
    cpf = criarCPF()
    nome = input("Digite o nome do motorista: ")
    carteira = selecionarCarteira()
    dicionarioMotoristas[cpf] = {
        'cpf': cpf,
        'nome': nome,
        'carteira': carteira
    }
    controller.salvarDicionarioJson(dicionarioMotoristas)
    print('\033[1;32mMotorista cadastrado com sucesso!\033[m')

    print('Deseja cadastar outro motorista? ')
    print('\033[31m[1]\033[m - Sim')
    print('\033[31m[2]\033[m - Não')
    cadastrarOutoMotorista = int(input())
    if cadastrarOutoMotorista == 1:
        cadastrarMotorista()


def criarCPF():
    while True:
        cpf = int(input("Digite o CPF do motorista (sem sinais): "))
        igual = controller.verificarCPF(cpf)
        if igual == False:
            break
        else:
            print('\033[1;31mCPF já cadastrado!\033[m')
    return cpf


def selecionarCarteira():  # Essa função também será usado quando vamos listar um motorista por o seu tipo de
    # habilitação
    carteira = ""
    while True:
        print('\033[31m[1]\033[m - Carteira tipo A')
        print('\033[31m[2]\033[m - Carteira tipo B')
        print('\033[31m[3]\033[m - Carteira tipo AB')
        escolhaCarteira = int(input("DIGITE UMA DAS OPÇÕES>>> "))

        if escolhaCarteira == 1:
            carteira = "A"
            break
        elif escolhaCarteira == 2:
            carteira = "B"
            break
        elif escolhaCarteira == 3:
            carteira = "AB"
            break
        else:
            print("\033[31mEscolha inválida!\033[m")
    return carteira
