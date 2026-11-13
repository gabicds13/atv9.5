# Exercício 9.5 — FastAPI e Docker

Projeto do Laboratório 09 de Engenharia de Software, seguindo as etapas:

1. Implementar uma API RESTful com FastAPI.
2. Incluir um arquivo `.dockerignore`.
3. Criar uma imagem Docker da aplicação.
4. Executar a imagem localmente e testar a aplicação.
5. Testar a aplicação com o Postman.

**Entregável do professor:** prints de todos os passos. Não é exigida publicação na Azure neste exercício.

## Arquivos do projeto

- `app.py` — API RESTful com GET, POST, PUT, DELETE.
- `requirements.txt` — dependências Python.
- `Dockerfile` — instruções para montar a imagem.
- `.dockerignore` — exclui arquivos desnecessários do contexto de build.
- `postman_collection.json` — coleção Postman pronta para importar.

## Pré-requisitos

- Docker Desktop instalado e iniciado (Windows: mecanismo Linux/WSL 2 funcionando).
- Postman para testar requisições HTTP.
- Python instalado **somente** se quiser testar antes sem Docker.

## Executar com Docker

Abra um terminal **dentro da pasta** que contém o `Dockerfile`.

```bash
docker --version
docker build -t atv9-5-fastapi .
docker run --name atv9-5-api -p 8000:8000 atv9-5-fastapi
```

O terminal deve indicar que o servidor está ativo em `http://0.0.0.0:8000`.

No navegador:

- Página inicial: http://localhost:8000/
- Lista de tarefas: http://localhost:8000/tarefas
- Documentação automática: http://localhost:8000/docs

Para conferir contêineres em execução, abra **outro** terminal:

```bash
docker ps
```

Para parar a aplicação, use `Ctrl+C` no terminal do `docker run` ou `docker stop atv9-5-api`. Para rodar novamente com o mesmo nome, use `docker start -a atv9-5-api`, ou remova o contêiner parado com `docker rm atv9-5-api` antes de um novo `docker run`.

## Testar no Postman

1. Clique em **Import** e selecione `postman_collection.json`.
2. Confira que `baseUrl` vale `http://localhost:8000`.
3. Envie as requisições da coleção:
   - `GET /tarefas` → 200 OK
   - `POST /tarefas` → 201 Created
   - `PUT /tarefas/1` → 200 OK
   - `DELETE /tarefas/1` → 200 OK
   - `GET /tarefas/9999` → 404 Not Found (teste opcional)
4. No POST/PUT, o JSON de exemplo é:

```json
{"descricao": "Fazer o exercicio 9.5"}
```

> Este é um laboratório didático: as tarefas ficam apenas na memória. Elas voltam ao estado inicial quando a aplicação reinicia.

## Prints a entregar

1. `app.py` com os endpoints FastAPI no editor.
2. `Dockerfile` e `.dockerignore` visíveis.
3. Terminal exibindo `docker build` concluído com sucesso.
4. Docker Desktop ou terminal `docker ps` mostrando o contêiner em execução, além de `localhost:8000/docs` aberto.
5. Postman mostrando cada método (GET, POST, PUT e DELETE) e suas respostas.

## Teste alternativo sem Docker

```bash
python -m pip install -r requirements.txt
python -m uvicorn app:app --reload
```

Abra http://localhost:8000/docs. O teste sem Docker é opcional e **não substitui** a execução do contêiner exigida no exercício 9.5.
