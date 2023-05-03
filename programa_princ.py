from clientes import *
from apartamentos import *
from reservas import *
from auxiliar import *

# Criando dicionarios para armazenamento de dados:

BDclientes = {}
BDaptos = {}
BDreservas = {}

# Carregando os dados dos arquivos nos dicionários:

recupera_clientes(BDclientes)
recupera_aptos(BDaptos)
recupera_reservas(BDreservas)

# Variável para receber a opção do menu escolhida:
opc = 0

# Enquanto o usuário não escolher a opção fim....
    
while ( opc != 5 ):

    # Exibe o menu:
        
    print("1 - Gerenciar Clientes")
    print("2 - Gerenciar Apartamentos")
    print("3 - Gerenciar Reservas")
    print("4 - Relatório")
    print("5 - Finalizar programa")

    # Recebe a opção do usuário:
    opc = int( input("Digite uma opção: ") )

    # Chama função, conforme opção escolhida:
        
    if opc == 1:
        menu_clientes(BDclientes)
        print("\n\n\n\n")
            
    elif opc == 2:
        menu_aptos(BDaptos)
        print("\n\n\n\n")
            
    elif opc == 3:
        menu_reservas(BDclientes, BDaptos, BDreservas)
        print("\n\n\n\n")

    elif opc == 4:
        X = int( input("Digite o ano inicial:") )
        Y = int( input("Digite o ano final:") )
        relatorio(BDclientes, BDaptos, BDreservas, X, Y)
        print("\n\n\n\n")
        

##fim do while

print("\n\n*** FIM DO PROGRAMA ***\n\n")
