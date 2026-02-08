from dataclasses import dataclass

@dataclass
class Pais:
    """
    Representa um país do mundo.
    """
    id: int
    nome_comum: str
    nome_oficial: str
    capital: str
    populacao: int
    gentilico: str
    lingua_oficial: str