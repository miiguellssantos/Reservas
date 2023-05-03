#
# FUNÇÕES AUXILIARES
#


#
# Função: pausar
#
# Espera o usuário teclar "ENTER" para continuar
# o programa

def pausa():
    input("Tecle <ENTER> para continuar...\n")
    
    
    
# Função: existe_arquivo
#
# Verifica se um certo arquivo existe no disco.
#
# Parâmetro: nome - string com o nome do arquivo
#
# Retorna: True ou False
#

def existe_arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False
