# asMelhoresDaLorinha

O presente projeto consiste em uma aplicação de console desenvolvida em Linguagem Python, que utiliza o SQLite database e Dockerização para promover a sua containerização e persistência dos dados. 

Utilizou-se a arquitetura MVC (Model-View-Controller) para separar as regras de negócio (Model) da sua implementação (Service) e intermediar a interface com a qual o usuário interage (View) e a execução das funcionalidades da aplicação (Controller). 

## Configurações iniciais:

```bash:
docker compose up --build
```
## Modo de uso:

Em outro terminal, insira:

```bash:
docker compose run --rm db
```