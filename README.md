# Atividade Prática L.P - Catalógo de Países
Este é um sistema de catálogo de países, desenvolvido em Python para a matéria de Linguagem de Programação, ministrada pelo professor Jivago Medeiros, no curso de Sistemas de Informação da Universidade Federal de Mato Grosso.

## Desenvolvido por Fã Clube Cleiton Rasta
- 202511316025 - Guilherme Magalhães Moraes de Souza
- 202511316027 - Gustavo Anibal Pinheiro da Silva

## O que é este arquivo
Esse arquivo servirá tanto como uma documentação geral do projeto, tanto quanto um relatório de todo o processo de desenvolvimento deste projeto.

Ele será composto assim:
 - uma seção **Changelog** que registrará todos os passos do projeto, sejam eles definições de arquitetura, pesquisas realizadas, ou mudanças no código.
 exemplo:
> - **[07-02-2026 / Guilherme]** Refatoração do código de leitura do arquivo de dados
>    - Por acordo mútuo, decidimos utilizar a biblioteca Pandas para extração e leitura dos arquivos...

 - uma seção **Fontes de Pesquisa** que registrará todas as fontes de pesquisa utilizadas para a realização do projeto.
 exemplo:
> - [Sintaxe básica de escrita e formatação - GitHub](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

- uma seção **Como utilizar** que irá ensinar e demonstrar a utilização do programa.
exemplo:
> - Para visualizar as informações de um país, digite `pais visualizar [ID do País]`

## Changelog
- **[07-02-26 / Guilherme]** Inicialização do repositório e criação do README.md
    - Criei o repositório e adicionei o arquivo `README.md` que servirá como registro e relatório do projeto. Já escrevi em Markdown algumas vezes, mas tive que me referir a documentação do GitHub pra ter uma ajudinha de como escrever algumas coisas. 
- **[07-02-26 / Guilherme]** Criação do gitignore com um arquivo de exemplo
    - Criei o arquivo gitignore que define todos os arquivos de ambiente locais que não devem ser enviados ao repositório. Peguei um arquivo pronto para projetos Python, disponibilizado pelo GitHub.
- **[07-02-26 / Guilherme, Gustavo]** Definir estrutura dos dados dos países
    - Definimos a estrutura dos dados que iremos armazenar dos países. Será assim:
    - **País**
        - ID (obrigatório pelos requisitos da atividade)
        - Nome Comum
        - Nome Oficial
        - Capital
        - População
        - Gentílico
        - Língua Oficial
- **[07-02-06 / Guilherme]** Criar classe de model para País
    - Criei um arquivo com uma classe dataclass que representa um país. Primeiro eu tinha só feito uma classe simples, mas ai pesquisei na documentação e vi que uma Data Class seria mais adequado.
- **[07-02-06 / Guilherme, Gustavo]** Definido como armazenaremos os dados
    - Definimos como vamos armazenar esses dados. Será num arquivo .txt, que conterá todas as informações separadas por vírgula, na ordem dos campos definidos no model, por exemplo:
        - `[id],[nome_comum],[nome_oficial],[capital],[populacao],[gentilico],[lingua_oficial]`
        - `1,"China","República Popular da China",1414163974,"Chinês","Mandarim"`
    - *OBS: O controle dos códigos será feito de forma que, se um código já foi utilizado, ele nunca mais será utilizado novamente* 
- **[07-02-2026 / Guilherme]** Criado arquivo de repositório dos países
    - Foi criado um arquivo de repositório para os países, contendo métodos de cadastro, consulta e exclusão de países, criando e atualizando automaticamente os arquivos .txt de banco de dados. Utilizei bastante a referência da documentação do Python sobre input/output escrevendo e lendo em arquivos, e também a documentação oficial do método `open()` pra entender alguns comportamentos padrões.
    - Para conter esse arquivo, foi criado o módulo "services", responsável pelas regras de negócio do código.
- **[07-02-2026 / Guilherme]** Criado arquivo de service para os países
    - Foi criado um arquivo de service para o gerenciamento dos países. É ele que vai ser utilizado pela interface para interagir com o banco de dados, de forma tratada e limpa para separar corretamente as responsabilidades.
    - No geral ele só pega e repassa pros métodos do repositório mesmo, mas pode ser útil colocar validações dos dados talvez?

## Fontes de Pesquisa
- [Sintaxe básica de escrita e formatação - GitHub](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [github - A collection of .gitignore templates](https://github.com/github/gitignore/tree/main)
- [dataclasses — Data Classes — Documentação Python 3.14.3](https://docs.python.org/pt-br/3/library/dataclasses.html)
- [open() — Built-in Function — Documentação Python 3.14.3](https://docs.python.org/3/library/functions.html#open)
- [7. Input and Output — Documentação Python 3.14.3](https://docs.python.org/3/tutorial/inputoutput.html#)

## Como utilizar