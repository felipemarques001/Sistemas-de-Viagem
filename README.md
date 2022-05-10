# Sistemas-de-Viagem em Python
* Sistemas de viagem feito em Python para projeto prático na cadeira Introdução a Programação, na universidade UFRPE (Universidade Federal Rural de Pernambuco);
* A aplicação deve implementar o gerencimento de motoristas, veículos e viagens;
* A aplicação deve usar o conceito de modularização, ou seja, dividir as responsabilidades da aplicação a partir de módulos;
* Os veículos devem possuir motoristas aptos a conduzi-los, verificamos essa aptidão através do tipo de habilitação do motorista, esta habilitação poderá ser apenas A ou B ou AB;
* Usamos arquivos JSON para representar os bancos de dados de cada dicionário (motorista, veículo e viagem), cada banco de dados só poderá ser acessado pelo seu respectivo controlador;
* Veiculo será um dicionário com as chaves: placa, tipo e motorista:
* Motorista será um dicionário com as chaves: cpf, nome e carteira;
* Viagem será um dicionário com as chaves: id, veiculo, rota, status e data;
