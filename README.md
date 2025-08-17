# asMelhoresDaLorinha

O presente projeto consiste em uma aplicação de console desenvolvida em Linguagem Python, que utiliza o SQLite como banco de dados e Docker para promover a sua containerização e persistência desses dados, ambas de suma importancia para garantir a portabilidade e a consistência do sistema.

Utilizou-se a arquitetura MVC (Model-View-Controller) para separar as regras de negócio (Model) da sua implementação (Service) e intermediar a interface com a qual o usuário interage (View) e a execução das funcionalidades da aplicação (Controller). 

Trata-se um banco de dados interativo, em que o usuário pode registrar, excluir, acessar e atualizar novos álbuns e músicas da Taylor Swift. Através do prompt de comando, o usuário fornece entradas e recebe respostas explicativas que o orientam acerca de como usar a aplicação.

## Configurações iniciais:

```bash:
docker compose up --build

docker attach $(docker compose ps -q db)
```

Os comandos acima, respectivamente, buildam a imagem e anexam um segundo terminal ao container principal, com o qual é possível interagir.

## Modo de uso:

Uma vez que a imagem já foi construída, também é possível utilizar este comando:

```bash:
docker compose run --rm db
```

