"""
Representa um país do mundo.
"""
class Pais:
    id: int
    nome_comum: str
    nome_oficial: str
    capital: str
    populacao: int
    gentilico: str
    lingua_oficial: str
    
    def __init__(self, 
                 nome_comum: str, 
                 nome_oficial: str, 
                 capital: str, 
                 populacao: int, 
                 gentilico: str, 
                 lingua_oficial: str):
        self.nome_comum = nome_comum
        self.nome_oficial = nome_oficial
        self.capital = capital
        self.populacao = populacao
        self.gentilico = gentilico
        self.lingua_oficial = lingua_oficial