# asMelhoresDaLorinha

O presente projeto consiste um banco de dados interativo, em que o usuário pode registrar, excluir, acessar e atualizar novos álbuns e músicas da Taylor Swift. Através do prompt de comando, o usuário fornece entradas e recebe respostas explicativas que o orientam acerca de como usar a aplicação.

Trata-se de uma aplicação de console desenvolvida em Linguagem Python, que utiliza o SQLite como banco de dados e Docker para promover a sua containerização e persistência desses dados, ambas de suma importancia para garantir a portabilidade e a consistência do sistema.

Utilizou-se a arquitetura MVC (Model-View-Controller) para intermediar as regras de negócio e sua implementação (Model) e a interface com a qual o usuário interage (View) através do Controller, que executa as funcionalidades da aplicação.

Utilizou-se a arquitetura MVC (Model-View-Controller) para separar os dados e regras de negócio (Model) da interface com a qual o usuário interage (View). A intermediação destes é feita pelo Controller, que recebe as requisições do usuário, solicita a sua execução ao Model e atualiza a View com a resposta.

Foram usados os tipos de dados **INTEGER** e **TEXT**, este último suportando datas formatadas segundo o padrão ISO ('YYYY-MM-DD'). No que tange a **CONSTRAINTS**, somente a propriedade _album_, da tabela _Music_, é opcional (pois uma música pode ser single). Essa tabela também contém duas **FOREIGN KEYs**: _album_ e _artist_. Essa restringe a ação de exclusão da tupla correspondente na relação referenciada ("ON DELETE RESTRICT"), e aquela propaga em caso de atualização (ON UPDATE CASCADE). A relação _Album_ faz o mesmo para sua chave estrangeira de mesmo nome.

## Configurações iniciais:

```bash:
docker compose up --build

docker attach $(docker compose ps -q db)
```

Os comandos acima, respectivamente, builda a imagem e anexa um segundo terminal ao container principal, com o qual é possível interagir.

## Modo de uso:

Uma vez que a imagem já foi construída, também é possível utilizar este comando:

```bash:
docker compose run --rm db
```

