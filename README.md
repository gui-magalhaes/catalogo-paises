# Atividade Prática L.P - Catalógo de Países
Este é um sistema de catálogo de países, desenvolvido em Python para a matéria de Linguagem de Programação, ministrada pelo professor Jivago Medeiros, no curso de Sistemas de Informação da Universidade Federal de Mato Grosso.

Caso não esteja vendo isso no GitHub, você pode acessar a página do repositório e ver todos os commits e versões [clicando aqui.](https://github.com/gui-magalhaes/catalogo-paises)

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
- **[08-02-2026 / Gustavo]** Criado um novo arquivo de service para a interface
    - Foi criado um novo arquivo de service para gerenciamento de algumas funções da interface gráfica para o usuário, como a exibição de menu e a exibição dos cadastros já realizados de acordo com a solicitação do usuário. Como havia mais de uma função que interagia exclusivamente com a interface, fez-se necessária a criação desse novo arquivo
    - Mudança commitada pelo Guilherme por conta de problemas com o Git
- **[08-02-2026 / Gustavo]** Criado um novo arquivo de main para execução do código
    -  Foi criado um novo arquivo main para que o código pudesse ser executado. Nele há o controle de de estrutura de fluxo match case junto de algumas regras condicionais para realização das ações solicitadas pelo usuário.
    -  As principais funções as quais este arquivo utiliza para interação e execução estão nos arquivos pais_service.py e interface_service.py
    - Mudança commitada pelo Guilherme por conta de problemas com o Git

## Fontes de Pesquisa
- [Sintaxe básica de escrita e formatação - GitHub](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [github - A collection of .gitignore templates](https://github.com/github/gitignore/tree/main)
- [dataclasses — Data Classes — Documentação Python 3.14.3](https://docs.python.org/pt-br/3/library/dataclasses.html)
- [open() — Built-in Function — Documentação Python 3.14.3](https://docs.python.org/3/library/functions.html#open)
- [7. Input and Output — Documentação Python 3.14.3](https://docs.python.org/3/tutorial/inputoutput.html#)

## Como utilizar
 **Sistema de cadastro de países**
    -   Trata-se de um sistema capaz de realizar cadastros, consultas e exclusão de informações, além de gravar as alterações realizadas em um arquivo txt externo

 **Como Utilizar**
    -   O uso do sistema se dá exclusivamente por meio do terminal, sendo de fácil entendimento e direto em sua interação gráfica com o usuário.
    
 <img width="821" height="202" alt="image" src="https://github.com/user-attachments/assets/fb0a0bc8-3d8a-4063-8ab1-e980b50f82ce" />
   
   Por meio do terminal o usuário informa a ação que deseja do programa, e passa as informações solicitadas por ele, como no seguinte exemplo:
   
   <img width="558" height="149" alt="image" src="https://github.com/user-attachments/assets/df213f12-b92b-4bf4-a74c-6050e5ae50c2" />
    
 **Sobre o arquivo txt**    
    - Os arquivos .txt serão criados assim que o uusário realizar o primeiro cadastro de país por meio do programa, sendo eles:
       - Um que irá conter exclusivamente o índice atualizado do último cadastro realizado, chamado de ultimo_id.txt;
       
   <img width="174" height="108" alt="image" src="https://github.com/user-attachments/assets/61510a8a-55c4-49ce-8eab-36c9e515f299" />
    
   - E o outro que irá conter os registros atualizados feitos pelo usuário por meio do programa, incluindo exclusão de cadastros, como no exemplo a seguir, chamado de paises.txt.
     
   <img width="913" height="77" alt="image" src="https://github.com/user-attachments/assets/215513e6-b10b-4443-85c9-1cc509a9f9cb" />

   <img width="850" height="55" alt="image" src="https://github.com/user-attachments/assets/eda9a384-5179-48cd-ac80-f2a33e9ed3fa" />