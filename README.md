# asMelhoresDaLorinha

O presente projeto consiste em um banco de dados interativo, em que o usuário pode registrar, excluir, acessar e atualizar novos álbuns e músicas da Taylor Swift. Através do prompt de comando, o usuário fornece entradas e recebe respostas explicativas que o orientam acerca de como usar a aplicação.

Trata-se de uma aplicação de console desenvolvida em Linguagem Python, que utiliza o SQLite como banco de dados e Docker para promover a sua containerização e persistência desses dados, ambas de suma importancia para garantir a portabilidade e a consistência do sistema.

Utilizou-se a arquitetura MVC (Model-View-Controller) para separar os dados e regras de negócio (Model) da interface com a qual o usuário interage (View). A intermediação destes é feita pelo Controller, que recebe as requisições do usuário, solicita a sua execução ao Model e atualiza a View com a resposta.

Foram usados os tipos de dados **INTEGER** e **TEXT**, este último suportando datas formatadas segundo o padrão ISO ('YYYY-MM-DD'). No que tange a **CONSTRAINTS**, somente a propriedade _album_, da tabela _Music_, é opcional (pois uma música pode ser single). 

Essa tabela também contém duas **FOREIGN KEYs**: _album_ e _artist_. Aquela propaga em caso de atualização ("ON UPDATE CASCADE") e insere um valor nulo em caso de exclusão ("ON DELETE SET NULL"), e essa restringe a ação de exclusão da tupla correspondente na relação referenciada ("ON DELETE RESTRICT"). A relação _Album_ faz o mesmo para sua chave estrangeira de mesmo nome.

Na pasta _middlewares_ estão funções que verificam a formatação das entradas fornecidas pelo usuário.

## Configurações iniciais:

```bash:
docker compose up --build

docker attach $(docker compose ps -q db)
```

Os comandos acima, respectivamente, buildam a imagem e anexam um segundo terminal ao container principal, com o qual é possível interagir. O segundo comando deve ser inserido em outro terminal, enquanto o container estiver ativo (o container é ativado com o primeiro comando). Para parar a execução, pressione Ctrl+C.

## Modo de uso:

Uma vez que a imagem foi construída, também é possível utilizar este comando:

```bash:
docker compose run --rm db
```

Para parar a execução, pressione Ctrl+C.

Possíveis novas features que podem ser implementadas são: a possibilidade de "se arrepender" da opção escolhida e, ao invés de retornar o ID do álbum, retornar seu nome.
