# asMelhoresDaLorinha

O presente projeto consiste em uma aplicação de console utilizando SQLite como banco de dados e utilizando Dockerização para promover a sua persistência. 

Utilizou-se a arquitetura MVC (Model-View-Controller) para separar as regras de negócio (Model) da sua implementação (Service) e intermediar a interface com a qual o usuário interage (View) e a execução das funcionalidades da aplicação (Controller). 

## Configurações iniciais:

```bash:
docker compose up --build
```
## Modo de uso:

```bash:
docker compose run --rm db
```

algumas questões: 
<!-- arquitetura -->
garantir a coerência das entradas
build "trava" nos logs do docker
rotas
conferir se as constraints estão funcionando
inserir pelo menos um dado do tipo data "realese"