# Rest API Python usando Django com Docker Composer

[![Python required version: 3.7.3](https://img.shields.io/badge/python-3.7.3-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-373)
[![Documentation](https://img.shields.io/badge/docs-0.0.1-orange.svg?style=flat-square)](https://google.com)

Estee projeto foi criado por [Eneas Rodrigues](https://github.com/EneasJr-Rodrigues).
Pode entrar em contato com ele para mais instruções

## ⚠️ Atenção!

Este projeto precisa de ter instalado o docker engineer e o docker compose para rodar
Se houver alguma atualização nesta lib, a versão deve ser atualizada neste arquivo:)

Por favor siga o passo a passo do link a seguir: [docker](https://docs.docker.com/engine/install/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/) para instalar.

## Recursos adicionais

* Você pode utilizar uma API chamada de [TablePlus](https://tableplus.com/blog/2019/10/tableplus-linux-installation.html) para visizar as tabelas e os dados com mais facilidade
* Requerimento: Precisa de ter o [postgresql](https://www.postgresql.org/download/) instalado na maquina
* O [Postman](https://www.postman.com/downloads/) pode ler e efetuar as transações listadas da API

## API Documentação com Swagger UI Django

* Acesse a URL abaixo para poder ver a documentação do código fonte gerado pelo Swagger
* **requerimento**: As tabelas precisam de estar populadas para gerar a documentação, por isso é necessário utilizar os procedimentos abaixo para depois abrir a url do swagger

```shell
localhost:8000/api/schema/docs/#/
```

## Instruções básicas:

* abra o seu terminal e digite os comandos a seguir:
* com o terminal no diretorio raiz do projeto
  
```shell
sudo chmod +x build.sh run.sh stop.sh
```

## Build no projeto

* abra o seu terminal e digite os comandos a seguir:
* com o terminal no diretorio raiz do projeto
* comando bash
  
```shell
./build.sh
```

## Rodar o sistema

* abra o seu terminal e digite os comandos a seguir:
* com o terminal no diretorio raiz do projeto
* comando bash

```shell
./run.sh ## para startar e subir o server
./stop.sh ## para parar os containers
```

## Utilização do sistema:

* para incluir usuário na tabela de usuarios, utilize a URL abaixo:
* Pode utilizar o browser ou o postman para as transações

```shell
localhost:8000/personal/create_person
```

* Utilize um formato JSON para incluir o usuário no banco de dados, segue o exemplo abaixo:

```json
{
   "first_name":"João",
   "last_name": "das Neves",
   "birthday": "1991-09-91",
   "password": "*****",
   "username": "joao_das_neves",
   "user_id": "70c881d4a26984ddce795f6f71817c9cf4480e79"
}
```

### GET para visualizar o resultado utilize a URL abaixo:

```shell
localhost:8000/personal/_persons
```

* clique no botão get do framework

### PUT para fazer o update desse usuário:
  
```shell
localhost:8000/personal/update_person/{id}
```

### DELETE para deletar um usuário:

```shell
localhost:8000/personal/delete_person/{id}
```

* Todas essas modificações podem ser vistas no primeiro link (GET) para visualizar os resultados de cada uma das transações

No total são 6 tabelas que podem ser populadas e transacionadas conforme as instruções acima, segue abaixo a lista de cada uma das tabelas, lembrando que para acessalas são todas através dos links ['localhost:8000/] localhost:8000/tabela/tipo_transação/id

```shell
localhost:8000/

## Tabela
personal/
friend/
card/
transfer/
billing/
bank/

## tipo de transação
### Tabela de usuário
_persons # GET leitura de todos os dados da tabela (formato json)
create_person # POST - criacao de um novo usuario na tabela
read_person/{id} # GET - leitura de usuario por id
update_person/{id} # PUT - atualização de um registro por ID banco
delete_person/{id} # DELETE - deletar um usuario especifico pelo ID banco

### Tabela de Friends
_friends # GET leitura de todos os dados da tabela (formato json)
create_friend # POST - criacao de um novo usuario na tabela
read_friend/{id} # GET - leitura de usuario por id
update_friend/{id} # PUT - atualização de um registro por ID banco
delete_friend/{id} # DELETE - deletar um usuario especifico pelo ID banco

### Tabela de cartões
_cards # GET leitura de todos os dados da tabela (formato json)
create_card # POST - criacao de um novo card na tabela de cartões
read_card/{id} # GET - leitura de card por id
update_card/{id} # PUT - atualização de um registro por ID banco
delete_card/{id} # DELETE - deletar um card especifico pelo ID banco

### Tabela de billing
_billing # GET leitura de todos os dados da tabela (formato json)
create_billing # POST - criacao de um novo card na tabela de cartões
read_billing/{id} # GET - leitura de card por id
update_billing/{id} # PUT - atualização de um registro por ID banco
delete_billing/{id} # DELETE - deletar um card especifico pelo ID banco

### Tabela de transferencias
_transfer # GET leitura de todos os dados da tabela (formato json)
create_transfer  # POST - criacao de uma nova transferencia na tabela de transferencias
read_transfer/{id} # GET - leitura de transferencia por id
update_transfer/{id} # PUT - atualização de um registro por ID banco
delete_transfer/{id} # DELETE - deletar uma transferencia especifica pelo ID banco

### Tabela banco
_bank # GET leitura de todos os dados da tabela (formato json)
create_bank # POST - criacao de um novo registro bancario na tabela de bank
read_bank/{id} # GET - leitura dos dados bancarios por id
update_bank/{id} # PUT - atualização de um registro por ID banco
delete_bank/{id} # DELETE - deletar uma registro especifico pelo ID banco


```

### Para facilitar segue todos os links editaveis como exemplo:

```shell
## tabela usuarios com as transacoes de cada nivel
localhost:8000/personal/_persons
localhost:8000/personal/create_person
localhost:8000/personal/read_person/1
localhost:8000/personal/update_person/1
localhost:8000/personal/delete_person/1

## tabela friends com as transacoes de cada nivel
localhost:8000/friend/_friends
localhost:8000/friend/create_friend
localhost:8000/friend/read_friend/1
localhost:8000/friend/update_friend/1
localhost:8000/friend/delete_friend/1

## tabela cartões com as transacoes de cada nivel
localhost:8000/card/_cards
localhost:8000/card/create_card
localhost:8000/card/read_card/1
localhost:8000/card/update_card/1
localhost:8000/card/delete_card/1

## tabela billing com as transacoes de cada nivel
localhost:8000/billing/_billing
localhost:8000/billing/create_billing
localhost:8000/billing/read_billing/1
localhost:8000/billing/update_billing/1
localhost:8000/billing/delete_billing/1

## tabela transferencias com as transacoes de cada nivel
localhost:8000/transfer/_transfer
localhost:8000/transfer/create_transfer
localhost:8000/transfer/read_transfer/1
localhost:8000/transfer/update_transfer/1
localhost:8000/transfer/delete_transfer/1

## tabela banco com as transacoes de cada nivel
localhost:8000/bank/_bank
localhost:8000/bank/create_bank
localhost:8000/bank/read_bank/1
localhost:8000/bank/update_bank/1
localhost:8000/bank/delete_bank/1
```

---
#### LICENSE
```
MIT License

Copyright (c) 2020 Lucree Soluções Inteligentes.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


