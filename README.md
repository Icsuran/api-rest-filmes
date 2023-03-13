# README

## Setup

* BD: PostgreSQL (host: localhost, port=5432, username=postgres, password=postgres, dbaname=ubots)
* Conexão Python-PostgreSQL: psycopg2
* Linguagem: Python
* Framework: Flask
* Protocolo API Rest: JSON

## Rotas:

```
* Listar: http://127.0.0.1:5000/
* Atualizar: http://127.0.0.1:5000//atualizar/<id>/<titulo>/<sinopse>
* Criar: http://127.0.0.1:5000//criar/<titulo>/<sinopse>
* Deletar: http://127.0.0.1:5000//deletar/<id>
* Avaliar: http://127.0.0.1:5000//avaliar/<id>/<nota>
* Indicar: http://127.0.0.1:5000//indicar
```

