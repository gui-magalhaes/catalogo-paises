from models.pais import Pais

CAMINHO_BD = 'paises.txt'
CAMINHO_CONTROLE_ID = 'ultimo_id.txt'

def retorna_proximo_id() -> int:
    """
    Retorna o primeiro ID disponível.
    
    :return: O número de ID disponível para utilização.
    :rtype: int
    """
    try:
        with open(CAMINHO_CONTROLE_ID, 'r', encoding='utf-8') as f:
            ultimo_id = int(f.read())
            return ultimo_id + 1
    except FileNotFoundError:
        registrar_id(1)
        return 1

def registrar_id(id: int):
    """
    Registra um novo ID no arquivo de controle.
    
    :param id: Código de identificação a ser cadastrado.
    :type id: int
    """
    with open(CAMINHO_CONTROLE_ID, 'w', encoding='utf-8') as f:
        f.write(str(id))

def serializar_pais(pais: Pais) -> str:
    """
    Serializa um objeto do tipo Pais em uma string no formato `"[id],[nome_comum],[nome_oficial],[capital],[populacao],[gentilico],[lingua_oficial]"`.
    
    :param pais: O país a ser serializado.
    :type pais: Pais
    :return: Os dados do país de modo serializado, com os dados separados por vírgula (,).
    :rtype: str
    """
    return f"{pais.id},{pais.nome_comum},{pais.nome_oficial},{pais.capital},{pais.populacao},{pais.gentilico},{pais.lingua_oficial}"

def desserializar_pais(dados: str) -> Pais:
    """
    Desserializa uma string de dados separados por vírgula em um objeto Pais.
    
    :param dados: Os dados separados por vírgula (,).
    :type dados: str
    :return: O objeto país resultante desses dados.
    :rtype: Pais
    """
    campos = dados.split(',')
    return Pais(id=int(campos[0]), 
                nome_comum=campos[1], 
                nome_oficial=campos[2], 
                capital=campos[3], 
                populacao=int(campos[4]), 
                gentilico=campos[5], 
                lingua_oficial=campos[6])

def inserir_pais(pais: Pais):
    """
    Insere um novo país no banco de dados.
    
    :param pais: O país a ser inserido.
    :type pais: Pais
    """
    pais.id = retorna_proximo_id()
    with open(CAMINHO_BD, 'a', encoding='utf-8') as f:
        f.write(serializar_pais(pais) + '\n')
    
    registrar_id(pais.id)

def consultar_pais(id: int) -> Pais | None:
    """
    Consulta um país do banco de dados.
    
    :param id: O ID do país a ser pesquisado.
    :type id: int
    :return: O objeto Pais referente ao ID consultado, ou None se não houver.
    :rtype: Pais | None
    """
    try:
        with open(CAMINHO_BD, 'r', encoding='utf-8') as f:
            for dados in f:
                pais = desserializar_pais(dados.strip())
                if pais.id == id: 
                    return pais
            
        return None
    except FileNotFoundError:
        return None

def consultar_todos_paises() -> list[Pais]:
    """
    Consulta todos os países do banco de dados.
    
    :return: A lista de todos os países cadastrados.
    :rtype: list[Pais]
    """
    try:
        with open(CAMINHO_BD, 'r', encoding='utf-8') as f:
            return [desserializar_pais(dados.strip()) for dados in f]
    except FileNotFoundError:
        return []
    
def deletar_pais(pais_excluido: Pais):
    """
    Deleta um país do banco de dados.
    
    :param pais_excluido: O país a ser deletado.
    :type pais_excluido: Pais
    """
    paises = consultar_todos_paises()
    paises_atualizados = [pais for pais in paises if pais.id != pais_excluido.id]

    #Não removeu ninguém, então não tem porque atualizar o arquivo..
    if len(paises) == len(paises_atualizados):
        return

    with open(CAMINHO_BD, 'w', encoding='utf-8') as f:
        for pais in paises_atualizados:
            f.write(serializar_pais(pais) + '\n')