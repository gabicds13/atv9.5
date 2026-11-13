from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Exercicio 9.5 - API de Tarefas", version="1.0.0")


class TarefaEntrada(BaseModel):
    descricao: str = Field(min_length=1, max_length=200)


# Dados didaticos em memoria; nao sao persistidos apos reiniciar.
tarefas = {1: {"id": 1, "descricao": "Estudar FastAPI e Docker"}}
proximo_id = 2


@app.get("/")
def inicio():
    return {"mensagem": "API RESTful - Exercicio 9.5", "documentacao": "/docs"}


@app.get("/tarefas")
def listar_tarefas():
    return list(tarefas.values())


@app.get("/tarefas/{tarefa_id}")
def consultar_tarefa(tarefa_id: int):
    if tarefa_id not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    return tarefas[tarefa_id]


@app.post("/tarefas", status_code=status.HTTP_201_CREATED)
def cadastrar_tarefa(entrada: TarefaEntrada):
    global proximo_id
    tarefa = {"id": proximo_id, "descricao": entrada.descricao}
    tarefas[proximo_id] = tarefa
    proximo_id += 1
    return tarefa


@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, entrada: TarefaEntrada):
    if tarefa_id not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    tarefas[tarefa_id]["descricao"] = entrada.descricao
    return tarefas[tarefa_id]


@app.delete("/tarefas/{tarefa_id}")
def excluir_tarefa(tarefa_id: int):
    if tarefa_id not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    del tarefas[tarefa_id]
    return {"mensagem": "Tarefa excluida com sucesso"}
