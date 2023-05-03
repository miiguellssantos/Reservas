#
# Funções para gerenciamento de RESERVAS
#
# Formato do armazenamento (dicionário):
# - chave: tupla, contendo o CPF da pessoa e o código do apartamento
# - valor: tupla, contendo a data de entrada, saída e os ocupantes
#
# [ (CPF, codigo) ] = (entrada, saida, ocupantes)
#
###################################################



from auxiliar import *
from clientes import *
from apartamentos import *



#
# Função: existe_reserva
#
# Verifica se uma certa chave existe no dicionário.
#
# Parâmetros: dic -   o dicionário
#             chave - a chave a pesquisar
#
# Retorna: True ou False
#

def existe_reserva(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False

#
# Função: Ocupante existente
# Verifica se já existe o ocupante na lista.

def existe_ocupante(nome, lista):
    if nome in lista:
        return True
    else:
        return False
    
    

####################################################

####################################################


#
# Função: insere_reserva (o C do CRUD)
#
# Recebe os dados de uma reserva, e insere no dicionário.
#
# Parâmetros: dicC - o dicionário de clientes
#             dicA - o dicionário de apartamentos
#             dicR - o dicionário de reservas
#
# Não retorna nada, pois já insere os dados no dicionário.
#

def insere_reserva(dicC, dicA, dicR):

    # Recebe o CPF:
    CPF = input("Digite o CPF:")

    # Verifica se existe este CPF:
    
    if existe_clientes(dicC,CPF):

        # OK, a pessoa existe.

        # Recebe o código do apartamento:
        codigo = input("Digite o código do apartamento:")
        
        # Verifica se existe este apartamento:
        if existe_apto(dicA, codigo):

            # OK, o apartamento existe.

            # Montando a tupla que vai ser a chave (com cpf e código):
            chave = (CPF, codigo)

            # Verificando se esta reserva já existe:
            if ( existe_reserva(dicR, chave) ):

                # Ja existe!
                print("Esta reserva já existe!")
                pausa()

            else:

                # Não existe ainda.

                # Recebendo os demais dados:
                entrada = input("Digite a data de entrada (DD MM AAAA (ESPAÇADO)):")
                saida = input("Digite a data de saida (DD MM AAAA (ESPAÇADO)):")
                ocupantes = []
                o = int(input("Confirme a quantidade de ocupantes: "))
                for i in range (o):
                    nome = input(f"Digite o nome do {i+1}o ocupante: ")
                    if existe_ocupante(nome, ocupantes):
                        print("Ocupante já existente!")
                        nome = input(f"Digite o nome do {i+1}o ocupante: ")
                    else:
                        ocupantes.append(nome)


                # Montando a tupla que vai ser o valor associado a chave:
                valor = (entrada, saida, ocupantes)

                # Cria essa lotação no dicionário:
                dicR[ chave ] = valor

                print("Dados inseridos com sucesso!")
                pausa()

        else:

            # O apartamento digitado não existe!
            print("Este apartamento não existe!")
            pausa()

    else:

        # O CPF digitado não existe!
        print("Este CPF não existe!")
        pausa()

####################################################################

def relatorio(dicC, dicA, dicR, X, Y):

    # Exibe cabecalho do relatório:
    print("Relatório: Reservas com ano entre", X, " e ", Y)
    print("---------------------------------------------\n")
    
    # Vamos percorrer todas as chaves no dicionário:

    for chave in dicR:

        # Pega o valor referente a esta chave:
        valor = dicR[chave]

        # O ano de ingresso é o elemento valor[0].
        ano = valor[1].split()
        saida = int(ano[2])

        # Verifica se o ano de ingresso está entre X e Y:

        if ( saida >= X and saida <= Y ):

            # Esta lotação está nos limites pedidos.
            # Exibe os dados.

            # Pega os dados dessa chave:
            cpf = chave[0]
            codigo = chave[1]

            # Exibe os dados da lotação:
            mostra_reserva(dicC, dicA, dicR, cpf, codigo)

            print("----------------------------\n")

        ##fim do if, se não se enquadra nos limites, não faz nada!

    ##fim do for

    print("")
    pausa()

############################################################################

####################################################################

#
# Função: mostra_reserva (o R do CRUD)
#
# Exibe os dados de uma reserva, a partir do CPF e do código informados.
#
# Parâmetros: dicC  - o dicionário de clientes
#             dicA  - o dicionário de apartamentos
#             dicR  - o dicionário de reservas
#             cpf   - o CPF da reserva
#             codigo - a sigla do apartamento
#
# Não retorna nada, pois apenas exibe dados.
#

def mostra_reserva(dicC, dicA, dicR, cpf, codigo):

    # Montando uma tupla com o cpf e o código:
    chave = (cpf, codigo)

    # Verifica se a chave informada existe no dicionário:
    
    if existe_reserva(dicR,chave):
        
        # Recupera a tupla com os dados relativos a chave informada:
        dados = dicR[chave]

        print("Dados da lotação:")
        print("-----------------\n")

        # Mostrando os dados da pessoa:
        print("Pessoa:")
        print("-------")
        mostra_clientes(dicC, cpf)
        print()

        # Mostrando os dados do apartamento:
        print("Apartamento:")
        print("-------------")
        mostra_apto(dicA, codigo)
        print()

        # Exibindo os dados da reserva:
        print(f"Data de Entrada {dados[0]}")
        print(f"Data de Saída: {dados[1]}")
        print(f"Nome dos Ocupantes: {dados[2]}")
        
    else:

        # A chave informada não existe!!
        print("A reserva informada não existe")

######################################################################

#
# Função: altera_reserva (o U do CRUD)
#
# Permite alteração dos dados de uma reserva, a partir do CPF/código informados.
#
# Parâmetros: dicC  - o dicionário de clientes
#             dicA  - o dicionário de apartamentos
#             dicR  - o dicionário de reservas
#             cpf   - o CPF da reserva
#             código - o código do apartamento
#
# Não retorna nada, pois os dados são alterados
# diretamente no dicionário
#


def altera_reserva(dicC, dicA, dicR, cpf, codigo):

    # Montando uma tupla(chave) com cpf e código:
    chave = (cpf, codigo)

    # Verifica se a chave informada existe no dicionário:
    if existe_reserva(dicR, chave):

        # Exibe os dados relativos a essa chave:    
        mostra_reserva(dicC, dicA, dicR, cpf, codigo)

        # Pede confirmação para permitir alteração:
        confirma = input("Tem certeza que deseja alterá-la? (S/N): ").upper()
        
        if confirma == 'S':

            # Recebe os novos dados dessa lotacao:
            entrada = input("Digite a data de entrada (DD MM AAAA (ESPAÇADO)):")
            saida = input("Digite a data de saída (DD MM AAAA ESPAÇADO):")
            ocupantes = []
            o = int(input("Confirme a quantidade de ocupantes: "))
            for i in range (o):
                nome = input(f"Digite o nome do {i+1}o ocupante: ")
                if existe_ocupante(nome, ocupantes):
                    print("Ocupante já existente!")
                    nome = input(f"Digite o nome do {i+1}o ocupante: ")
                else:
                    ocupantes.append(nome)

            # Montando a tupla que vai ser o valor associado a chave:
            valor = (entrada, saida, ocupantes)

            # Troca os dados no dicionário:
            dicR[ chave ] = valor
            
            print("Dados alterados com sucesso!")
            pausa()
            
        else:

            # Usuário desistiu de alterar dados:
            print("Alteração cancelada!")
            pausa()

    else:

        # A reserva informada não existe!
        print("Esta reserva não está cadastrada!")
        pausa()

#########################################################################

#
# Função: remove_reserva (o D do CRUD)
#
# Permite exclusão dos dados de uma reserva, a partir do CPF informado.
#
# Parâmetros: dicC  - o dicionário de clientes
#             dicA  - o dicionário de apartamentos
#             dicR  - o dicionário de reservas
#             cpf   - o CPF da lotação
#             código - o código do apartamento
#
# Não retorna nada, pois os dados são apagados
# diretamente no dicionário
#

def remove_reserva(dicC, dicA, dicR, cpf, codigo):

    # Montando uma tupla(chave) com cpf e sigla:
    chave = (cpf, codigo)    
    
    # Verifica se a chave informada existe no dicionário:
    
    if existe_reserva(dicR,chave):

        # Exibe os dados relativos a essa lotacao:
        mostra_reserva(dicC, dicA, dicR, cpf, codigo)

        # Pede confirmação para permitir alteração:
        confirma = input("Tem certeza que deseja apagar? (S/N): ").upper()
        
        if confirma == 'S':

            # Apaga esta chave no dicionário:
            del dicR[chave]
       
            print("Dados apagados com sucesso!")
            pausa()
            
        else:

            # Usuário desistiu de apagar dados:
            print("Exclusão cancelada!")
            pausa()

    else:

        # A reserva informada não existe!
        print("Esta reserva não está cadastrada!")
        pausa()

#########################################################################

# Função: mostra_todas_reservas
#
# Exibe todas as reservas.
#
# Parâmetros: dicC  - o dicionário de clientes
#             dicA  - o dicionário de apartamentos
#             dicR  - o dicionário de reservas
#
# Não retorna nada, pois apenas exibe os dados.
#

def mostra_todas_reservas(dicC, dicA, dicR):

    # Exibe cabecalho do relatório:
    print("Relatório: Todas as reservas")
    print("----------------------------\n")
    
    # Vamos percorrer todas as chaves no dicionário:

    for chave in dicR:

        # Pega os dados dessa chave:
        cpf = chave[0]
        codigo = chave[1]

        # Exibe os dados da lotação:
        mostra_reserva(dicC, dicA, dicR, cpf, codigo)

        print("----------------------------\n")

    ##fim do for

    print("")
    pausa()

############################################################################

#
# Função: grava_reservas
#
# Grava os dados do dicionário no arquivo "reservas.txt".
#
# Parâmetro: dic - o dicionário de reservas
#
# Não retorna nada, pois apenas grava os dados no arquivo.
#

def grava_reserva(dic):

    # Abre o arquivo para gravação:
    arq = open("reservas.txt", "w")

    # Percorrer todas as loteçeõs no dicionário:
    
    for chave in dic:

        # Pega os dados dessa chave:
        cpf = chave[0]
        codigo = chave[1]

        # Pega a tupla com dados dessa chave:
        tupla = dic[chave]

        # Pega os dados dessa tupla:
        entrada =  tupla[0]
        saida = tupla[1]
        ocupantes = tupla[2]

        # Monta linha com dados, para gravação:
        linha = cpf+";"+codigo+";"+entrada+";"+saida+";"+str(ocupantes)+"\n"

        # Grava no arquivo:
        arq.write(linha)

    ##fim do for

    # Fecha o arquivo:
    arq.close()

###########################################################################

#
# Função: recupera_reservas
#
# Se o arquivo "reservas.txt" existir, lê os dados para dentro do dicionário.
#
# Parâmetro: dic - o dicionário
#
# Não retorna nada, pois lê os dados diretamente do arquivo.
#
    
def recupera_reservas(dic):

    # Verificando se o arquivo existe:
    if ( existe_arquivo("reservas.txt") ):

        # Existe! Abrindo arquivo para leitura:
        arq = open("reservas.txt", "r")

        # Percorrendo as linhas do arquivo:
        for linha in arq:

            # a linha é:
            # cpf;codigo;entrada;saida;ocupantes
            
            # Tirando o \n do final:
            linha = linha[:len(linha)-1]

            # Vamos quebrar por ;
            lista = linha.split(";")

            # cpf esta em lista[0]
            # sigla está em lista[1]
            # entrada está em lista[2]
            # saida está em lista[3]
            # ocupantes está em lista[4]
            cpf = lista[0]
            codigo = lista[1]
            entrada = lista[2]
            saida = lista[3]
            ocupantes = lista[4]

            # Gerando chave com cpf e sigla:
            chave = (cpf, codigo)

            # Colocando os dados no dicionario:
            dic[chave] = (entrada, saida, ocupantes)

        ##fim do for

    ## Não teremos "else", porque se o arquivo não existir,
    ## não precisamos fazer nada, o dicionário já está vazio mesmo...

############################################################################

#
# Função: menu_reservas
#
# Gerencia todo o armazenamento (CRUD) dos dados das reservas,
# incluindo leitura/gravação em arquivo.
#
# Parâmetros: dicC  - o dicionário de clientes
#             dicA  - o dicionário de apartamentos
#             dicR  - o dicionário de reservas
#
# Não retorna nada, pois gerencia diretamente o dicionário.
#

def menu_reservas(dicC, dicA, dicR):

    # Variável para receber a opção do menu escolhida:
    opc = 0

    # Enquanto o usuário não escolher a opção fim....
    
    while ( opc != 6 ):

        # Exibe o menu:
        print("\nGerenciamento de reservas\n")
        print("1 - Insere uma Reserva")
        print("2 - Altera uma Reserva")
        print("3 - Remove uma Reserva")
        print("4 - Mostra uma Reserva")
        print("5 - Mostra todas as Reservas")
        print("6 - Sair do menu de Reservas")

        # Recebe a opção do usuário:
        opc = int( input("Digite uma opção: ") )

        # Chama função, conforme opção escolhida:
        
        if opc == 1:
            insere_reserva(dicC, dicA, dicR)
            
        elif opc == 2:
            print("Alterar reserva:")
            cpf = input("Digite o CPF: ")
            codigo = input("Digite o código do apto.")
            altera_reserva(dicC, dicA, dicR, cpf, codigo)
            
        elif opc == 3:
            print("Remover reserva:")
            cpf = input("Digite o CPF: ")
            codigo = input("Digite o código do apto.")
            remove_reserva(dicC, dicA, dicR, cpf, codigo)
            
        elif opc == 4:
            print("Consultar reserva:")
            cpf = input("Digite o CPF: ")
            codigo = input("Digite o código do apto.")
            mostra_reserva(dicC, dicA, dicR, cpf, codigo)
            pausa()
            
        elif opc == 5:
            mostra_todas_reservas(dicC, dicA, dicR)
            
        elif opc == 6:
            # Se escolheu sair, grava os dados no arquivo.
            grava_reserva(dicR)

    ##fim do while

##################################################################