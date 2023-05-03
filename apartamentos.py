#
# Funções para gerenciamento de APARTAMENTOS
#
# Formato do armazenamento (dicionário):
# - chave: string
# - valor: tupla, contendo vários dados
#
# [código] = (tipo [standard, luxo, superluxo], número de pessoas, valor da diária)
#
###################################################
from auxiliar import *

#
# Função: existe_apto
#
# Verifica se uma certa chave existe no dicionário.
#
# Parâmetros: dic -   o dicionário
#             chave - a chave a pesquisar
#
# Retorna: True ou False
#

def existe_apto(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False

####################################################


# Função: insere_apto (o C do CRUD)
#
# Recebe os dados de um apartamento, e insere no dicionário.
#
# Parâmetro: dic - o dicionário
#
# Não retorna nada, pois já insere os dados no dicionário.
#

def insere_apto(dic):

    # Recebe a sigla:
    codigo = input("Digite o código do apartamento:")

    # Verifica se já existe no dicionário:
    
    if existe_apto(dic,codigo):
        print("Apartamento já cadastrado!")
        pausa()
        
    else:

        # A chave não existe.
        # Receber os demais dados do apartamento:

        tipo = input("Digite o tipo de apartamento (standard, luxo, superluxo): ").upper()
        numero_p = input("Digite a quantidade de pessoas: ")
        valor = input("Digite o valor da diária: ")
        
        
            
        # Insere os dados do apartamento no dicionário.
        # chave: código
        # valor: tupla com tipo, qtd de pessoas e valor da diária
        dic[codigo]=(tipo, numero_p, valor)

        print("Dados inseridos com sucesso!")
        pausa()

####################################################################

#
# Função: mostra_apto (o R do CRUD)
#
# Exibe os dados de um apartamento, a partir do código informado.
#
# Parâmetros: dic   - o dicionário
#             chave - a chave (código) que se quer exibir os dados
#
# Não retorna nada, pois apenas exibe dados.
#

def mostra_apto(dic,chave):

    # Verifica se a chave informada existe no dicionário:
    
    if existe_apto(dic,chave):
        
        # Recupera a tupla com os dados relativos a chave informada:
        dados = dic[chave]

        # Exibindo os dados da tupla recuperada.
        # Lembrando, o acesso a dados dentro da tupla
        # é feito da mesma forma que numa lista.
        
        print(f"Tipo: {dados[0]}")
        print(f"Número de Pessoas: {dados[1]}")
        print(f"Valor da diária: {dados[2]}")
        
    else:

        # A chave informada não existe!!
        print("Apartamento não cadastrado!")

######################################################################

#
# Função: altera_apto (o U do CRUD)
#
# Permite alteração dos dados de um apartamento, a partir do código informado.
#
# Parâmetros: dic   - o dicionário
#             chave - a chave (código) que se quer alterar os dados
#
# Não retorna nada, pois os dados são alterados
# diretamente no dicionário
#


def altera_apto(dic,chave):

    # Verifica se a chave informada existe no dicionário:
    
    if existe_apto(dic,chave):

        # Exibe os dados relativos a essa chave:    
        mostra_apto(dic,chave)

        # Pede confirmação para permitir alteração:
        confirma = input("Tem certeza que deseja alterar? (S/N): ").upper()
        
        if confirma == 'S':

            # Recebe os novos dados desse apartamento:

            tipo = input("Digite o tipo de apartamento (standard, luxo, superluxo): ").upper()
            numero_p = input("Digite a quantidade de pessoas: ")
            valor = input("Digite a valor da diária: ")

            # Troca os dados do apartamento no dicionário, nesta sigla:
            dic[chave]=(tipo, numero_p, valor)
            
            print("Dados alterados com sucesso!")
            pausa()
            
        else:
            # Usuário desistiu de alterar dados:
            print("Alteração cancelada!")
            pausa()

    else:

        # O código informado não existe!
        print("Apartamento não cadastrado!")
        pausa()

#########################################################################

#########################################################################


#
# Função: remove_apto (o D do CRUD)
#
# Permite exclusão dos dados de um apartamento, a partir do código informado.
#
# Parâmetros: dic   - o dicionário
#             chave - a chave (código) que se quer apagar os dados
#
# Não retorna nada, pois os dados são apagados
# diretamente no dicionário
#

def remove_apto(dic,chave):
    
    # Verifica se a chave informada existe no dicionário:
    
    if existe_apto(dic,chave):

        # Exibe os dados relativos a essa chave:    
        mostra_apto(dic,chave)

        # Pede confirmação para permitir alteração:
        confirma = input("Tem certeza que deseja apagar? (S/N): ").upper()
        
        if confirma == 'S':

            # Apaga esta chave no dicionário:
            del dic[chave]
       
            print("Dados apagados com sucesso!")
            pausa()
            
        else:

            # Usuário desistiu de apagar dados:
            print("Exclusão cancelada!")
            pausa()

    else:

        # O código informada não existe!
        print("Apartamento não cadastrado!")
        pausa()

#########################################################################

# Função: mostra_todos_aptos
#
# Exibe todos os dados do dicionário, no formato de tabela.
#
# Parâmetro: dic - o dicionário
#
# Não retorna nada, pois apenas exibe os dados.
#

def mostra_todos_aptos(dic):

    # Exibe cabecalho do relatório:
    print("Relatório: Todos os apartamentos\n")
    print("CÓDIGO - TIPO - QUANTIDADE DE PESSOAS - VALOR DA DIÁRIA\n")
    
    # Vamos percorrer todas as chaves no dicionário:

    for codigo in dic:

        # Pega a tupla com dados dessa sigla:
        tupla = dic[codigo]


        # Monta string com dados:
        linha = codigo + " - " + tupla[0] + " - " + tupla[1] + " - " + tupla[2] + "\n"

        # Exibe a string:
        print(linha)

    ##fim do for

    print("")
    pausa()

############################################################################


# Função: grava_aptos
#
# Grava os dados do dicionário no arquivo "aptos.txt".
#
# Parâmetro: dic - o dicionário
#
# Não retorna nada, pois apenas grava os dados no arquivo.
#

def grava_aptos(dic):

    # Abre o arquivo para gravação:
    arq = open("aptos.txt", "w")

    # Percorrer todas os códigos no dicionário:
    
    for codigo in dic:

        # Pega a tupla com dados dessa sigla:
        tupla = dic[codigo]

        # Monta linha para gravação:
        linha = codigo + ";" + tupla[0] + ";" + tupla[1] + ";" + tupla[2] + "\n"

        # Grava no arquivo:
        arq.write(linha)

    ##fim do for

    # Fecha o arquivo:
    arq.close()

###########################################################################

#Função: recupera_aptos
#
# Se o arquivo "aptos.txt" existir, lê os dados para dentro do dicionário.
#
# Parâmetro: dic - o dicionário
#
# Não retorna nada, pois lê os dados diretamente do arquivo.
#
    
def recupera_aptos(dic):

    # Verificando se o arquivo existe:
    if ( existe_arquivo("aptos.txt") ):

        # Existe! Abrindo arquivo para leitura:
        arq = open("aptos.txt", "r")

        # Percorrendo as linhas do arquivo:
        for linha in arq:

            # a linha é:
            # codigo, tipo, qtd de pessoas e valor.

            # Tirando o \n do final:
            linha = linha[:len(linha)-1]
            
            # Vamos quebrar por ;
            lista = linha.split(";")

            # codigo esta em lista[0]
            # tipo está em lista[1]
            # qtd está em lista[2]
            # valor está em lista[3]
            
            codigo = lista[0]
            tipo = lista[1]
            qtd = lista[2]
            valor = lista[3]

            # Colocando os dados no dicionario:
            dic[codigo] = (tipo, qtd, valor)

        ##fim do for

    ## Não teremos "else", porque se o arquivo não existir,
    ## não precisamos fazer nada, o dicionário já está vazio mesmo...

############################################################################

#
# Função: menu_aptos
#
# Gerencia todo o armazenamento (CRUD) dos dados dos apartamentos,
# incluindo leitura/gravação em arquivo.
#
# Parâmetro: dic_aptos - o dicionário
#
# Não retorna nada, pois gerencia diretamente o dicionário.
#

def menu_aptos(dic_aptos):

    # Variável para receber a opção do menu escolhida:
    opc = 0

    # Enquanto o usuário não escolher a opção fim....
    
    while ( opc != 6 ):

        # Exibe o menu:
        print("\nGerenciamento de apartamentos\n")
        print("1 - Insere Apartamento")
        print("2 - Altera Apartamento")
        print("3 - Remove Apartamento")
        print("4 - Mostra um Apartamento")
        print("5 - Mostra todos os Apartamentos")
        print("6 - Sair do menu de Apartamentos")

        # Recebe a opção do usuário:
        opc = int( input("Digite uma opção: ") )

        # Chama função, conforme opção escolhida:
        
        if opc == 1:
            insere_apto(dic_aptos)
            
        elif opc == 2:
            codigo = input("Sigla do apto. a ser alterado: ")
            altera_apto(dic_aptos, codigo)
            
        elif opc == 3:
            codigo=input("Sigla do apto. a ser removido: ")
            remove_apto(dic_aptos, codigo)
            
        elif opc == 4:
            codigo=input("Sigla do apto. a ser consultado: ")
            mostra_apto(dic_aptos, codigo)
            pausa()
            
        elif opc == 5:
            mostra_todos_aptos(dic_aptos)
            
        elif opc == 6:
            # Se escolheu sair, grava os dados no arquivo.
            grava_aptos(dic_aptos)

    ##fim do while

##################################################################