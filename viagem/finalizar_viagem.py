from viagem import controller_viagem

def finalizarViagem():
    print('\n\033[1;32m-----------FINALIZAR VIAGEM---------\033[m')
    viagens = controller_viagem.lerDadosJson()
    if len(viagens) != 0:
        placa = input('Digite a placa do veículo da viagem para finalizá-la: ')
        resposta = controller_viagem.finalizarViagem(placa)
        if resposta == True:
            print('\033[1;32mViagem finalizada com sucesso!\033[m')
        else:
            print('\033[1;31mValor da placa incorreto, viagem não encontrada!\033[m')
    else:
        print('\033[1;31mNenhuma viagem cadastrada!\033[m')
