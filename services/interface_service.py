from models.pais import Pais
from os import system

def limpa():
    system("cls")

def exibir_paises(paises: list[Pais]):
    """
    Função com objetivo de exibir os países
    solicitados pelo usuário nas opções 3 e 4 ddo menu de maneira organizada
    """
    if not paises:
        print("Nenhum país cadastrado.")
        return

    
    for pais in paises:
        print("ID: ", pais.id)
        print("Nome Comum: ", pais.nome_comum)
        print("Nome Oficial: ", pais.nome_oficial)
        print("Capital: ", pais.capital)
        print("População: ", pais.populacao)
        print("Gentílico: ", pais.gentilico)
        print("Língua Oficial: ", pais.lingua_oficial, "\n")


def menu():
    """
    Função que tem como finalidade exibir o menu ao usuário e coletar a opção digitada
    """
    print("===== MENU =====")
    print("1 - Cadastrar país")
    print("2 - Deletar país")
    print("3 - Exibir informação de um país")
    print("4 - Listar países cadastrados")
    print("5 - Créditos")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))
    return opcao