#
# Funções para gerenciamento de CLIENTES
#
# Formato do armazenamento (dicionário):
# - chave: string
# - valor: tupla, contendo vários dados
#
# [CPF] = (nome, endereço, cidade, telefone, datanasc)
#
###################################################



from auxiliar import *



#
# Função: existe_clientes
#
# Verifica se uma certa chave existe no dicionário.
#
# Parâmetros: dic -   o dicionário
#             chave - a chave a pesquisar
#
# Retorna: True ou False
#

def existe_clientes(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False

####################################################


#
# Função: insere_clientes (o C do CRUD)
#
# Recebe os dados de uma pessoa, e insere no dicionário.
#
# Parâmetro: dic - o dicionário
#
# Não retorna nada, pois já insere os dados no dicionário.
#

def insere_clientes(dic):

    # Recebe o CPF:
    CPF = input("Digite o CPF:")

    # Verifica se já existe no dicionário:
    
    if existe_clientes(dic,CPF):
        print("Pessoa já cadastrada!")
        pausa()
        
    else:

        # A chave não existe.
        # Receber os demais dados da pessoa:
        
        nome = input("Digite o nome: ")
        endereco = input("Digite o endereço: ")
        cidade= input("Digite o nome da cidade que mora:")
        telefone= int(input("Digite seu telefone (SEM ESPAÇOS!):"))
        datanasc = input("Digite a data de nasc. (DD/MM/AAAA): ")
        

        # Insere os dados da pessoa no dicionário.
        # chave: CPF
        # valor: tupla com nome, endereco, datanasc e salario
        dic[CPF]=(nome, endereco, cidade, telefone, datanasc)

        print("Dados inseridos com sucesso!")
        pausa()

####################################################################


#
# Função: mostra_clientes (o R do CRUD)
#
# Exibe os dados de uma pessoa, a partir do CPF informado.
#
# Parâmetros: dic   - o dicionário
#             chave - a chave (CPF) que se quer exibir os dados
#
# Não retorna nada, pois apenas exibe dados.
#

def mostra_clientes(dic,chave):

    # Verifica se a chave informada existe no dicionário:
    
    if existe_clientes(dic,chave):
        
        # Recupera a tupla com os dados relativos a chave informada:
        dados = dic[chave]

        # Exibindo os dados da tupla recuperada.
        # Lembrando, o acesso a dados dentro da tupla
        # é feito da mesma forma que numa lista.
        
        print(f"Nome: {dados[0]}")
        print(f"Endereço: {dados[1]}")
        print(f"Cidade: {dados[2]}")
        print(f"Telefone: {dados[3]}")
        print(f"Data de Nascimento: {dados[4]}")
        
    else:

        # A chave informada não existe!!
        print("Cliente não cadastrado no sistema!")

######################################################################


#
# Função: altera_clientes (o U do CRUD)
#
# Permite alteração dos dados de uma pessoa, a partir do CPF informado.
#
# Parâmetros: dic   - o dicionário
#             chave - a chave (CPF) que se quer alterar os dados
#
# Não retorna nada, pois os dados são alterados
# diretamente no dicionário
#


def altera_clientes(dic,chave):

    # Verifica se a chave informada existe no dicionário:
    
    if existe_clientes(dic,chave):

        # Exibe os dados relativos a essa chave:    
        mostra_clientes(dic,chave)

        # Pede confirmação para permitir alteração:
        confirma = input("Tem certeza que deseja alterá-la? (S/N): ").upper()
        
        if confirma == 'S':

            # Recebe os novos dados dessa pessoa:
            nome = input("Digite o nome: ")
            endereco = input("Digite o endereço: ")
            cidade= input("Digite o nome da cidade que mora:")
            telefone= int(input("Digite seu telefone:"))
            datanasc = input("Digite a data de nasc. (DD/MM/AAAA): ")
        
            # Troca os dados no dicionário, neste CPF:
            dic[chave]= (nome, endereco, cidade, telefone, datanasc)
            
            print("Dados alterados com sucesso!")
            pausa()
            
        else:

            # Usuário desistiu de alterar dados:
            print("Alteração cancelada!")
            pausa()

    else:

        # O CPF informado não existe!
        print("Cliente não cadastrada!")
        pausa()

#########################################################################


#
# Função: remove_clientes (o D do CRUD)
#
# Permite exclusão dos dados de uma pessoa, a partir do CPF informado.
#
# Parâmetros: dic   - o dicionário
#             chave - a chave (CPF) que se quer apagar os dados
#
# Não retorna nada, pois os dados são apagados
# diretamente no dicionário
#

def remove_clientes(dic,chave):
    
    # Verifica se a chave informada existe no dicionário:
    
    if existe_clientes(dic,chave):

        # Exibe os dados relativos a essa chave:    
        mostra_clientes(dic,chave)

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

        # O CPF informado não existe!
        print("Cliente não cadastrada!")
        pausa()

#########################################################################


#
# Função: mostra_todas_clientes
#
# Exibe todos os dados do dicionário, no formato de tabela.
#
# Parâmetro: dic - o dicionário
#
# Não retorna nada, pois apenas exibe os dados.
#

def mostra_todas_clientes(dic):

    # Exibe cabecalho do relatório:
    print("Relatório: Todos os clientes\n")
    print("CPF - Nome - Endereço - Cidade - Telefone - Dt.Nascimento\n")
    
    # Vamos percorrer todas as chaves no dicionário:

    for CPF in dic:

        # Pega a tupla com dados desse CPF:
        tupla = dic[CPF]

        # Monta string com dados:
        linha = CPF + " - " + tupla[0] + " - " + tupla[1] + " - " + tupla[2] + " - " + str(tupla[3]) + " - " + tupla[4]

        # Exibe a string:
        print(linha)

    ##fim do for

    print("")
    pausa()

############################################################################


#
# Função: grava_clientes
#
# Grava os dados do dicionário no arquivo "clientes.txt".
#
# Parâmetro: dic - o dicionário
#
# Não retorna nada, pois apenas grava os dados no arquivo.
#

def grava_clientes(dic):

    # Abre o arquivo para gravação:
    arq = open("clientes.txt", "w")

    # Percorrer todos os CPFs no dicionário:
    
    for CPF in dic:

        # Pega a tupla com dados desse CPF:
        tupla = dic[CPF]

        # Monta linha com dados, para gravação:
        linha = CPF+";"+tupla[0]+";"+tupla[1]+";"+tupla[2]+";"+str(tupla[3])+";"+tupla[4]+"\n"

        # Grava no arquivo:
        arq.write(linha)

    ##fim do for

    # Fecha o arquivo:
    arq.close()

###########################################################################


#
# Função: recupera_clientes
#
# Se o arquivo "pessoas.txt" existir, lê os dados para dentro do dicionário.
#
# Parâmetro: dic - o dicionário
#
# Não retorna nada, pois lê os dados diretamente do arquivo.
#
    
def recupera_clientes(dic):

    # Verificando se o arquivo existe:
    if ( existe_arquivo("clientes.txt") ):

        # Existe! Abrindo arquivo para leitura:
        arq = open("clientes.txt", "r")

        # Percorrendo as linhas do arquivo:
        for linha in arq:

            # a linha é:
            # cpf;nome;endeço;cidade;telefone;datanasc
            
            # Tirando o \n do final:
            linha = linha[:len(linha)-1]

            # Vamos quebrar por ;
            lista = linha.split(";")

            # cpf esta em lista[0]
            # nome está em lista[1]
            # endereço está em lista[2]
            # cidade está em lista[3]
            # telefone esta em lista[4]
            # datanasc está em lista[5]
            cpf = lista[0]
            nome = lista[1]
            end = lista[2]
            cidade = lista[3]
            telefone = float( lista[4] )
            datanasc = lista[5]

            # Colocando os dados no dicionario:
            dic[cpf] = (nome, end, cidade, telefone, datanasc)

        ##fim do for

    ## Não teremos "else", porque se o arquivo não existir,
    ## não precisamos fazer nada, o dicionário já está vazio mesmo...

############################################################################


#
# Função: menu_pessoas
#
# Gerencia todo o armazenamento (CRUD) dos dados das pessoas,
# incluindo leitura/gravação em arquivo.
#
# Parâmetro: dic_pessoas - o dicionário
#
# Não retorna nada, pois gerencia diretamente o dicionário.
#

def menu_clientes(dic_clientes):

    # Variável para receber a opção do menu escolhida:
    opc = 0

    # Enquanto o usuário não escolher a opção fim....
    
    while ( opc != 6 ):

        # Exibe o menu:
        print("\nGerenciamento de Clientes:\n")
        print("1 - Inserir Cliente")
        print("2 - Alterar Cliente")
        print("3 - Remover Cliente")
        print("4 - Mostra um Cliente")
        print("5 - Mostrar todos os Clientes")
        print("6 - Sair do menu de Clientes")

        # Recebe a opção do usuário:
        opc = int( input("Digite uma opção: ") )

        # Chama função, conforme opção escolhida:
        
        if opc == 1:
            insere_clientes(dic_clientes)
            
        elif opc == 2:
            CPF = input("CPF a ser alterado: ")
            altera_clientes(dic_clientes, CPF)
            
        elif opc == 3:
            CPF=input("CPF a ser removido: ")
            remove_clientes(dic_clientes, CPF)
            
        elif opc == 4:
            CPF=input("CPF a ser consultado: ")
            mostra_clientes(dic_clientes, CPF)
            pausa()
            
        elif opc == 5:
            mostra_todas_clientes(dic_clientes)
            
        elif opc == 6:
            # Se escolheu sair, grava os dados no arquivo.
            grava_clientes(dic_clientes)

    ##fim do while

##################################################################
        

