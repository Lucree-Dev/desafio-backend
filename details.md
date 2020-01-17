# Ferramentas usadas
- Golang (linguagem)
- RethinkDB (banco de dados)
- JWT (authenticação)
- Docker (isolamento de ambiente com containers)
- docker-compose (organizador de containers)

# Pacotes do Golang
- chi (responsável para criar as rotas da API)
- chi-render (responsável para criar a respostas em json para o cliente)
- chi-jwt (responsável por criar a autenticação JWT - JSON WEB TOKEN)
- jwt-go (o chi-jwt usa ele como base, então foi necessário instalá-lo também)
- validator (responsável por autenticar/validar os campos provientes do body da request)
- rethinkdbgo (driver para a comunicação entre o go e o rethinkdb)

# Como Rodar
##  Com docker
Na pasta raiz do projeto há uma arquivo chamado "docker-compose.yaml",
com o docker-compose previamente instalado basta usar os seguintes comandos

```console
  $ cd pasta-raiz
  $ docker-compose build
  $ docker-compose up
```
Quando o container lucree_api estiver sendo criado, é executado o script 'setup.sh', este script é responsável por configurar todo o ambiente necessário para rodar a API (ele demora um pouco para se executado, por isso um pouco de paciência)

## Manualmente
Há possibilidade de rodá-lo sem a necessidade de docker-compose, mas é necessário o docker para rodar o banco,
use o comando:

Primeiro crie um network(bridge) para o conteiner sair do NAT:
```console
  $ docker network create --subnet=172.28.0.0/16 lucree_net
```

Agora inicie o banco em um container:
```bash 
  $ docker run -it --rm --network lucree_net --ip 172.28.0.3 -p 28015:28015 -p 9000:8080 rethinkdb
```
Iniciado o banco de dados, há possibilidade de rodar a API dentro de um container docker, mas é necessario copiar o dockerfile dentro da pasta docker para dentro da pasta raiz. Execute os comandos:

```console
  $ cd pastaraiz
  $ cp docker/Dockfile .
  $ docker build -t api_lucree .
  $ docker run -it --name api_lucree -p 8080:8080 -e DATABASE_ADDRESS=172.28.0.3:28015 -v $pwd:/go/src/github.com/n0bode/desafio-backend api_lucree
```

# API

Nessa API foi incluida a autenticação por JWT (json web token), então existe rotas públicas a e restritas. Essas são as rotas:

**PÚBLICAS:**
`[POST]  /session`
`[POST]  /account/person`

**RETRISTAS (necessário JWT):**
`[DELETE] /session`
`[GET]    /account/friends`
`[POST]   /account/card`
`[GET]    /account/cards`
`[POST]   /account/transfer`
`[GET]    /account/bank-statement`
`[GET]    /account/bank-statement/{userId}`

##### Para poder acessar essas rotas, é necesário autenticar, para a gerar o token usa-se a rota:
`[POST]   /session`

Ele deve receber um json contendo "username" e "password" do usuário:
```json
  {
    "username": "Tony",
    "password": "Montana",
  }
```

O Tony já existe para teste e é criado quando a migração é executada. Pode-se testar usando o CURL.
```bash
  $ curl -X POST -d '{"username" : "Tony","password":"Montana"}' http://localhost:8080/session -i
```
Todas os retorna das rotas por padrão tem o formato abaixo, esse formato fornece mais informação sobre a requesição, também é trabalhado com [statuscode](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html):
```json
{
    "message":"aqui informa o error",
    "data":"só existe esse campo, quando statuscode for positivo"
}
```

Só são consideradas respostas possitivas:
`[POST] 201 - Created`
`[GET]  200 - OK`
