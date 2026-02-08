from services.pais_service import *
from services.interface_service import *


print("Bem vindo ao sistema de cadastro de países, segue a seguir o menu com as opções disponíveis:")
"""
Mostra o menu ao usuário e recebe o valor digitado

"""
opcao = menu()
"""
Recebe a opção selecionada pelo usuário no menu e entra no teste condicional 
para selecionar a ação desejada

"""
while opcao != 0:
    limpa()
    match opcao:
        case 1:
            """
             Realiza o cadastro do país de acordo com as informações passadas pelo usuário
             e de acordo com os parâmetros da função
            """
            nome_comum = input("Informe o nome comum do país ")
            nome_oficial= input("Informe o nome oficial país ")
            capital = input("Informe a capital do país ")
            populacao = int(input("Informe a população do país "))
            gentilico = input("Informe o gentilício designado do país ")
            lingua_oficial = input("Informe o idioma oficial do país ")
            cadastrar_pais(nome_comum,nome_oficial,capital,populacao,
                                        gentilico,lingua_oficial)
            print("País cadastrado com sucesso ")
        case 2:
            """
            Realiza a busca do país que o usuário deseja deletar, de acordo com o id informado,
            com a função obter_pais().
            Caso não haja sucesso na busca, retornará mensagem informando erro,
            caso contrário irá retornar as informações o país solicitado
            """
            id = int(input("Informe o id do país a ser deletado "))
            pais= obter_pais(id)
            if pais is None:
                print("País não encontrado ")
            else:
                remover_pais(pais)
                print("País deletado ")
        case 3:
            """
            Faz a busca pelo país solicitado por meio da função obter_pais()
            caso encontre, mostrará ao usuário, 
            caso contrário mostra uma mensagem informando o erro
            O país em questão é passado como lista para a função ([pais])
            para que esteja de acordo com o parâmetro a ser passado pela função
            """
            id=int(input("Informe o id do país que deseja obter informação "))
            pais = obter_pais(id)
            if pais:
                exibir_paises([pais])
            else:
                print("País nao encontrado ")
        case 4:
            """
            Faz uma validação se possui cadastro de algum país para realizar a listagem completa.
            Se não houver informa uma mensagem informando ao usuário, 
            caso contrário, mostrará todos os países cadastrados
            """
            print("Segue a seguir todos os países cadastrados e atualizados ")
            paises =  obter_todos_paises()
            if not paises:
                print("Nenhum país cadastrado. ")
            else:
                exibir_paises(paises)
        case 5:
            """
            Mostra os créditos
            """
            print("Fã Clube Cleiton Rasta")
            print("202511316025 - Guilherme Magalhães Moraes de Souza")
            print("202511316027 - Gustavo Anibal Pinheiro da Silva")
        case 0:
            print("Saindo do programa ")
        case _:
            print("Opção inválida ")
    if opcao != 0:
        input("Digite ENTER para continuar")
        limpa()
        opcao = menu()
        
    