from .pais_repository import *
from models.pais import Pais

def cadastrar_pais(nome_comum: str, 
               nome_oficial: str, 
               capital: str, 
               populacao: int, 
               gentilico: str, 
               lingua_oficial: str) -> Pais:
    """
    Cadastra um novo país no sistema.
    
    :param nome_comum: Nome comum do país (ex: "Brasil")
    :type nome_comum: str
    :param nome_oficial: Nome oficial do país (ex: "República Federativa do Brasil")
    :type nome_oficial: str
    :param capital: Nome da capital do país (ex: "Brasília")
    :type capital: str
    :param populacao: Número de habitantes do país (ex: 213421037)
    :type populacao: int
    :param gentilico: O gentílico utilizado para pessoas deste país (ex: "Brasileiro")
    :type gentilico: str
    :param lingua_oficial: A língua oficial utilizada no país (ex: "Português")
    :type lingua_oficial: str
    :return: O objeto Pais do país cadastrado.
    :rtype: Pais
    """
    pais = Pais(0, nome_comum, nome_oficial, capital, populacao, gentilico, lingua_oficial)
    inserir_pais(pais)

    return pais
    
def obter_pais(id: int) -> Pais | None:
    """
    Retorna um país cadastrado no sistema a partir do código. Caso não encontre, retorna None.

    :param id: O código do país a ser consultado
    :type id: int
    :return: O país cadastrado, ou None se não houver.
    :rtype: Pais | None
    """
    return consultar_pais(id)

def obter_todos_paises() -> list[Pais]:
    """
    Retorna todos os países cadastrados no sistema.

    :return: Uma lista com todos os países cadastrados.
    :rtype: list[Pais]
    """
    return consultar_todos_paises()

def remover_pais(pais: Pais):
    """
    Remove o cadastro de um país do sistema.
    
    :param pais: O país a ser removido.
    :type pais: Pais
    """
    deletar_pais(pais) 
